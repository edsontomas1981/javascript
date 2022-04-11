CREATE DATABASE Escola;

USE Escola;

CREATE TABLE Alunos  (
  cpf varchar(11) NOT NULL,
  nome varchar(50) NOT NULL,
  endereco varchar(50) NOT NULL,
  telefone varchar(50) NOT NULL,
  dt_nasc varchar(11) NOT NULL,
  PRIMARY KEY (cpf)
);

CREATE TABLE Compoe  (
  id_curso int NOT NULL,
  id_disciplina int NOT NULL
);

CREATE TABLE Cursa  (
  cpf_aluno varchar(11) NOT NULL,
  id_disciplina int NULL
);

CREATE TABLE Cursos  (
  id int NOT NULL AUTO_INCREMENT,
  nome varchar(50) NOT NULL,
  descricao varchar(50) NOT NULL,
  id_dpto int NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE Departamentos  (
  id int NOT NULL AUTO_INCREMENT,
  nome varchar(50) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE Disciplinas  (
  id int NOT NULL AUTO_INCREMENT,
  nome varchar (50) NOT NULL,
  qtde_creditos int NOT NULL,
  matricula_professor int NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE Matricula  (
  id_curso_matricula int NOT NULL,
  cpf_aluno_matricula varchar(11)NOT NULL,
  dt_matr_matricula date NOT NULL
);

CREATE TABLE Pre_req  (
  id_disciplina_pr int NOT NULL,
  id_pre_requisito int NOT NULL
);

CREATE TABLE Professores  (
  matricula_id int NOT NULL AUTO_INCREMENT,
  nome varchar(50) NOT NULL,
  endereco varchar(50) NOT NULL,
  telefone varchar(11) NOT NULL,
  dt_nasc date NOT NULL,
  id_depto_prof int NOT NULL,
  dt_contratacao date NOT NULL,
  PRIMARY KEY (matricula_id)
);

ALTER TABLE Compoe ADD CONSTRAINT id_curso FOREIGN KEY (id_curso) REFERENCES Cursos (id);
ALTER TABLE Compoe ADD CONSTRAINT id_discipĺina FOREIGN KEY (id_disciplina) REFERENCES Disciplinas (id);
ALTER TABLE Cursa ADD CONSTRAINT cpf_aluno FOREIGN KEY (cpf_aluno) REFERENCES Alunos (cpf);
ALTER TABLE Cursa ADD CONSTRAINT id_disciplina FOREIGN KEY (id_disciplina) REFERENCES Disciplinas (id);
ALTER TABLE Cursos ADD CONSTRAINT id_depto FOREIGN KEY (id_dpto) REFERENCES Departamentos (id);
ALTER TABLE Matricula ADD CONSTRAINT id_curso_matricula FOREIGN KEY (id_curso_matricula) REFERENCES Cursos (id);
ALTER TABLE Matricula ADD CONSTRAINT cpf_aluno_matricula FOREIGN KEY (cpf_aluno_matricula) REFERENCES Alunos (cpf);
ALTER TABLE Pre_req ADD CONSTRAINT id_disciplina_pr FOREIGN KEY (id_disciplina_pr) REFERENCES Disciplinas (id);
ALTER TABLE Pre_req ADD CONSTRAINT id_pre_requisito FOREIGN KEY (id_pre_requisito) REFERENCES Disciplinas (id);
ALTER TABLE Professores ADD CONSTRAINT id_depto_prof FOREIGN KEY (id_depto_prof) REFERENCES Departamentos (id);
ALTER TABLE Disciplinas  ADD CONSTRAINT matricula_professor  FOREIGN KEY (matricula_professor) REFERENCES Professores (matricula_id);


INSERT INTO Departamentos (nome) VALUES 
	('Data'), -- 1
	('Web'), -- 2
	('Gestão'); -- 3

INSERT INTO Professores (nome,endereco,telefone,dt_nasc,id_depto_prof,dt_contratacao) VALUES 
	('Matheus','Rua lets , 1','11111111111','1980-01-01',1,'2022-01-01'),
	('Rafael','Rua lets , 2','22222222222','1980-01-02',2,'2022-01-02'),
	('Brian','Rua lets , 3','33333333333','1980-01-03',3,'2022-01-03'),
	('Fernando','Rua lets , 4','44444444444','1980-01-04',1,'2022-01-04'),
	('Paulo','Rua lets , 5','55555555555','1980-01-05',2,'2022-01-05'),
	('Rodrigo','Rua lets , 6','66666666666','1980-01-06',3,'2022-01-06');

INSERT INTO Alunos (cpf,nome,endereco,telefone,dt_nasc) VALUES
	('30784315831','Edson Tomas','Rua 1','11111111111','1980-01-01'),
	('30784315832','Ana Tomas','Rua 2','22222222222','1980-01-02'),
	('30784315833','Sandra Tomas','Rua 3','33333333333','1980-01-03'),
	('30784315834','Gabriel Tomas','Rua 4','44444444444','1980-01-04'),
	('30784315835','Uriel Tomas','Rua 5','55555555555','1980-01-02'), 
	('30784315836','Rosaura Tomas','Rua 6','66666666666','1980-01-02');

INSERT INTO Cursos (nome,descricao,id_dpto) VALUES 
	('Ciência de dados','Análise, estatística, modelagem',1),
	('Front-end','HTML, CSS e JavaScript',2),
	('Inovação & Gestão','Gestão de produtos e projetos',3);

INSERT INTO Matricula (id_curso_matricula,cpf_aluno_matricula,dt_matr_matricula) VALUES 
	(1,'30784315831','2022-01-10'),
	(1,'30784315832','2022-01-10'),
	(2,'30784315833','2022-01-10'),
	(2,'30784315834','2022-01-10'),
	(3,'30784315835','2022-01-10'),
	(3,'30784315836','2022-01-10');

INSERT INTO Disciplinas (qtde_creditos,matricula_professor,nome) VALUES
	(50,1,'Logica de Programação'), 
	(50,1,'Algoritimos'),
	(50,1,'Python'),
	(50,4,'Banco de Dados'),
	(50,4,'Modelagem de Dados'),
	(50,4,'SQL'),
	(50,2,'Html & CSS'),
	(50,2,'Arquitetura CSS'),
	(50,2,'Acessibilidade Web'),
	(50,5,'Javascript'), 
	(50,5,'Javascript na web'),
	(50,5,'Git & Github'),
	(50,3,'Foco:trazendo mais resultados'),
	(50,3,'Produtividade 1 :estratégias para o dia a dia.'),
	(50,3,'Produtividade 2 :Organização e prioridade'),
	(50,6,'Lean Startup:Primeiros passos'),
	(50,6,'Empreendedorismo'),
	(50,6,'Ciclo de vida do produto');

INSERT INTO Compoe (id_curso,id_disciplina) VALUES 
	(1,1),
	(1,2),
	(1,3),
	(1,4),
	(1,5),
	(1,6),
	(2,7),
	(2,8),
	(2,9),
	(2,10),
	(2,11),
	(2,12),	
	(3,13),
	(3,14),
	(3,15),
	(3,16),
	(3,17),
	(3,18);
INSERT INTO Cursa (cpf_aluno,id_disciplina) VALUES 
	('30784315831',1),
	('30784315832',1),
	('30784315831',4),
	('30784315832',4),
	('30784315833',7),
	('30784315834',7),
	('30784315833',10),
	('30784315834',10),
	('30784315835',13),
	('30784315836',13),
	('30784315835',16),
	('30784315836',16);

INSERT INTO Pre_req(id_disciplina_pr,id_pre_requisito) VALUES 
	(1,1),
	(2,1),
	(3,2),
	(4,4),
	(5,4),
	(6,5),
	(7,7),
	(8,7),
	(9,8),
	(10,10),
	(11,10),
	(12,11),
	(13,13),
	(14,13),
	(15,14),
	(17,17),
	(17,16),
	(18,17);
