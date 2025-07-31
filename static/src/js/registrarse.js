const form = document.getElementById('registrarseForm');
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

document.addEventListener('DOMContentLoaded', () => {
    if (form) {
        form.reset();
    }
    const passwordInput = document.getElementById('contrasena');
    const confirmPasswordInput = document.getElementById('confirmar-contrasena');
    const passwordStrengthBar = document.getElementById('password-strength-bar');
    const documento = document.getElementById('documento');
    buscarDNI();
    // Validación en tiempo real para la fortaleza de la contraseña
    passwordInput.addEventListener('input', function () {
        const password = this.value;
        const strength = calculatePasswordStrength(password);
        updatePasswordStrengthBar(strength);
    });

    // Validación en tiempo real para confirmar contraseña
    confirmPasswordInput.addEventListener('input', function () {
        validatePasswordMatch();
    });

    // Validación al enviar el formulario
    form.addEventListener('submit', function (event) {
        event.preventDefault();

        if (validateForm()) {
            crearUser();
        }
    });

    // Función para validar todo el formulario
    function validateForm() {
        let isValid = true;
        // Validar número de documento

        // Validar nombre
        const nombre = document.getElementById('nombre');
        if (!nombre.value || !nombre.checkValidity()) {
            showError(nombre, 'nombre-error');
            isValid = false;
        } else {
            hideError(nombre, 'nombre-error');
        }

        // Validar apellidos
        const apellidos = document.getElementById('apellidos');
        if (!apellidos.value || !apellidos.checkValidity()) {
            showError(apellidos, 'apellidos-error');
            isValid = false;
        } else {
            hideError(apellidos, 'apellidos-error');
        }

        // Validar correo
        const correo = document.getElementById('correo');
        if (!correo.value || !correo.checkValidity()) {
            showError(correo, 'correo-error');
            isValid = false;
        } else {
            hideError(correo, 'correo-error');
        }

        // Validar celular
        const celular = document.getElementById('celular');
        celular.value = celular.value.replace(/\D/g, '');
        if (!celular.value || !celular.checkValidity()) {
            showError(celular, 'celular-error');
            isValid = false;
        } else {
            hideError(celular, 'celular-error');
        }

        // Validar contraseña
        const contrasena = document.getElementById('contrasena');
        if (!contrasena.value || !contrasena.checkValidity()) {
            showError(contrasena, 'contrasena-error');
            isValid = false;
        } else {
            hideError(contrasena, 'contrasena-error');
        }

        // Validar coincidencia de contraseñas
        if (!validatePasswordMatch()) {
            isValid = false;
        }

        return isValid;
    }

    // Función para validar coincidencia de contraseñas
    function validatePasswordMatch() {
        const password = passwordInput.value;
        const confirmPassword = confirmPasswordInput.value;

        if (password && confirmPassword && password !== confirmPassword) {
            confirmPasswordInput.classList.add('error');
            document.getElementById('confirmar-contrasena-error').style.display = 'block';
            return false;
        } else {
            confirmPasswordInput.classList.remove('error');
            document.getElementById('confirmar-contrasena-error').style.display = 'none';
            return true;
        }
    }

    // Función para mostrar errores
    function showError(inputElement, errorElementId) {
        inputElement.classList.add('error');
        document.getElementById(errorElementId).style.display = 'block';
    }

    // Función para ocultar errores
    function hideError(inputElement, errorElementId) {
        inputElement.classList.remove('error');
        document.getElementById(errorElementId).style.display = 'none';
    }

    // Función para calcular la fortaleza de la contraseña
    function calculatePasswordStrength(password) {
        let strength = 0;

        // Longitud mínima
        if (password.length >= 6) strength += 1;
        if (password.length >= 10) strength += 1;

        // Contiene letras mayúsculas y minúsculas
        if (/[a-z]/.test(password) && /[A-Z]/.test(password)) strength += 1;

        // Contiene números
        if (/[0-9]/.test(password)) strength += 1;

        // Contiene caracteres especiales
        if (/[^A-Za-z0-9]/.test(password)) strength += 1;

        return strength;
    }

    // Función para actualizar la barra de fortaleza de la contraseña
    function updatePasswordStrengthBar(strength) {
        const strengthPercent = (strength / 5) * 100;
        passwordStrengthBar.style.width = strengthPercent + '%';

        // Cambiar color según la fortaleza
        if (strength <= 1) {
            passwordStrengthBar.style.backgroundColor = '#ef4444'; // Rojo
        } else if (strength <= 3) {
            passwordStrengthBar.style.backgroundColor = '#f59e0b'; // Amarillo
        } else {
            passwordStrengthBar.style.backgroundColor = '#10b981'; // Verde
        }
    }

});
function buscarDNI() {
    documento.addEventListener('keypress', function (event) {
        if (event.key === 'Enter' || event.keyCode === 13) {
            event.preventDefault();
            respuestaDNI();
        }
    });
    document.getElementById("buscarBtn").addEventListener('click', function () {
        respuestaDNI();
    });
}
function respuestaDNI() {
    const dni = documento.value;

    if (dni && dni.length === 8) {
        fetch("/Icasoft/APIDNI/", {
            method: "POST",
            body: `dni=${dni}`,
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken,
            },
        })
            .then(async res => {
                const data = await res.json();
                if (!res.ok) {
                    alert(data.error || "Ocurrió un error desconocido");
                    form.reset();
                    throw new Error(data.error); // Para evitar seguir ejecutando
                }
                return data;
            })
            .then(data => {
                const nombre = document.querySelector('.nombreDNI');
                const apellido = document.querySelector('.apellidoDNI');
                nombre.value = data.nombres;
                apellido.value = `${data.apellidoPaterno} ${data.apellidoMaterno}`;
            })
    } else {
        alert("DNI debe tener 8 dígitos");
    }
}
function crearUser() {
    const formData = new FormData(form);
    fetch("/Icasoft/Registrarse/", {
        method: "POST",
        body: formData,
        headers: {
            'X-CSRFToken': csrfToken,
        },
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            alert("ÉXITO: " + data.success);
            window.location.href = "/Icasoft/"
        } else if (data.error) {
            alert("ERROR: " + data.error);
        }
    })
    .catch(error => {
        alert('Error: ' + error);
    });
}