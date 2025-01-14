from bar import bar
def download_progressive(yt,dl2, path):
    
    # stream = dl.streams.get_by_tag(tag of resolution selected)
    stream = yt.streams.filter(progressive=True, resolution=dl2).first()
    
    # tell downloading
    print("downloading...")
    #adds load bar
    bar(stream, path, f"{yt.title}.mp4")
    stream.download(output_path=path)
    print(f"{yt.title}.mp4 downloaded")
    exit()