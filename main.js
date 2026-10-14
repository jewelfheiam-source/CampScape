// CampScape - shared site behavior
document.addEventListener('DOMContentLoaded', function () {
  // Active nav highlighting
  var path = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('nav.main-nav a').forEach(function (a) {
    if (a.getAttribute('href') === path) a.classList.add('active');
  });

  // Mobile menu toggle
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.querySelector('nav.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Year in footer
  document.querySelectorAll('.year').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // Booking / contact / inquiry forms (client-side demo handling)
  document.querySelectorAll('form.demo-form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var success = form.parentElement.querySelector('.form-success') ||
                    document.getElementById(form.dataset.successId || '');
      // simple required-field check
      var valid = true;
      form.querySelectorAll('[required]').forEach(function (f) {
        if (!f.value.trim() || !f.checkValidity()) { valid = false; f.style.borderColor = '#c0392b'; }
        else { f.style.borderColor = ''; }
      });
      if (!valid) return;
      if (success) {
        success.classList.add('show');
        success.setAttribute('role', 'status');
        var msgEl = success.querySelector('.ref-num');
        if (msgEl) {
          msgEl.textContent = 'CS-' + Date.now().toString().slice(-6);
        }
        success.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      form.reset();
    });
  });

  // Preselect a destination or package from links
  var params = new URLSearchParams(location.search);
  var btype = document.getElementById('b-type');
  if (btype) {
    var wanted = params.get('package') || params.get('dest') || '';
    var map = { 'nature-escape':'Nature Escape Package (3D2N)', 'beach-camping':'Beach Camping Adventure (3D2N)', 'adventure-exploration':'Adventure & Exploration Package (4D3N)', 'white-beach':'White Beach, Puerto Galera', 'sabang':'Sabang Beach, Puerto Galera', 'bulalacao':'Bulalacao Island Circuit', 'banilad':'Banilad Beach, Pinamalayan', 'naujan':'Lake Naujan National Park', 'halcon':'Mount Halcon expedition', 'tukuran':'Tukuran Falls' };
    if (map[wanted]) btype.value = map[wanted];
  }

  // Gallery lightbox
  document.querySelectorAll('.gallery-item img').forEach(function (img) {
    img.addEventListener('click', function () {
      var overlay = document.createElement('div');
      overlay.style.cssText = 'position:fixed;inset:0;background:rgba(20,30,24,.92);display:flex;align-items:center;justify-content:center;z-index:999;cursor:zoom-out;padding:2rem';
      var big = document.createElement('img');
      big.src = img.src.replace(/\/\d+px-/, '/1600px-');
      if (big.src.indexOf('/img/') === -1) big.src = img.src;
      big.style.cssText = 'max-width:95%;max-height:90%;border-radius:8px;object-fit:contain';
      overlay.appendChild(big);
      overlay.addEventListener('click', function () { overlay.remove(); });
      document.body.appendChild(overlay);
    });
  });
});
