FROM continuumio/miniconda3
ADD *.ipynb /home/
RUN pip install numpy scikit-learn pandas matplotlib sklearn scipy
RUN conda install numpy scikit-learn pandas jupyter
