import os
import glob
import re

base_path = r"e:\Projects\Virasat_Bihar"
html_files = glob.glob(os.path.join(base_path, "*.html"))

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to match the current logo-container
    pattern = r'<div class="logo-container">\s*<a href="index\.html"><img src="assets/logo\.svg".*?></a>\s*</div>'
    
    replacement = """<div class="logo-container">
            <a href="index.html" style="display: flex; align-items: center; text-decoration: none; gap: 15px;">
                <img src="assets/logo.svg" alt="Virasat Bihar Logo" style="height: 60px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
                <h1 style="margin: 0; font-family: 'Cinzel', serif; font-size: 2.2rem; color: var(--accent-color); text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">Virasat Bihar</h1>
            </a>
        </div>"""
        
    content = re.sub(pattern, replacement, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated header with Virasat Bihar text in {len(html_files)} files.")
