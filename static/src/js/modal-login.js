document.addEventListener('DOMContentLoaded', () => {
  // Login modal elementos
  const openModalBtnHeader = document.getElementById('openModalBtnHeader');
  const openModalBtnMenu = document.getElementById('openModalBtnMenu');
  const loginModal = document.getElementById('miModal');
  const closeLoginBtn = document.getElementById('closeModalBtn');
  const closeLoginBtn2 = document.getElementById('closeModalBtn2');

  // Registro modal elementos
  const registerModal = document.getElementById('miModalRegistro');
  const closeRegisterBtn = document.getElementById('closeModalRegistroBtn');
  const closeRegisterBtn2 = document.getElementById('closeModalRegistroBtn2');
  const openRegisterFromLogin = document.getElementById('openModalRegistroFromLogin');

  // Abrir modal login
  openModalBtnHeader.addEventListener('click', () => {
    loginModal.classList.remove('hidden');
  });
  openModalBtnMenu.addEventListener('click', () => {
    loginModal.classList.remove('hidden');
  });

  // Cerrar modal login
  closeLoginBtn.addEventListener('click', () => {
    loginModal.classList.add('hidden');
  });
  closeLoginBtn2.addEventListener('click', () => {
    loginModal.classList.add('hidden');
  });

  // Abrir modal registro desde link en login
  openRegisterFromLogin.addEventListener('click', (e) => {
    e.preventDefault();
    loginModal.classList.add('hidden');
    registerModal.classList.remove('hidden');
  });

  // Cerrar modal registro
  closeRegisterBtn.addEventListener('click', () => {
    registerModal.classList.add('hidden');
  });
  closeRegisterBtn2.addEventListener('click', () => {
    registerModal.classList.add('hidden');
  });
});
