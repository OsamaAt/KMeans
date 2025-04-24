import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

x,_=make_blobs(n_samples=500 , random_state=42)


inertia=[]
k_range=range(1,11)
for k in k_range:
    k_means=KMeans(n_clusters=k , random_state=42)
    k_means.fit(x)
    inertia.append(k_means.inertia_)

plt.plot(inertia , k_range , marker='o')
plt.title('Elbow Method')
plt.xlabel('Clusters')
plt.ylabel("Inertia")
plt.legend()
plt.show()

k_means=KMeans(n_clusters=8 , random_state=42)
y_kmeans=k_means.fit_predict(x)

colors=['yellow' , 'brown' , 'blue' , 'gray' , 'green' , 'orange' , 'purple' , 'aqua']

for i in range(8):
    plt.scatter(x[y_kmeans==i,0] , x[y_kmeans==i,1] , c=colors[i] , s=20 , marker='x')
    
plt.scatter(k_means.cluster_centers_[:,0] , k_means.cluster_centers_[:,1] , color='red' , s=200 , marker='X')

plt.title('Cluster Of Customers')
plt.legend()
plt.show()