from tqdm import tqdm
import os
from urllib.error import URLError

def bar(stream, path, filename):
    # Open the file in write mode
    with open(os.path.join(path, filename), 'wb') as f:
        # Wrap the stream w tqdm 
        with tqdm(total=stream.filesize, unit='B', unit_scale=True, desc=filename) as pbar:
            # Use iter_chunks to download in chunks
            for chunk in stream.iter_chunks():
                f.write(chunk)  # Chunk to file
                pbar.update(len(chunk))  #keep updating chunk w file size
