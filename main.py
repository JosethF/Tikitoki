import csv
import os
import warnings
import requests

warnings.filterwarnings("ignore")
current_path = os.getcwd()
videos_path = os.path.join(current_path, "Resources", "Videos")

def download_video(file_name, download_link):
    respuesta = requests.get(download_link)
    downloaded_file_path = os.path.join(videos_path, file_name + ".mp4")  # Use videos_path to store videos

    with open(downloaded_file_path, "wb") as archivo:
        archivo.write(respuesta.content)

def download_list_videos(file_name):
    path_list_videos =  os.path.join(current_path, "Resources", "Videos_CSV", file_name + ".csv")
    video_count = 0
    with open(path_list_videos, "r") as archivo:
        lector = csv.reader(archivo)
        next(lector, None) # Se salta la primera línea del csv
        for fila in lector:
            if video_count < 10:
                downloaded_video_name = file_name + "_" + str(video_count)
                download_video(downloaded_video_name, fila[3])
                video_count += 1

if __name__ == "__main__":
    download_list_videos("Poetry")