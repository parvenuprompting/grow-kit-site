// Mobiele navigatie drawer handler voor Grow Kit
(function() {
  function initMobileNav() {
    const sideNav = document.getElementById('side-nav');
    const openBtn = document.getElementById('mobileMenuBtn');
    const closeBtn = document.getElementById('sideNavCloseBtn');
    const overlay = document.getElementById('sideNavOverlay');

    if (!sideNav) return;

    function openNav() {
      sideNav.classList.add('is-open');
      if (overlay) overlay.classList.add('is-active');
      document.body.style.overflow = 'hidden'; // voorkom scrollen achter drawer
    }

    function closeNav() {
      sideNav.classList.remove('is-open');
      if (overlay) overlay.classList.remove('is-active');
      document.body.style.overflow = '';
    }

    if (openBtn) openBtn.addEventListener('click', openNav);
    if (closeBtn) closeBtn.addEventListener('click', closeNav);
    if (overlay) overlay.addEventListener('click', closeNav);

    // Escape toets sluit het menu
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && sideNav.classList.contains('is-open')) {
        closeNav();
      }
    });

    // Sluit bij klik op menu item op mobiel
    const navItems = sideNav.querySelectorAll('a.item');
    navItems.forEach(item => {
      item.addEventListener('click', () => {
        if (window.innerWidth <= 840) {
          closeNav();
        }
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMobileNav);
  } else {
    initMobileNav();
  }
})();
