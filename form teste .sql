-------------------------------------------------------------------------
--Cria a tabela t_alunos
	if not exists(select * from INFORMATION_SCHEMA.tables where table_name = 'cadastro') 
	begin
	create table cadastro
	(
		id_alunos integer identity(1,1) constraint PK_cadastro primary key,
		name varchar(255) not null,
		data_de_nascimento varchar(10) not null,
		idade int null,
		inserir_genero int,
		email varchar(40),
		objetivo_da_graduacao varchar(100) null
	)
	end
	go
--- drop table t_alunos
-------------------------------------------------------------------------

select * from cadastro


drop table cadastro