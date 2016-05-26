import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
from scipy.stats import chisquare,chi2_contingency
from csv import DictReader

f, (ax1) = plt.subplots(1)

#with open("geo_information_final_cluster.csv") as datafile:
with open("../../millionsongtestset/MSD_master_data.csv") as datafile:
	data = list(DictReader(datafile))

table_dict = {}
genre_ids = {}
genre_id = 0
for track in data:
	#genre = track["genre"].split("|")[0]
	genre = track["genre"]
	if genre not in table_dict.keys():
		table_dict[genre] = {track["topic"]: 0 for track in data}
		genre_ids[genre] = genre_id
		genre_id += 1

for track in data:
	#genre = track["genre"].split("|")[0]
	genre = track["genre"]
	table_dict[genre][track["topic"]] += 1

table = []
for genre in table_dict:
	row = []
	for cluster in table_dict[genre]:
		row.append(table_dict[genre][cluster])
	table.append(row)


with open("genre_topic.csv", "w+") as outfile:
	outfile.write(",".join(table_dict.keys())+"\n")
	for row in table:
		rowString = ""
		for column in row:
			rowString += str(column/sum(row))+","		
		outfile.write(rowString.rstrip(',')+"\n")


for row in table:
	print(row)
'''
print("Chi Squared")
print(chisquare(table))
print("Pearson's Chi Squared")
print(chi2_contingency(table))
'''