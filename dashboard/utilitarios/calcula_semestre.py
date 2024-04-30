import datetime

def semestre(ano_aluno):

    ano_atual = datetime.datetime.now().year
    ano_curso =  ano_atual - ano_aluno + 1
    if datetime.datetime.now().month <= 6: semestre_aluno = ano_curso + (ano_atual - ano_aluno)
    else: semestre_aluno  = ano_curso + (ano_atual - ano_aluno) + 1
    return semestre_aluno
