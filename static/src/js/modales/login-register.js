    document.addEventListener('DOMContentLoaded', function () {
      const loginModal = document.getElementById('login-modal');
      const registerModal = document.getElementById('register-modal');
      const openModalBtn = document.getElementById('openModalBtnHeader');
      const closeModalBtn = document.querySelector('.close-login-modal');
      const closeRegisterBtn = document.querySelector('.close-register-modal');
      const openLoginFromRegister = document.getElementById('open-login-from-register');
      const openRegisterFromLogin = document.getElementById('open-register-from-login');
      const openModalBtnMobile = document.getElementById('openModalBtnMobile');

      // Abrir modal de login
      openModalBtn.addEventListener('click', function (e) {
        e.preventDefault();
        loginModal.classList.add('active');
      });

      // Cerrar modal de login
      closeModalBtn.addEventListener('click', function () {
        loginModal.classList.remove('active');
      });

      // Cerrar modal de registro
      closeRegisterBtn.addEventListener('click', function () {
        registerModal.classList.remove('active');
      });

      // Cerrar modales al hacer clic fuera
      loginModal.addEventListener('click', function (e) {
        if (e.target === loginModal || e.target.classList.contains('login-modal-background')) {
          loginModal.classList.remove('active');
        }
      });

      registerModal.addEventListener('click', function (e) {
        if (e.target === registerModal || e.target.classList.contains('register-modal-background')) {
          registerModal.classList.remove('active');
        }
      });

      // Abrir registro desde login
      if (openRegisterFromLogin) {
        openRegisterFromLogin.addEventListener('click', function (e) {
          e.preventDefault();
          loginModal.classList.remove('active');
          registerModal.classList.add('active');
        });
      }

      // Abrir login desde registro
      if (openLoginFromRegister) {
        openLoginFromRegister.addEventListener('click', function (e) {
          e.preventDefault();
          registerModal.classList.remove('active');
          loginModal.classList.add('active');
        });
      }

      // Abrir modal de login desde móvil
      if (openModalBtnMobile) {
        openModalBtnMobile.addEventListener('click', function (e) {
          e.preventDefault();
          loginModal.classList.add('active');
          document.getElementById('mobile-menu').classList.add('hidden');
        });
      }

      // Manejo del menú móvil
      const mobileMenuButton = document.getElementById('mobile-menu-button');
      const mobileMenu = document.getElementById('mobile-menu');
      const closeMobileMenu = document.getElementById('close-mobile-menu');

      if (mobileMenuButton && mobileMenu && closeMobileMenu) {
        mobileMenuButton.addEventListener('click', function() {
          mobileMenu.classList.remove('hidden');
        });

        closeMobileMenu.addEventListener('click', function() {
          mobileMenu.classList.add('hidden');
        });
      }

      // Manejo del submenú de productos en móvil
      const mobileProductosBtn = document.getElementById('mobile-productos-btn');
      const mobileProductosSubmenu = document.getElementById('mobile-productos-submenu');

      if (mobileProductosBtn && mobileProductosSubmenu) {
        mobileProductosBtn.addEventListener('click', function() {
          mobileProductosSubmenu.classList.toggle('hidden');
        });
      }

      // Manejo del menú de productos en desktop
      const menuProductosText = document.getElementById('menu-productos-text');
      const menuProductos = document.getElementById('menu-productos');

      if (menuProductosText && menuProductos) {
        menuProductosText.addEventListener('click', function() {
          menuProductos.classList.toggle('hidden');
        });

        // Cerrar al hacer clic fuera
        document.addEventListener('click', function(e) {
          if (!menuProductos.contains(e.target) && e.target !== menuProductosText) {
            menuProductos.classList.add('hidden');
          }
        });
      }
    });
  