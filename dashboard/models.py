from django.db import models

class Aluno(models.Model):

    nro_usp = models.CharField(primary_key=True, max_length=10)
    nome = models.CharField(max_length=80)
    ano_ingresso = models.IntegerField()

    def __str__(self) -> str:
        return self.nro_usp

class Disciplina(models.Model):

    codigo = models.CharField(primary_key=True, max_length=7)
    nome = models.CharField(max_length=50, default="")
    semestre_ideal = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.codigo

class Demanda_por_disciplina(models.Model):

    disciplina = models.ForeignKey(Disciplina, on_delete=models.DO_NOTHING)
    aluno = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING)
    cursando = models.BooleanField(default=False)
    atrasado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.disciplina}/{self.aluno}"