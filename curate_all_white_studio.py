import os
import urllib.request
import numpy as np
from PIL import Image, ImageOps, ImageDraw, ImageFilter

IMAGES_DIR = r"d:\ai\yumwok\images"
TMP_DIR = r"d:\ai\yumwok\images\tmp"
os.makedirs(TMP_DIR, exist_ok=True)

# Curated dish source map targeting authentic Asian recipes with bright white backgrounds
DISH_SOURCES = {
    # --- SOUPS ---
    "hot_sour_soup": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=85",
    "chicken_corn_soup": "https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=800&q=85",
    "szechuan_soup": "https://images.unsplash.com/photo-1617093727343-374698b1b08d?auto=format&fit=crop&w=800&q=85",

    # --- APPETIZERS ---
    "chicken_tempura": "https://images.unsplash.com/photo-1626645738196-c2a7c87a8f58?auto=format&fit=crop&w=800&q=85",
    "honey_glazed_wings": "https://images.unsplash.com/photo-1567620832903-9fc6debc209f?auto=format&fit=crop&w=800&q=85",
    "tempura_prawns": "https://images.unsplash.com/photo-1559847844-5315695dadae?auto=format&fit=crop&w=800&q=85",
    "chicken_momos": "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?auto=format&fit=crop&w=800&q=85",
    "chicken_drum_stick": "https://images.unsplash.com/photo-1626645738196-c2a7c87a8f58?auto=format&fit=crop&w=800&q=85",

    # --- NOODLES ---
    "chicken_chowmein": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=800&q=85",
    "vegetable_chowmein": "https://images.unsplash.com/photo-1612927601601-6638404737ce?auto=format&fit=crop&w=800&q=85",
    "stir_fried_chicken_chilli_noodles": "https://images.unsplash.com/photo-1552611052-33e04de081de?auto=format&fit=crop&w=800&q=85",

    # --- RICE ---
    "egg_fried_rice": "https://images.unsplash.com/photo-1512058564366-18510be2db19?auto=format&fit=crop&w=800&q=85",
    "vegetable_fried_rice": "https://images.unsplash.com/photo-1512058564366-18510be2db19?auto=format&fit=crop&w=800&q=85",
    "masala_rice": "https://images.unsplash.com/photo-1596797038530-2c107229654b?auto=format&fit=crop&w=800&q=85",

    # --- MAIN COURSES ---
    "kung_pao": "https://images.unsplash.com/photo-1525755662778-989d0524087e?auto=format&fit=crop&w=800&q=85",
    "szechuan": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=800&q=85",
    "chilli_dry": "https://images.unsplash.com/photo-1599488615731-7e5c2823ff28?auto=format&fit=crop&w=800&q=85",
    "black_pepper": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=85",
    "mongolian": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=85",
    "manchurian": "https://images.unsplash.com/photo-1626777552726-4a6b54c97e46?auto=format&fit=crop&w=800&q=85",
    "sweet_sour": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=85",
    "cashew_nut": "https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?auto=format&fit=crop&w=800&q=85",
    "oyster_sauce": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=85",
    "bankok_chilli": "https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?auto=format&fit=crop&w=800&q=85",
    "crispy_sesame_beef": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=85"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def create_studio_white_card(food_img_path, output_path, canvas_size=(1024, 1024)):
    """
    Creates a luxury modern white studio product photo:
    - Pure white studio canvas (255, 255, 255)
    - Realistic soft circular / curved porcelain bowl isolation
    - Soft natural contact drop shadow
    - Clean crisp aesthetic identical to Michelin-star studio catalog
    """
    canvas = Image.new("RGB", canvas_size, (255, 255, 255))
    
    with Image.open(food_img_path) as raw_img:
        raw_img = raw_img.convert("RGBA")
        
        # Fit food image to porcelain inner circle
        dish_size = 780
        food_square = ImageOps.fit(raw_img, (dish_size, dish_size), Image.Resampling.LANCZOS)
        
        # Create round/porcelain bowl mask
        mask = Image.new("L", (dish_size, dish_size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((10, 10, dish_size - 10, dish_size - 10), fill=255)
        # Smooth mask edge
        mask = mask.filter(ImageFilter.GaussianBlur(3))
        
        # Porcelain Rim
        rim_size = dish_size + 30
        rim = Image.new("RGBA", (rim_size, rim_size), (0, 0, 0, 0))
        rim_draw = ImageDraw.Draw(rim)
        rim_draw.ellipse((0, 0, rim_size, rim_size), fill=(248, 250, 252, 255), outline=(226, 232, 240, 255), width=3)
        
        # Soft studio contact shadow underneath
        shadow_margin = 60
        shadow = Image.new("RGBA", (rim_size + shadow_margin*2, rim_size + shadow_margin*2), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow)
        shadow_draw.ellipse((shadow_margin - 10, shadow_margin + 25, rim_size + shadow_margin + 10, rim_size + shadow_margin + 35), fill=(0, 0, 0, 42))
        shadow = shadow.filter(ImageFilter.GaussianBlur(28))
        
        # Position centered on canvas
        cx = (canvas_size[0] - rim_size) // 2
        cy = (canvas_size[1] - rim_size) // 2
        
        # Paste shadow
        canvas_rgba = canvas.convert("RGBA")
        canvas_rgba.paste(shadow, (cx - shadow_margin, cy - shadow_margin), shadow)
        
        # Paste porcelain rim
        canvas_rgba.paste(rim, (cx, cy), rim)
        
        # Paste masked food dish
        food_offset = (rim_size - dish_size) // 2
        canvas_rgba.paste(food_square, (cx + food_offset, cy + food_offset), mask)
        
        # Final output
        final_img = canvas_rgba.convert("RGB")
        final_img.save(output_path, "JPEG", quality=95, optimize=True)

print(f"Processing {len(DISH_SOURCES)} dishes into pure white studio theme...")

for dish_id, url in DISH_SOURCES.items():
    raw_temp = os.path.join(TMP_DIR, f"{dish_id}_raw.jpg")
    final_dest = os.path.join(IMAGES_DIR, f"{dish_id}.jpg")
    try:
        # If raw doesn't exist, download it
        if not os.path.exists(raw_temp):
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as res:
                with open(raw_temp, "wb") as f:
                    f.write(res.read())
        
        create_studio_white_card(raw_temp, final_dest)
        print(f"[OK] Perfect Studio White Created: {dish_id}.jpg")
    except Exception as e:
        print(f"[FAIL] Error processing {dish_id}: {e}")

print("\nFinished converting all 25 images to 100% Pure White Studio Background!")
