FROM python:3.10.12
RUN pip install jupyterlab==4.4.2
RUN pip install pandas==2.1.3
RUN pip install gensim==4.3.2
RUN pip install scipy==1.10.1
RUN pip install spacy==3.7.4
RUN pip install ipdb==0.13.13 
RUN pip install scikit-learn==1.6.1
RUN pip install plotly==6.0.1 
RUN pip install jupyterlab-code-formatter==3.0.2
RUN pip install black==25.1.0
RUN pip install isort==6.0.1
RUN pip install spacy==3.7.4
RUN python -m spacy download de_core_news_sm
RUN pip install hnswlib==0.8.0
RUN jupyter server extension enable --py jupyterlab_code_formatter
ENV JUPYTER_CONFIG_DIR /veld/storage/jupyter_config/
WORKDIR /veld/code/

