const menuButton = document.querySelector('.menu-button');
const nav = document.querySelector('#site-nav');
const postsMenu = document.querySelector('.posts-menu');
const postsToggle = document.querySelector('.posts-toggle');
const progressBar = document.querySelector('#progress-bar');

menuButton?.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  menuButton.setAttribute('aria-expanded', String(open));
});

postsToggle?.addEventListener('click', () => {
  const open = postsMenu.classList.toggle('open');
  postsToggle.setAttribute('aria-expanded', String(open));
});

nav?.addEventListener('click', (event) => {
  if (event.target.matches('a')) {
    nav.classList.remove('open');
    postsMenu?.classList.remove('open');
    menuButton?.setAttribute('aria-expanded', 'false');
    postsToggle?.setAttribute('aria-expanded', 'false');
  }
});

function updateProgress() {
  const scrollable = document.documentElement.scrollHeight - window.innerHeight;
  const ratio = scrollable > 0 ? window.scrollY / scrollable : 0;
  progressBar.style.width = `${Math.min(100, Math.max(0, ratio * 100))}%`;
}

document.addEventListener('scroll', updateProgress, { passive: true });
updateProgress();
