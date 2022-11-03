## https://github.com/johnwmillr/LyricsGenius

import lyricsgenius
token = 'UqUj62xJC7doECrI5R49JPYoJSmzAE3EhNLBLtAj_t4R4pOQ3I5u2I4olJUp0vqU'
genius = lyricsgenius.Genius(token)

# Turn off status messages
genius.verbose = False

# Remove section headers (e.g. [Chorus]) from lyrics when searching
genius.remove_section_headers = True

# Include hits thought to be non-songs (e.g. track lists)
genius.skip_non_songs = False


artist = "Los Campesinos!"
song = "We've Got Your Back"

#artist = genius.search_artist("Say Anything", max_songs=5)
song = genius.search_song(song, artist)
lyrics_new_line_breaks = song.lyrics
print(lyrics_new_line_breaks)

lyrics = lyrics_new_line_breaks.replace("\n", " ")
print(lyrics)

#song.save_lyrics()