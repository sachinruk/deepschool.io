# DeeuL earning Tutorials

In order to run this either install anaconda and tensorflow (or other packages as directed in my Videos). Or run (from the ml_class directory):
```
docker run --rm -p 8888:8888 -v ${PWD}:/notebooks -it jupyter/tensorflow-notebook bash
cd /notebooks
jupyter notebook
```

```
docker build -t kerasimage .
docker run -d -p 8888:8888 -e KERAS_BACKEND=theano -v ${PWD}:/notebook kerasimage
```
