#!/bin/bash

# setup conda
source ~/miniconda3/etc/profile.d/conda.sh
echo "> Creating a new environment named nlp2024"
conda create --name nlp2024 python=3.11 -y
conda activate nlp2024
pip install polars tqdm gdown -y
echo "> ... done!"