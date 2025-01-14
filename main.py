from pytubefix import YouTube
import argparse
from combo_stream import rest_o_streams, combine_streams
from progressive_stream import download_progressive
import os

# from image import show_thumbnail


def is_it_youtube(url):
    return "youtu.be" or "youtube" in url.lower()





parser = argparse.ArgumentParser()
#req arguments
parser.add_argument("--url", help="The Url of the youtube video, will give prompts on what resolutions are avaliable.")
# parser.add_argument("--url", "--output")
# parser.add_argument("--url", "--output", "--resolution")
parser.add_argument("--output", required=False, help="The output path you want the video to be downloaded to, add a / at the end for mac os")
parser.add_argument("--resolution", required=False, help="The resolution you want to download the video in")
args = parser.parse_args()


if not is_it_youtube(args.url):
    print("The Url doesnt even come from youtube! This is a youtube downloader! Try again")
    exit()



#Make object 
yt = YouTube(f"{args.url}")

# show_thumbnail(yt.thumbnail_url)




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


if args.output and os.path.exists(os.path.dirname(args.output)):
    path = os.path.dirname(args.output)
else:
    if args.output:
        print(f"{os.path.dirname(args.output)} is not a working path,  downloading to current dir")
    path = os.getcwd() 


    









if args.resolution:
        good = yt.streams.filter(progressive="True", resolution=args.resolution).first()
        if good:
            print(f"Found stream in {args.resolution} for quick download!")
            download_progressive(yt, args.resolution, path)
        else:
            bad = yt.streams.filter(res=args.resolution, file_extension="mp4", only_video=True).first()
            if bad:
                combine_streams(yt, args.resolution, path)
            else:
                print(f"Sorry no videos found in {args.resolution} ")
else:
    rest_o_streams(yt, path)




for x in yt.streams:
    list_o_good = []
    if x.is_progressive:
        list_o_good.append(x.resolution)
    if len(list_o_good) == 0:
        confirm0 = input("Sorry, no videos were found for quick download! Would you like to check for other video types? Y/N").strip().upper()
        if confirm0 == "N":
            print("Okay, exiting application")
            exit()
        elif confirm0 == "Y":
            rest_o_streams(yt, path)
            



            
    elif len(list_o_good) == 1:
        print(f"The only video resolution found for quick download is {x.resolution}")
        confirm1 = input(f"Would you like to download or would you like to look for other resolutions avaliable to be converted? 'Y' for download in this resolution or 'N' for search for more").strip().upper()
        if confirm1 == "Y":
            dl2 = x.resolution
            download_progressive(yt,dl2, path)
        elif confirm1 == "N":
            rest_o_streams(yt, path) 
            



    elif len(list_o_good) > 1: 
        print(f"the avaliable resolutions for quick download are {list_o_good}")
        confirm2 = input("Would you like to download one of these resolutions? or Search for more resolutions? Y for download one of these resolutions, N for search for more  ").strip().upper()
        # if yes print({list_o_good}
        if confirm2 == "Y":
            dl2 = input("Type one of the avaliable resolutions to convert and download, for example '360p' ")
            download_progressive(yt, dl2, path)
        elif confirm2 == "N":
            rest_o_streams(yt, path)

            
            

        
        
        
        
    
        









