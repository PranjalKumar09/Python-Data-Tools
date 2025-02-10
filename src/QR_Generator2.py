import qrcode
from PIL import Image




simpler_advanced = ""
while simpler_advanced != "simple" and  simpler_advanced != "advanced":# here not or but apply and bcz ((not and ...not and..) =>not( .. or .. )
    simpler_advanced = input("Simple or Advanced option: ").lower()

qr_text = input("Enter the string or website(full address) you want to make qrcode: ")
file_name = input("Enter the file name(without png) you save: ") + ".png"

if simpler_advanced== "simple":
    img = qrcode.make(qr_text)
    img.save(file_name)
    
elif simpler_advanced == "advanced":
    border_temp = int(input("Enter the border size : "))
    fill_color_temp = input("Enter fill colour: ").lower()
    back_color_temp = input("Enter back-ground colour: ").lower()
    
    qr_object = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H,
                       box_size = 10, border = border_temp)
    qr_object.add_data(qr_text)
    qr_object.make(fit = True)
    img = qr_object.make_image(fill_color = fill_color_temp, back_color = back_color_temp)
    img.save(file_name)

    
    