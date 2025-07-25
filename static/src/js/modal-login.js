document.addEventListener('DOMContentLoaded', function () {
  const loginModal = document.getElementById('login-modal');
  const openModalBtnHeader = document.getElementById('openModalBtnHeader');
  const openModalBtnMobile = document.getElementById('openModalBtnMobile');
  const closeModalBtn = document.querySelector('.close-login-modal');

  // Función para abrir el modal
  function openLoginModal() {
    loginModal.classList.add('active');
    document.body.style.overflow = 'hidden'; // Evitar scroll del body
  }

  // Función para cerrar el modal
  function closeLoginModal() {
    loginModal.classList.remove('active');
    document.body.style.overflow = ''; // Restaurar scroll del body
  }

  // Abrir modal desde el header (desktop)
  if (openModalBtnHeader) {
    openModalBtnHeader.addEventListener('click', function (e) {
      e.preventDefault();
      openLoginModal();
    });
  }

  // Abrir modal desde el menú móvil
  if (openModalBtnMobile) {
    openModalBtnMobile.addEventListener('click', function (e) {
      e.preventDefault();
      openLoginModal();
      // Cerrar también el menú móvil si está abierto
      const mobileMenu = document.getElementById('mobile-menu');
      if (mobileMenu && !mobileMenu.classList.contains('hidden')) {
        mobileMenu.classList.add('hidden');
      }
    });
  }

  // Cerrar modal al hacer clic en la X
  if (closeModalBtn) {
    closeModalBtn.addEventListener('click', closeLoginModal);
  }

  // Cerrar modal al hacer clic fuera del contenido
  loginModal.addEventListener('click', function (e) {
    if (e.target === loginModal || e.target.classList.contains('login-modal-background')) {
      closeLoginModal();
    }
  });

  


  // Manejar el envío del formulario
  const loginForm = document.getElementById('loginForm');
  if (loginForm) {
    loginForm.addEventListener('submit', function (e) {
      e.preventDefault();
      
  
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
      
      if (!email || !password) {
        alert('Por favor complete todos los campos');
        return;
      }
      
      window.location.href = '/'; // Redirige a la página principal
      
      closeLoginModal();
    });
  }
  // Cerrar modal con la tecla ESC
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && loginModal.classList.contains('active')) {
      closeLoginModal();
    }
  });
});


