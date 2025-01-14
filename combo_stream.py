
from pytubefix import YouTube
import subprocess
import os
from bar import bar


def rest_o_streams(yt, path):
    # init list_o_bad
    list_o_bad = []
    # find stream that is not progressive and a video 
    for x in yt.streams.filter(file_extension="mp4", progressive=False, only_video=True):
        # but not if resolution is none
        if x.resolution is not None:
            # or a duplicate
            if x.resolution not in list_o_bad:
                # add resolution to list
                list_o_bad.append(x.resolution)
        # if x.resolution == None:
        #     list_o_bad.pop(x)
    # tell user avaliable resolutions
    print(f"{list_o_bad} are the avaliable resolutions")
    # loop so they choose right resolution
    while True:
        # user selects resolution
        res = input("Type one of the avaliable resolutions to convert and download, for example '360p' ").strip().lower()
        # if resolution is in list call combine_streams w res
        if res in list_o_bad:

            combine_streams(yt,res, path)
        # otherwise tell em its not in the list and repeat 
        else:
            print("Resolution not in list!")
    
    
    





def combine_streams(yt, res, path):
        # init var for specific stream w chosen atrib
        vid = yt.streams.filter(res=res, file_extension="mp4", only_video=True).first()
        sound = yt.streams.filter(only_audio=True, file_extension="mp4").first()
        # if no sound then tell user no sound and exit program
        if not sound:
            print("No audio avaliable for these streams at all! Sorry, try again")
            exit()
            
        

        # set var to downloaded files and call bar for a loading bar 
        vid_real = vid.download(output_path=path, filename="video_temp.mp4")
        bar(vid, path, "video_temp.mp4")
        sound_real = sound.download(output_path=path, filename="sound_temp.mp4")
        bar(sound, path, "sound_temp.mp4")
        # set var for path_to_file/file.title
        real_title = os.path.join(path, f"{yt.title}.mp4")


        try:
            #----------------------input video-----input audio--------copy codec   set codec to aac----expir to set to aac---file name
            command = ['ffmpeg', '-i', vid_real, '-i', sound_real, '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental', real_title]
            # gets rid of extra info
            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
            # delete temp files
            os.remove(vid_real)
            os.remove(sound_real)
            print(f"Downloaded {yt.title} {real_title}")
        except Exception as e:
            # tell error if failure
            print(f"Error combining: {e}")
        exit()



