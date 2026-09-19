import os
import glob
import re

base_path = r"e:\Projects\Virasat_Bihar"
html_files = glob.glob(os.path.join(base_path, "*.html"))

new_footer = """    <footer class="main-footer">
        <div class="footer-container">
            <div class="footer-nav">
                <a href="index.html">Home</a>
                <a href="index.html#destinations">Destinations</a>
            </div>
            <div class="footer-logo-section">
                <img src="assets/logo.svg" alt="Virasat Bihar Logo" class="footer-logo">
                <h2 class="footer-title">विरासत बिहार</h2>
            </div>
            <div class="footer-nav">
                <a href="about.html">About Us</a>
                <a href="index.html#contact">Contact</a>
            </div>
        </div>
        <p class="copyright">&copy; 2026 Virasat Bihar. All rights reserved.</p>
    </footer>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace old footer
    content = re.sub(r'<footer>\s*<p>&copy; 2026 Virasat Bihar\. All rights reserved\.</p>\s*</footer>', new_footer, content)
    
    # Replace index.html specific hero text
    if os.path.basename(file) == "index.html":
        content = content.replace("<h1>Experience the Royal Heritage</h1>", "<h1>हमारा बिहार</h1>")
        content = content.replace("<p>Journey through the ancient and majestic lands of Bihar</p>", "<p>Experience the Royal Heritage & Soul of Ancient India</p>")
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} HTML files with new footer and text.")
