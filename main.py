import sqlite3
from db.database import Banco
from controle_banco.controle import ControleBanco
from model.professor_classe import Professor
from dao.professorDAO import ManipularProfessor
from dao.niveisDAO import ManipularNiveis
from model.niveis_classe import Niveis
from model.aluno_classe import Aluno  

def main():
    opcao = -1
    meu_banco = Banco()
    controle = ControleBanco(meu_banco)
    prof_dao = ManipularProfessor(meu_banco)
    niveis_dao = ManipularNiveis(meu_banco)

    while opcao != 0:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Criar tabelas")
        print("2 - Adicionar alunos")
        print("3 - Gerenciar professores")
        print("4 - Ver alunos")
        print("5 - Gerenciar níveis do aluno")
        print("0 - Encerrar programa")

        try:
            opcao = int(input("Opção: "))
        except ValueError:
            print("Deve digitar um número válido.")
            continue

        match opcao:
            case 1:
                try:
                    meu_banco.conectar()
                    print("Conectado ao banco de dados.")
                except sqlite3.Error as e:
                    print(f"Erro ao conectar ao banco de dados: {e}")

            case 2:
                

            case 3:
                # --- SUBMENU PROFESSOR ---
                while True:
                    print("\n--- MENU PROFESSOR ---")
                    print("1 - Criar tabela Professor")
                    print("2 - Adicionar professor")
                    print("3 - Listar professores")
                    print("4 - Excluir professor")
                    print("0 - Voltar ao menu principal")

                    try:
                        sub_opcao = int(input("Opção: "))
                    except ValueError:
                        print("Digite um número válido.")
                        continue

                    if sub_opcao == 0:
                        break

                    match sub_opcao:
                        case 1:
                            try:
                                cur = meu_banco.meuCursor()
                                cur.execute("""
                                    CREATE TABLE IF NOT EXISTS Professor (
                                        id INTEGER PRIMARY KEY,
                                        nome TEXT NOT NULL,
                                        avaliador TEXT
                                    );
                                """)
                                meu_banco.con.commit()
                                print("Tabela 'Professor' criada com sucesso!")
                            except sqlite3.Error as e:
                                print(f"Erro ao criar tabela: {e}")

                        case 2:
                            try:
                                id_prof = int(input("ID do professor: "))
                                nome = input("Nome: ")
                                avaliador = input("Avaliador (Sim/Não): ")
                                p = Professor(id=id_prof, nome=nome, avaliador=avaliador)
                                prof_dao.adicionarProfessor(p)
                            except Exception as e:
                                print(f"Erro ao adicionar professor: {e}")

                        case 3:
                            professores = prof_dao.listarProfessores()
                            if professores:
                                print("\nLista de Professores:")
                                for p in professores:
                                    print(f"ID: {p.id} | Nome: {p.nome} | Avaliador: {p.avaliador}")
                            else:
                                print("Nenhum professor cadastrado.")

                        case 4:
                            try:
                                id_exc = int(input("ID do professor a excluir: "))
                                prof_dao.excluirProfessor(id_exc)
                            except Exception as e:
                                print(f"Erro ao excluir professor: {e}")

                        case _:
                            print("Opção inválida no menu de professor.")

            case 4:
                print("Função ainda em desenvolvimento.")

            case 5:
                # --- SUBMENU NÍVEIS ---
                while True:
                    print("\n------ MENU NÍVEIS ------")
                    print("1 - Criar tabela de níveis")
                    print("2 - Inserir/Atualizar nível de aluno")
                    print("3 - Listar níveis")
                    print("4 - Excluir nível")
                    print("0 - Voltar ao menu principal")

                    try:
                        sub_opcao = int(input("Opção: "))
                    except ValueError:
                        print("Digite um número válido.")
                        continue

                    if sub_opcao == 0:
                        break

                    match sub_opcao:
                        case 1:
                            try:
                                niveis_dao.criarTabela()
                            except Exception as e:
                                print(f"Erro ao criar tabela: {e}")

                        case 2:
                            try:
                                id_nivel = int(input("ID do nível: "))
                                id_aluno = int(input("ID do aluno: "))
                                nome_aluno = input("Nome do aluno: ")
                                nivel_aluno = input("Nível atual do aluno: ")
                                data_modificacao = input("Data da modificação (dd-mm-aaaa): ")

                                aluno = Aluno(id=id_aluno, nome=nome_aluno, nivel=None)
                                n = Niveis(
                                    id=id_nivel,
                                    nivel=nivel_aluno,
                                    aluno=aluno,
                                    data_modificacao=data_modificacao
                                )

                                niveis_dao.adicionarNivel(n)
                            except Exception as e:
                                print(f"Erro ao adicionar/atualizar nível: {e}")

                        case 3:
                            try:
                                niveis = niveis_dao.listarNiveis()
                                if niveis:
                                    print("\nLista de níveis:")
                                    for n in niveis:
                                        print(
                                            f"ID: {n.id} | "
                                            f"Aluno: {n.aluno.nome} (ID {n.aluno.id}) | "
                                            f"Nível: {n.nivel} | "
                                            f"Data: {n.data_modificacao}"
                                        )
                                else:
                                    print("Nenhum nível cadastrado.")
                            except Exception as e:
                                print(f"Erro ao listar níveis: {e}")

                        case 4:
                            try:
                                id_exc = int(input("Digite o ID do nível a excluir: "))
                                niveis_dao.excluirNivel(id_exc)
                            except Exception as e:
                                print(f"Erro ao excluir nível: {e}")

                        case _:
                            print("Opção inválida no menu de níveis.")

            case 0:
                if meu_banco.con:
                    meu_banco.desconectar()
                    print("Banco desconectado. Encerrando programa...")
                else:
                    print("Encerrando...")

            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    main()
