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
                currentIndex = Math.floor(cards.length / cardsPerPage) * cardsPerPage;
            }
        }

        slider.style.transform = `translateX(-${(currentIndex / cardsPerPage) * 100}%)`;
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
    const productNames = document.querySelectorAll('.scrolling-title'); // Para obtener el nombre del producto

    plusButtons.forEach((button, index) => {
        button.addEventListener('click', function() {
            let quantity = parseInt(quantityDisplays[index].textContent);
            quantityDisplays[index].textContent = quantity + 1;
        });
    });

    minusButtons.forEach((button, index) => {
        button.addEventListener('click', function() {
            let quantity = parseInt(quantityDisplays[index].textContent);
            if (quantity > 1) {
                quantityDisplays[index].textContent = quantity - 1;
            }
        });
    });

    // Agregar productos al carrito
    cartButtons.forEach((button, index) => {
        button.addEventListener('click', function() {
            const productName = productNames[index].textContent;
            const productQuantity = parseInt(quantityDisplays[index].textContent);

            // Guardar el producto y la cantidad en el localStorage
            const cart = JSON.parse(localStorage.getItem('cart')) || [];
            const product = { name: productName, quantity: productQuantity };

            // Verificar si el producto ya está en el carrito
            const existingProduct = cart.find(p => p.name === productName);
            if (existingProduct) {
                existingProduct.quantity += productQuantity;
            } else {
                cart.push(product);
            }

            // Guardar de nuevo el carrito en localStorage
            localStorage.setItem('cart', JSON.stringify(cart));

            // Actualizar el número de productos en el carrito en el header
            updateCartInHeader();
        });
    });

    // Función para actualizar el número de productos en el carrito en el header
    function updateCartInHeader() {
        const cart = JSON.parse(localStorage.getItem('cart')) || [];
        const cartCount = cart.reduce((total, product) => total + product.quantity, 0);

        // Actualizar el número en el icono del carrito en el header
        const cartNumberElement = document.querySelector('.cart-number');
        if (cartNumberElement) {
            cartNumberElement.textContent = cartCount;
        }
    }

    // Llamar a updateCartInHeader al cargar la página para mostrar el número actual
    updateCartInHeader();
});
