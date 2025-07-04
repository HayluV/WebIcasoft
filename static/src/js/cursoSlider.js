document.addEventListener('DOMContentLoaded', () => {
  const slider = document.getElementById('slider');
  const cards = slider.children;
  const totalCards = cards.length;
  let currentIndex = 0;

  function cardsPerView() {
    const vw = window.innerWidth;
    if (vw <= 480) return 1;
    if (vw <= 768) return 2;
    return 4;
  }

  function maxIndex() {
    return Math.max(0, totalCards - cardsPerView());
  }

  function updateSlider() {
    const cardStyle = getComputedStyle(cards[0]);
    const cardWidth = cards[0].offsetWidth
      + parseInt(cardStyle.marginLeft)
      + parseInt(cardStyle.marginRight);

    if (currentIndex < 0) currentIndex = 0;
    if (currentIndex > maxIndex()) currentIndex = maxIndex();

    const offset = -currentIndex * cardWidth;
    slider.style.transform = `translateX(${offset}px)`;
  }

  document.getElementById('arrow-left').addEventListener('click', () => {
    currentIndex--;
    updateSlider();
  });

  document.getElementById('arrow-right').addEventListener('click', () => {
    currentIndex++;
    updateSlider();
  });

  window.addEventListener('resize', () => {
    if (currentIndex > maxIndex()) {
      currentIndex = maxIndex();
    }
    updateSlider();
  });

  updateSlider();
});
