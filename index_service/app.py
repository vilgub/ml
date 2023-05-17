from flask import Flask, request, jsonify
import requests
import numpy as np
import json
import os
import joblib

CLUSTER_ID = os.environ['CLUSTER_ID']
index = joblib.load(f'/indices/clust_{CLUSTER_ID}/index')

with open(f'/indices/clust_{CLUSTER_ID}/sentences.json') as f:
    raw_sentences = json.load(f)

app = Flask(__name__)


@app.route('/get_best_from_k', methods=['POST'])
def get_best_from_k():
    input_emb = np.array(request.json['emb'], dtype='float32')
    ans = get_neighbours(input_emb)
    return jsonify(best_match=ans, cluster_id=CLUSTER_ID)


def get_neighbours(input_emb):
    dists, neigh_ind = index.search(input_emb.reshape(1, -1), 20)
    neigh_ind = neigh_ind.flatten()
    neigh_emb = np.array([index.reconstruct(int(ind)) for
                          ind in neigh_ind], dtype='float32')
    argmax_closest_emb = predict_match(neigh_emb)
    best_match_ind = neigh_ind[argmax_closest_emb]

    # Если тут падает приложение взять вариант с str

    # best_match_sentence = raw_sentences[best_match_ind]
    best_match_sentence = raw_sentences[str(best_match_ind)]

    return best_match_sentence


def predict_match(neigh_emb):
    return np.random.randint(0, len(neigh_emb))


if __name__ == "__main__":
    app.run()