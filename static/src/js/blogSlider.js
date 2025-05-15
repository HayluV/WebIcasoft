let currentSlide = 0;
const blogSlider = document.getElementById('blog-slider');
const totalSlides = blogSlider.children.length;

function moveSlider(direction) {
  currentSlide += direction;
  if (currentSlide < 0) currentSlide = totalSlides - 1;
  if (currentSlide >= totalSlides) currentSlide = 0;

  const offset = -currentSlide * (blogSlider.children[0].offsetWidth + 24); 
  blogSlider.style.transform = `translateX(${offset}px)`;
}
