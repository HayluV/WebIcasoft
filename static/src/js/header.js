document.addEventListener('DOMContentLoaded', () => {
  // Elements
  const mobileMenuButton = document.getElementById('mobile-menu-button');
  const mobileMenu = document.getElementById('mobile-menu');
  const closeMobileMenu = document.getElementById('close-mobile-menu');
  const mobileProductosBtn = document.getElementById('mobile-productos-btn');
  const mobileProductosSubmenu = document.getElementById('mobile-productos-submenu');
  const menuProductosText = document.getElementById('menu-productos-text');
  const menuProductos = document.getElementById('menu-productos');
  const menuProductosBackground = document.querySelector('.menu-productos-background');
  const productosContainer = document.querySelector('.productos-container');
  const openModalBtnHeader = document.getElementById('openModalBtnHeader');
  const openModalBtnMobile = document.getElementById('openModalBtnMobile');

  // Toggle mobile menu with animation
  const toggleMobileMenu = (show) => {
    if (show) {
      mobileMenu.classList.remove('hidden');
      setTimeout(() => {
        mobileMenu.classList.add('icasoft-menu-show');
      }, 10);
    } else {
      mobileMenu.classList.remove('icasoft-menu-show');
      setTimeout(() => {
        mobileMenu.classList.add('hidden');
      }, 300);
    }
  };

  // Toggle products menu with animation
  const toggleProductsMenu = (show) => {
    if (show) {
      menuProductos.classList.remove('hidden');
      setTimeout(() => {
        menuProductos.classList.add('icasoft-menu-show');
      }, 10);
    } else {
      menuProductos.classList.remove('icasoft-menu-show');
      setTimeout(() => {
        menuProductos.classList.add('hidden');
      }, 300);
    }
  };

  // Mobile menu functionality
  if (mobileMenuButton && mobileMenu) {
    mobileMenuButton.addEventListener('click', (e) => {
      e.stopPropagation();
      toggleMobileMenu(!mobileMenu.classList.contains('icasoft-menu-show'));
    });
  }

  // Close mobile menu
  if (closeMobileMenu && mobileMenu) {
    closeMobileMenu.addEventListener('click', () => {
      toggleMobileMenu(false);
    });
  }

  // Toggle productos submenu in mobile with arrow animation
  if (mobileProductosBtn && mobileProductosSubmenu) {
    mobileProductosBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      mobileProductosBtn.classList.toggle('active');
      mobileProductosSubmenu.classList.toggle('hidden');
    });
  }

  // Products menu functionality (desktop)
  if (menuProductosText && menuProductos) {
    menuProductosText.addEventListener('click', (e) => {
      e.stopPropagation();
      toggleProductsMenu(!menuProductos.classList.contains('icasoft-menu-show'));
    });
  }

  // Close products menu when clicking on background
  if (menuProductosBackground) {
    menuProductosBackground.addEventListener('click', () => {
      toggleProductsMenu(false);
    });
  }

  // Close menus when clicking outside
  document.addEventListener('click', (event) => {
    // Products menu (desktop)
    if (menuProductos && menuProductos.classList.contains('icasoft-menu-show') &&
      !menuProductos.contains(event.target) &&
      event.target !== menuProductosText) {
      toggleProductsMenu(false);
    }

    // Mobile menu
    if (mobileMenu && !mobileMenu.contains(event.target) &&
      event.target !== mobileMenuButton) {
      toggleMobileMenu(false);
    }
  });

  // Prevent clicks inside the menus from closing them
  if (productosContainer) {
    productosContainer.addEventListener('click', (e) => {
      e.stopPropagation();
    });
  }

  // Escape key to close menus
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      if (menuProductos && menuProductos.classList.contains('icasoft-menu-show')) {
        toggleProductsMenu(false);
      }
      if (mobileMenu && mobileMenu.classList.contains('icasoft-menu-show')) {
        toggleMobileMenu(false);
      }
    }
  });

  // Connect modal buttons
  if (openModalBtnMobile) {
    openModalBtnMobile.addEventListener('click', () => {
      toggleMobileMenu(false);
      if (openModalBtnHeader) openModalBtnHeader.click();
    });
  }

  // Close mobile submenu when clicking a link
  const mobileSubmenuLinks = mobileProductosSubmenu?.querySelectorAll('a');
  if (mobileSubmenuLinks) {
    mobileSubmenuLinks.forEach(link => {
      link.addEventListener('click', () => {
        toggleMobileMenu(false);
      });
    });
  }
});

document.addEventListener('DOMContentLoaded', function () {
  const openModalBtns = document.querySelectorAll('#openModalBtnHeader, #openModalBtnMobile');
  const loginModal = document.getElementById('login-modal');
  const closeLoginModal = document.querySelector('.close-login-modal');
  const loginModalBackground = document.querySelector('.login-modal-background');

  openModalBtns.forEach(btn => {
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      // Cerrar otros menús si están abiertos
      document.getElementById('menu-productos').classList.remove('icasoft-menu-show');
      document.getElementById('mobile-menu').classList.add('hidden');

      // Alternar el modal de login
      loginModal.classList.toggle('hidden');
      loginModal.classList.toggle('icasoft-login-show');
    });
  });

  closeLoginModal.addEventListener('click', function () {
    loginModal.classList.add('hidden');
    loginModal.classList.remove('icasoft-login-show');
  });

  loginModalBackground.addEventListener('click', function () {
    loginModal.classList.add('hidden');
    loginModal.classList.remove('icasoft-login-show');
  });

  // Cerrar modal al hacer clic fuera
  document.addEventListener('click', function (e) {
    if (!loginModal.contains(e.target) && !Array.from(openModalBtns).includes(e.target)) {
      loginModal.classList.add('hidden');
      loginModal.classList.remove('icasoft-login-show');
    }
  });
});