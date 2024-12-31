import requests
import json

url = 'http://127.0.0.1:8000'

global command

#playing song
def play_song(song_name, song_index, songs): 
    status = requests.get(f'{url}/play?song_name={song_name}').text

    def instructions():

        print('INSTRUCTIONS')
        print('1. To play another song type the song number')
        print('2, To pause the song type "pause"')
        print('3. To increase volume type "+"')
        print('4. To decrease volume type "-"')
        print('5. To play next song, type "next"')
        print('6. To play previous song type "prev"')
        print('7. To resume the song type "res"')

        command = input('Enter: ')
        print(command)

        if command == 'next':
            new_song_index = song_index - 2

            status = requests.get(f'{url}/stop').text
            play_song(songs[new_song_index], new_song_index, songs)

            print(f'Playing {song_name}')
        elif command == 'prev':
            new_song_index = song_index - 2

            status = requests.get(f'{url}/stop').text
            play_song(songs[new_song_index], new_song_index, songs)

            print(f'Playing {song_name}')
        elif command == 'res':
            status = requests.get(f'{url}/resume').text
            print(status)
        elif command == 'pause':
            status = requests.get(f'{url}/pause').text
            print(status)
        else:
            instructions()
        instructions()
    instructions()    


#selecting song
def select_song():
    songs = json.loads(requests.post(f'{url}/songs').text)

    for i in range(len(songs)):
        print(f'{songs[i]} -{i + 1}')

    song_index = int(input('Enter song number: '))

    play_song(songs[song_index - 1], song_index, songs)

if __name__ == '__main__':
    select_song()

