import qrcode

image = qrcode.make("http://192.168.3.208:8000")
image.save("qr.png")