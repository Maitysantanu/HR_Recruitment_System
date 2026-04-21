#!/bin/bash

python -m scripts.clean
python -m scripts.load_mysql

echo "Pipeline completed" >> logs/pipeline.log