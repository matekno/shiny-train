import re
texto= 'promo code is godeto25y869'
codeViejo='fds'
def code20(texto,codeViejo):     #godeto
    if re.search('.*(godeto[0-9]+[a-z][0-9]+)',str(texto)) and len(texto) >= 12:
        texto=re.findall('.*(godeto[0-9]+[a-z][0-9]+)',str(texto))[0]
    else:
        texto=codeViejo
    return texto

nana=code20(texto,codeViejo)
print(nana)