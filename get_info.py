#!/usr/bin/env python

import h5py
import PythonSrc.hdf5_getters as getters
import argparse
import os
import sys
import numpy as np

getter_mappings = {	
    'num_songs': getters.get_num_songs,
    'artist_familiarity': getters.get_artist_familiarity,
    'artist_hotttnesss': getters.get_artist_hotttnesss,
    'artist_id': getters.get_artist_id,
    'artist_mbid': getters.get_artist_mbid,
    'artist_playmeid': getters.get_artist_playmeid,
    'artist_7digitalid': getters.get_artist_7digitalid,
    'artist_latitude': getters.get_artist_latitude,
    'artist_longitude': getters.get_artist_longitude,
    'artist_location': getters.get_artist_location,
    'artist_name': getters.get_artist_name,
    'release': getters.get_release,
    'release_7digitalid': getters.get_release_7digitalid,
    'song_id': getters.get_song_id,
    'song_hotttnesss': getters.get_song_hotttnesss,
    'title': getters.get_title,
    'track_7digitalid': getters.get_track_7digitalid,
    'similar_artists': getters.get_similar_artists,
    'artist_terms': getters.get_artist_terms,
    'artist_terms_freq': getters.get_artist_terms_freq,
    'artist_terms_weight': getters.get_artist_terms_weight,
    'analysis_sample_rate': getters.get_analysis_sample_rate,
    'audio_md5': getters.get_audio_md5,
    'danceability': getters.get_danceability,
    'duration': getters.get_duration,
    'end_of_fade_in': getters.get_end_of_fade_in,
    'energy': getters.get_energy,
    'key': getters.get_key,
    'key_confidence': getters.get_key_confidence,
    'loudness': getters.get_loudness,
    'mode': getters.get_mode,
    'mode_confidence': getters.get_mode_confidence,
    'start_of_fade_out': getters.get_start_of_fade_out,
    'tempo': getters.get_tempo,
    'time_signature': getters.get_time_signature,
    'time_signature_confidence': getters.get_time_signature_confidence,
    'track_id': getters.get_track_id,
    'segments_start': getters.get_segments_start,
    'segments_confidence': getters.get_segments_confidence,
    'segments_pitches': getters.get_segments_pitches,
    'segments_timbre': getters.get_segments_timbre,
    'segments_loudness_max': getters.get_segments_loudness_max,
    'segments_loudness_max_time': getters.get_segments_loudness_max_time,
    'segments_loudness_start': getters.get_segments_loudness_start,
    'sections_start': getters.get_sections_start,
    'sections_confidence': getters.get_sections_confidence,
    'beats_start': getters.get_beats_start,
    'beats_confidence': getters.get_beats_confidence,
    'bars_start': getters.get_bars_start,
    'bars_confidence': getters.get_bars_confidence,
    'tatums_start': getters.get_tatums_start,
    'tatums_confidence': getters.get_tatums_confidence,
    'artist_mbtags': getters.get_artist_mbtags,
    'artist_mbtags_count': getters.get_artist_mbtags_count,
    'year': getters.get_year
}

def ndarray_to_string( array ):
    if array.ndim == 1:
        val = '[' + ' '.join(map(str,array)) + ']'
        return val
    else:
        row_strs = []
        for row in array:
            row_strs.append(ndarray_to_string(row))
        return '[' + ''.join(row_strs) + ']'


def get_info(files, getter_list):
    header = ['tid'] + getter_list
    info_list = np.array([header])

    iteration = 0
    total = len(files)
    #print_progress(iteration, total, prefix = 'Progress:', suffix = 'Complete', barLength=50)
    for fil in files:
        fo = getters.open_h5_file_read(fil)

        tid = fil.split('/')[-1].split('.')[0]
        file_data = [tid]

        for getter_str in getter_list:
			
            try:
                getter_func = getter_mappings[getter_str]
            except:
                print "Error: " + getter_str + " is not a valid option."
                exit()
            
            getter_data = getter_func(fo)

            if isinstance(getter_data, np.ndarray):
                getter_data = ndarray_to_string(getter_data)

            file_data.append(getter_data)

        tmp_arr = np.array([file_data])
        info_list = np.concatenate((info_list, tmp_arr), axis=0)

        fo.close()

        iteration+=1
        print_progress(iteration, total, prefix = 'Progress:', suffix = 'Complete', barLength=50)

    return info_list

def print_progress (iteration, total, prefix = '', suffix = '', decimals = 2, barLength = 100):
    filledLength    = int(round(barLength * iteration / float(total)))
    percents        = round(100.00 * (iteration / float(total)), decimals)
    bar             = '#' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('%s [%s] %s%s %s\r' % (prefix, bar, percents, '%', suffix)),
    sys.stdout.flush()
    if iteration == total:
        print("\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', dest='dir_name')
    parser.add_argument('-o', '--out', dest='outfile_name')
    parser.add_argument('-f', '--file', dest='infile_name')
    parser.add_argument('getters', nargs='*')

    args = parser.parse_args()

    if args.dir_name:
        dir_name = args.dir_name
    else:
        dir_name = 'subset/'

    if args.outfile_name:
        outfile_name = args.outfile_name
    else:
        outfile_name = 'data_ouput.csv'

    if args.infile_name:
        try:
            fo = open(args.infile_name, 'r')
            line = fo.readline()
            h5_getters = line.split()

        except:
            print args.infile_name + " does not exist"
            exit()
    else:
        h5_getters = args.getters

    files = [dir_name + fil for fil in os.listdir(dir_name) if fil.endswith('.h5')]

    print "Fetching data..."
    infos = get_info(files, h5_getters)
    
    with open(outfile_name, 'w') as f:
        np.savetxt(f, infos, delimiter=',', fmt="%s")

    print outfile_name + ' created'

if __name__=='__main__':
    main()

