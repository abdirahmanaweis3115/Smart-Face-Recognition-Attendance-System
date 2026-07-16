"""
Download required Dlib models and extract them into the `data/` folder.
This script downloads .bz2 archives from dlib.net and decompresses them to .dat.
"""

import os
import urllib.request
import bz2

MODEL_URLS = {
    'shape_predictor_68_face_landmarks.dat':
        'http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2',
    'dlib_face_recognition_resnet_model_v1.dat':
        'http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2',
}

DATA_DIR = 'data'

os.makedirs(DATA_DIR, exist_ok=True)

for name, url in MODEL_URLS.items():
    target = os.path.join(DATA_DIR, name)
    if os.path.exists(target):
        print(f"{target} already exists, skipping download.")
        continue

    bz2_path = target + '.bz2'
    print(f"Downloading {url} -> {bz2_path}...")
    urllib.request.urlretrieve(url, bz2_path)
    print("Download finished, extracting...")

    with bz2.open(bz2_path, 'rb') as f_in:
        data = f_in.read()
        with open(target, 'wb') as f_out:
            f_out.write(data)

    os.remove(bz2_path)
    print(f"Saved {target}")

print("All models are downloaded and ready in the data/ directory.")
