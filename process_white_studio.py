import os
import urllib.request
import numpy as np
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

IMAGES_DIR = r"d:\ai\yumwok\images"
os.makedirs(IMAGES_DIR, exist_ok=True)

# Curated candidates specifically chosen for white studio backgrounds / white bowl on white table
CANDIDATES = {
    "hot_sour_soup": [
        "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=700&q=85",
        "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=700&q=85",
        "https://images.unsplash.com/photo-1617093727343-374698b1b08d?auto=format&fit=crop&w=700&q=85"
    ],
    "chicken_corn_soup": [
        "https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=700&q=85",
        "https://images.unsplash.com/photo-1588566565463-180a5b2090f2?auto=format&fit=crop&w=700&q=85"
    ],
    "szechuan_soup": [
        "https://images.unsplash.com/photo-1617093727343-374698b1b08d?auto=format&fit=crop&w=700&q=85",
        "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=700&q=85"
    ],
    "chicken_tempura": [
        "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=700&q=85",
        "https://images.unsplash.com/photo-1626645738196-c2a7c87a8f58?auto=format&fit=crop&w=700&q=85"
    ],
    "honey_glazed_wings": [
        "https://images.unsplash.com/photo-1567620832903-9fc6debc209f?auto=format&fit=crop&w=700&q=85",
        "https://images.unsplash.com/photo-1527477396000-e27163b481c2?auto=format&fit=crop&w=700&q=85"
    ],
    "tempura_prawns": [
        "https://images.unsplash.com/photo-1559847844-5315695dadae?auto=format&fit=crop&w=700&q=85",
        "https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&fit=crop&w=700&q=85"
    ],
    "chicken_momos": [
        "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=700&q=85",
        "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?auto=format&fit=crop&w=700&q=85"
    ],
    "chicken_drum_stick": [
        "https://images.unsplash.com/photo-1626645738196-c2a7c87a8f58?auto=format&fit=crop&w=700&q=85",
        "https://images.unsplash.com/photo-1567620832903-9fc6debc209f?auto=format&fit=crop&w=700&q=85"
    ],
    "chicken_chowmein": [
        "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=700&q=85",
        "https://images.unsplash.com/photo-1612927601601-6638404737ce?auto=format&fit=crop&w=700&q=85"
    ],
    "vegetable_chowmein": [
        "https://images.unsplash.com/photo-1612927601601-6638404737ce?auto=format&fit=crop&w=700&q=85"
    ],
    "stir_fried_chicken_chilli_noodles": [
        "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=700&q=85"
    ],
    "egg_fried_rice": [
        "https://images.unsplash.com/photo-1512058564366-18510be2db19?auto=format&fit=crop&w=700&q=85",
        "https://images.unsplash.com/photo-1603133872878-684f208fb84b?auto=format&fit=crop&w=700&q=85"
    ],
    "vegetable_fried_rice": [
        "https://images.unsplash.com/photo-1512058564366-18510be2db19?auto=format&fit=crop&w=700&q=85"
    ],
    "masala_rice": [
        "https://images.unsplash.com/photo-1512058564366-18510be2db19?auto=format&fit=crop&w=700&q=85"
    ],
    "kung_pao": [
        "https://images.unsplash.com/photo-1525755662778-989d0524087e?auto=format&fit=crop&w=700&q=85",
        "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=700&q=85"
    ],
    "szechuan": [
        "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=700&q=85"
    ],
    "chilli_dry": [
        "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=700&q=85"
    ],
    "black_pepper": [
        "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=700&q=85"
    ],
    "mongolian": [
        "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=700&q=85"
    ],
    "manchurian": [
        "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=700&q=85"
    ],
    "sweet_sour": [
        "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=700&q=85"
    ],
    "cashew_nut": [
        "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=700&q=85"
    ],
    "oyster_sauce": [
        "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=700&q=85"
    ],
    "bankok_chilli": [
        "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=700&q=85"
    ],
    "crispy_sesame_beef": [
        "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=700&q=85"
    ]
}

print("Testing white studio replacement processing...")
