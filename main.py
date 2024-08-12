import pyqrcode
from pyqrcode import QRCode

s = "https://www.youtube.com/"

url = pyqrcode.create(s)
print("url ", url)

url.svg("gmail-qr.svg", scale=8)
