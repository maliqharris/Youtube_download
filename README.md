# YouTube Video Downloader !

A program for downloading YouTube videos

## Features

- Download YouTube videos in different resolutions.
- Downloads progressive streams(quick download) or combining video and audio streams.
- Customize output path for downloaded videos.
- Validate and confirm the URL before starting the download.
- Handle different video resolutions for best quality.

## Requirements

Install the required dependencies. You can install them via the `requirements.txt` file.
use pip install -r requirements.txt 

## Istructions 

Command line takes in url argument like so 
python main.py --url "link-to-youtube-video"

the only required argument is url. 

### Their are 2 optional arguments!

resolution and output !

### Call like:

python main.py --url "link-to-youtube-video" --resolution "resolution_you_want_for_example_360p"
python main.py --url "link-to-youtube-video" --output "path_to_where_you_want_video"

### or for all 3:

python main.py --url "link-to-youtube-video" --resolution "resolution_you_want_for_example_360p" --output "path_to_where_you_want_video"


## Use python main.py help for a reminder

# If using mac os try brew install ffmpeg if getting error not found



