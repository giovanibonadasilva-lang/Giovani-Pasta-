Numero1=int(input(print("escreva o primeiro numero")))
Numero2=int(input(print("escreva o segundo numero")))
Sinal=str(input(print("escreva o sinal")))

if Sinal=="+":    
    audicao= Numero1+Numero2
    print(audicao)


if Sinal=="-":
    Subtraction= Numero1-Numero2
    print(Subtraction)

if Sinal=="*":
    Multiplication= Numero1*Numero2
    print(Multiplication)

if Sinal=="/":
     if Numero2!=0:   
        Division=Numero1/Numero2
        print(Division)
        print("0")


if Sinal=="%":
    Modulus=Numero1%Numero2
    print(Modulus)

if Sinal=="**":
    Exponentiation=Numero1**Numero2
    print(Exponentiation)
if Sinal=="//":
    Floordivision=Numero1//Numero2
    print(Floordivision)



