# 3. Сгенерируйте псевдослучайные числа, для алгоритма кластеризации.
# Определите графически, при каких параметрах модель имеет наилучшие значения правильности.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

features, target = make_blobs(n_samples=100,
                                n_features=2,
                                centers=3,
                                cluster_std=0.5,
                                shuffle=True,
                                random_state=1)


plt.figure(figsize=(8, 6))
plt.scatter(features[:, 0], features[:, 1], c=target, cmap='viridis', edgecolor='k')
plt.title("Истинные кластеры")
plt.show()
print(target)

k_values = [2, 3, 4, 5]
plt.figure(figsize=(15, 10))
best_ari = []

for i, k in enumerate(k_values):

    kmeans = KMeans(n_clusters=k, random_state=1)
    pred_labels = kmeans.fit_predict(features)

    ari = adjusted_rand_score(target, pred_labels)
    best_ari.append(ari)

    plt.subplot(2, 2, i + 1)
    plt.scatter(features[:, 0], features[:, 1], c=pred_labels, cmap='viridis', edgecolor='k')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, marker='X', c='red')
    plt.title(f'K={k}\nARI: {ari:.2f}')

plt.tight_layout()
plt.show()

best_k = np.argmax(best_ari)
best_model = KMeans(n_clusters=best_k, random_state=1)
best_model.fit(features)

print("Оптимальное количество кластеров:", best_k)
print(f"Правильность модели при оценке методом ARI (Точность: {max(best_ari):.2f})")
