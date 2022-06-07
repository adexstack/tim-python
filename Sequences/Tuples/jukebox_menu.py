from nested_data import albums

print(albums)

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exits:")
    for index, (title, artist, year, song) in enumerate(albums):
        print(index + 1, title)
    choice = int(input())
    if 1 <= choice <= len(albums):
        song_list = albums[choice - 1][3]
    else:
        print("Not a valid album number")
        break
    print("Please choose your song invalid choice exits:")
    for index, (track_number, song) in enumerate(song_list):
        print(index + 1, song)
    song_choice = int(input())
    if 1 <= song_choice <= len(song_list):
        title = song_list[song_choice - 1][SONG_TITLE_INDEX]
        print(f"{title} now playing")
    else:
        print("That is not a valid song number")
    print("=" * 40)
