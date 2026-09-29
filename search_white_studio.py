import urllib.request
import json
import os
from PIL import Image, ImageOps
import numpy as np

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def search_unsplash_white_bg(query):
    encoded_q = urllib.parse.quote(query + " isolated white background")
    url = f"https://unsplash.com/napi/search/photos?query={encoded_q}&per_page=10"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as res:
            data = json.loads(res.read().decode())
            results = data.get("results", [])
            urls = []
            for r in results:
                raw_url = r.get("urls", {}).get("regular")
                if raw_url:
                    urls.append(raw_url)
            return urls
    except Exception as e:
        print(f"Error searching for {query}: {e}")
        return []

def is_pure_white_bg(image_path):
    try:
        with Image.open(image_path) as im:
            im = im.convert("RGB")
            arr = np.array(im)
            # Sample corners
            c1 = arr[:20, :20, :].mean(axis=(0,1))
            c2 = arr[:20, -20:, :].mean(axis=(0,1))
            c3 = arr[-20:, :20, :].mean(axis=(0,1))
            c4 = arr[-20:, -20:, :].mean(axis=(0,1))
            corners = np.array([c1, c2, c3, c4])
            avg_corner = corners.mean(axis=0)
            lum = avg_corner[0]*0.299 + avg_corner[1]*0.587 + avg_corner[2]*0.114
            # Also check if R, G, B are all > 220
            is_white = (lum >= 215 and avg_corner[0] >= 210 and avg_corner[1] >= 210 and avg_corner[2] >= 210)
            return is_white, lum, avg_corner
    except Exception as e:
        return False, 0, [0,0,0]

print("White studio search helper initialized.")
