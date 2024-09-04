from django.db import models

class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_descricao = models.CharField(max_length=50)

class Professor(models.Model):
    prof_id = models.AutoField(primary_key=True)
    prof_nome = models.CharField(max_length=50)
    prof_telefone = models.CharField(max_length=50)
    prof_email = models.CharField(max_length=100)
    prof_nascimento = models.DateField()
    prof_cep = models.CharField(max_length=15)
    prof_endereco = models.CharField(max_length=255)
    prof_bairro = models.CharField(max_length=150)
    prof_cidade = models.CharField(max_length=150)
    prof_estado = models.CharField(max_length=50)
    prof_status = models.ForeignKey(Status, on_delete=models.RESTRICT)

class Turma(models.Model):
    turma_id = models.AutoField(primary_key=True)
    turma_descricao = models.CharField(max_length=50)
    turma_idade_limite = models.BigIntegerField()
    turma_status = models.ForeignKey(Status, on_delete=models.RESTRICT)

class ProfessorTurma(models.Model):
    prof_turma_id = models.AutoField(primary_key=True)
    prof_turma_professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    prof_turma_turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

class Aluno(models.Model):
    aluno_id = models.AutoField(primary_key=True)
    aluno_status = models.ForeignKey(Status, on_delete=models.RESTRICT)
    aluno_turma = models.ForeignKey(Turma, on_delete=models.RESTRICT)
    aluno_nome = models.CharField(max_length=255)
    aluno_nascimento = models.DateField()
    aluno_nome_mae = models.CharField(max_length=255)
    aluno_nascimento_mae = models.DateField()
    aluno_nome_pai = models.CharField(max_length=255)
    aluno_nascimento_pai = models.DateField()
    aluno_cep = models.CharField(max_length=15)
    aluno_endereco = models.CharField(max_length=255)
    aluno_bairro = models.CharField(max_length=150)
    aluno_cidade = models.CharField(max_length=150)
    aluno_estado = models.CharField(max_length=50)
    aluno_telefone = models.CharField(max_length=100)
    aluno_email = models.CharField(max_length=150)

class Aula(models.Model):
    aula_id = models.AutoField(primary_key=True)
    aula_descricao = models.CharField(max_length=50)
    aula_data = models.DateField()
    aula_turma = models.ForeignKey(Turma, on_delete=models.RESTRICT)

class PresencaAula(models.Model):
    pres_id = models.AutoField(primary_key=True)
    pres_aula = models.ForeignKey(Aula, on_delete=models.RESTRICT)
    pres_aluno = models.ForeignKey(Aluno, on_delete=models.RESTRICT)

#No banco de dados, exclua uma linha 'profiles'da tabela 'django_migrations'

#Exemplo de relations
#https://docs.djangoproject.com/en/5.1/ref/models/fields/#django.db.models.RESTRICT
#class Artist(models.Model):
#    name = models.CharField(max_length=10)

#class Album(models.Model):
#    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

#class Song(models.Model):
#    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
#    album = models.ForeignKey(Album, on_delete=models.RESTRICT)