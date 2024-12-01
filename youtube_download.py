from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=OKuiyX5k6zg&t=5779s"
youtube_1 = YouTube(url, on_complete_callback=on_progress)
print(youtube_1.title)
print(youtube_1.thumbnail_url)
caption = youtube_1.captions["a.hi"]
caption.save_captions("caption.txt")
print(caption.generate_srt_captions())
videos = youtube_1.streams.get_highest_resolution()
videos.download()


