import numpy as np
from scipy.stats import chisquare
from csv import DictReader

with open("geo_information_final_cluster.csv") as datafile:
	data = list(DictReader(datafile))

genre_ids = {}
genre_id = 0
for track in data:
	if track["genre"] not in genre_ids.keys():
		genre_ids[track["genre"]] = genre_id
		genre_id += 1


genres = [genre_ids[track["genre"]] for track in data]
clusters = [int(track["cluster"]) for track in data]

obs = np.array([genres, clusters]).T

print(chisquare(obs))