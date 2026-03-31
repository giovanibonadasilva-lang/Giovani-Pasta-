N1 = [7.5,8.0,6.5,9.0]
print(N1)
soma = sum(N1)
print(soma)
divisor=len(N1)
R1 = (soma/divisor)
print(R1)
N1.append(5.0)
print(N1)
N1.pop(2)
print(N1)
Ordem = sorted(N1)
print(Ordem)
print(list(reversed(Ordem)))
umatuple =(1,2,3,4)
print(umatuple)
list(umatuple)
print(umatuple)

T1 =(1,2)
T2 =(3,4)
doistuple =(T1 + T2)
print(doistuple)
umset = (1,3,3,6,5)
print(set(umset))
sett = {1,3,3,6,5}
sett.add(2)
sett.remove(6)
print(sett)

S1 ={1,2,3}
S2 ={3,4,5}
print(S1 & S2)
print(S1 | S2)
print(S2 - S1)

trestuple =(22,25,27,21)
if max(trestuple) > 26:
    print("o clima esta quente")

quartoset =(2,4,6,8)
print(quartoset)
digitado = (int(input("escreva o numero")))
if digitado in quartoset:
      print(quartoset)


