let currentReview = 0;
const reviewSlider = document.getElementById('review-slider');
const totalReviews = reviewSlider.children.length;

function loadReview(index) {
  const reviews = document.querySelectorAll('.review-item');
  reviews.forEach((review, i) => {
    review.style.display = (i === index) ? 'flex' : 'none';  /* Asegúrate de usar 'flex' en vez de 'block' */
  });
}

function moveReview(direction) {
  currentReview += direction;

  if (currentReview < 0) currentReview = totalReviews - 1;
  if (currentReview >= totalReviews) currentReview = 0;
  loadReview(currentReview);
}

loadReview(currentReview);

setInterval(() => {
  moveReview(1);  
}, 3000); 
