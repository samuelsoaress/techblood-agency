const toggleBtn = document.getElementById('menu-toggle');
const mobileMenu = document.getElementById('mobile-menu');
const overlay = document.getElementById('menu-overlay');

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