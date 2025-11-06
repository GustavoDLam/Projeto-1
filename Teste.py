
numeros = input("Digite os números separados por espaço: ").split() 
pares = filter(lambda x: int(x) % 2 == 0, numeros) 
print("Números pares:", " ".join(pares)) 


produtos = input("Digite os produtos separados por vírgula: ").split(",") 
precos = input("Digite os preços separados por vírgula: ").split(",") 
 
for produto, preco in zip(produtos, precos): 
    print(f"{produto.strip()}: {preco.strip()}") 

print("Teste para commits e atualizações do git/github, alteração 2")