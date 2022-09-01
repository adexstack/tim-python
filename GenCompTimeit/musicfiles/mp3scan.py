# creating custom generators for walking files in our file systes
import os
import fnmatch


def return_full_filename(start, file_name):
    caps_name = file_name.upper()
    for path, directories, files in os.walk(start):
        for file in (d for d in files if fnmatch.fnmatch(d.upper(), caps_name)):
            print(file)
            #yield os.path.join(album_path, album), album


song_list = return_full_filename('music', 'Waterfall.emp3')

for s in song_list:
    print(s)