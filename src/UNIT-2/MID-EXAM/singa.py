

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen.
    """
    copyOfSongs = songs[:]
    if copyOfSongs[0][2] < max_size:
        finalPlaylist = [copyOfSongs[0][0]]
        size = copyOfSongs[0][2]
    else:
        return []
    copyOfSongs = copyOfSongs[1:]
    copyOfSongs.sort(key=lambda tup: tup[2])
    for s in copyOfSongs:
        if size+s[2] < max_size:
            finalPlaylist.append(s[0])
            size += s[2]
        else:
            break
    return finalPlaylist


songss = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
print(song_playlist(songss, 12))
