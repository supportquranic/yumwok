import re
import os

files = [r"d:\ai\yumwok\the_pizza_master_app.html", r"d:\ai\yumwok\index.html"]

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Update Hero banner image to local kung_pao.jpg
    content = content.replace(
        'src="https://images.unsplash.com/photo-1525755662778-989d0524087e?auto=format&fit=crop&w=300&q=80"',
        'src="images/kung_pao.jpg"'
    )

    # Replace all unsplash images inside the item definitions with local images/{id}.jpg
    # Pattern 1: without price field before image
    pattern1 = re.compile(r"(id:\s*'([a-z0-9_]+)',\s*category:\s*'[^']+',\s*name:\s*'[^']+',\s*desc:\s*'[^']+',\s*image:\s*)'https://[^']+'")
    content = pattern1.sub(r"\1'images/\2.jpg'", content)

    # Pattern 2: with price field before image
    pattern2 = re.compile(r"(id:\s*'([a-z0-9_]+)',\s*category:\s*'[^']+',\s*name:\s*'[^']+',\s*desc:\s*'[^']+',\s*price:\s*\d+,\s*image:\s*)'https://[^']+'")
    content = pattern2.sub(r"\1'images/\2.jpg'", content)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated image paths in {fpath}")

print("All HTML files updated successfully!")
