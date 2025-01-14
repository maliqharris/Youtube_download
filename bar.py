from tqdm import tqdm
import os

def bar(stream, path, filename):
    # Open the file in binary write mode
    with open(os.path.join(path, filename), 'wb') as f:
        # Wrap the stream in tqdm to show the progress bar
        with tqdm(total=stream.filesize, unit='B', unit_scale=True, desc=filename) as pbar:
            # Use iter_chunks to download the stream in manageable chunks
            for chunk in stream.iter_chunks():
                f.write(chunk)  # Write the chunk to the file
                pbar.update(len(chunk))  # Update the progress bar with the chunk size
