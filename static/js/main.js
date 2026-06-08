// Kruassanov — UI interactions
(function () {
  'use strict';

  // ----- sticky nav -----
  const nav = document.querySelector('.nav');
  if (nav) {
    const syncNavHeight = () => {
      document.documentElement.style.setProperty(
        '--nav-height',
        `${nav.offsetHeight}px`
      );
    };

    const onScroll = () => {
      if (window.scrollY > 30) {
        nav.classList.add('scrolled');
      } else {
        nav.classList.remove('scrolled');
      }
      syncNavHeight();
    };

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', syncNavHeight);
    onScroll();
    syncNavHeight();
  }

  // ----- mobile drawer -----
  const toggle = document.querySelector('.nav__toggle');
  const drawer = document.querySelector('.nav__drawer');
  const backdrop = document.querySelector('.nav__drawer-backdrop');
  const closeBtn = document.querySelector('.nav__drawer-close');

  const setDrawerOpen = (open) => {
    if (!toggle || !drawer) return;
    toggle.classList.toggle('is-open', open);
    drawer.classList.toggle('is-open', open);
    document.body.classList.toggle('nav-open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    drawer.setAttribute('aria-hidden', open ? 'false' : 'true');
    toggle.setAttribute('aria-label', open ? 'Закрыть меню' : 'Открыть меню');
  };

  if (toggle && drawer) {
    toggle.addEventListener('click', () => {
      setDrawerOpen(!drawer.classList.contains('is-open'));
    });

    if (backdrop) {
      backdrop.addEventListener('click', () => setDrawerOpen(false));
    }

    if (closeBtn) {
      closeBtn.addEventListener('click', () => setDrawerOpen(false));
    }

    drawer.querySelectorAll('.nav__drawer-link, .nav__drawer-footer a').forEach((link) => {
      link.addEventListener('click', () => setDrawerOpen(false));
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && drawer.classList.contains('is-open')) {
        setDrawerOpen(false);
      }
    });
  }

  // ----- hero loaded class (kick scale animation) -----
  const hero = document.querySelector('.hero');
  if (hero) {
    requestAnimationFrame(() => hero.classList.add('loaded'));
  }

  // ----- reveal-on-scroll -----
  const revealEls = document.querySelectorAll('.reveal');
  if (revealEls.length && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('in-view');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15, rootMargin: '0px 0px -60px 0px' }
    );
    revealEls.forEach((el) => observer.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add('in-view'));
  }

  // ----- subtle parallax for hero background -----
  const heroBg = document.querySelector('.hero-bg');
  if (heroBg) {
    let ticking = false;
    window.addEventListener(
      'scroll',
      () => {
        if (!ticking) {
          window.requestAnimationFrame(() => {
            const y = window.scrollY;
            if (y < window.innerHeight) {
              heroBg.style.transform =
                `translate3d(0, ${y * 0.25}px, 0) scale(${1 + y * 0.0003})`;
            }
            ticking = false;
          });
          ticking = true;
        }
      },
      { passive: true }
    );
  }

  // ----- year in footer -----
  const year = document.querySelector('[data-year]');
  if (year) year.textContent = new Date().getFullYear();
})();
