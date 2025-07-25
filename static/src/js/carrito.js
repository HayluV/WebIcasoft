document.addEventListener('DOMContentLoaded', function () {
    const carritoContainer = document.getElementById('carrito-items');
    const totalPriceElement = document.getElementById('total-price');
    const checkoutBtn = document.getElementById('checkout-btn');

    // Cargar carrito desde localStorage con validación
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    // Función para sanitizar los productos del carrito
    function sanitizeCart() {
        cart = cart.filter(product =>
            product &&
            product.name &&
            product.quantity &&
            product.quantity > 0
        ).map(product => ({
            ...product,
            price: typeof product.price === 'number' ? product.price : 0,
            quantity: parseInt(product.quantity) || 1
        }));

        localStorage.setItem('cart', JSON.stringify(cart));
    }

    function renderCart() {
        sanitizeCart(); // Limpiamos el carrito antes de mostrar

        if (cart.length === 0) {
            carritoContainer.innerHTML = '<p class="empty-cart">Tu carrito está vacío</p>';
            totalPriceElement.textContent = '0.00';
            return;
        }

        // Crear la estructura de la tabla
        carritoContainer.innerHTML = `
        <table class="cart-table">
            <thead>
                <tr>
                    <th>Producto</th>
                    <th>Precio</th>
                    <th>Cantidad</th>
                    <th>Total</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody id="cart-table-body">
            </tbody>
            <tfoot>
                <tr class="cart-total-row">
                    <td colspan="3">Total del carrito:</td>
                    <td colspan="2" id="cart-grand-total">S/ 0.00</td>
                </tr>
            </tfoot>
        </table>
    `;

        const tableBody = document.getElementById('cart-table-body');
        let total = 0;

        cart.forEach((product, index) => {
            const price = product.price || 0;
            const productTotal = price * product.quantity;
            total += productTotal;

            const row = document.createElement('tr');
            row.className = 'cart-item-row';
            row.innerHTML = `
            <td class="product-info-cell">
                <div class="product-info-container">
                    <img src="${product.image || 'img/default-product.png'}" alt="${product.name}" class="cart-product-image">
                    <div class="product-text-info">
                        <div class="cart-product-title">${product.name}</div>
                        ${product.marca ? `<div class="cart-product-brand">${product.marca}</div>` : ''}
                    </div>
                </div>
            </td>
            <td class="product-price-cell">S/ ${price.toFixed(2)}</td>
            <td class="product-quantity-cell">
                <div class="quantity-controls">
                    <button class="quantity-btn minus-btn" data-index="${index}">-</button>
                    <span class="quantity-value">${product.quantity}</span>
                    <button class="quantity-btn plus-btn" data-index="${index}">+</button>
                </div>
            </td>
            <td class="product-total-cell">S/ ${productTotal.toFixed(2)}</td>
            <td class="product-actions-cell">
                <button class="remove-btn" data-index="${index}">Eliminar</button>
            </td>
        `;

            tableBody.appendChild(row);
        });

        // Actualizar el total general
        document.getElementById('cart-grand-total').textContent = `S/ ${total.toFixed(2)}`;
        totalPriceElement.textContent = total.toFixed(2);
    }

    // El evento click puede permanecer igual, solo asegúrate de que los selectores coincidan
    carritoContainer.addEventListener('click', function (e) {
        const index = e.target.getAttribute('data-index');
        if (index === null || index < 0 || index >= cart.length) return;

        if (e.target.classList.contains('minus-btn')) {
            if (cart[index].quantity > 1) {
                cart[index].quantity--;
            } else {
                cart.splice(index, 1);
            }
        } else if (e.target.classList.contains('plus-btn')) {
            cart[index].quantity++;
        } else if (e.target.classList.contains('remove-btn')) {
            cart.splice(index, 1);
        }

        localStorage.setItem('cart', JSON.stringify(cart));
        updateCartInHeader();
        renderCart();
    });
    // Si existe el checkoutBtn, agregar el evento click, no existe cuando no está logueado
    // Botón de pago
    if (checkoutBtn) {
        checkoutBtn.addEventListener('click', function () {
            if (cart.length === 0) {
                alert('Tu carrito está vacío');
                return;
            }

            const hasInvalidProducts = cart.some(product =>
                typeof product.price !== 'number' || product.price < 0
            );

            if (hasInvalidProducts) {
                alert('Algunos productos en tu carrito tienen precios no válidos. Por favor, actualiza tu carrito.');
                return;
            }

            window.location.href = '/checkout';
        });
    }
    const modalLoginBtn = document.getElementById('modalLogin');
    // Si existe el modalLoginBtn, agregar el evento click
    if (modalLoginBtn) {
        modalLoginBtn.addEventListener('click', function () {
            alert('Por favor, inicia sesión para continuar con la compra.');
        });
    }

    // Actualizar el número en el header
    function updateCartInHeader() {
        const cartNumberElements = document.querySelectorAll('.cart-number');
        const totalItems = cart.reduce((total, product) => total + (product.quantity || 0), 0);

        cartNumberElements.forEach(element => {
            element.textContent = totalItems;
        });
    }

    // Renderizar el carrito al cargar la página
    renderCart();
    updateCartInHeader();
});