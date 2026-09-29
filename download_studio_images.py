import os
import urllib.request
from PIL import Image, ImageOps

IMAGES_DIR = r"d:\ai\yumwok\images"
os.makedirs(IMAGES_DIR, exist_ok=True)

# Curated high-resolution studio food photography URLs (Clean / White studio aesthetic)
PHOTO_MAP = {
    # --- SOUPS ---
    "hot_sour_soup": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=700&q=85",
    "chicken_corn_soup": "https://images.unsplash.com/photo-1603105037880-880cd4edfb0d?auto=format&fit=crop&w=700&q=85",
    "szechuan_soup": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?auto=format&fit=crop&w=700&q=85",
    
    # --- APPETIZERS ---
    "chicken_tempura": "https://images.unsplash.com/photo-1562967914-608f82629710?auto=format&fit=crop&w=700&q=85",
    "honey_glazed_wings": "https://images.unsplash.com/photo-1527477396000-e27163b481c2?auto=format&fit=crop&w=700&q=85",
    "tempura_prawns": "https://images.unsplash.com/photo-1559847844-5315695dadae?auto=format&fit=crop&w=700&q=85",
    "chicken_momos": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=700&q=85",
    "chicken_drum_stick": "https://images.unsplash.com/photo-1567620832903-9fc6debc209f?auto=format&fit=crop&w=700&q=85",
    
    # --- NOODLES ---
    "chicken_chowmein": "https://images.unsplash.com/photo-1585032226651-759b368d7246?auto=format&fit=crop&w=700&q=85",
    "vegetable_chowmein": "https://images.unsplash.com/photo-1612927601601-6638404737ce?auto=format&fit=crop&w=700&q=85",
    "stir_fried_chicken_chilli_noodles": "https://images.unsplash.com/photo-1552611052-33e04de081de?auto=format&fit=crop&w=700&q=85",
    
    # --- RICE ---
    "egg_fried_rice": "https://images.unsplash.com/photo-1603133872878-684f208fb84b?auto=format&fit=crop&w=700&q=85",
    "vegetable_fried_rice": "https://images.unsplash.com/photo-1512058564366-18510be2db19?auto=format&fit=crop&w=700&q=85",
    "masala_rice": "https://images.unsplash.com/photo-1596797038530-2c107229654b?auto=format&fit=crop&w=700&q=85",
    "wok_special_rice": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=700&q=85",
    
    # --- MAIN COURSES ---
    "kung_pao": "https://images.unsplash.com/photo-1525755662778-989d0524087e?auto=format&fit=crop&w=700&q=85",
    "szechuan": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=700&q=85",
    "chilli_dry": "https://images.unsplash.com/photo-1599488615731-7e5c2823ff28?auto=format&fit=crop&w=700&q=85",
    "black_pepper": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=700&q=85",
    "mongolian": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=700&q=85",
    "manchurian": "https://images.unsplash.com/photo-1626777552726-4a6b54c97e46?auto=format&fit=crop&w=700&q=85",
    "sweet_sour": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=700&q=85",
    "hot_garlic": "https://images.unsplash.com/photo-1546069901-d13865d491f9?auto=format&fit=crop&w=700&q=85",
    "cashew_nut": "https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?auto=format&fit=crop&w=700&q=85",
    "oyster_sauce": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=700&q=85",
    "bankok_chilli": "https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?auto=format&fit=crop&w=700&q=85",
    "crispy_sesame_beef": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=700&q=85",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print(f"Downloading {len(PHOTO_MAP)} dish images...")

success_count = 0
for name, url in PHOTO_MAP.items():
    dest_path = os.path.join(IMAGES_DIR, f"{name}.jpg")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            with open(dest_path + ".tmp", "wb") as f:
                f.write(response.read())
        
        # Open and crop/resize to uniform 600x600 high quality square
        with Image.open(dest_path + ".tmp") as img:
            img = img.convert("RGB")
            img_square = ImageOps.fit(img, (600, 600), Image.Resampling.LANCZOS)
            img_square.save(dest_path, "JPEG", quality=90, optimize=True)
            
        if os.path.exists(dest_path + ".tmp"):
            os.remove(dest_path + ".tmp")
            
        print(f"[OK] Saved: {name}.jpg (600x600)")
        success_count += 1
    except Exception as e:
        print(f"[FAIL] Failed for {name}: {e}")

print(f"\nDone! Successfully downloaded & processed {success_count}/{len(PHOTO_MAP)} images.")
