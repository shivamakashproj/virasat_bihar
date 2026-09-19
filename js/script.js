// js/script.js

document.addEventListener('DOMContentLoaded', () => {
    // Dynamically find all galleries on the page. 
    // To add a new city, admin only needs to copy HTML and change data-city="newcity"
    const galleries = document.querySelectorAll('.image-gallery');
    
    // Max number of images to attempt loading per destination. 
    // Increased to 100 to support "any number of images"
    const maxImagesToTry = 100; 
    
    galleries.forEach(gallery => {
        const dest = gallery.getAttribute('data-city');
        if (!dest) return;

        let imagesLoaded = 0;

        // Try loading images sequentially for multiple formats
        for (let i = 1; i <= maxImagesToTry; i++) {
            
            ['jpg', 'png', 'jpeg', 'webp', 'gif'].forEach(ext => {
                const imgPath = `assets/${dest}/${i}.${ext}`;
                const img = new Image();
                
                img.onload = function() {
                    // If this is the first successfully loaded image, clear the placeholder text
                    if (imagesLoaded === 0) {
                        gallery.innerHTML = '';
                    }
                    
                    img.classList.add('gallery-img');
                    img.alt = `${dest} heritage site image ${i}`;
                    
                    // Add click event for a simple lightbox effect
                    img.style.cursor = 'pointer';
                    img.title = "View Image";
                    
                    img.addEventListener('click', () => {
                        if (typeof openLightbox === 'function') {
                            openLightbox(img.src);
                        }
                    });
                    
                    gallery.appendChild(img);
                    imagesLoaded++;
                };
                
                img.onerror = function() {
                    // Fail silently, allows admin to drop in files without code edits
                };

                img.src = imgPath;
            });
        }
    });

    // Lightbox Setup
    const lightbox = document.createElement('div');
    lightbox.id = 'custom-lightbox';
    
    const lightboxImg = document.createElement('img');
    const closeBtn = document.createElement('span');
    closeBtn.innerHTML = '&times;';
    closeBtn.className = 'lightbox-close';
    
    lightbox.appendChild(lightboxImg);
    lightbox.appendChild(closeBtn);
    document.body.appendChild(lightbox);
    
    closeBtn.addEventListener('click', () => {
        lightbox.style.display = 'none';
    });
    
    lightbox.addEventListener('click', (e) => {
        if (e.target !== lightboxImg) {
            lightbox.style.display = 'none';
        }
    });

    window.openLightbox = function(src) {
        lightboxImg.src = src;
        lightbox.style.display = 'flex';
    };
});
