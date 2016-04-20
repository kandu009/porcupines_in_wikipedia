#!/bin/bash

start_range=$1
end_range=$2
input_file_prefix='enwiki-20160305-pages-meta-current'
input_file_suffix='_flat.json'
output_file_prefix='bq_input_'
output_file_suffix='.csv'

project_root_dir='/home/ravalikandur/git/porcupines_in_wikipedia'

for i in $(seq $start_range $end_range); do
	`python ${project_root_dir}/src/SentimentAnalyzer.py ${project_root_dir}/data/wiki/talkpage/${input_file_prefix}${i}${input_file_suffix} ${project_root_dir}/data/bigquery/sentiment/${output_file_prefix}${i}${output_file_suffix}`
done
