texto=input("Tu texto: ")
if texto== texto.upper():
    abc="caracteres especial"
else:
    abc="caracteres especiales"
k=int(input("Valor de desplazamiento "))
cifrad=""
for c in texto:
    if c in abc:
        cifrad+= abc[(abc.index(c)+k)%(len(abc))]
    else:
        cifrad+=c
print("Texto cifrado: ", cifrad)
                    
