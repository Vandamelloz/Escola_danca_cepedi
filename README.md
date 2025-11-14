# 🩰 Projeto Alunos— Sistema de Avaliação (Escola de Dança) 

Projeto desenvolvido como atividade prática do curso — backend-python CEPEDI VCA para gestão de alunos, professores e exames em uma escola de dança. Este repositório registra nosso aprendizado em Programação Orientada a Objetos (POO) e persistência com SQLite.

---

## 🎯 Objetivos coloborativos deste projeto
- Aplicar conceitos de POO em um projeto real (Model, DAO, Service);
- Implementar padrões básicos (DAO, organização em camadas);
- Praticar tratamento de persistência com SQLite e operações CRUD;
- Gerenciar histórico de exames e evolução de alunos;
- Aprender a proteger credenciais usando hashes.

---

## ⚙️ Funcionalidades (implementadas / em desenvolvimento)
- Cadastro, edição, listagem de alunos e professores
- Registro de exames com critérios (condução, abraço, mecânica, ritmo, marcação)
- Histórico de exames por aluno
- Autenticação básica de administrador (hash SHA‑256)
- Migrações e scripts utilitários (scripts/)

Nota: algumas funcionalidades ainda estão em evolução.

---

## 📁 Estrutura do projeto
- db/ — conexão e scripts do banco (database.py)  
- model/ — classes de domínio (Aluno, Professor, Exame, Admin, Niveis)  
- dao/ — Data Access Objects (CRUD)  
- controle_banco/ — rotinas para criar/manter tabelas  
- utils/ — utilitários (ex.: seguranca.py para hash de senhas)  
- scripts/ — scripts auxiliares (migrações, seeds)  
- test/ — exemplos e testes manuais  
- main.py — CLI / ponto de entrada

---

## ▶️ Como executar (local / para testes)
1. Clone:
```bash
git clone https://github.com/Vandamelloz/Escola_danca_cepedi.git
cd Escola_danca_cepedi
```
2. (Opcional) criar e ativar venv:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. Inicializar banco (pelo menu ou script):
```bash
python3 main.py   # use as opções para criar tabelas
# ou
python3 scripts/criar_tabelas.py
```
4. Executar a aplicação:
```bash
python3 main.py
```

---

## 🔐 Senhas
Senhas são armazenadas como hash SHA‑256 em utils/seguranca.py. Use ManipularAdmin para criação e login de administradores.

---

## 📚 Aprendizado demonstrado
- Uso de classes, propriedades e métodos especiais
- Separação entre camada de modelo, persistência e interface
- Boas práticas mínimas: queries parametrizadas, commit/rollback, tratamento de exceções

---

## 🛠 Observações
- Projeto em desenvolvimento — PRs, issues e sugestões são bem-vindas


---

## 📝 Autor
Alunos: Francis Ricardo Silva, Helen da Cruz, Vanderléia Mello, Yan Mangabeira(repositório de estudo e prática)

---

## 📜 Licença
Adicionar LICENSE conforme necessário (recomendado: MIT para projetos de estudo)

