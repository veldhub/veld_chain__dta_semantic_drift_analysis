# ![veld chain](https://raw.githubusercontent.com/veldhub/.github/refs/heads/main/images/symbol_V_letter.png) veld_chain__veld_chain__dta_semantic_drift_analysis

This repo contains [chain velds](https://zenodo.org/records/13322913) encapsulating semantic drift 
analysis on the 'Deutsches Textarchiv' (https://www.deutschestextarchiv.de/), using static vector
word embeddings, trained with [fastText](https://fasttext.cc/), 
[GloVe](https://nlp.stanford.edu/projects/glove/), and 
[word2vec](https://code.google.com/archive/p/word2vec/).

## requirements

- git
- docker compose (note: older docker compose versions require running `docker-compose` instead of 
  `docker compose`)

Clone this repo with all its submodules
```
git clone --recurse-submodules https://github.com/veldhub/veld_chain__dta_semantic_drift_analysis.git
```

## how to reproduce

The following chain velds were used. Open the respective veld yaml file for more information.

**[./veld_step_1_download.yaml](./veld_step_1_download.yaml)** 

Downloads and extracts a corpus including metadata provided by dta at 
https://www.deutschestextarchiv.de/media/download/dta-lingattr-tei_2020-07-27.zip .

```
docker compose -f veld_step_1_download.yaml up
```

