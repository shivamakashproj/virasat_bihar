import os
import glob

base_path = r"e:\Projects\Virasat_Bihar"
html_files = glob.glob(os.path.join(base_path, "*.html"))

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the image logo from the footer
    content = content.replace('<img src="assets/logo.svg" alt="Virasat Bihar Logo" class="footer-logo">\n                ', '')
    content = content.replace('<img src="assets/logo.svg" alt="Virasat Bihar Logo" class="footer-logo">', '')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Removed logo image from footer in {len(html_files)} files.")
