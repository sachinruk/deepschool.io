FROM sachinruk/ds_base

RUN apt-get update && apt-get install -y graphviz
RUN pip install graphviz xgboost

VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888
CMD jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --NotebookApp.token=
