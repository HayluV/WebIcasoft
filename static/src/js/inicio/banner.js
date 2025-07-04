 const images = document.querySelectorAll('.banner-images img');
    let current = 0;
    setInterval(() => {
      images[current].classList.remove('active');
      current = (current + 1) % images.length;
      images[current].classList.add('active');
    }, 3000);