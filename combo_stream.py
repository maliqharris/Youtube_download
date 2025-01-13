
from pytubefix import YouTube
import subprocess
import os




def rest_o_streams(yt):
    list_o_bad = []
    for x in yt.streams.filter(file_extension="mp4", progressive=False, only_video=True):
        if x.resolution is not None:
            if x.resolution not in list_o_bad:
                list_o_bad.append(x.resolution)
        # if x.resolution == None:
        #     list_o_bad.pop(x)
    print(f"{list_o_bad} are the avaliable resolutions")
    combine_streams(yt, list_o_bad)
    
    exit()





def combine_streams(yt, list_o_bad):
    
    while True:
        res = input("Type one of the avaliable resolutions to convert and download, for example '360p' ").strip().lower()

        if res not in list_o_bad:
            print("Resolution not in avaliable list! Try again")
            continue



        vid = yt.streams.filter(res=res, file_extension="mp4", only_video=True).first()
        sound = yt.streams.filter(only_audio=True, file_extension="mp4").first()

        if not sound:
            print("No audio avaliable for these streams at all!")
            return

        vid_real = vid.download(filename="video_temp.mp4")
        sound_real = sound.download(filename="sound_temp.mp4")

        real_title = f"{yt.title}.mp4"

        try:
            
            command = ['ffmpeg', '-i', vid_real, '-i', sound_real, '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental', real_title]

            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
            os.remove("video_temp.mp4")
            os.remove("sound_temp.mp4")
            print(f"Downloaded {real_title}")
        except Exception as e:
            print(f"Error merging: {e}")
        

        exit()



