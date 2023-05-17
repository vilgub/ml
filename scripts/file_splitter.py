import numpy as np
import json
import faiss
import joblib
import os
import pickle

# Скрипт разбивки файлов файлов хранящие результаты кластеризации эмбеддингов на индексы

dim = 512

for dg in [1, 2]:

    with open(f'data/clusters_use_dg{dg}.json') as f:
        clusters = json.load(f)
    os.makedirs(f'dgs/dg_{dg}', exist_ok=True)

    for clust_id in range(4):
        os.makedirs(f'dgs/dg_{dg}/clust_{clust_id}', exist_ok=True)
        with open(f'dgs/dg_{dg}/clust_{clust_id}/sentences.json', 'w') as f:
            json.dump(clusters[str(clust_id)], f)

for dg in [1, 2]:

    with open(f'data/clusters_use_dg{dg}.json') as f:
        clusters = json.load(f)

    with open(f'data/use_embeddings_dg{dg}.pkl', 'rb') as f:
        use_embeddings = pickle.load(f)

    for clust_id in range(4):
        embs_cluster = np.vstack(
            [use_embeddings[clusters[str(clust_id)][i]] for i in
             range(len(clusters[str(clust_id)]))])
        index = faiss.IndexFlatL2(dim)
        index.add(embs_cluster)
        joblib.dump(index, f'dgs/dg_{dg}/clust_{clust_id}/index')

for dg in [1, 2]:
    with open(f'data/clusters_centers_use_dg{dg}.pkl', 'rb') as f:
        clusters_centers = pickle.load(f)

        clust_centers_m = np.array([clusters_centers[str(i)] for i in range(4)])
        np.save(f'dgs/dg_{dg}/clust_centers', clust_centers_m)