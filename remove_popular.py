import re

files = [r"d:\ai\yumwok\the_pizza_master_app.html", r"d:\ai\yumwok\index.html"]

badge_pattern = re.compile(
    r'\s*\$\{item\.isPopular\s*\?\s*`\s*<span class="[^"]*">\s*POPULAR\s*</span>\s*`\s*:\s*\'\'\}',
    re.MULTILINE
)

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Remove the HTML badge rendering
    content = badge_pattern.sub('', content)

    # 2. Set all isPopular to false in data
    content = re.sub(r'isPopular:\s*true,?', 'isPopular: false,', content)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Removed POPULAR from {fpath}")

print("Successfully removed POPULAR badge from every product!")
