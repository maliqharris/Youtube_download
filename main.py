from pytubefix import YouTube
import argparse
from combo_stream import rest_o_streams, combine_streams
from progressive_stream import download_progressive
import os


# developing feature
# from image import show_thumbnail

# Check if url is plausable 
def is_it_youtube(url):
    return "youtu.be" or "youtube" in url.lower()





parser = argparse.ArgumentParser()
#req argument
parser.add_argument("--url", help="The Url of the youtube video, will give prompts on what resolutions are avaliable.")
# Set required to False , optional
parser.add_argument("--output", required=False, help="The output path you want the video to be downloaded to, add a / at the end for mac os")
parser.add_argument("--resolution", required=False, help="The resolution you want to download the video in")

args = parser.parse_args()

# if not a plausable url then tell user and exit
if not is_it_youtube(args.url):
    print("The Url doesnt even come from youtube! This is a youtube downloader! Try again")
    exit()



#Make youtube object 
yt = YouTube(f"{args.url}")


# feature being worked on
# show_thumbnail(yt.thumbnail_url)




# While loop to ask if the user has the right video url
while True:
    confirm = input(f'The video you want to download is {yt.title}, Correct? Y/N').strip().upper()
    if confirm == 'Y':
        break
    # exit loop
    elif confirm == 'N':
        print("Try again with the right URL!")
        exit()
        # exit who thing
    else:
        print("Wrong input! Enter Y or N!")
        # loop keeps going 

# if the user inputed output path and that path is real then set path variable
if args.output and os.path.exists(os.path.dirname(args.output)):
    path = os.path.dirname(args.output)
else:
    # if user inputed output path is not a real path then tell the user and download to current dir
    if args.output:
        print(f"{os.path.dirname(args.output)} is not a working path,  downloading to current dir")
    path = os.getcwd() 


    








# if user inputed the resolution we check if their is a progressive stream
if args.resolution:
        good = yt.streams.filter(progressive="True", resolution=args.resolution).first()
        # if we find a stream with the resolution provided we tell user and we call download_progressive to download
        if good:
            print(f"Found stream in {args.resolution} for quick download!")
            download_progressive(yt, args.resolution, path)
        else:
            # if their is no stream that is progressive check if their is a stream that is not progressive
            bad = yt.streams.filter(res=args.resolution, file_extension="mp4", only_video=True).first()
            # if their is then we call combine_streams with those param
            if bad:
                combine_streams(yt, args.resolution, path)
            # if not we tell user that there is no videos in that resolution and then call rest_o_streams to tell user avaliable resolutions
            else:
                print(f"Sorry no videos found in {args.resolution} ")
                rest_o_streams(yt, path)




#for every object in streams
for x in yt.streams:
    # init list_o_good 
    list_o_good = []
    # if progressive add resolution to good list
    if x.is_progressive:
        list_o_good.append(x.resolution)
    # if no progresive streams then tell user that and ask if they would like to check the non progressive streams
    if len(list_o_good) == 0:
        confirm0 = input("Sorry, no videos were found for quick download! Would you like to check for other video types? Y/N").strip().upper()
        # If no then exit
        if confirm0 == "N":
            print("Okay, exiting application")
            exit()
        # if yes then call rest_o_streams
        elif confirm0 == "Y":
            rest_o_streams(yt, path)
            



    # if progressive streams only has one value 
    elif len(list_o_good) == 1:
        # tell user that
        print(f"The only video resolution found for quick download is {x.resolution}")
        # ask if they would like to look for more streamns
        confirm1 = input(f"Would you like to download or would you like to look for other resolutions avaliable to be converted? 'Y' for download in this resolution or 'N' for search for more").strip().upper()
        # if yes then d
        if confirm1 == "Y":
            # init resolution chosen and call download_progressive
            dl2 = x.resolution
            download_progressive(yt,dl2, path)
        # if no then call rest_o_streams
        elif confirm1 == "N":
            rest_o_streams(yt, path) 
            


    # if list is longer than 1 for progressive streams
    elif len(list_o_good) > 1: 
        # teel user that and show the progressive streams
        print(f"the avaliable resolutions for quick download are {list_o_good}")
        # ask if they would want to dl one of these progressive stream resolutions or search for more res that are non progre
        confirm2 = input("Would you like to download one of these resolutions? or Search for more resolutions? Y for download one of these resolutions, N for search for more  ").strip().upper()
        # if yes 
        if confirm2 == "Y":
            # init the resolution  and pass to download_progressive
            dl2 = input("Type one of the avaliable resolutions to convert and download, for example '360p' ")
            download_progressive(yt, dl2, path)
        # if no 
        elif confirm2 == "N":
            # call rest_o_streams
            rest_o_streams(yt, path)

            
            

        
        
        
        
    
        









