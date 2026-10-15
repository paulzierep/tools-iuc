import os
import sys

import yaml

SCHEMAS = ['ENA_study', 'ENA_sample', 'ENA_experiment', 'ENA_run']


def fetch_table_data(table_path):
    data_dict = {}
    with open(table_path) as table_to_load:
        # load headers
        headers = table_to_load.readline().strip('\n').split('\t')
        row_id = 0
        for line in table_to_load.readlines():
            # print(line)
            line_data = line.strip('\n').split('\t')
            row_dict = {}
            for col_num in range(len(headers)):
                col_name = headers[col_num]
                row_dict[col_name] = line_data[col_num]
            data_dict[row_id] = row_dict
            row_id += 1
        return data_dict


all_data_dict = {}
print('YAML -------------')
for schema, table_path in zip(SCHEMAS, sys.argv[1:]):
    # a table can be missing for submissions that do not use it (e.g. a
    # study-only submission) or when the corresponding output is filtered out
    if not os.path.isfile(table_path):
        all_data_dict[schema] = {}
        continue
    all_data_dict[schema] = fetch_table_data(table_path)
print(yaml.dump(all_data_dict))
print('YAML -------------')
