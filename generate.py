import os
import shutil
import re

districts = [
    "Araria", "Arwal", "Aurangabad", "Banka", "Begusarai", "Bhagalpur", "Bhojpur", "Buxar",
    "Darbhanga", "Gopalganj", "Jamui", "Jehanabad", "Kaimur", "Katihar", "Khagaria", "Kishanganj",
    "Lakhisarai", "Madhepura", "Madhubani", "Munger", "Muzaffarpur", "Nawada", "Purnia", "Rohtas",
    "Saharsa", "Samastipur", "Saran", "Sheikhpura", "Sheohar", "Sitamarhi", "Siwan", "Supaul",
    "East Champaran", "West Champaran"
]

base_path = r"e:\Projects\Virasat_Bihar"
template_path = os.path.join(base_path, "vaishali.html")

with open(template_path, "r", encoding="utf-8") as f:
    template_content = f.read()

placeholder_img = os.path.join(base_path, "assets", "background.jpg")
dashboard_links = []

for district in districts:
    lower_name = district.lower().replace(" ", "_")
    asset_dir = os.path.join(base_path, "assets", lower_name)
    os.makedirs(asset_dir, exist_ok=True)
    
    dest_img = os.path.join(asset_dir, "1.jpg")
    if not os.path.exists(dest_img):
        shutil.copy(placeholder_img, dest_img)

    html_content = template_content
    
    # Replace specific long texts BEFORE replacing 'Vaishali'
    html_content = html_content.replace(
        "Vaishali holds the glory of being the world's first republic. It is closely associated with Mahavira and Lord Buddha, standing as a pillar of ancient Indian history.",
        f"{district} is one of the beautiful and culturally rich districts of Bihar, offering a unique blend of heritage, local traditions, and historical significance."
    )
    
    html_content = re.sub(
        r'<li>Visit the Ashokan Pillar</li>\s*<li>Explore the Buddha Stupas</li>\s*<li>See the coronation tank \(Abhishek Pushkarini\)</li>',
        "<li>Explore local heritage sites</li>\n                        <li>Experience the vibrant culture</li>\n                        <li>Visit historical monuments</li>",
        html_content
    )
    
    html_content = html_content.replace(
        "It's located about an hour's drive from Patna. Hiring a private cab from Patna is the most convenient way to explore Vaishali.",
        "Plan your trip during the festive seasons to experience the true essence of the region."
    )

    # Replace the remaining occurrences of Vaishali
    html_content = html_content.replace("Vaishali", district)
    html_content = html_content.replace("vaishali", lower_name)

    html_path = os.path.join(base_path, f"{lower_name}.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    link = f"""                <a href="{lower_name}.html" class="city-box" style="background-image: url('assets/{lower_name}/1.jpg');">
                    <div class="city-box-overlay"></div>
                    <h3>{district}</h3>
                </a>"""
    dashboard_links.append(link)

index_path = os.path.join(base_path, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

# Using regex to find the end of dashboard-grid section
pattern = re.compile(r'(</div>\s*</section>\s*</main>)')
if pattern.search(index_content):
    # Insert new links right before the closing tags
    new_index = pattern.sub('\n' + '\n'.join(dashboard_links) + r'\n        \1', index_content)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_index)
    print("Successfully updated index.html")
else:
    print("ERROR: Could not find insertion marker in index.html")

print(f"Generated {len(districts)} new districts.")
