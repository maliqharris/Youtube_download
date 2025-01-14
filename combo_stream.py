
from pytubefix import YouTube
import subprocess
import os
from bar import bar



def rest_o_streams(yt, path):
    list_o_bad = []
    for x in yt.streams.filter(file_extension="mp4", progressive=False, only_video=True):
        if x.resolution is not None:
            if x.resolution not in list_o_bad:
                list_o_bad.append(x.resolution)
        # if x.resolution == None:
        #     list_o_bad.pop(x)
    print(f"{list_o_bad} are the avaliable resolutions")
    while True:
        res = input("Type one of the avaliable resolutions to convert and download, for example '360p' ").strip().lower()
        if res in list_o_bad:

            combine_streams(yt,res, path)
        else:
            print("Resolution not in list!")
    
    
    





def combine_streams(yt, res, path):
    
    

        vid = yt.streams.filter(res=res, file_extension="mp4", only_video=True).first()
        sound = yt.streams.filter(only_audio=True, file_extension="mp4").first()

        if not sound:
            print("No audio avaliable for these streams at all!")
            return

        vid_real = vid.download(output_path=path, filename="video_temp.mp4")
        bar(vid, path, "video_temp.mp4")
        sound_real = sound.download(output_path=path, filename="sound_temp.mp4")
        bar(sound, path, "sound_temp.mp4")
        real_title = os.path.join(path, f"{yt.title}.mp4")

        try:
            
            command = ['ffmpeg', '-i', vid_real, '-i', sound_real, '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental', real_title]

            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
            os.remove(vid_real)
            os.remove(sound_real)
            print(f"Downloaded {yt.title} {real_title}")
        except Exception as e:
            print(f"Error merging: {e}")
        

        exit()



