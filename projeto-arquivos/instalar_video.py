# Instala vídeos do YT
from pytube import YouTube
from pytube.cli import on_progress

link = input("Insira o URL:\n")

yt = YouTube(link, on_progress_callback=on_progress)
print(f"Title: {yt.title} || Views: {yt.views}")
# ys = yt.streams.get_highest_resolution()
# ys.download()
