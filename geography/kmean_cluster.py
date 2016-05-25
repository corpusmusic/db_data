#from __future__ import print_function, division, absolute_import, unicode_literals
import csv
import numpy as np
import os
import scipy as sp
from sklearn.cluster import KMeans


def append_cluster_column(filename):
    with open(filename, 'rb') as infile:
        if filename.lower().endswith('.csv'):
            reader = csv.reader(infile)
        if filename.lower().endswith('.tsv'):
            reader = csv.reader(infile, delimiter='\t')
        
        #skip header line
        next(reader, None)

        X = []
        Y = []
        for line in reader:
            Y.append(line[0])
            lon = float(line[4])
            lat = float(line[3])
            X.append([lon, lat])

        K = 15  #number of clusters
        km = KMeans(n_clusters=K, n_init=5000, init='random')
        km.fit(X,Y)

        cluster_num = {}
        for track_id, cluster in zip(Y, km.labels_):
            cluster_num[track_id] = cluster

        with open(os.path.splitext(filename)[0] + '_cluster.csv','wb') as outfile:
            writer = csv.writer(outfile, lineterminator='\n')
            header_row = ['track_id','genre','artist_location','latitude','longitude','cluster']
            writer.writerow(header_row)
            infile.seek(0)
            
            #skip header line
            next(reader, None)
            for line in reader:
                if len(line) > 0:
                    line.append(cluster_num[line[0]])
                    writer.writerow(line)
        
geofile_final = 'geo_information_final.csv'

append_cluster_column(geofile_final)
