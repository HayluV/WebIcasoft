const menuInfoToggle = document.getElementById('menu-info-toggle');
const menuInfo = document.getElementById('menu-info');
const closeMenuInfo = document.getElementById('close-menu-info');
const menuProductosText = document.getElementById('menu-productos-text');
const menuProductos = document.getElementById('menu-productos');
const closeMenuProductos = document.getElementById('close-menu-productos');

menuInfoToggle.addEventListener('click', () => {
    menuInfo.classList.toggle('hidden');
});

menuProductosText.addEventListener('click', () => {
    menuProductos.classList.toggle('show');
});

closeMenuProductos.addEventListener('click', () => {
    menuProductos.classList.remove('show');
});

closeMenuInfo.addEventListener('click', () => {
    menuInfo.classList.add('hidden');
});
