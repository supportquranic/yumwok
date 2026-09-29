import urllib.request
import re
import os

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

KEYWORDS = {
    # Soups
    "hot_sour_soup": "hot-and-sour-soup",
    "chicken_corn_soup": "corn-soup",
    "szechuan_soup": "asian-spicy-soup",
    
    # Appetizers
    "chicken_tempura": "chicken-tempura",
    "honey_glazed_wings": "glazed-chicken-wings",
    "tempura_prawns": "tempura-prawns",
    "chicken_momos": "momos-dumplings",
    "chicken_drum_stick": "fried-chicken-drumsticks",
    
    # Noodles
    "chicken_chowmein": "chicken-chow-mein",
    "vegetable_chowmein": "vegetable-noodles",
    "stir_fried_chicken_chilli_noodles": "spicy-chili-noodles",
    
    # Rice
    "egg_fried_rice": "egg-fried-rice",
    "vegetable_fried_rice": "vegetable-fried-rice",
    "masala_rice": "spicy-fried-rice",
    
    # Main Courses
    "kung_pao": "kung-pao-chicken",
    "szechuan": "sichuan-chicken",
    "chilli_dry": "chilli-chicken",
    "black_pepper": "black-pepper-beef",
    "mongolian": "mongolian-beef",
    "manchurian": "chicken-manchurian",
    "sweet_sour": "sweet-and-sour-chicken",
    "cashew_nut": "cashew-chicken",
    "oyster_sauce": "beef-with-mushrooms-oyster-sauce",
    "bankok_chilli": "thai-basil-chicken",
    "crispy_sesame_beef": "sesame-beef"
}

def get_photos(keyword):
    url = f"https://unsplash.com/s/photos/{keyword}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode("utf-8")
            # Extract photo ids
            matches = re.findall(r"photo-([0-9a-f\-]{10,})\?", html)
            seen = set()
            urls = []
            for pid in matches:
                if pid not in seen:
                    seen.add(pid)
                    urls.append(f"https://images.unsplash.com/photo-{pid}?auto=format&fit=crop&w=800&q=85")
            return urls
    except Exception as e:
        print(f"Error fetching {keyword}: {e}")
        return []

print("Searching exact dish photos...")
found_map = {}
for dish_id, kw in KEYWORDS.items():
    urls = get_photos(kw)
    if not urls:
        # Fallback keyword
        fallback_kw = kw.split("-")[0]
        urls = get_photos(fallback_kw)
    found_map[dish_id] = urls
    print(f" - {dish_id:<35} ({kw}): found {len(urls)} candidates")

print("Done scanning candidate photos.")
