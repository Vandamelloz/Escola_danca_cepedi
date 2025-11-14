import sqlite3
from db.database import Banco
from controle_banco.controle import ControleBanco
from model.professor_classe import Professor
from dao.professorDAO import ManipularProfessor
from dao.niveisDAO import ManipularNiveis
from model.niveis_classe import Niveis
from model.aluno_classe import Aluno
from model.admin import Admin
from dao.adminDAO import ManipularAdmin

def main():
    opcao = -1
    meu_banco = Banco()
    controle = ControleBanco(meu_banco)
    prof_dao = ManipularProfessor(meu_banco)
    niveis_dao = ManipularNiveis(meu_banco)


    while opcao != 0:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Criar tabelas")
        print("2 - Gerenciar exames")
        print("3 - Gerenciar professores")
        print("4 - Gerenciar alunos")
        print("5 - Gerenciar níveis do aluno")
        print("6 - Gerenciar admins")
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
                    controle.criar_tabelas()
                    print("Conectado ao banco de dados.")
                except sqlite3.Error as e:
                    print(f"Erro ao conectar ao banco de dados: {e}")

            case 2:
              while True:
                    print("\n--- MENU EXAMES ---")
                    print("1 - Salvar exame")
                    print("2 - Listar exames")
                    print("3 - Atualizar exames")
                    print("4 - Excluir exame")
                    print("5 - Listar exames por aluno")
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
                                from model.exame_classe import Exame
                                from dao.exameDAO import ManipularExame
                                exame_dao = ManipularExame(meu_banco)

                                id_aluno = int(input("ID do aluno: "))
                                id_professor = int(input("ID do professor: "))
                                conduzao_resposta = int(input("Condução/Resposta: "))
                                abraco = int(input("Abraço: "))
                                mecanica = int(input("Mecânica: "))
                                ritmo = int(input("Ritmo: "))
                                marcacao = int(input("Marcação: "))
                                data_exame = input("Data do exame (dd-mm-aaaa): ")

                                exame = Exame(
                                    conduzao_resposta=conduzao_resposta,
                                    abraco=abraco,
                                    mecanica=mecanica,
                                    ritmo=ritmo,
                                    marcacao=marcacao,
                                    data_exame=data_exame
                                )

                                exame_dao.salvarExame(exame, id_aluno, id_professor)
                            except Exception as e:
                                print(f"Erro ao salvar exame: {e}")
                        case 2:
                            try:
                              from dao.exameDAO import ManipularExame
                              exame_dao = ManipularExame(meu_banco)
                              exame_dao.listarExames()
                            except Exception as e:
                                print(f"Erro ao listar exames: {e}")
                        case 3:
                            try:
                                from model.exame_classe import Exame
                                from dao.exameDAO import ManipularExame
                                exame_dao = ManipularExame(meu_banco)

                                id_exame = int(input("ID do exame a atualizar: "))
                                conduzao_resposta = int(input("Nova Condução/Resposta: "))
                                abraco = int(input("Novo Abraço: "))
                                mecanica = int(input("Nova Mecânica: "))
                                ritmo = int(input("Novo Ritmo: "))
                                marcacao = int(input("Nova Marcação: "))
                                data_exame = input("Nova Data do exame (dd-mm-aaaa): ")

                                exame = Exame(
                                    conduzao_resposta=conduzao_resposta,
                                    abraco=abraco,
                                    mecanica=mecanica,
                                    ritmo=ritmo,
                                    marcacao=marcacao,
                                    data_exame=data_exame
                                )

                                exame_dao.atualizarExame(id_exame, exame)
                            except Exception as e:
                                print(f"Erro ao atualizar exame: {e}")
                        case 4:
                            try:
                                from dao.exameDAO import ManipularExame
                                exame_dao = ManipularExame(meu_banco)

                                id_exame = int(input("ID do exame a excluir: "))
                                exame_dao.excluirExame(id_exame)
                            except Exception as e:
                                print(f"Erro ao excluir exame: {e}")
                        case 5:
                            try:
                                from dao.exameDAO import ManipularExame
                                exame_dao = ManipularExame(meu_banco)

                                id_aluno = int(input("ID do aluno para listar exames: "))
                                exame_dao.listarExamesPorAluno(id_aluno)
                            except Exception as e:
                                print(f"Erro ao listar exames por aluno: {e}")
                        case _:
                            print("Opção inválida no menu de exames.")

                          

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
                        print("Deve digitar um número válido.")
                        continue

                    if sub_opcao == 0:
                        break

                    match sub_opcao:
                        case 1:
                            try:
                                controle.criarTabelaProfessor()
                                print("Tabela Professor criada com sucesso!")
                            except sqlite3.Error as e:
                                print(f"Erro ao criar tabela: {e}")

                        case 2:
                            try:
                                id_prof = int(input("ID do professor: "))
                                nome = input("Nome do professor: ")
                                avaliador = input("Avaliador externo(S/N): ")
                                prof = Professor(id_prof, nome, avaliador)
                                prof_dao.adicionarProfessor(prof)
                            except Exception as e:
                                print(f"Erro ao adicionar professor: {e}")

                        case 3:
                            try:
                                prof_dao.listarProfessores()
                            except Exception as e:
                                print(f"Erro ao listar professores: {e}")

                        case 4:
                            try:
                                id_prof = int(input("ID do professor a excluir: "))
                                prof_dao.excluirProfessor(id_prof)
                            except Exception as e:
                                print(f"Erro ao excluir professor: {e}")

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
                while True:
                    print("\n--- MENU ALUNO ---")
                    print("1- Adicionar aluno")
                    print("2- Listar alunos")
                    print("3- Atualizar dados do aluno")
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
                                id_aluno = int(input("ID do aluno: "))
                                nome_aluno = input("Nome do aluno: ")
                                matricula = int(input("Matrícula do aluno: "))
                                idade = int(input("Idade do aluno: "))
                                nivel_condutor = input("Nível Condutor: ")
                                nivel_conduzido = input("Nível Conduzido: ")
                                data_nivel_condutor = input("Data Nível Condutor (dd-mm-aaaa): ")
                                data_nivel_conduzido = input("Data Nível Conduzido (dd-mm-aaaa): ")

                                a = Aluno(
                                    id=id_aluno,
                                    nome=nome_aluno,
                                    matricula=matricula,
                                    idade=idade,
                                    nivelCondutor=nivel_condutor,
                                    nivelConduzido=nivel_conduzido,
                                    dataNivelCondutor=data_nivel_condutor,
                                    dataNivelConduzido=data_nivel_conduzido
                                )

                                from dao.alunoDAO import ManipularAluno
                                aluno_dao = ManipularAluno(meu_banco)
                                aluno_dao.adicionarAluno(a)
                        
                            except Exception as e:
                                print(f"Erro ao listar alunos: {e}")
                        case 2:
                          try:
                                from dao.alunoDAO import ManipularAluno
                                aluno_dao = ManipularAluno(meu_banco)
                                aluno_dao.listar_alunos()
                          except Exception as e:
                                print(f"Erro ao listar alunos: {e}")
                        case 3:
                            try:
                                id_aluno = int(input("ID do aluno a atualizar: "))
                                nome_aluno = input("Nome do aluno: ")
                                matricula = int(input("Matrícula do aluno: "))
                                idade = int(input("Nova idade do aluno: "))
                                nivel_condutor = input("Novo Nível Condutor: ")
                                nivel_conduzido = input("Novo Nível Conduzido: ")
                                data_nivel_condutor = input("Nova Data Nível Condutor (dd-mm-aaaa): ")
                                data_nivel_conduzido = input("Nova Data Nível Conduzido (dd-mm-aaaa): ")

                                a = Aluno(
                                    id=id_aluno,
                                    nome=nome_aluno,
                                    matricula=matricula,
                                    idade=idade,
                                    nivelCondutor=nivel_condutor,
                                    nivelConduzido=nivel_conduzido,
                                    dataNivelCondutor=data_nivel_condutor,
                                    dataNivelConduzido=data_nivel_conduzido
                                )

                                from dao.alunoDAO import ManipularAluno
                                aluno_dao = ManipularAluno(meu_banco)
                                aluno_dao.atualizarDadosPessoasAluno(a)
                            except Exception as e:
                                print(f"Erro ao atualizar dados do aluno: {e}")

                        case _:
                            print("Opção inválida no menu de aluno.")

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
            case 6:
                # --- SUBMENU ADMIN ---
                import hashlib

                def criptografia(senha) -> str:
                    return hashlib.sha256(senha.encode('utf-8')).hexdigest()
                
                usuario = input("Usuário admin: ")
                senha = input("Senha admin: ")

                senhaCifrada = criptografia(senha)
                slq = "SELECT * FROM admin WHERE usuario = ?;"

                cur = meu_banco.meuCursor()
                cur.execute(slq, (usuario,))
                resultado = cur.fetchone()

                if resultado is None:
                    print("Acesso negado! Usuário admin não encontrado.")
                elif resultado[1] == senhaCifrada:
                    print("Login admin bem-sucedido!")
                    while True:
                        print("\n--- MENU ADMIN ---")
                        print("1 - Criar tabela Admin")
                        print("2 - Adicionar admin")
                        print("3 - Login admin")
                        print("4 - Atualizar senha admin")
                        print("5 - Listar admins")
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
                                    adm_dao = ManipularAdmin(meu_banco)
                                    adm_dao.criarTabelaAdmin()
                                except Exception as e:
                                    print(f"Erro ao criar tabela Admin: {e}")

                            case 2:
                                try:
                                    usuario = input("Nome de usuário do admin: ")
                                    senha = input("Senha do admin: ")
                                    novo_admin = Admin(usuario, senha)
                                    adm_dao = ManipularAdmin(meu_banco)
                                    adm_dao.adicionarAdmin(novo_admin)
                                except Exception as e:
                                    print(f"Erro ao adicionar admin: {e}")

                            case 3:
                                try:
                                    usuario = input("Usuário: ")
                                    senha = input("Senha: ")
                                    adm_dao = ManipularAdmin(meu_banco)
                                    if adm_dao.login(usuario, senha):
                                        print("Acesso de administrador permitido!")
                                    else:
                                        print("Acesso negado!")
                                except Exception as e:
                                    print(f"Erro ao fazer login: {e}")

                            case 4:
                                try:
                                    usuario = input("Usuário: ")
                                    senha_antiga = input("Senha antiga: ")
                                    senha_nova = input("Senha nova: ")
                                    adm_dao = ManipularAdmin(meu_banco)
                                    adm_dao.atualizarSenhaAdmin(usuario, senha_antiga, senha_nova)
                                except Exception as e:
                                    print(f"Erro ao atualizar senha: {e}")

                            case 5:
                                try:
                                    adm_dao = ManipularAdmin(meu_banco)
                                    adm_dao.listarAdmins()
                                except Exception as e:
                                    print(f"Erro ao listar admins: {e}")

                            case _:
                                print("Opção inválida no menu de admin.")
                else:
                    print("Acesso negado! Senha incorreta.")
                    continue

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
