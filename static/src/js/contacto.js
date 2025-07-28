
        document.addEventListener('DOMContentLoaded', function() {
            const formulario = document.getElementById('formulario-contacto');
            const mensajeExito = document.getElementById('mensaje-exito');
            
            formulario.addEventListener('submit', function(e) {
                e.preventDefault();
                
                // Validar checkbox de privacidad
                if (!document.getElementById('privacidad').checked) {
                    alert('Debe aceptar la política de privacidad');
                    return;
                }
                
                // Simular envío (para prueba)
                console.log('Datos del formulario (simulación):');
                console.log({
                    tipo: document.getElementById('tipo-solicitante').value,
                    nombre: document.getElementById('nombre').value,
                    email: document.getElementById('email').value,
                    telefono: document.getElementById('telefono').value,
                    servicio: document.getElementById('servicio').value,
                    mensaje: document.getElementById('mensaje').value
                });
                
                // Mostrar mensaje de éxito
                formulario.style.display = 'none';
                mensajeExito.style.display = 'block';
                
                // Opcional: Resetear después de 5 segundos (para pruebas)
                setTimeout(() => {
                    formulario.reset();
                    formulario.style.display = 'block';
                    mensajeExito.style.display = 'none';
                }, 5000);
            });
        });