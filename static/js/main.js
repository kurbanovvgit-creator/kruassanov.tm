// Kruassanov — UI interactions
(function () {
  'use strict';

  // ----- sticky nav -----
  const nav = document.querySelector('.nav');
  if (nav) {
    const onScroll = () => {
      if (window.scrollY > 30) {
        nav.classList.add('scrolled');
      } else {
        nav.classList.remove('scrolled');
      }
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // ----- mobile menu -----
  const burger = document.querySelector('.burger');
  const mobileMenu = document.querySelector('.mobile-menu');
  if (burger && mobileMenu) {
    const toggle = () => {
      burger.classList.toggle('open');
      mobileMenu.classList.toggle('open');
      document.body.style.overflow =
        mobileMenu.classList.contains('open') ? 'hidden' : '';
    };
    burger.addEventListener('click', toggle);
    mobileMenu.querySelectorAll('a').forEach((a) =>
      a.addEventListener('click', () => {
        if (mobileMenu.classList.contains('open')) toggle();
      })
    );
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
