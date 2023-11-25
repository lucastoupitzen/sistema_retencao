from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .utilitarios.Planilha import Planilha
from .utilitarios.Upload_DB import Upload
from .utilitarios.calcula_semestre import semestre
import os
from .models import Aluno, Disciplina, Demanda_por_disciplina
from .Rotinas.Rotinas import Rotinas
from tqdm import tqdm
import json
from .utilitarios.Gera_pdf import Gera_pdf
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def home(request):
    #upload_planilha(request)
    return render(request, 'home.html')

def firststeps(request):
    #upload_planilha(request)
    return render(request, 'firststeps.html')

def carregar_planilha(request): 
    return render(request, 'carregarplanilha.html') 

def retorna_info_materia(request):
    

    codigo = request.GET.get("codigo")
    if not codigo: codigo = "ACH2053"
    print(codigo)
    rotina = Rotinas()
    return JsonResponse(rotina.informações_disciplina(codigo))
    # print(rotina.informações_disciplina("ACH2033"))
    # print(rotina.listar_disciplinas_atrasados())
    #print(rotina.listar_alunos_atrasados())
    
    
def lista_materias_atrasados_impar(request):
    rotina = Rotinas()
    return JsonResponse(rotina.listar_disciplinas_atrasados_semestre_impar())


def lista_materias_atrasados_par(request):
    rotina = Rotinas()
    return JsonResponse(rotina.listar_disciplinas_atrasados_semestre_par())

def upload_planilha(request):

    Demanda_por_disciplina.objects.all().delete()
    Aluno.objects.all().delete()
    arquivo = os.path.abspath("dashboard/arquivo.xls")
    print(arquivo)
    planilha = Planilha(arquivo)
    lista_de_materias = Disciplina.objects.all()
    for materia in lista_de_materias:
        db = planilha.get_arquivo_materia(materia.codigo)
        print("Carregando a materia " + materia.codigo)
        for indice, linha in tqdm(db.iloc[1:].iterrows(), total=len(db) - 1, unit='linha'):
            Upload.upload_Alunos(linha["Número USP"], linha["Nome do Aluno"], linha["Data de ingresso"])
            Upload.upload_Demanda(materia.codigo, linha["Número USP"], linha["Cursando?"])
        print(materia.codigo + " carregada com sucesso!")
       



def generate_pdf(request):
    
    semestre = request.GET.get("semestre")
    print(semestre)
    rotina = Rotinas()
    if semestre == "Ímpar":
        data = rotina.listar_disciplinas_atrasados_semestre_impar()
    else: data = rotina.listar_disciplinas_atrasados_semestre_par()
    
    gerador_pdf = Gera_pdf(data, f"Alunos atrasados por disciplina - Semestre {semestre}")
    gerador_pdf.gera_pdf()
    
    with open("relatorio.pdf", "rb") as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type="application/pdf")

    # Define o nome do arquivo para download
    response['Content-Disposition'] = 'attachment; filename=relatorio.pdf'

    return response

def listar_alunos_atrasados(request):
    rotina = Rotinas()
    return JsonResponse(rotina.listar_alunos_atrasados())
