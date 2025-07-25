document.addEventListener('DOMContentLoaded', function () {
    // Cargar datos del carrito desde localStorage
    const cart = JSON.parse(localStorage.getItem('cart')) || [];

    // Calcular subtotal
    const subtotal = cart.reduce((sum, product) => sum + (product.price * product.quantity), 0);

    // Cargar datos de entrega si existen
    const deliveryData = JSON.parse(localStorage.getItem('deliveryData')) || {
        dni: '12345678',
        firstName: 'Ingrese su nombre',
        lastName: 'Ingrese su apellido paterno',
        motherLastName: 'Ingrese su apellido materno',
        shippingType: '',
        phone: '912232432',
        address: '',
        departamento: '',
        provincia: '',
        distrito: ''
    };

    // Calcular costo de envío según tipo
    let shippingCost = 0;
    if (deliveryData.shippingType === 'pickup') {
        shippingCost = 0;
    } else if (deliveryData.shippingType === 'delivery') {
        shippingCost = 18;
    } else if (deliveryData.shippingType === 'shalom') {
        shippingCost = 10;
    } else if (deliveryData.shippingType === 'olva') {
        shippingCost = 20;
    }

    const total = subtotal + shippingCost;

    // Mostrar totales
    document.getElementById('subtotal').textContent = `S/ ${subtotal.toFixed(2)}`;
    document.getElementById('shipping').textContent = `S/ ${shippingCost.toFixed(2)}`;
    document.getElementById('total').textContent = `S/ ${total.toFixed(2)}`;

    // Mostrar datos de entrega
    renderDeliveryInfo(deliveryData);

    // Modal de edición
    const modal = document.getElementById('delivery-modal');
    const editBtn = document.getElementById('edit-delivery-btn');
    const closeBtn = document.querySelector('.close');
    const deliveryForm = document.getElementById('delivery-form');
    const shippingTypeSelect = document.getElementById('shipping-type');

    // Datos de ubicación simplificados
    const ubicacionData = {
        departamentos: {
            "Lima": {
                provincias: {
                    "Lima": ["Lima", "Miraflores", "Barranco", "Surco"],
                    "Huaura": ["Huacho", "Hualmay", "Caleta de Carquín"]
                }
            },
            "Arequipa": {
                provincias: {
                    "Arequipa": ["Arequipa", "Cayma", "Yanahuara"],
                    "Camaná": ["Camaná", "José María Quimper"]
                }
            },
            "Cusco": {
                provincias: {
                    "Cusco": ["Cusco", "San Jerónimo", "San Sebastián"],
                    "Quispicanchi": ["Urcos", "Andahuaylillas"]
                }
            },
            "Piura": {
                provincias: {
                    "Piura": ["Piura", "Castilla", "Veintiséis de Octubre"],
                    "Sullana": ["Sullana", "Bellavista"]
                }
            },
            "La Libertad": {
                provincias: {
                    "Trujillo": ["Trujillo", "La Esperanza", "El Porvenir"],
                    "Chepén": ["Chepén", "Pacanga"]
                }
            }
        }
    };

    // Función para actualizar provincias
    function updateProvincias(departamentoSelectId, provinciaSelectId, selectedProvincia = '') {
        const departamento = document.getElementById(departamentoSelectId).value;
        const provinciaSelect = document.getElementById(provinciaSelectId);

        provinciaSelect.innerHTML = '<option value="">Seleccione una provincia</option>';

        if (departamento && ubicacionData.departamentos[departamento]) {
            const provincias = Object.keys(ubicacionData.departamentos[departamento].provincias);
            provincias.forEach(provincia => {
                const option = document.createElement('option');
                option.value = provincia;
                option.textContent = provincia;
                if (provincia === selectedProvincia) {
                    option.selected = true;
                }
                provinciaSelect.appendChild(option);
            });
        }
    }

    // Función para actualizar distritos
    function updateDistritos(departamentoSelectId, provinciaSelectId, distritoSelectId, selectedDistrito = '') {
        const departamento = document.getElementById(departamentoSelectId).value;
        const provincia = document.getElementById(provinciaSelectId).value;
        const distritoSelect = document.getElementById(distritoSelectId);

        distritoSelect.innerHTML = '<option value="">Seleccione un distrito</option>';

        if (departamento && provincia &&
            ubicacionData.departamentos[departamento] &&
            ubicacionData.departamentos[departamento].provincias[provincia]) {

            const distritos = ubicacionData.departamentos[departamento].provincias[provincia];
            distritos.forEach(distrito => {
                const option = document.createElement('option');
                option.value = distrito;
                option.textContent = distrito;
                if (distrito === selectedDistrito) {
                    option.selected = true;
                }
                distritoSelect.appendChild(option);
            });
        }
    }

    // Event listeners para Shalom
    document.getElementById('shalom-departamento').addEventListener('change', function () {
        updateProvincias('shalom-departamento', 'shalom-provincia');
        document.getElementById('shalom-distrito').innerHTML = '<option value="">Seleccione un distrito</option>';
    });

    document.getElementById('shalom-provincia').addEventListener('change', function () {
        updateDistritos('shalom-departamento', 'shalom-provincia', 'shalom-distrito');
    });

    // Event listeners para Olva
    document.getElementById('olva-departamento').addEventListener('change', function () {
        updateProvincias('olva-departamento', 'olva-provincia');
        document.getElementById('olva-distrito').innerHTML = '<option value="">Seleccione un distrito</option>';
    });

    document.getElementById('olva-provincia').addEventListener('change', function () {
        updateDistritos('olva-departamento', 'olva-provincia', 'olva-distrito');
    });

    // Manejar cambio en tipo de envío
    shippingTypeSelect.addEventListener('change', function () {
        const shippingType = this.value;

        // Ocultar todos los campos dependientes
        document.querySelectorAll('.shipping-dependent-field').forEach(field => {
            field.classList.remove('visible');
        });

        // Mostrar los campos correspondientes
        if (shippingType === 'pickup') {
            document.getElementById('pickup-fields').classList.add('visible');
        } else if (shippingType === 'delivery') {
            document.getElementById('delivery-fields').classList.add('visible');
        } else if (shippingType === 'shalom') {
            document.getElementById('shalom-fields').classList.add('visible');
        } else if (shippingType === 'olva') {
            document.getElementById('olva-fields').classList.add('visible');
        }

        // Actualizar costo de envío en tiempo real
        updateShippingCost(shippingType);
    });

    function updateShippingCost(shippingType) {
        let shippingCost = 0;
        if (shippingType === 'pickup') {
            shippingCost = 0;
        } else if (shippingType === 'delivery') {
            shippingCost = 18;
        } else if (shippingType === 'shalom') {
            shippingCost = 10;
        } else if (shippingType === 'olva') {
            shippingCost = 20;
        }

        const subtotal = parseFloat(document.getElementById('subtotal').textContent.replace('S/ ', ''));
        const total = subtotal + shippingCost;

        document.getElementById('shipping').textContent = `S/ ${shippingCost.toFixed(2)}`;
        document.getElementById('total').textContent = `S/ ${total.toFixed(2)}`;
    }

    editBtn.addEventListener('click', function () {
        // Llenar el formulario con los datos actuales
        document.getElementById('dni').value = deliveryData.dni;
        document.getElementById('first-name').value = deliveryData.firstName;
        document.getElementById('last-name').value = deliveryData.lastName;
        document.getElementById('mother-last-name').value = deliveryData.motherLastName;
        document.getElementById('shipping-type').value = deliveryData.shippingType;
        document.getElementById('phone').value = deliveryData.phone;

        // Disparar el evento change para mostrar los campos correctos
        shippingTypeSelect.dispatchEvent(new Event('change'));

        // Llenar campos según tipo de envío
        if (deliveryData.shippingType === 'pickup') {
            // No necesita más datos para recoger en local
        } else if (deliveryData.shippingType === 'delivery') {
            document.getElementById('address').value = deliveryData.address || '';
        } else if (deliveryData.shippingType === 'shalom') {
            document.getElementById('shalom-address').value = deliveryData.address || '';
            document.getElementById('shalom-departamento').value = deliveryData.departamento || '';
            updateProvincias('shalom-departamento', 'shalom-provincia', deliveryData.provincia);
            updateDistritos('shalom-departamento', 'shalom-provincia', 'shalom-distrito', deliveryData.distrito);
        } else if (deliveryData.shippingType === 'olva') {
            document.getElementById('olva-address').value = deliveryData.address || '';
            document.getElementById('olva-departamento').value = deliveryData.departamento || '';
            updateProvincias('olva-departamento', 'olva-provincia', deliveryData.provincia);
            updateDistritos('olva-departamento', 'olva-provincia', 'olva-distrito', deliveryData.distrito);
        }

        modal.style.display = 'block';
    });

    closeBtn.addEventListener('click', function () {
        modal.style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });

    deliveryForm.addEventListener('submit', function (e) {
        e.preventDefault();

        // Validar campos obligatorios comunes
        const firstName = document.getElementById('first-name').value;
        const lastName = document.getElementById('last-name').value;
        const motherLastName = document.getElementById('mother-last-name').value;
        const dni = document.getElementById('dni').value;
        const phone = document.getElementById('phone').value;

        if (!firstName || !lastName || !motherLastName || !dni || !phone) {
            alert('Por favor complete todos los campos obligatorios: Nombre, Apellido Paterno, Apellido Materno, DNI y Teléfono');
            return;
        }

        const shippingType = document.getElementById('shipping-type').value;
        let newDeliveryData = {
            dni: dni,
            firstName: firstName,
            lastName: lastName,
            motherLastName: motherLastName,
            shippingType: shippingType,
            phone: phone
        };

        // Agregar datos específicos según el tipo de envío
        if (shippingType === 'pickup') {
            newDeliveryData.departamento = 'Ica';
            newDeliveryData.provincia = 'Ica';
            newDeliveryData.distrito = 'Ica';
            newDeliveryData.address = 'Recojo en local';
        } else if (shippingType === 'delivery') {
            newDeliveryData.address = document.getElementById('address').value || 'No especificado';
            newDeliveryData.departamento = 'Ica';
            newDeliveryData.provincia = 'Ica';
            newDeliveryData.distrito = 'Ica';
        } else if (shippingType === 'shalom') {
            newDeliveryData.address = document.getElementById('shalom-address').value || 'No especificado';
            newDeliveryData.departamento = document.getElementById('shalom-departamento').value || 'No especificado';
            newDeliveryData.provincia = document.getElementById('shalom-provincia').value || 'No especificado';
            newDeliveryData.distrito = document.getElementById('shalom-distrito').value || 'No especificado';
        } else if (shippingType === 'olva') {
            newDeliveryData.address = document.getElementById('olva-address').value || 'No especificado';
            newDeliveryData.departamento = document.getElementById('olva-departamento').value || 'No especificado';
            newDeliveryData.provincia = document.getElementById('olva-provincia').value || 'No especificado';
            newDeliveryData.distrito = document.getElementById('olva-distrito').value || 'No especificado';
        }

        localStorage.setItem('deliveryData', JSON.stringify(newDeliveryData));

        // Calcular nuevo costo de envío
        updateShippingCost(shippingType);

        renderDeliveryInfo(newDeliveryData);
        modal.style.display = 'none';
        
        // Recargar la página para actualizar Culqi
        location.reload();
    });

    function renderDeliveryInfo(data) {
        const deliveryInfo = document.getElementById('delivery-info');
        let shippingText = '';
        let locationText = '';

        switch (data.shippingType) {
            case 'pickup':
                shippingText = 'Recojo en el local';
                locationText = `${data.distrito}, ${data.provincia}, ${data.departamento}`;
                break;
            case 'delivery':
                shippingText = 'Delivery (solo Ica)';
                locationText = `${data.address}<br>${data.distrito}, ${data.provincia}, ${data.departamento}`;
                break;
            case 'shalom':
                shippingText = 'Envío por Shalom';
                locationText = `${data.address}<br>${data.distrito}, ${data.provincia}, ${data.departamento}`;
                break;
            case 'olva':
                shippingText = 'Envío por Olva Courier';
                locationText = `${data.address}<br>${data.distrito}, ${data.provincia}, ${data.departamento}`;
                break;
            default:
                shippingText = 'No especificado';
                locationText = 'No especificado';
        }

        deliveryInfo.innerHTML = `
            <p><strong>${data.firstName} ${data.lastName} ${data.motherLastName}</strong> (DNI: ${data.dni})</p>
            <p><strong>Tipo de envío:</strong> ${shippingText}</p>
            <p><strong>Dirección:</strong> ${locationText}</p>
            <p><strong>Teléfono:</strong> ${data.phone}</p>
        `;
    }
});