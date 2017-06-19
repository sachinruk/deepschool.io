# Deep Learning Tutorials

The lessons will cover the fundamentals of deep learning.

0. Lesson 0: Introduction to regression.
1. Lesson 1: Penalising weights to fit better (scikit learn intro)
2. Lesson 2: Gradient Descent. Using basic optimisation methods.
3. Lesson 3: Tensorflow intro: zero layer hidden networks (i.e. normal regression).
4. Lesson 4: Tensorflow hidden layer introduction.
5. Lesson 5: Using keras to simplify multi layer neural nets.
6. Lesson 6: Embeddings to deal with categorical data. (Keras)
7. Lesson 7: Word2Vec. Embeddings to visualise words. (Tensorflow)

## Running from Docker images

Use the following commands to run from docker.
```
git clone git@github.com:sachinruk/ml_class.git
cd ml_class
docker-compose up --build
```
Now go to `localhost:8888` on your browser to start using the jupyter notebooks.

Refer to this [Dockerfile](https://github.com/sachinruk/Dockerfiles/blob/master/ML_class/Dockerfile) and [this](https://github.com/sachinruk/Dockerfiles/blob/master/DS_base/Dockerfile) for information on how the docker image was built.
