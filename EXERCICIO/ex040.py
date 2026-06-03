print("-=-")
print("Analisador de triângulos")
print("-=-" * 10)
a = float(input("primeiro segmento"))
b = float(input("segundo segmento"))
c = float(input("terceiro segmento"))
if a<b+c and b<a+c and c<a+b and a== b == c:
    print("Os segmentos acima podem formar um triangulo Equilatero")
elif a<b+c and b<a+c and c<a+b and a== b or a== b==c:
    print("Os segmentos acima podem formar um triangulo Isósceles")
elif a<b+c and b<a+c and c<a+b and a!= b and a!= c and b!=c:
    print("Os segmentos acima podem formar um triangulo Escaleno")
