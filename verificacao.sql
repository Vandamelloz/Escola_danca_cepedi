--DROP TABLE IF EXISTS Niveis;

DROP TABLE IF EXISTS teste;

DROP TABLE IF EXISTS Professor;

DROP TABLE IF EXISTS lod;

DROP TABLE IF EXISTS lois;

DROP TABLE IF EXISTS medalha;

DROP TABLE IF EXISTS medalhas;

DROP TABLE IF EXISTS testesd;

CREATE TABLE IF NOT EXISTS dadostabela_niveis (
    id INTEGER NOT NULL,
    nome VARCHAR(30),
    PRIMARY KEY(id)
);

INSERT INTO dadostabela_niveis (id, nome) VALUES 
(1, 'Branco'), 
(2, 'Amarelo'), 
(3, 'Vermelho'), 
(4, 'Azul'), 
(5, 'Roxo'), 
(6, 'Rosa');

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

CREATE TABLE IF NOT EXISTS Professor (
            Nome VARCHAR(50) NOT NULL,  
            id INTEGER NOT NULL,  
            Avaliador VARCHAR(20) NOT NULL,
            PRIMARY KEY(id)
        );


CREATE TABLE IF NOT EXISTS Exame (
            id_aluno INTEGER NOT NULL,  
            id_professor INTEGER NOT NULL,
            tipo_exame INTEGER NOT NULL,
            ConducaoResposta INTEGER NOT NULL,  
            Abraco INTEGER NOT NULL,  
            Mecanica INTEGER NOT NULL,  
            Ritmo INTEGER NOT NULL,  
            Marcacao INTEGER NOT NULL,
            data_exame DATE,
            FOREIGN KEY (id_aluno) REFERENCES Aluno(id),
            FOREIGN KEY (id_professor) REFERENCES Professor(id)
        );

INSERT INTO Aluno (nome, Matricula, Idade, Nivel_Condutor, Nivel_Conduzido, Data_nivel) VALUES 
('Carlos Silva', 1001, 25, 2, 1, '2024-01-15'),
('Ana Pereira', 1002, 30, 3, 2, '2024-02-20'),
('Marcos Souza', 1003, 22, 1, 1, '2024-03-10');