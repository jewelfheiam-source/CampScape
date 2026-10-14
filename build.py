# -*- coding: utf-8 -*-
"""Builds shared header/footer into each page. Run: python3 build.py"""
import re, pathlib

def header(active, hero_html=None):
    items = [
        ("index.html","Home"),("about.html","About Us"),("destinations.html","Destinations"),
        ("packages.html","Tour Packages"),("gallery.html","Gallery"),
        ("location-info.html","Location Info"),("travel-guide.html","Travel Guide"),
        ("booking.html","Book Now"),("community.html","Community"),("contact.html","Contact"),
    ]
    links = "".join(f'<a href="{h}">{t}</a>' for h,t in items)
    return f'''<header class="site">
  <div class="container navbar">
    <a class="logo" href="index.html" aria-label="CampScape home">
      <svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="30" fill="#2d5a3d"/><path d="M14 44 L32 18 L50 44 Z" fill="#f5efe3"/><path d="M23 44 L32 30 L41 44 Z" fill="#e8842c"/><circle cx="32" cy="13" r="5" fill="#e8842c"/><path d="M8 48 Q32 40 56 48 L56 52 L8 52 Z" fill="#7a5230"/></svg>
      <span class="logo-text">Camp<span>Scape</span></span>
    </a>
    <button class="menu-toggle" aria-label="Toggle navigation menu" aria-expanded="false">&#9776; Menu</button>
    <nav class="main-nav" aria-label="Main navigation"><ul>{links}</ul></nav>
  </div>
</header>'''

def footer():
    return '''<footer class="site">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="logo" href="index.html" style="margin-bottom:.8rem">
          <svg viewBox="0 0 64 64" aria-hidden="true" style="width:34px;height:34px"><circle cx="32" cy="32" r="30" fill="#2d5a3d"/><path d="M14 44 L32 18 L50 44 Z" fill="#f5efe3"/><path d="M23 44 L32 30 L41 44 Z" fill="#e8842c"/><circle cx="32" cy="13" r="5" fill="#e8842c"/><path d="M8 48 Q32 40 56 48 L56 52 L8 52 Z" fill="#7a5230"/></svg>
          <span class="logo-text" style="font-size:1.2rem">Camp<span>Scape</span></span>
        </a>
        <p>Explore. Camp. Discover Mindoro. CampScape is an academic sample website promoting camping destinations and outdoor adventures in Oriental Mindoro, Philippines.</p>
        <div class="social-links">
          <a href="https://www.facebook.com/" target="_blank" rel="noopener">Facebook (sample)</a>
          <a href="https://www.instagram.com/" target="_blank" rel="noopener">Instagram (sample)</a>
          <a href="https://www.youtube.com/" target="_blank" rel="noopener">YouTube (sample)</a>
        </div>
      </div>
      <div>
        <h4>Quick Links</h4>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="about.html">About Us</a></li>
          <li><a href="destinations.html">Camping Destinations</a></li>
          <li><a href="packages.html">Tour Packages</a></li>
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="travel-guide.html">Travel Guide</a></li>
        </ul>
      </div>
      <div>
        <h4>Plan Your Trip</h4>
        <ul>
          <li><a href="location-info.html">How to Get There</a></li>
          <li><a href="booking.html">Book / Inquire</a></li>
          <li><a href="community.html">Blog &amp; Community</a></li>
          <li><a href="contact.html">Contact Us</a></li>
          <li><a href="credits.html">Photo Credits</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li>Email: hello@campscape.ph (sample)</li>
          <li>Mobile: +63 917 555 0143 (sample)</li>
          <li>Calapan City, Oriental Mindoro (sample)</li>
          <li>Mon to Sat, 8:00 AM to 6:00 PM (sample)</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span class="year"></span> CampScape. Student academic project for Applied Business Tools and Technologies in Tourism.</span>
      <span><a href="credits.html">Photo credits &amp; disclaimer</a> | Sample content, not a real tour operator.</span>
    </div>
  </div>
</footer>
<script src="js/main.js"></script>'''

for f in pathlib.Path('.').glob('*.html'):
    html = f.read_text(encoding='utf-8')
    m = re.search(r'<!--HEADER:([\w-]+)-->', html)
    if m:
        html = re.sub(r'<!--HEADER:[\w-]+-->', header(m.group(1)), html)
    if 'href="css/style.css"' not in html:
        html = html.replace('</head>', '  <link rel="stylesheet" href="css/style.css">\n</head>')
    html = html.replace('<!--FOOTER-->', footer())
    f.write_text(html, encoding='utf-8')
    print('built', f.name)
