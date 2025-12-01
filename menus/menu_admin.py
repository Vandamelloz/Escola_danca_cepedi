from dao.adminDAO import ManipularAdmin
from db.database import Banco
from model import Admin

def exibir_menu(meu_banco: Banco):
    adm_dao= ManipularAdmin(meu_banco)
    print("\n--- MENU ADMIN ---")
    print("1 - Criar tabela Admin")
    print("2 - Adicionar admin")
    print("3- Atualizar senha admin")
    print("4 -listar admins")
    print("0 - Voltar ao menu principal")

    try:
        sub_opcao=int(input("Opção: "))
    except ValueError:
        print("Digite um número válido!")
    if sub_opcao ==0:
        print("Voltando ao menu principal! ")
        return 1
    match sub_opcao:
        case 1:
            try:
                adm_dao.criarTabelaAdmin()
                print("✅ Tabela Admin criada com sucesso.")
            except Exception as e:
                print(f"❌ Erro ao criar tabela Admin: {e}")  
        case 2:
            try:
                usuario=input("Nome de usuário do novo administrador: ")
                senha=input("Senha do novo administrador: ")

                novo_admin= Admin(usuario, senha)

                adm_dao.adicionarAdmin(novo_admin)
                print(f"Administrador '{usuario}' adicionado com sucesso!")
            except Exception as e:
                print(f"Erro ao adicionar administrador: {e}")
        case 3:
            try:
                usuario= input("Nome do usuário que deseja atualizar: ")
                senha_antiga=input("Senha antiga: ")
                senha_nova=input("digite a nova senha aqui: ")

                if adm_dao.atualizarSenha(usuario, senha_antiga, senha_nova):
                    print(f"Senha do administrador '{usuario}' atualizada com sucesso para '{senha_nova}'")
            except Exception as e:
                print(f"Erro ao atualizar senha do '{usuario}', erro: {e}")
        case 4:
            try:
                adm_dao.listarAdmin()
            except Exception as e:
                print(f"Erro ao listar administradores: {e}")
            
                      







    