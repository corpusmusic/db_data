import csv

with open('../otherdata.csv') as f:
	reader = csv.reader(f)
	next(reader)
	track_id = set(row[0] for row in reader)
	f.seek(0)
	reader = csv.reader(f)
	next(reader)
	genre = {row[0]: row[1] for row in reader}

#with open('geo_information_nan_location_coordinates.csv') as f:
with open('geo_information_coordinates.csv') as f:
	new_row = [{
	'track_id': row[0],
	'genre': genre[row[0]],
	'location': row[1],
	'latitude': row[2],
	'longitude': row[3],
	} for row in csv.reader(f) if row[0] in track_id]

OUTPUT_FIELDS = [
	'track_id',
	'genre',
	'location',
	'latitude',
	'longitude',
]

#with open('geo_information_nan_location_coordinates_final.csv', "wb") as f:
with open('geo_information_coordinates_final.csv', "wb") as f:
	output = csv.writer(f)
	output.writerow(OUTPUT_FIELDS)
	for row in new_row:
		output.writerow([row[field] for field in OUTPUT_FIELDS])