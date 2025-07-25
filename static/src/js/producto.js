// Lógica para mover los productos en bloques de 3
  function moverSliderProductos(direccion) {
    const contenedor = document.getElementById('producto-contenedor-productos');
    const visor = document.querySelector('.producto-visor-slider');

    // Obtener el ancho de un producto
    const tarjeta = contenedor.querySelector('.producto-tarjeta');
    const styleTarjeta = window.getComputedStyle(tarjeta);
    const margenDerecho = parseInt(styleTarjeta.marginRight); // Margen derecho de las tarjetas
    const anchoTarjeta = tarjeta.offsetWidth + margenDerecho;

    // Calcular el ancho total visible del visor
    const anchoVisible = visor.offsetWidth;

    // Definir cuántos productos se muestran
    let productosVisibles;
    if (window.innerWidth <= 480) {
      productosVisibles = 3; // Mostrar 3 productos a la vez
    } else {
      productosVisibles = 3; // Si necesitas ajustar esto en dispositivos más grandes, cámbialo
    }

    // Calcular la posición máxima del contenedor
    const anchoTotal = contenedor.scrollWidth;
    const maxPosicion = Math.ceil((anchoTotal - anchoVisible) / (anchoTarjeta * productosVisibles));

    let posicion = parseInt(contenedor.dataset.posicion) || 0;
    
    // Mover la posición según la dirección
    posicion += direccion;
    if (posicion < 0) posicion = 0; // No permitir desplazamiento hacia atrás más allá del primer conjunto
    if (posicion > maxPosicion) posicion = maxPosicion; // No permitir desplazamiento más allá del final

    // Aplicar el desplazamiento
    contenedor.style.transform = `translateX(${-posicion * productosVisibles * anchoTarjeta}px)`;
    contenedor.dataset.posicion = posicion; // Guardar la posición actual para futuras referencias
  }

  window.addEventListener('resize', () => {
    const contenedor = document.getElementById('producto-contenedor-productos');
    contenedor.dataset.posicion = 0;
    contenedor.style.transform = 'translateX(0)';
  });