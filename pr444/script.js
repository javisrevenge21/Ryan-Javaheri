const menuButton = document.querySelector('.menu-button');
const nav = document.querySelector('#site-nav');
const progressBar = document.querySelector('#progress-bar');

menuButton?.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  menuButton.setAttribute('aria-expanded', String(open));
});

nav?.addEventListener('click', (event) => {
  if (event.target.matches('a')) {
    nav.classList.remove('open');
    menuButton?.setAttribute('aria-expanded', 'false');
  }
});

const navDropdown = document.querySelector('.nav-dropdown');
const dropdownToggle = document.querySelector('.nav-dropdown-toggle');

dropdownToggle?.addEventListener('click', (event) => {
  event.stopPropagation();
  const open = navDropdown.classList.toggle('open');
  dropdownToggle.setAttribute('aria-expanded', String(open));
});

document.addEventListener('click', (event) => {
  if (navDropdown && navDropdown.classList.contains('open') && !navDropdown.contains(event.target)) {
    navDropdown.classList.remove('open');
    dropdownToggle?.setAttribute('aria-expanded', 'false');
  }
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && navDropdown?.classList.contains('open')) {
    navDropdown.classList.remove('open');
    dropdownToggle?.setAttribute('aria-expanded', 'false');
    dropdownToggle?.focus();
  }
});

function updateProgress() {
  const scrollable = document.documentElement.scrollHeight - window.innerHeight;
  const ratio = scrollable > 0 ? window.scrollY / scrollable : 0;
  progressBar.style.width = `${Math.min(100, Math.max(0, ratio * 100))}%`;
}

document.addEventListener('scroll', updateProgress, { passive: true });
updateProgress();
