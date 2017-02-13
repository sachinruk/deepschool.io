FROM continuumio/miniconda3
ADD *.ipynb /home/
RUN conda install numpy scikit-learn pandas matplotlib jupyter
