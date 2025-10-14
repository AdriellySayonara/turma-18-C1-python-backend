"""

Exercício 1: Criando o Catálogo (CREATE TABLE)
Tarefa: Escreva o comando SQL para criar uma tabela chamada Livros. 
Ela deve ter as seguintes colunas:

livro_id: Um número inteiro que será a chave primária.

titulo: O título do livro (texto), que não pode ser nulo.

autor: O nome do autor (texto), que também não pode ser nulo.

ano_publicacao: O ano de publicação do livro (número inteiro).

genero: O gênero do livro (texto).

Exercício 2: Adicionando Livros ao Catálogo (INSERT INTO)
Tarefa: A biblioteca acabou de receber novos livros. Escreva os comandos INSERT INTO para adicionar os 4 livros a seguir à sua tabela Livros.

('1984', 'George Orwell', 1948, 'Ficção Distópica')

('O Guia do Mochileiro das Galáxias', 'Douglas Adams', 1979, 'Ficção Científica')

('Cem Anos de Solidão', 'Gabriel García Márquez', 1967, 'Realismo Mágico')

('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 1997, 'Fantasia')

Exercício 3: Encontrando Livros (SELECT e WHERE)
Tarefa: Agora, escreva as consultas SELECT para encontrar as seguintes informações no catálogo:

a) Liste o título e o autor de todos os livros na tabela.
b) Encontre todos os dados do livro cujo autor é 'George Orwell'.
c) Liste todos os livros que foram publicados antes do ano 2000.

Exercício 4: Organizando a Estante (ORDER BY e LIMIT)
Tarefa: Para organizar a visualização do catálogo, escreva as seguintes consultas:

a) Liste todos os livros em ordem alfabética pelo título.
b) Encontre os 2 livros mais antigos da biblioteca (com base no ano de publicação).

Exercício 5: Corrigindo e Removendo Livros (UPDATE e DELETE)
Tarefa: Um erro foi encontrado no catálogo e um livro foi doado.

a) O ano de publicação do livro '1984' foi catalogado incorretamente. Atualize o registro para corrigir o ano para 1949.
b) O livro 'O Guia do Mochileiro das Galáxias' foi doado e precisa ser removido. Delete este livro da tabela."""