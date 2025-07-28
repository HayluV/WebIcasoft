formCuenta = document.getElementById('profile-form');
document.addEventListener('DOMContentLoaded', function () {
    const passwordInput = document.getElementById('password');
    const togglePassword = document.getElementById('togglePassword');
    const saveChangesBtn = document.getElementById('save-changes');

    // Mostrar/ocultar contraseña
    togglePassword.addEventListener('click', function () {
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);
        this.textContent = type === 'password' ? 'Mostrar' : 'Ocultar';
    });

    // Al enfocar el campo contraseña, limpiar para permitir cambio
    passwordInput.addEventListener('focus', function () {
        if (passwordInput.value === '********') {
            passwordInput.value = '';
        }
    });

    // Validar contraseña
    function validatePassword() {
        const password = passwordInput.value;
        let isValid = true;

        if (password.length > 0 && password.length < 6) {
            document.getElementById('password-error').style.display = 'block';
            isValid = false;
        } else {
            document.getElementById('password-error').style.display = 'none';
        }

        return isValid;
    }

    saveChangesBtn.addEventListener('click', function () {
        if (validatePassword()) {
            updateUser();
        }
    });
});
function updateUser() {
    const formData = new FormData(formCuenta);
    for (let pair of formData.entries()) {
        console.log(pair[0] + ': ' + pair[1]);
    }
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    fetch("/Icasoft/MiCuenta/", {
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
                window.location.href = "/Icasoft/MiCuenta/"
            } else if (data.error) {
                console.error('Errores del formulario:', data.form_errors);
                alert('Error: ' + JSON.stringify(data.form_errors));
            }
        })
        .catch(error => {
            alert('Error: ' + error);
        });
}