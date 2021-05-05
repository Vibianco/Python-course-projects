text = "X-DSPAM-Confidence:    0.8475"

busqueda = text.find('0.8475')
rtado = (text[busqueda:])
rtadonum = float(rtado)
print(rtadonum)
