#LOCAL IMPORTS
import sqlite3
from banco.database import Banco
from controle_banco.bancoDAO import ControleBanco
from controle_banco.professorDAO import ManipularProfessor
from model.professor_classe import Professor 

#Parte principal do programa
def main():
    opcao = -1
    meu_banco = Banco()
    controle = ControleBanco(meu_banco)  # Criando uma única instância do ControleBanco
    professor2 = Professor( )
    professor = ManipularProfessor(meu_banco, professor2)

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
        else:
            match opcao: #ainda não organizei os casos !!!!!!!!!!!!!!!
                case 1:
                    try:
                        meu_banco.conectar()
                    except sqlite3.Error as e:
                        print(f"Erro ao conectar ao banco de dados: {e}")
                case 2:
                    controle.criar_tabelas()
                case 3:
                    professor.adicionarProfessor(professor.nome,professor.id, professor.avaliador)
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