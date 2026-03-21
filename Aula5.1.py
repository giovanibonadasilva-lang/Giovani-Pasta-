T=(int(input("escreva as horas")))
preço=(int(10+5*T))
P2=(int(20+8*T))
if T<1:
    print("Gratis")

if T>=1 and T<3:
    print(10+5*T -5)

if T>=3:
    N2=(int(T+P2))
    print(20+8*T -8)