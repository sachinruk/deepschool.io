docker pull sachinruk/bayesian_docker
mkdir -p ../data
docker run -d -p 8888:8888 -v $${PWD}:/notebook \
           -v $${PWD}/../data:/notebook/data sachinruk/bayesian_docker
