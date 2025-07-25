document.addEventListener('DOMContentLoaded', function() {
    const slider = document.getElementById('productos-top-slider');
    const prevButton = document.querySelector('.arrow-left');
    const nextButton = document.querySelector('.arrow-right');
    const cards = document.querySelectorAll('.producto-card');
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
    window.addEventListener('resize', function() {
        setCardsPerPage();
        updateSliderPosition();
    });

    function updateSliderPosition() {
        slider.style.transform = `translateX(-${(currentIndex / cardsPerPage) * 100}%)`;
    }

    function moveSlider(direction) {
        if (direction === 'next') {
            currentIndex += cardsPerPage;
            if (currentIndex >= cards.length) {
                currentIndex = 0;
            }
        } else if (direction === 'prev') {
            currentIndex -= cardsPerPage;
            if (currentIndex < 0) {
                currentIndex = Math.max(0, Math.floor((cards.length - 1) / cardsPerPage) * cardsPerPage);
            }
        }
        updateSliderPosition();
    }

    prevButton.addEventListener('click', function() {
        moveSlider('prev');
    });

    nextButton.addEventListener('click', function() {
        moveSlider('next');
    });

    // Agregar funcionalidad para incrementar y decrementar la cantidad
    const plusButtons = document.querySelectorAll('.plus-btn');
    const minusButtons = document.querySelectorAll('.minus-btn');
    const quantityDisplays = document.querySelectorAll('.quantity-display');
    const cartButtons = document.querySelectorAll('.cart-btn');
    const productNames = document.querySelectorAll('.scrolling-title');

    plusButtons.forEach((button, index) => {
        button.addEventListener('click', function() {
            let quantity = parseInt(quantityDisplays[index].textContent) || 0;
            quantityDisplays[index].textContent = quantity + 1;
        });
    });

    minusButtons.forEach((button, index) => {
        button.addEventListener('click', function() {
            let quantity = parseInt(quantityDisplays[index].textContent) || 0;
            if (quantity > 0) {
                quantityDisplays[index].textContent = quantity - 1;
            }
        });
    });

    cartButtons.forEach((button, index) => {
        button.addEventListener('click', function() {
            const quantity = parseInt(quantityDisplays[index].textContent) || 0;
            if (quantity <= 0) {
                alert('Por favor seleccione al menos 1 producto');
                return;
            }

            const productCard = this.closest('.producto-card');
            const product = {
                id: index,
                name: productNames[index].textContent,
                marca: productCard.querySelector('.producto-marca').textContent.trim(),
                price: parseFloat(productCard.querySelector('.text-xl').textContent.replace('S/ ', '')),
                image: productCard.querySelector('img').src,
                quantity: quantity
            };

            let cart = JSON.parse(localStorage.getItem('cart')) || [];
            
            const existingProduct = cart.find(p => p.id === product.id);
            if (existingProduct) {
                existingProduct.quantity += product.quantity;
            } else {
                cart.push(product);
            }

            localStorage.setItem('cart', JSON.stringify(cart));
            updateCartInHeader();
            
            // Reset quantity after adding to cart
            quantityDisplays[index].textContent = '0';
            
            // Notificación de producto agregado
            alert(`${product.quantity} ${product.name} agregado(s) al carrito`);
        });
    });

    // Función para actualizar el número de productos en el carrito en el header
    function updateCartInHeader() {
        const cart = JSON.parse(localStorage.getItem('cart')) || [];
        const cartCount = cart.reduce((total, product) => total + product.quantity, 0);

        const cartNumberElement = document.querySelector('.cart-number');
        if (cartNumberElement) {
            cartNumberElement.textContent = cartCount;
        }
    }

    // Llamar a updateCartInHeader al cargar la página para mostrar el número actual
    updateCartInHeader();
});