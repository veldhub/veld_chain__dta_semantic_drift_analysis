# ![veld chain](https://raw.githubusercontent.com/veldhub/.github/refs/heads/main/images/symbol_V_letter.png) veld_chain__veld_chain__dta_semantic_drift_analysis

This repo contains [chain velds](https://zenodo.org/records/13322913) encapsulating semantic drift 
analysis on the 'Deutsches Textarchiv' (https://www.deutschestextarchiv.de/), using static vector
word embeddings, trained with [word2vec](https://code.google.com/archive/p/word2vec/), 
[fastText](https://fasttext.cc/), and [GloVe](https://nlp.stanford.edu/projects/glove/).

## requirements

- git
- docker compose (note: older docker compose versions require running `docker-compose` instead of 
  `docker compose`)

Clone this repo with all its submodules
```
git clone --recurse-submodules https://github.com/veldhub/veld_chain__dta_semantic_drift_analysis.git
```

## how to reproduce

### all steps in one go

If you want to reproduce the entirety this repo, you can do this by running this chain veld (see
inside the file for more information):

**[./veld_step_all.yaml](./veld_step_all.yaml)**

```
docker compose -f veld_step_all.yaml up
```

### individual steps

Alternatively, all workflows can be individually reproduced, as described below. Open their 
respective veld yaml file for more information.

**[./veld_step_1_download.yaml](./veld_step_1_download.yaml)** 

Downloads the corpus including metadata provided by dta at 
https://www.deutschestextarchiv.de/media/download/dta-lingattr-tei_2020-07-27.zip .

```
docker compose -f veld_step_1_download.yaml up
```

**[./veld_step_2_extract.yaml](./veld_step_2_extract.yaml)** 

Extracts and transforms the relevant texts, and merging them into text files per decade. 

```
docker compose -f veld_step_2_extract.yaml up
```


**[./veld_step_3_preprocess_clean.yaml](./veld_step_3_preprocess_clean.yaml)**

Removes sentences which don't have enough textual content.

```
docker compose -f veld_step_3_preprocess_clean.yaml up
```

**[./veld_step_4_train_word2vec.yaml](./veld_step_4_train_word2vec.yaml)** 

Trains word2vec models for each decade.

```
docker compose -f veld_step_4_train_word2vec.yaml up
```

**[./veld_step_5_train_fasttext.yaml](./veld_step_5_train_fasttext.yaml)** 

Trains fastText models for each decade.

```
docker compose -f veld_step_5_train_fasttext.yaml up
```

**[./veld_step_6_train_glove.yaml](./veld_step_6_train_glove.yaml)** 

Trains fastText models for each decade.

```
docker compose -f veld_step_6_train_glove.yaml up
```

**[./veld_step_7_run_embeddings_sql_server.yaml](./veld_step_7_run_embeddings_sql_server.yaml)** 

Starts a postgres + pgvector instance, which will aggregate and harmonize all word embeddings.

```
docker compose -f veld_step_7_run_embeddings_sql_server.yaml up
```

**[./veld_step_8_analyse_semantic_drift.yaml](./veld_step_8_analyse_semantic_drift.yaml)** 

Launches a jupyter notebook (reachable at [http://localhost:8888](http://localhost:8888/) which analyses and compares the semantic differences of all words
between decades.

```
docker compose -f veld_step_8_analyse_semantic_drift.yaml up
```

