from flask import Flask, request, jsonify
import requests
import json
import numpy as np

# Загружаем индексы кластеров
clust_centers_m = np.load('/indices/clust_centers.npy')
app = Flask(__name__)

# Конфиги где поднят tensorflow embedding server
host = 'host.docker.internal'
port_rest = 8501
model = 'use'

@app.route('/input', methods=['POST'])
def get_data():
    # Обрабатываем JSON
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json_val = request.json
        query = json_val['query']

        data = {
            "inputs":  [query],
        }
        rest_results = requests.post(f'http://{host}:{port_rest}/v1/models/{model}:predict', json=data).json()

        input_emb = rest_results['outputs'][0]
        input_emb = np.array(input_emb)

        u_v = np.sum(input_emb*clust_centers_m, axis=1)
        abs_u = np.sqrt(np.sum(input_emb * input_emb))
        abs_v = np.sqrt(np.sum(clust_centers_m * clust_centers_m, axis=1))
        cos_sims = u_v / (abs_u * abs_v)
        input_cluster = np.argmin(cos_sims)

        resp = json.loads(
            requests.post(
                f'http://host.docker.internal:1400{input_cluster}/get_best_from_k',
                json={'emb':input_emb.tolist() }
            ).text)

        match = resp['best_match']
        cluster = resp['cluster_id']

        return jsonify(best_match=match, cluster=cluster)
    else:
        return 'Content-Type not supported! Please use JSON with \"query\" field.'

if __name__ == "__main__":
    app.run()