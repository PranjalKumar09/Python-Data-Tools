"""
make -> basic fn of QR module
img = qrcode.make(link/string any one)
type(img)  # qrcode.image.pil.PilImage
img.save("name_of_file.png")

ADVANCED USAGE by QRCode 
qr = qrcode.QRCode(
    version=1, #The version parameter is an integer from 1 to 40 that controls the size of the QR Code (the smallest, version 1, is a 21x21 matrix)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10, #The box_size parameter controls how many pixels each “box” of the QR code is.
    border=4, #The border parameter controls how many boxes thick the border should be (the default is 4, which is the minimum according to the specs).
)
qr.add_data(link/string any one)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

ERROR_CORRECT_L
About 7% or less errors can be corrected.

ERROR_CORRECT_M (default)
About 15% or less errors can be corrected.

ERROR_CORRECT_Q
About 25% or less errors can be corrected.

ERROR_CORRECT_H.
About 30% or less errors can be corrected


"""



import qrcode
from PIL import Image

img = qrcode.make("https://www.google.com")
img.save("qr1_youtube.png")

qr_object = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H,
          box_size = 10, border = 4,)
qr_object.add_data("https://www.wscubetech.com/")
qr_object.make(fit = True)
img = qr_object.make_image(fill_color = "red" , back_color = "blue")
img.save("QR2_edited.png")