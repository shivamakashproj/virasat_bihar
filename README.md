# 🏛️ Virasat Bihar - Experience the Royal Heritage

<div align="center">
  <h3>A Digital Journey Through the Ancient and Majestic Lands of Bihar</h3>
  <p><strong>HTML5 | CSS3 | JavaScript | Responsive Design</strong></p>
</div>

---

## 🎯 Objective
**Virasat Bihar** is an aesthetic, static web application designed to promote the rich cultural, historical, and spiritual heritage of Bihar. The project aims to serve as a digital "Royal Emissary," guiding tourists and history enthusiasts through all 38 districts of Bihar. It showcases essential travel information, historical overviews, and immersive image galleries in a highly responsive, user-friendly, and visually stunning format.

## ⚠️ Problem Statement
Despite being the birthplace of major world religions (Buddhism and Jainism), home to the world's oldest university (Nalanda), and the center of ancient Indian empires (Magadha), Bihar's tourism potential remains vastly underrepresented on the modern web. Existing regional tourism sites often lack a cohesive, visually appealing "heritage" aesthetic or are too complex to navigate. **Virasat Bihar** solves this by providing a clean, distraction-free, and immersive user experience with a scalable architecture that allows easy content management without requiring a complex backend database.

---

## 🚀 Key Features
- **Comprehensive Coverage:** Dedicated detail pages for all 38 districts of Bihar.
- **Dynamic Image Galleries:** An automated JavaScript gallery loading system that builds grids seamlessly.
- **Fully Responsive Architecture:** Flawless layout scaling across Desktop, Tablet, and Mobile screens.
- **Heritage Aesthetic:** Custom UI/UX featuring elegant fonts ('Cinzel' & 'Playfair Display'), Chhath Puja thematic backgrounds, and a royal creamy-brown color palette.
- **Direct Admin Contact:** Integrated direct-to-app links for WhatsApp, Email, and Phone calls for instant travel inquiries.

---

## 🛠️ Admin Guide: How to Manage Content

The architecture of this project is highly scalable and requires **zero coding knowledge** for the admin to update images!

### 1. Updating the Destination Galleries
Inside the `assets/` folder, you will find subfolders for every district (e.g., `assets/patna/`, `assets/rajgir/`).
*   Save your high-quality images as `.jpg` or `.png`.
*   Name them sequentially using numbers: `1.jpg`, `2.jpg`, `3.jpg`, etc.
*   Place them in the respective district's folder.
*   *The website's custom JavaScript will automatically detect and display them in the beautiful gallery grid!*

### 2. Updating Contact Information
If you need to update the phone number or email:
1. Open any HTML file in a code editor (e.g., `index.html`).
2. Scroll to the bottom to the `<section class="inquiry-footer">`.
3. Update the WhatsApp link (`href="https://wa.me/..."`), phone link (`href="tel:..."`), and email link (`href="mailto:..."`).

---

## 🔮 Future Enhancements
- [ ] **Interactive Web Map:** A clickable SVG map of Bihar on the dashboard to select districts geographically instead of just a grid.
- [ ] **Multi-language Support:** Add Hindi, Bhojpuri, and Maithili translations for better regional accessibility and connection.
- [ ] **Backend / CMS Integration:** Migrate from a static file architecture to a Content Management System (like Node.js/MongoDB or Firebase) to allow admins to upload images directly via a secure web portal.
- [ ] **Virtual Tours (360°):** Integrate 360-degree panoramic views of historical monuments like the Golghar, Bodhi Tree, and Nalanda Ruins.
- [ ] **Booking API Integration:** Connect with local tour guides, transport services, and hotels for direct booking.

---
<div align="center">
  <p><i>Made with ❤️ to celebrate the golden heritage of Bihar.</i></p>
</div>
