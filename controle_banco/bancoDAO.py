import sqlite3
from banco.database import Banco

#Controle de operações no banco de dados
class ControleBanco:
    def __init__(self, db: Banco):
        self.banco = db
        self.banco.conectar()

    #Criar tabelas no banco de dados
    def criar_tabelas(self):

        cur = self.banco.meuCursor()
        con = self.banco.con

        # id, Matricula, Nome, Idade, Nivel_Condutor, Nivel_Conduzido, Data_nivel
        tabela_aluno = '''
        CREATE TABLE IF NOT EXISTS Aluno (
            id INTEGER NOT NULL,
            Matricula INTEGER UNIQUE NOT NULL,
            Nome VARCHAR(50) NOT NULL,  
            Idade INTEGER,  
            Nivel_Condutor INTEGER,
            Nivel_Conduzido INTEGER,
            Data_nivel DATE,
            FOREIGN KEY(Nivel_Condutor) REFERENCES Niveis(id),
            FOREIGN KEY(Nivel_Conduzido) REFERENCES Niveis(id), 
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
        #id_exame, id_aluno, id_professor, tipo_exame, Conducao/Resposta, Abraco, Mecanica, Ritmo, Marcacao
        tabela_exame = '''
        CREATE TABLE IF NOT EXISTS Exame (
            id_exame INTEGER UNIQUE AUTOINCREMENT,
            id_aluno INTEGER NOT NULL,  
            id_professor INTEGER NOT NULL,
            tipo_exame INTEGER NOT NULL,
            ConducaoResposta INTEGER NOT NULL,  
            Abraco INTEGER NOT NULL,  
            Mecanica INTEGER NOT NULL,  
            Ritmo INTEGER NOT NULL,  
            Marcacao INTEGER NOT NULL,
            data_exame DATE,
            PRIMARY KEY(id_exame),
            FOREIGN KEY (id_aluno) REFERENCES Aluno(id),
            FOREIGN KEY (id_professor) REFERENCES Professor(id)
        );
        '''

        dadostabela_niveis = '''
        CREATE TABLE IF NOT EXISTS dadostabela_niveis (
            id INTEGER NOT NULL,
            nome VARCHAR(30),
            PRIMARY KEY(id);
        )'''
        
        cores_niveis = """
        INSERT TO Niveis (id, nome) VALUES 
        (1, 'Branco'), 
        (2, 'Amarelo'), 
        (3, 'Vermelho'), 
        (4, 'Azul'), 
        (5, 'Roxo'), 
        (6, 'Rosa');
        """

        try: 
            cur.execute(tabela_aluno)
            cur.execute(tabela_professor)
            cur.execute(tabela_exame)
            cur.execute(dadostabela_niveis)
            cur.execute(cores_niveis)

            con.commit()
        except sqlite3.Error as e:
            con.rollback()
            print(f"Erro ao criar as tabelas: {e}")
            return
        else:
            print("Tabelas criadas")
    
    #Adicionar aluno ao banco de dados
    def adicionar_aluno(self):

        cur = self.banco.meuCursor()
        con = self.banco.con

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
            try:
                cur.execute(inserir, (id, matricula, nome, idade, nivel_condutor, nivel_conduzido, data))
                con.commit()
                print("Aluno adicionado")
            except sqlite3.Error as e:
                con.rollback()
                print(f"Erro ao adicionar aluno: {e}")
                return

    #Adicionar professor ao banco de dados
    def adicionar_professor(self):

        cur = self.banco.meuCursor()
        con = self.banco.con

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

            try:
                cur.execute(inserir, (nome, id, avaliador))
                con.commit()
                print("Professor adicionado")
            except sqlite3.Error as e:
                con.rollback()
                print(f"Erro ao adicionar professor: {e}")
                return
    
    #Mostrar alunos através do id 
    def ver_alunos(self):

        cur = self.banco.meuCursor()
        
        try:
            id = int(input("Digite o id que deseja buscar: "))    
        except ValueError as v:
            print(f"Erro {v}")
            return
        else:
            aluno = f'''
            SELECT * FROM Aluno where id = {id};
            '''

            try:
                for linha in cur.execute(aluno):
                    print(linha)
            except sqlite3.Error as e:
                print(f"Erro ao buscar aluno: {e}")
                return