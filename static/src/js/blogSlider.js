(function() {
  let blogCurrentIndex = 0;
  const blogSlider = document.getElementById('blog-slider');
  if (!blogSlider) return;
  const blogTotalCards = blogSlider.children.length;

  function blogSlidesToMove() {
    return window.innerWidth <= 768 ? 2 : 4;
  }

  function blogMoveSlider(direction) {
    const moveCount = blogSlidesToMove();

    blogCurrentIndex += direction * moveCount;

    if (blogCurrentIndex < 0) blogCurrentIndex = 0;
    if (blogCurrentIndex > blogTotalCards - moveCount) blogCurrentIndex = blogTotalCards - moveCount;

    const firstCard = blogSlider.children[0];
    const style = getComputedStyle(firstCard);
    const marginRight = parseInt(style.marginRight) || 0;
    const cardWidth = firstCard.offsetWidth + marginRight;

    const offset = -blogCurrentIndex * cardWidth;
    blogSlider.style.transform = `translateX(${offset}px)`;
  }

  window.blogMoveSlider = blogMoveSlider;

  window.addEventListener('resize', () => {
    blogCurrentIndex = 0;
    if (blogSlider) blogSlider.style.transform = 'translateX(0)';
  });
})();
