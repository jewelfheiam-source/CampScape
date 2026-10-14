"""Generate a QR code after deploying CampScape.
Usage: python3 generate_qr.py https://YOUR-USERNAME.github.io/campscape-mindoro/
Install: python3 -m pip install qrcode[pil]
"""
import sys
import qrcode
if len(sys.argv) != 2 or not sys.argv[1].startswith(('https://','http://')):
    raise SystemExit('Usage: python3 generate_qr.py https://YOUR-LIVE-SITE-URL/')
url=sys.argv[1]
qr=qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4)
qr.add_data(url); qr.make(fit=True)
qr.make_image(fill_color='#1e3f2a', back_color='white').save('campscape-qr.png')
print('Created campscape-qr.png for', url)
