import os

'''

Assim que se usa para fazer comentarios!

Inputs:


Outputs:



'''

restaurantes = [{"Nome":"Iwata", "Categoria":"Japones", "Ativo":False}, 
                {"Nome":"Dom Peppi", "Categoria":"Pizza", "Ativo":True}, 
                {"Nome":"La Pergoletta", "Categoria":"Italiano", "Ativo":False}]

def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alterar Estado Do Restaurante')
    print('4. Sair')

def finalizar_app():
    os.system('cls')
    print("Finalizando o app!\n")

def voltar_ao_menu_principal():
    input("Digite uma tecla para voltar ao menu principal: ")
    main()
    
def opcao_invalida():
    print("Opcao invalida!\n")
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    os.system('cls')
    print("Cadastro de novos restaurantes\n")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante: {nome_do_restaurante}")
    dados_do_restaurante = {"Nome":nome_do_restaurante, "Categoria":categoria, "Ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
    input("Digite uma tecla para voltar ao menu principal: ")
    main()

def listar_restaurantes():
    os.system('cls')
    print("Listando os restaurantes")
    
    print(f"{"Nome do restaurante".ljust(21)} | {"Categoria".ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["Nome"]
        categoria_restaurante = restaurante["Categoria"]
        ativo = "Ativado" if restaurante["Ativo"] else "Desativado"
        print(f"-{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}")
    input("Digite uma tecla para voltar ao menu principal: ")
    main()

def alternar_estado_restaurante():
    print("Alterando estado do restaurante. ")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["Nome"]:
            restaurante_encontrado = True
            restaurante["Ativo"] = not restaurante["Ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["Ativo"] else f"O retaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
    
    if not restaurante_encontrado:
        print("O restaurante nao foi encontrado")

    voltar_ao_menu_principal()
    
def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))
        print(f'Voce escolheu a opcao {opcao_escolhida}!')
        print(type(opcao_escolhida))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main()
