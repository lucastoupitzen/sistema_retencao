from django.contrib import admin
from .models import Aluno, Disciplina, Demanda_por_disciplina

admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Demanda_por_disciplina)
