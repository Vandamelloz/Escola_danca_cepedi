import sqlite3

#Conectar/Criar banco de dados
def conectar():
    global con
    global cur
    con = sqlite3.connect("escola.db")
    cur = con.cursor()
    print("Conectado")

#Criar tabelas
def criar_tabelas():

    # id, Matricula, Nome, Idade, Nivel_Condutor, Nivel_Conduzido, Data_nivel
    tabela_aluno = '''
    CREATE TABLE IF NOT EXISTS Aluno (
        id INTEGER NOT NULL,
        Matricula INTEGER UNIQUE NOT NULL,
        Nome VARCHAR(50) NOT NULL,  
        Idade INTEGER,  
        Nivel_Condutor VARCHAR(20),
        Nivel_Conduzido VARCHAR(20),
        Data_nivel DATE,  
        PRIMARY KEY(id)
    );
    '''

    # Nome, id, Avaliador
    tabela_professor = '''
    CREATE TABLE IF NOT EXISTS Professor (
        Nome VARCHAR(50) NOT NULL,  
        id INTEGER NOT NULL,  
        Avaliador VARCHAR(20) NOT NULL,
        PRIMARY KEY(id)
    );
    '''
    #id_aluno, id_professor, Conducao/Resposta, Abraco, Mecanica, Ritmo, Marcacao
    tabela_exame = '''
    CREATE TABLE IF NOT EXISTS Exame_condutor (
        id_aluno INTEGER NOT NULL,  
        id_professor INTEGER NOT NULL,  
        ConducaoResposta INTEGER NOT NULL,  
        Abraco INTEGER NOT NULL,  
        Mecanica INTEGER NOT NULL,  
        Ritmo INTEGER NOT NULL,  
        Marcacao INTEGER NOT NULL,
        FOREIGN KEY (id_aluno) REFERENCES Aluno(id),
        FOREIGN KEY (id_professor) REFERENCES Professor(id)
    );
    '''

    tabela_niveis = '''
    CREATE IF NOT EXISTS Niveis (
        id INTEGER NOT NULL,
        nivel VARCHAR(30),
        id_aluno INTEGER NOT NULL,
        PRIMARY KEY(id),
        FOREIGN KEY(id_aluno) REFERENCES aluno(id)
    );
    '''

    cur.execute(tabela_aluno)
    cur.execute(tabela_professor)
    cur.execute(tabela_exame)
    cur.execute(tabela_niveis)

    con.commit()
    print("Tabelas criadas")

#Adicionar aluno
def adicionar_aluno():

    try:
        id = int(input("Digite o id do aluno: "))
        nome = input("Digite o nome do aluno: ")
        matricula = int(input("Digite o número de matricula do aluno: "))
        idade = int(input("Digite a idade do aluno: "))
        nivel_condutor = input("Qual nível de condutor do aluno? \"Branco, Amarelo, Vermelho, Azul, Roxo, Rosa\": ")
        nivel_conduzido = input("Qual nível de conduzido do aluno? \"Branco, Amarelo, Vermelho, Azul, Roxo, Rosa\": ")
        data = input("Digite a data que o aluno ganhou o nível no formato \"dd-mm-aaaa\": ")
    except sqlite3.IntegrityError as s: #erro ao cadastrar chave primária repetida
        print(f"Id já cadastrado no banco de dados {s}")
        return
    except ValueError as v:
        print(f"Valor inserido incorreto {v}")
        return
    except Exception as e:
        print(f"Erro {e}")
        return
    else:
        inserir = '''
        INSERT INTO Aluno (id, Matricula, Nome, Idade, Nivel_Condutor, Nivel_Conduzido, Data_nivel)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        '''

        cur.execute(inserir, (id, matricula, nome, idade, nivel_condutor, nivel_conduzido, data))
        con.commit()
        print("Aluno adicionado")

#Adicionar professor
def adicionar_professor():

    try:
        nome = input("Digite o nome do professor: ")
        id = int(input("Digite o id do professor: "))
        avaliador = input("digite se é um avaliador externo/interno: ")
    except sqlite3.IntegrityError as s:
        print(f"Id já cadastrado no banco de dados {s}")
        return
    except ValueError as v:
        print(f"Valor inserido incorreto {v}")
        return
    except Exception as e:
        print(f"Erro {e}")
        return
    else:    

        inserir = '''
        INSERT INTO Professor (Nome, id, Avaliador) VALUES (?, ?, ?);
        '''

        cur.execute(inserir, (nome, id, avaliador))
        con.commit()
        print("Professor adicionado")

#Mostrar alunos através do id
def ver_alunos():
    try:
        id = int(input("Digite o id que deseja buscar: "))    
    except ValueError as v:
        print(f"Erro {v}")
        return
    else:
        aluno = f'''
        SELECT * FROM Aluno where id = {id};
        '''

        for linha in cur.execute(aluno):
            print(linha)

#Modificar nível do aluno 
def modificar_nivel():

    try:
        id = int(input("Digite o id do aluno que deseja modificar o nível: "))
        escolha = int(input("O nível a ser modificado é? 1 - Condutor ou 2 - Conduzido: "))
        cor = input("Digite a cor do novo nível do aluno: ")
    except ValueError as v:
        print(f"Erro {v}")
        return
    else:
        if escolha == 1:
            modificacao = '''
            UPDATE Aluno SET Nivel_condutor = ? WHERE id = ?;
            '''
            #Usar corretamente os dados de busca e alteração
            cur.execute(modificacao, (cor, id))
            print("Nível alterado")
            con.commit()

        elif escolha == 2:
            modificacao = '''
            UPDATE Aluno SET Nivel_conduzido = ? WHERE id = ?;
            '''
            cur.execute(modificacao, (cor, id))
            print("Nível alterado")
            con.commit()
        else:
            print("Opção inválida, voltando para o menu")
            return

#Parte principal do programa
if __name__ == "__main__":

    opcao = -1

    while opcao != 0:
        print("1 - Adicionar aluno")
        print("2 - Adicionar professor")
        print("3 - Ver alunos")
        print("4 - Alterar nível do aluno")
        print("0 - Encerrar programa")

        try:
            opcao = int(input("Opção: "))
        except ValueError:
            print("Deve digitar um número inteiro")
        else:
            match opcao:
                case 1:
                    conectar()
                    adicionar_aluno()
                case 2:
                    conectar()
                    adicionar_professor()
                case 3:
                    conectar()
                    ver_alunos()
                case 4:
                    conectar()
                    modificar_nivel()
                case 0:
                    print("Encerrando... ")
                    con.close()
                case _:
                    print("Opção inválida")