import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
from scipy.stats import chisquare
from csv import DictReader

f, (ax1) = plt.subplots(1)

with open("geo_information_final_cluster.csv") as datafile:
	data = list(DictReader(datafile))

table_dict = {}
genre_ids = {}
genre_id = 0
for track in data:
	genre = track["genre"].split("|")[0]
	if genre not in table_dict.keys():
		table_dict[genre] = {track["cluster"]: 0 for track in data}
		genre_ids[genre] = genre_id
		genre_id += 1

for track in data:
	genre = track["genre"].split("|")[0]
	table_dict[genre][track["cluster"]] += 1

table = []
for genre in table_dict:
	row = []
	for cluster in table_dict[genre]:
		row.append(table_dict[genre][cluster])
	table.append(row)

pprint(table)

print(chisquare(table))