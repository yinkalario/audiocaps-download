#!/bin/bash

set -e

anaconda_dir='/home/yincao/miniconda3'

. $anaconda_dir'/etc/profile.d/conda.sh'
conda remove -n audiocaps_dl --all -y
conda create -n audiocaps_dl python=3.11 -y
conda activate audiocaps_dl
# pip install -r ./requirements.txt
python -m pip install -e .
python -m pip install -e .[dev]