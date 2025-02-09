import random
import vlc
from pytube import Playlist
import pafy

# Ensure pafy uses yt-dlp
import yt_dlp as youtube_dl

# Manually set the backend
pafy.backend_shared.BaseBackend.yt_dlp = youtube_dl.YoutubeDL

def play_audio(url):
    video = pafy.new(url)
    bestaudio = video.getbestaudio()
    playurl = bestaudio.url
    
    # Create an instance of VLC player
    instance = vlc.Instance()
    player = instance.media_player_new()
    
    # Add media
    media = instance.media_new(playurl)
    player.set_media(media)
    player.play()
    
    # Wait for the media to finish playing
    while True:
        state = player.get_state()
        if state == vlc.State.Ended or state == vlc.State.Error:
            break

def main(playlist_url, random_play=False):
    playlist = Playlist(playlist_url)
    videos = list(playlist.video_urls)
    
    if random_play:
        random.shuffle(videos)
    
    for video_url in videos:
        print(f'Playing audio from {video_url}')
        play_audio(video_url)

if __name__ == "__main__":
    playlist_url = input("Enter YouTube playlist URL: ")
    random_play = input("Play videos randomly? (yes/no): ").strip().lower() == 'yes'
    main(playlist_url, random_play)
