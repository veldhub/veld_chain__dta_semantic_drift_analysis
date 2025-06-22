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
RUN pip install jupyterlab-lsp==5.1.1
RUN pip install "python-lsp-server[all]"==1.12.2
RUN jupyter server extension enable --py jupyterlab_code_formatter
RUN apt update
RUN apt install -y libhunspell-dev=1.7.1* hunspell-de-de=20161207*
RUN pip install hunspell==0.5.5
RUN pip install fasttext==0.9.3
RUN pip install psycopg[binary]==3.2.9
RUN pip install pgvector==0.4.1
RUN pip install joblib==1.5.1
ENV JUPYTER_CONFIG_DIR /veld/storage/jupyter_config/
WORKDIR /veld/code/

