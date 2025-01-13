
def download_progressive(yt,dl2):
    
    # stream = dl.streams.get_by_tag(tag of resolution selected)
    stream = yt.streams.filter(progressive=True, resolution=dl2)
    print("downloading...")
    stream.download()