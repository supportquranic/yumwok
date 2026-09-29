import os
from PIL import Image
import numpy as np

img_dir = r"d:\ai\yumwok\images"

files = [
    # Soups
    "hot_sour_soup.jpg", "chicken_corn_soup.jpg", "szechuan_soup.jpg", "thai_clear_soup.jpg", "wok_special_soup.jpg",
    # Appetizers
    "chicken_tempura.jpg", "honey_glazed_wings.jpg", "tempura_prawns.jpg", "chicken_momos.jpg", "chicken_drum_stick.jpg", "dynamite_prawns.jpg",
    # Noodles
    "chicken_chowmein.jpg", "vegetable_chowmein.jpg", "wok_special_chowmein.jpg", "stir_fried_chicken_chilli_noodles.jpg", "stir_fried_beef_chilli_noodles.jpg",
    # Rice
    "egg_fried_rice.jpg", "vegetable_fried_rice.jpg", "chicken_fried_rice.jpg", "masala_rice.jpg", "wok_special_rice.jpg",
    # Main Courses
    "kung_pao.jpg", "szechuan.jpg", "chilli_dry.jpg", "black_pepper.jpg", "mongolian.jpg", "manchurian.jpg", "sweet_sour.jpg", "hot_garlic.jpg", "cashew_nut.jpg", "oyster_sauce.jpg", "bankok_chilli.jpg", "crispy_sesame_beef.jpg"
]

white_list = []
non_white_list = []

for f in files:
    path = os.path.join(img_dir, f)
    if not os.path.exists(path):
        non_white_list.append((f, 0, "File missing"))
        continue
    im = Image.open(path).convert('RGB')
    arr = np.array(im)
    
    # 4 corners
    h, w, _ = arr.shape
    corner_pixels = np.concatenate([
        arr[:25, :25].reshape(-1, 3),
        arr[:25, -25:].reshape(-1, 3),
        arr[-25:, :25].reshape(-1, 3),
        arr[-25:, -25:].reshape(-1, 3)
    ])
    
    # Border 15px
    border_pixels = np.concatenate([
        arr[:15, :].reshape(-1, 3),
        arr[-15:, :].reshape(-1, 3),
        arr[:, :15].reshape(-1, 3),
        arr[:, -15:].reshape(-1, 3)
    ])
    
    corner_mean = corner_pixels.mean(axis=0)
    border_mean = border_pixels.mean(axis=0)
    
    corner_lum = corner_mean[0]*0.299 + corner_mean[1]*0.587 + corner_mean[2]*0.114
    border_lum = border_mean[0]*0.299 + border_mean[1]*0.587 + border_mean[2]*0.114
    
    # Check if pure/near white (luminance > 210 with low color saturation)
    corner_sat = np.std(corner_mean)
    is_white = (corner_lum >= 200 and border_lum >= 190 and corner_sat < 25)
    
    desc = f"Corner Lum: {corner_lum:.1f}/255, Border Lum: {border_lum:.1f}/255, RGB: [{corner_mean[0]:.0f},{corner_mean[1]:.0f},{corner_mean[2]:.0f}]"
    
    if is_white:
        white_list.append((f, corner_lum, desc))
    else:
        non_white_list.append((f, corner_lum, desc))

print(f"TOTAL CHECKED: {len(files)}")
print(f"WHITE STUDIO BACKGROUND: {len(white_list)}")
print(f"NOT WHITE STUDIO BACKGROUND (Dark/Wooden/Cluttered): {len(non_white_list)}\n")

print("=== [NON-WHITE / DARK / TABLE / CLUTTERED BACKGROUNDS] ===")
for name, lum, desc in non_white_list:
    print(f" - {name:<35} | {desc}")

print("\n=== [TRUE WHITE STUDIO BACKGROUNDS] ===")
for name, lum, desc in white_list:
    print(f" - {name:<35} | {desc}")
