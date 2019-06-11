import os
import json
import csv
import ast

reviews_data = open('reviews.csv', 'w')

csv_writer = csv.writer(reviews_data,delimiter=';', lineterminator='\n')

empresas = ['accenture', 'stefanini', 'ibm', 'totvs', 'algar-tech', 'sonda-it', 'hp-inc', 'dell', 'linx', 'oracle', 'resource-it-solutions', 'ericsson', 'vivo-telefonica-brasil', 'tivit', 'tim', 'claro-brasil', 'b2w-digital', 'concentrix', 'nextel-telecomunicacoes']

csv_writer.writerow(["user", "avaliation"])

for root, dirs, files in os.walk("/home/anamss/workspace/lovemondays-experiment/generate-dataset-spreadsheet/"):
    for name in files:
        if name.endswith((".json")):
            for i in empresas:
                filename = "data/" + i + "/" + name
                actual_json_file = open(filename)
                currentFile  = json.load(actual_json_file)
                csv_writer.writerow(currentFile["user"], currentFile["avaliation"])
reviews_data.close()