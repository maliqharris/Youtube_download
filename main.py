from pytubefix import YouTube
import argparse

parser = argparse.ArgumentParser()
#req arguments
parser.add_argument("--url")
# parser.add_argument("--url", "--output")
# parser.add_argument("--url", "--output", "resolution")

args = parser.parse_args()
#Make object 
yt = YouTube(f"{args.url}")

print(f'The video you want to download is {yt.title}, Correct? Y/N')
# user has to input y/n

for x in yt.streams:
    list_o_good = []
    if x.is_progressive:
        list_o_good.append(x.resolution)
        if list_o_good.length == 0:
            print("Sorry, no videos were found for quick download! Would you like to check for other video types? Y/N")
            # user has to input Y/N
        elif list_o_good.length == 1:
            print(f"only video resolution found for quick download is {x.resolution}")
            print("Would you like to download or would you like to look for other resolutions avaliable? Y/N")
            # user has to input y or n 
        elif list_o_good.length > 1: 
            print(f"the avaliable resolutions are {list_o_good}")
            print("Would you like to download one of these resolutions? Y/N ")
            # user has to input y or n
            
            

        
        
        
        
    # elif x.mime_type == "video/mp4": 
    #     print(x.itag)
        
# for x in yt.streams.filter(file_extension="mp4"):
#     print(x)
    

# print(yt.streams)







