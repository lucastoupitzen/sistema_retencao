from django.db import models

class Student(models.Model):

    nro_usp = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=80)
    start_year = models.IntegerField()

    def __str__(self) -> str:
        return self.nro_usp

class Discipline(models.Model):

    code = models.CharField(primary_key=True, max_length=7)
    name = models.CharField(max_length=50, default="")
    ideal_semester = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.code

class DisciplineDemand(models.Model):

    discipline = models.ForeignKey(Discipline, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    currently_studying = models.BooleanField(default=False)
    late = models.BooleanField(default=False)
    year = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.discipline}/{self.student}/{self.year}"