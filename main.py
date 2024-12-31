import vlc
import time
from fastapi import FastAPI

app = FastAPI()

volume = 80
song = None

@app.get('/')
def root():
    return 'hello'

@app.get('/play')
def play_song(song_name: str):
    song = vlc.MediaPlayer(f'songs/{song_name}.mp3')
    song.audio_set_volume(volume)
    song.play()
    return 'played song'

@app.post('/vol')
def increase_vol(increase: bool):
    global volume, song

    if song is None:
        return {'error': 'No song is currently playing.'}

    if increase:
        volume = min(100, volume + 5)  # Ensure volume stays within range
    else:
        volume = max(0, volume - 5)    # Ensure volume stays within range

    song.audio_set_volume(volume)
    return {'Volume': volume}
