import umap

reducer = umap.UMAP()
embedding = reducer.fit_transform(iris.data)
embedding.shape



