#coding -*- utf-16 _*-
from csv import DictReader

with open("otherdata.csv") as csvfile:
	data = list(DictReader(csvfile))


for track in data[:-1]:
	track_id = track["track_id"]
	lyrics = track["lyrics"]

	lyricsString = ""
	for word in lyrics.split(" ")[:-1]:
		w = word.split("|")[0]
		c = word.split("|")[1]
		for i in range(int(c)):
			lyricsString += w + " "

	with open("lyrics/%s.txt" % track_id, "w") as outfile:
		outfile.write(lyricsString)