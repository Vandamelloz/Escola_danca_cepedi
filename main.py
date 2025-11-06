#LOCAL IMPORTS
from db.database import Banco
from controle_banco.controle import ControleBanco

#Parte principal do programa
def main():
    opcao = -1
    meu_banco = Banco() 

    while opcao != 0:
        print("1 - Criar tabelas")
        print("2 - Adicionar alunos")
        print("3 - Adicionar professor")
        print("4 - Ver alunos")
        print("5 - Alterar nível do aluno")
        print("0 - Encerrar programa")

        try:
            opcao = int(input("Opção: "))
        except ValueError:
            print("Deve digitar um número inteiro")
            continue

        match opcao: #ainda não organizei os casos !!!!!!!!!!!!!!!
            case 1:
                meu_banco.conectar()
            case 2:
                controle = ControleBanco(meu_banco)
                controle.criar_tabelas()
            case 3:
                print("caso 3")
            case 4:
                print("caso 4")
            case 5:
                print("caso 5")
            case 0:
                if meu_banco.con:
                    meu_banco.deconectar()
                    print("Banco desconectado. Encerrando programa...")
                else:
                    print("Encerrando...")
            case _:
                print("Opção inválida") 

if __name__ == "__main__":
    main()