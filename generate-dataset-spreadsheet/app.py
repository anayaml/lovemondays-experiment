import os
import json
import csv
import ast

reviews_data = open('reviews.csv', 'w')

empresas = ['#']
for root, dirs, files in os.walk("#"):
    for name in files:
        if name.endswith((".json")):
            for i in empresas:
                print(i)
                filename = "data/" + i + "/" + name
                currentFile  = open(filename, 'r', encoding="utf8")
                data = json.dump(currentFile.read(), reviews_data)
reviews_data.close()

            