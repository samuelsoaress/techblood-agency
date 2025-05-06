document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('menu-toggle');
  const mobileMenu = document.getElementById('ekit-megamenu-menu-principal');
  const overlay = document.getElementById('menu-overlay');
  const closeButton = document.getElementById('menu-close');

  if (toggleBtn && mobileMenu && overlay && closeButton) {
    
    closeButton.addEventListener('click', () => {
      toggleBtn.classList.remove('active');
      mobileMenu.classList.remove('active');
      overlay.classList.remove('active');
    });

    // Adiciona o evento de clique ao botão de menu
    // para abrir o menu
    toggleBtn.addEventListener('click', () => {
      toggleBtn.classList.toggle('active');
      mobileMenu.classList.toggle('active');
      overlay.classList.toggle('active');
    });

    overlay.addEventListener('click', () => {
      toggleBtn.classList.remove('active');
      mobileMenu.classList.remove('active');
      overlay.classList.remove('active');
    });
  } else {
    console.warn('Algum dos elementos do menu não foi encontrado no DOM.');
  }
});