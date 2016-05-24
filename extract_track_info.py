import os
import sqlite3

track_ids = []
for root, dirnames, files in os.walk("subset"):
	for filename in files:
		track_ids.append(filename.rstrip(".h5"))


print track_ids