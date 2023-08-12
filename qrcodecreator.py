import qrcode

texto='ESSE É O PARAMÊTRO QUE DEVE SER MUDADO PARA ALTERAR O QRCODE'

qr_generator=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr_generator.add_data(texto)
qr_generator.make(fit=True)
img= qr_generator.make_image(fill_color='black',bank_color='white')

img.save('qrcode.png')