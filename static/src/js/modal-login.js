document.addEventListener('DOMContentLoaded', () => {
  const openModalBtnHeader = document.getElementById('openModalBtnHeader');
  const openModalBtnMenu = document.getElementById('openModalBtnMenu');
  const modal = document.getElementById('miModal');
  const closeModalBtn = document.getElementById('closeModalBtn');
  const closeModalBtn2 = document.getElementById('closeModalBtn2');

  openModalBtnHeader.addEventListener('click', () => {
    modal.classList.remove('hidden');
  });

  openModalBtnMenu.addEventListener('click', () => {
    modal.classList.remove('hidden');
  });

  closeModalBtn.addEventListener('click', () => {
    modal.classList.add('hidden');
  });

  closeModalBtn2.addEventListener('click', () => {
    modal.classList.add('hidden');
  });
});
