#pip install pyqrcode module

import pyqrcode
qr = pyqrcode.create("https://www.linkedin.com/in/lava-kumar-reddy-501878261/")
qr.png("Linkedin.png")
