from pytubefix import YouTube
import argparse
from combo_stream import rest_o_streams
from progressive_stream import download_progressive
parser = argparse.ArgumentParser()
#req arguments
parser.add_argument("--url")
# parser.add_argument("--url", "--output")
# parser.add_argument("--url", "--output", "--resolution")

args = parser.parse_args()
#Make object 
yt = YouTube(f"{args.url}")

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
            rest_o_streams(yt)
            

            
    elif len(list_o_good) == 1:
        print(f"The only video resolution found for quick download is {x.resolution}")
        confirm1 = input(f"Would you like to download or would you like to look for other resolutions avaliable to be converted? 'Y' for download in this resolution or 'N' for search for more").strip().upper()
        if confirm1 == "Y":
            dl2 = x.resolution
            download_progressive(yt,dl2)
        elif confirm1 == "N":
            rest_o_streams(yt) 
            
    elif len(list_o_good) > 1: 
        print(f"the avaliable resolutions for quick download are {list_o_good}")
        confirm2 = input("Would you like to download one of these resolutions? or Search for more resolutions? Y for download one of these resolutions, N for search for more  ").strip().upper()
        # if yes print({list_o_good}
        if confirm2 == "Y":
            dl2 = input("Type one of the avaliable resolutions to convert and download, for example '360p' ")
            download_progressive(yt, dl2)
        elif confirm2 == "N":
            rest_o_streams(yt)

            
            

        
        
        
        
    
        









