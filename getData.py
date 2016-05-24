#!/usr/bin/env python
import sys
import h5py
sys.path.append('./PythonSrc')
import hdf5_getters as getters
import argparse
import os
import numpy as np
import csv
# get_table = {'track_id': getters.get_track_id(curFile), 'segments_pitches': getters.get_segments_pitches(curFile), 'time_signature_confidence': getters.get_time_signature_confidence(curFile), 'song_hotttnesss': getters.get_song_hotttnesss(curFile), 'artist_longitude': getters.get_artist_longitude(curFile), 'tatums_confidence': getters.get_tatums_confidence(curFile), 'num_songs': getters.get_num_songs(curFile), 'duration': getters.get_duration(curFile), 'start_of_fade_out': getters.get_start_of_fade_out(curFile), 'artist_name': getters.get_artist_name(curFile), 'similar_artists': getters.get_similar_artists(curFile), 'artist_mbtags': getters.get_artist_mbtags(curFile), 'artist_terms_freq': getters.get_artist_terms_freq(curFile), 'release': getters.get_release(curFile), 'song_id': getters.get_song_id(curFile), 'track_7digitalid': getters.get_track_7digitalid(curFile), 'title': getters.get_title(curFile), 'artist_latitude': getters.get_artist_latitude(curFile), 'energy': getters.get_energy(curFile), 'key': getters.get_key(curFile), 'release_7digitalid': getters.get_release_7digitalid(curFile), 'artist_mbid': getters.get_artist_mbid(curFile), 'segments_confidence': getters.get_segments_confidence(curFile), 'artist_hotttnesss': getters.get_artist_hotttnesss(curFile), 'time_signature': getters.get_time_signature(curFile), 'segments_loudness_max_time': getters.get_segments_loudness_max_time(curFile), 'mode': getters.get_mode(curFile), 'segments_loudness_start': getters.get_segments_loudness_start(curFile), 'tempo': getters.get_tempo(curFile), 'key_confidence': getters.get_key_confidence(curFile), 'analysis_sample_rate': getters.get_analysis_sample_rate(curFile), 'bars_confidence': getters.get_bars_confidence(curFile), 'artist_playmeid': getters.get_artist_playmeid(curFile), 'artist_terms_weight': getters.get_artist_terms_weight(curFile), 'segments_start': getters.get_segments_start(curFile), 'artist_location': getters.get_artist_location(curFile), 'loudness': getters.get_loudness(curFile), 'year': getters.get_year(curFile), 'artist_7digitalid': getters.get_artist_7digitalid(curFile), 'audio_md5': getters.get_audio_md5(curFile), 'segments_timbre': getters.get_segments_timbre(curFile), 'mode_confidence': getters.get_mode_confidence(curFile), 'end_of_fade_in': getters.get_end_of_fade_in(curFile), 'danceability': getters.get_danceability(curFile), 'artist_familiarity': getters.get_artist_familiarity(curFile), 'artist_mbtags_count': getters.get_artist_mbtags_count(curFile), 'tatums_start': getters.get_tatums_start(curFile), 'artist_id': getters.get_artist_id(curFile), 'segments_loudness_max': getters.get_segments_loudness_max(curFile), 'bars_start': getters.get_bars_start(curFile), 'beats_start': getters.get_beats_start(curFile), 'artist_terms': getters.get_artist_terms(curFile), 'sections_start': getters.get_sections_start(curFile), 'beats_confidence': getters.get_beats_confidence(curFile), 'sections_confidence': getters.get_sections_confidence(curFile)}

