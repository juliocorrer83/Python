
repetir  = 's'
fatura = []
total = 0

while repetir == 's' :
    produto = input('digite o nome do produto : ').lower()
    preco = float(input('digite o preço do produto : '))
    fatura.append([produto,preco])
    total += preco
    repetir = input('deseja comprar mais algum produto , sim ou não ').lower()
    
for i in fatura:
    print(i[0],'-',i[1])

print ('o total da fatura é:', total)
    
    
