/* ВалуПро — site behaviour. No inline handlers (CSP-friendly). */
(function () {
  'use strict';

  var LANG = (document.documentElement.getAttribute('lang') || 'bg').slice(0,2);
  var LOCALE = LANG === 'en' ? 'en-US' : 'bg-BG';
  var MSG_OK = LANG === 'en'
    ? 'Thank you! Your message passed validation. Connect the form to your server to actually send it.'
    : 'Благодарим! Съобщението е валидирано. Свържете формата с вашия сървър, за да се изпраща.';

  // safe localStorage wrapper (degrades gracefully if blocked)
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };

  /* ---- Theme ---- */
  var saved = store.get('vp-theme');
  if (saved === 'dark' || saved === 'light') {
    document.documentElement.setAttribute('data-theme', saved);
  }
  function toggleTheme() {
    var cur = document.documentElement.getAttribute('data-theme');
    if (!cur) {
      cur = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    var next = cur === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    store.set('vp-theme', next);
  }

  /* ---- Mobile nav ---- */
  function toggleNav(btn) {
    var links = document.getElementById('navLinks');
    if (!links) return;
    var open = links.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }

  /* ---- Sticky nav shadow ---- */
  var nav = document.querySelector('.nav');
  function onScroll() {
    if (nav) nav.classList.toggle('scrolled', window.scrollY > 8);
    var tt = document.getElementById('toTop');
    if (tt) tt.classList.toggle('show', window.scrollY > 500);
  }

  /* ---- Count-up ---- */
  function countUp(el) {
    var target = parseFloat(el.getAttribute('data-target'));
    var suffix = el.getAttribute('data-suffix') || '';
    var dur = 1400, start = null;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      var val = Math.floor(eased * target);
      el.textContent = val.toLocaleString(LOCALE) + suffix;
      if (p < 1) requestAnimationFrame(step);
      else el.textContent = target.toLocaleString(LOCALE) + suffix;
    }
    requestAnimationFrame(step);
  }

  /* ---- Reveal + count via IntersectionObserver ---- */
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function initReveal() {
    var items = document.querySelectorAll('.reveal');
    var nums = document.querySelectorAll('[data-target]');
    if (reduce || !('IntersectionObserver' in window)) {
      items.forEach(function (i) { i.classList.add('in'); });
      nums.forEach(function (n) { n.textContent = parseFloat(n.getAttribute('data-target')).toLocaleString(LOCALE) + (n.getAttribute('data-suffix') || ''); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.15 });
    items.forEach(function (i) { io.observe(i); });

    var io2 = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { countUp(e.target); io2.unobserve(e.target); }
      });
    }, { threshold: 0.5 });
    nums.forEach(function (n) { io2.observe(n); });
  }

  /* ---- FAQ accordion (a11y) ---- */
  function initFaq() {
    document.querySelectorAll('.faq-q').forEach(function (q) {
      q.setAttribute('aria-expanded', 'false');
      q.addEventListener('click', function () {
        var item = q.parentElement;
        var open = item.classList.toggle('open');
        q.setAttribute('aria-expanded', open ? 'true' : 'false');
        var a = item.querySelector('.faq-a');
        if (a) a.style.maxHeight = open ? a.scrollHeight + 'px' : '0';
      });
    });
  }

  /* ---- Cookie consent (GDPR) ---- */
  function initCookie() {
    var banner = document.getElementById('cookieBanner');
    if (!banner) return;
    if (!store.get('vp-cookie')) banner.classList.add('show');
    banner.addEventListener('click', function (e) {
      var action = e.target.getAttribute('data-cookie');
      if (action) { store.set('vp-cookie', action); banner.classList.remove('show'); }
    });
  }

  /* ---- Contact form validation + honeypot ---- */
  function initForm() {
    var form = document.getElementById('contactForm');
    if (!form) return;
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      // honeypot: bots fill hidden field -> silently drop
      var hp = form.querySelector('input[name="company_website"]');
      if (hp && hp.value) return;
      var ok = true;
      form.querySelectorAll('[data-required]').forEach(function (f) {
        var field = f.closest('.field');
        var valid = f.value.trim() !== '';
        if (f.type === 'email') valid = valid && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f.value);
        field.classList.toggle('invalid', !valid);
        if (!valid) ok = false;
      });
      if (ok) {
        var msg = document.getElementById('formMsg');
        if (msg) { msg.classList.add('ok'); msg.textContent = MSG_OK; }
        form.reset();
      }
    });
  }

  /* ---- Wire up ---- */
  document.addEventListener('DOMContentLoaded', function () {
    var tb = document.getElementById('themeToggle');
    if (tb) tb.addEventListener('click', toggleTheme);
    var nt = document.getElementById('navToggle');
    if (nt) nt.addEventListener('click', function () { toggleNav(nt); });
    var tt = document.getElementById('toTop');
    if (tt) tt.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); });
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
    initReveal(); initFaq(); initCookie(); initForm();
    var ls = document.querySelector('.lang-switch');
    if (ls) ls.addEventListener('click', function () { try { localStorage.setItem('vp-lang', ls.getAttribute('data-lang')); } catch (e) {} });
  });
})();
