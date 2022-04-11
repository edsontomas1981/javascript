USE Escola;
/*Relatório 2-A Alunos e Cursos matriculados */
SELECT 
	a.cpf CPF,a.nome Nome,a.endereco Endereço,
	a.telefone Telefone,c.nome Curso,DATE_FORMAT(m.dt_matr_matricula,'%d/%m/%y') 'Data matricula' 
	FROM Alunos a 
	JOIN Matricula m ON (a.cpf = m.cpf_aluno_matricula )
	JOIN Cursos c ON (c.id  = m.id_curso_matricula);
/*Relatório 2-B Cursos e Disciplinas*/
SELECT 
	c.nome Curso,d.id 'ID Disciplina',d.nome Disciplina 
	FROM Cursos c 
	JOIN Compoe co ON (co.id_curso = c.id  )
	JOIN Disciplinas d ON (co.id_disciplina  = d.id);

/*Relatório 2-C Alunos e Disciplinas*/
SELECT 
	a.nome Aluno ,d.nome Disciplina  
	FROM Alunos a 
	JOIN Cursa c ON (c.cpf_aluno  = a.cpf  )
	JOIN Disciplinas d ON (d.id  = c.id_disciplina);

/*Relatório 2-D Professores e Disciplinas*/
SELECT 
	p.nome 'Professor(a)',d.nome Disciplina  
	FROM Professores p
	JOIN Disciplinas d ON (d.matricula_professor  = p.matricula_id);

/*Relatório 2-E Disciplinas e Pré Requisitos*/
SELECT 
	d.id 'ID Disciplina', d.nome Disciplina ,d.qtde_creditos Créditos, 
	(CASE WHEN pr.id_pre_requisito <> d.id then
	(SELECT nome FROM Disciplinas WHERE id = pr.id_pre_requisito) end) as 'Pré-Requisitos',
	(CASE WHEN p.matricula_id = d.matricula_professor  then
	(SELECT nome FROM Professores WHERE matricula_id = d.matricula_professor) end) as 'Professor(a)'	
	FROM Disciplinas d
	JOIN Pre_req pr ON (d.id = pr.id_disciplina_pr)
	JOIN Professores p ON (p.matricula_id = d.matricula_professor);

/*Relatório 2-F Média de idade por Cursos*/
SELECT 
	c.nome Curso ,AVG(DATEDIFF(CURRENT_DATE(),a.dt_nasc)/365) 'Média de idade (anos)'  
	FROM Alunos a 
	JOIN Matricula m ON (a.cpf = m.cpf_aluno_matricula )
	JOIN Cursos c ON (c.id  = m.id_curso_matricula) GROUP BY m.id_curso_matricula ; 

/*Relatório 2-G Cursos por departamentos*/
SELECT 
	d.nome Departamento,c.nome Curso  
	FROM Departamentos d 
	JOIN Cursos c ON (c.id_dpto = d.id);



	





	





	