# lst = ['analysis_sample_rate', 'audio_md5', 'danceability', 'duration', 'end_of_fade_in', 'energy', 'key', 'key_confidence', 'loudness', 'mode', 'mode_confidence', 'start_of_fade_out', 'tempo', 'time_signature', 'time_signature_confidence', 'track_id', 'segments_start', 'segments_confidence', 'segments_pitches', 'segments_timbre', 'segments_loudness_max', 'segments_loudness_max_time', 'segments_loudness_start', 'sections_start', 'sections_confidence', 'beats_start', 'beats_confidence', 'bars_start', 'bars_confidence', 'tatums_start', 'tatums_confidence', 'artist_mbtags', 'artist_mbtags_count', 'year']
def getInfo(files):
    data = []
    build_str = ''
    with open(sys.argv[1], 'r') as f:
        contents = f.read()
        c = contents.split()
    f.close()
    print("creating csv with following fields:" + contents)
    for i in c:
        build_str = build_str + i + ','
    build_str = build_str[:-1]
    build_str = build_str + '\n'
    for fil in files:
        curFile = getters.open_h5_file_read(fil)
        d2 = {}
        get_table = {'track_id': getters.get_track_id(curFile), 'segments_pitches': getters.get_segments_pitches(curFile), 'time_signature_confidence': getters.get_time_signature_confidence(curFile), 'song_hotttnesss': getters.get_song_hotttnesss(curFile), 'artist_longitude': getters.get_artist_longitude(curFile), 'tatums_confidence': getters.get_tatums_confidence(curFile), 'num_songs': getters.get_num_songs(curFile), 'duration': getters.get_duration(curFile), 'start_of_fade_out': getters.get_start_of_fade_out(curFile), 'artist_name': getters.get_artist_name(curFile), 'similar_artists': getters.get_similar_artists(curFile), 'artist_mbtags': getters.get_artist_mbtags(curFile), 'artist_terms_freq': getters.get_artist_terms_freq(curFile), 'release': getters.get_release(curFile), 'song_id': getters.get_song_id(curFile), 'track_7digitalid': getters.get_track_7digitalid(curFile), 'title': getters.get_title(curFile), 'artist_latitude': getters.get_artist_latitude(curFile), 'energy': getters.get_energy(curFile), 'key': getters.get_key(curFile), 'release_7digitalid': getters.get_release_7digitalid(curFile), 'artist_mbid': getters.get_artist_mbid(curFile), 'segments_confidence': getters.get_segments_confidence(curFile), 'artist_hotttnesss': getters.get_artist_hotttnesss(curFile), 'time_signature': getters.get_time_signature(curFile), 'segments_loudness_max_time': getters.get_segments_loudness_max_time(curFile), 'mode': getters.get_mode(curFile), 'segments_loudness_start': getters.get_segments_loudness_start(curFile), 'tempo': getters.get_tempo(curFile), 'key_confidence': getters.get_key_confidence(curFile), 'analysis_sample_rate': getters.get_analysis_sample_rate(curFile), 'bars_confidence': getters.get_bars_confidence(curFile), 'artist_playmeid': getters.get_artist_playmeid(curFile), 'artist_terms_weight': getters.get_artist_terms_weight(curFile), 'segments_start': getters.get_segments_start(curFile), 'artist_location': getters.get_artist_location(curFile), 'loudness': getters.get_loudness(curFile), 'year': getters.get_year(curFile), 'artist_7digitalid': getters.get_artist_7digitalid(curFile), 'audio_md5': getters.get_audio_md5(curFile), 'segments_timbre': getters.get_segments_timbre(curFile), 'mode_confidence': getters.get_mode_confidence(curFile), 'end_of_fade_in': getters.get_end_of_fade_in(curFile), 'danceability': getters.get_danceability(curFile), 'artist_familiarity': getters.get_artist_familiarity(curFile), 'artist_mbtags_count': getters.get_artist_mbtags_count(curFile), 'tatums_start': getters.get_tatums_start(curFile), 'artist_id': getters.get_artist_id(curFile), 'segments_loudness_max': getters.get_segments_loudness_max(curFile), 'bars_start': getters.get_bars_start(curFile), 'beats_start': getters.get_beats_start(curFile), 'artist_terms': getters.get_artist_terms(curFile), 'sections_start': getters.get_sections_start(curFile), 'beats_confidence': getters.get_beats_confidence(curFile), 'sections_confidence': getters.get_sections_confidence(curFile)}
        tid = fil.split('/')[-1].split('.')[0]
        # print(c)
        for i in c:
            if i in get_table: 
               d2[i] = get_table[i]
               d2[i] = str(d2[i]).replace('\n','')  
               build_str = build_str + d2[i] + ','
            else:
                print('error: unspecified field')
                exit(0)
        build_str = build_str[:-1]
        # print(build_str[:-1])
        build_str = build_str + '\n'
        curFile.close()
    build_str = build_str.replace('b','').replace("'",'').replace('"','')  
    return (build_str)
    # print(d2)

    # infoList = np.vstack([infoList, curArr])
    # print(infoList)
    # return infoList

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', dest='dirName')
    parser.add_argument(sys.argv[1])
    args = parser.parse_args()
    if args.dirName:
        dirName = args.dirName
    else:
        dirName = '/Users/JU/Downloads/cproject/db_data/subset/'
    files = [dirName + fil for fil in os.listdir(dirName) if fil.endswith('.h5')]
    # print('creating tsv with following fields:',contents)
    infos = getInfo(files)
    # print(infos)
    
    with open('test05.csv', 'w') as f:
        f.write(infos)
    # with open("test02.csv", "w") as csv_file:
    #     writer = csv.writer(csv_file, delimiter=',')
    #     for line in infos.split(','):
    #         print(line)
    #         writer.writerow(line)
    print("done")


if __name__=='__main__':
    main()