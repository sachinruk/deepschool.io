FROM sachinruk/miniconda3

RUN conda install -y \
    h5py \
    pandas \
    jupyter \
    matplotlib \
    seaborn \
    scikit-learn \
    pandas

RUN conda config --append channels conda-forge

RUN conda install -c conda-forge -y pymc3

RUN conda install -y mkl-service

RUN conda clean --yes --tarballs --packages --source-cache

VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888
CMD jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --NotebookApp.token=

