document.addEventListener('DOMContentLoaded', function() {
    const slider = document.getElementById('blog-slider');
    const prevButton = document.querySelector('.arrow-left-blog');
    const nextButton = document.querySelector('.arrow-right-blog');
    const cards = document.querySelectorAll('.portafolio-card');
    let cardsPerPage;
    let currentIndex = 0;

    function setCardsPerPage() {
        if (window.innerWidth <= 480) {
            cardsPerPage = 1;  
        } else if (window.innerWidth <= 768) {
            cardsPerPage = 2;  
        } else {
            cardsPerPage = 3;  
        }
    }

    setCardsPerPage(); 
    window.addEventListener('resize', setCardsPerPage);  

    function moveSlider(direction) {
        if (direction === 'next') {
            currentIndex += cardsPerPage;
            if (currentIndex >= cards.length) {
                currentIndex = 0; 
            }
        } else if (direction === 'prev') {
            currentIndex -= cardsPerPage;
            if (currentIndex < 0) {
                currentIndex = Math.floor(cards.length / cardsPerPage) * cardsPerPage; // Volver al final si va por debajo
            }
        }

        // Actualizar la posición del slider
        slider.style.transform = `translateX(-${(currentIndex / cardsPerPage) * 100}%)`;
    }

    // Agregar eventos a las flechas para mover el slider
    prevButton.addEventListener('click', function() {
        moveSlider('prev');
    });

    nextButton.addEventListener('click', function() {
        moveSlider('next');
    });
});
