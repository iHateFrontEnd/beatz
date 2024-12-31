import vlc
import os
from fastapi import FastAPI

app = FastAPI()

volume = 80
song = None

#root
@app.get('/')
def root():
    return 'Working'

#listing out all songs
@app.post('/songs')
def list_songs():
    songs = os.listdir('../songs') 
    return songs 

#playing a song
@app.get('/play')
def play_song(song_name: str):
    global song
    print(f"Playing song: {song_name}")
    
    song = vlc.MediaPlayer(f'../songs/{song_name}')
    song.audio_set_volume(volume)
    song.play()
    
    return 'played song'

#pausing a song
@app.get('/pause')
def pause_song():
    global song

    if song.is_playing(): 
        song.pause()
        return 'paused the song'
    else:
        return 'No song is currently playing'

#resuming the song
@app.get('/resume')
def resume_song():
    global song

    if song is not None:
        if not song.is_playing():
            song.play()
            return 'resumed the song'
        else:
            return 'Song is already playing'
    else:
        return 'No song has been played yet'

#stopping a song
@app.get('/stop')
def stop_song():
    global song

    if song.is_playing(): 
        song.stop()
        return 'stopped the song'
    else:
        return 'No song is currently playing'