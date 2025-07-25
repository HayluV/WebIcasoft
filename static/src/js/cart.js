// static/src/js/cart.js
document.addEventListener('DOMContentLoaded', function() {
    // Función para actualizar el contador del carrito en TODAS las páginas
    function updateCartCounter() {
        const cart = JSON.parse(localStorage.getItem('cart')) || [];
        const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
        
        // Actualiza todos los contadores del carrito en la página
        document.querySelectorAll('.cart-number').forEach(el => {
            el.textContent = totalItems;
        });
    }

    // Actualizar al cargar la página
    updateCartCounter();

    // Escuchar eventos personalizados cuando el carrito se actualice
    document.addEventListener('cartUpdated', updateCartCounter);
    
    // Lógica para añadir cursos al carrito
    document.querySelectorAll('.btn-carrito').forEach(button => {
        button.addEventListener('click', function() {
            const cursoCard = this.closest('.curso-card');
            const curso = {
                name: document.querySelector('.titulo-curso').textContent.trim(),
                price: document.querySelector('.precio').textContent.trim(),
                image: cursoCard.querySelector('.curso-imagen').src,
                quantity: 1
            };
            
            let cart = JSON.parse(localStorage.getItem('cart')) || [];
            
            // Verificar si el curso ya está en el carrito
            const existingItem = cart.find(item => item.name === curso.name);
            if (existingItem) {
                existingItem.quantity += 1;
            } else {
                cart.push(curso);
            }
            
            localStorage.setItem('cart', JSON.stringify(cart));
            document.dispatchEvent(new Event('cartUpdated'));
            
            // Opcional: Mostrar notificación
            alert('Curso añadido al carrito');
        });
    });
});