document.addEventListener('DOMContentLoaded', function() {
  // Elementos del modal
  const loginModal = document.getElementById('loginModal');
  const openModalBtns = document.querySelectorAll('[data-modal-toggle="loginModal"]');
  const closeModalBtns = document.querySelectorAll('[data-modal-hide="loginModal"]');
  const showRegisterModal = document.getElementById('showRegisterModal');
  
  // Elementos del formulario
  const loginForm = document.getElementById('loginForm');
  const togglePassword = document.getElementById('togglePassword');
  const passwordInput = document.getElementById('password');
  const passwordIcon = document.getElementById('passwordIcon');

  // Función para abrir el modal
  function openLoginModal() {
    loginModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  // Función para cerrar el modal
  function closeLoginModal() {
    loginModal.classList.remove('active');
    document.body.style.overflow = 'auto';
  }

  // Event listeners para abrir el modal
  openModalBtns.forEach(btn => {
    btn.addEventListener('click', openLoginModal);
  });

  // Event listeners para cerrar el modal
  closeModalBtns.forEach(btn => {
    btn.addEventListener('click', closeLoginModal);
  });

  // Cerrar al hacer clic fuera del modal
  loginModal.addEventListener('click', function(e) {
    if (e.target === loginModal) {
      closeLoginModal();
    }
  });

  // Alternar visibilidad de la contraseña
  if (togglePassword && passwordInput && passwordIcon) {
    togglePassword.addEventListener('click', function() {
      const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
      passwordInput.setAttribute('type', type);
      
      // Cambiar el icono
      passwordIcon.classList.toggle('icofont-eye');
      passwordIcon.classList.toggle('icofont-eye-blocked');
    });
  }

  // Mostrar modal de registro
  if (showRegisterModal) {
    showRegisterModal.addEventListener('click', function(e) {
      e.preventDefault();
      closeLoginModal();
      
      // Abrir modal de registro después de un pequeño retraso
      setTimeout(() => {
        const registerModal = document.getElementById('registerModal');
        if (registerModal) {
          registerModal.classList.add('active');
          document.body.style.overflow = 'hidden';
        }
      }, 300);
    });
  }

  // Manejar el envío del formulario
  if (loginForm) {
    loginForm.addEventListener('submit', function(e) {
      e.preventDefault();
      
      // Aquí iría la lógica de autenticación
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
      const rememberMe = document.getElementById('remember-me').checked;
      
      console.log('Iniciando sesión con:', { email, password, rememberMe });
      
      // Simular autenticación exitosa
      setTimeout(() => {
        alert('Inicio de sesión exitoso!');
        closeLoginModal();
      }, 1000);
    });
  }

  // Cerrar con la tecla ESC
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && loginModal.classList.contains('active')) {
      closeLoginModal();
    }
  });
});