from django.shortcuts import render
from .models import Aluno ,Status ,Turma ,Professor ,ProfessorTurma ,Aula ,PresencaAula

#Utilizacao de query usando Exists
from django.db.models import Exists

#imports para exigir de autenticacao login onde estiver o decorator @login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

########################### STATUS ###########################
@login_required
def homeStatus(request):
    #Exibir status cadastrados
    statuss ={
        'statuss': Status.objects.all()
    }
    #retornar os dados para a pagina
    return render(request,'status/index.html',statuss)

@login_required
def inserirStatus(request):
    #retornar os dados para a pagina
    return render(request,'status/inserir.html')

@login_required
def retornarStatusRequest(request):
    statusid = request.POST.get('status_id')
    
    if statusid != None:
        objeto = Status.objects.get(status_id=statusid)
    else:    
        objeto = Status()

    objeto.status_descricao = request.POST.get('status_descricao')

    return objeto

@login_required
def cadastrarStatus(request):
    try:
        data = {}
        objeto = retornarStatusRequest(request)
        objeto.save()

        statuss = Status.objects.all()
        #print(statuss)
        data['msg'] = 'Cadastro realizado com sucesso !'
        data['class'] = 'alert-success'
        context = {'statuss': statuss, 'data': data}

        #retornar os dados para a pagina
        return render(request,'status/index.html',context)
    except:
        statuss = Status.objects.all()
        data['msg'] = 'Erro ao realizar operação !'
        data['class'] = 'alert-danger'
        context = {'statuss': statuss, 'data': data}
        #retornar os dados para a pagina
        return render(request,'status/inserir.html',context)

@login_required
def selecionarStatus(request):
    statusid = request.POST.get('status_id')
    #Criando dict para retorno das informacoes ao form
    status ={
        'status': Status.objects.get(status_id=statusid)
    }
    return render(request,'status/alterar.html',status)

@login_required
def alterarStatus(request):
    statusid = request.POST.get('status_id')
    objeto = Status.objects.get(status_id=statusid)
    objeto.status_descricao = request.POST.get('status_descricao')
    objeto.save()

    data = {}
    statuss = Status.objects.all()
    data['msg'] = 'Alteração realizada com sucesso !'
    data['class'] = 'alert-success'
    context = {'statuss': statuss, 'data': data}
    return render(request,'status/index.html',context)

def deletarStatus(request):
    statusid = request.POST.get('status_id')
    objeto = Status.objects.get(status_id=statusid)
    objeto.delete()
    
    data = {}
    statuss = Status.objects.all()
    data['msg'] = 'Exclusão realizada com sucesso !'
    data['class'] = 'alert-success'
    context = {'statuss': statuss, 'data': data}
    return render(request,'status/index.html',context)    

########################### PROFESSOR ###########################
@login_required
def homeProfessor(request):
    #Exibir professores cadastrados
    professores ={
        'professores': Professor.objects.all()
    }
    #retornar os dados para a pagina
    return render(request,'professor/index.html',professores)

@login_required
def retornarProfessorRequest(request):
    profid = request.POST.get('prof_id')
    #print('Professor id')   
    #print(profid)   

    if profid != None:
        objeto = Professor.objects.get(prof_id=profid)
        prof_status_id = objeto.prof_status_id
    else:    
        objeto = Professor()
        prof_status_id = request.POST.get('prof_status_id')

    objeto.prof_nome = request.POST.get('prof_nome')
    objeto.prof_telefone = request.POST.get('prof_telefone')
    objeto.prof_nascimento = request.POST.get('prof_nascimento')
    objeto.prof_cep = request.POST.get('prof_cep')
    objeto.prof_endereco = request.POST.get('prof_endereco')
    objeto.prof_bairro = request.POST.get('prof_bairro')
    objeto.prof_cidade = request.POST.get('prof_cidade')
    objeto.prof_estado = request.POST.get('prof_estado')
    objeto.prof_email = request.POST.get('prof_email')
    objeto.prof_telefone = request.POST.get('prof_telefone')

    objeto.prof_status = Status.objects.get(status_id=prof_status_id)

    return objeto

@login_required
def inserirProfessor(request):
    statuss = {
        'statuss' : Status.objects.all()
    }
    #retornar os dados para a pagina
    return render(request,'professor/inserir.html',statuss)

@login_required
def cadastrarProfessor(request):
    #try:
    data = {}
    professor = retornarProfessorRequest(request)
    professor.save()

    professores = Professor.objects.all()
    data['msg'] = 'Cadastro realizado com sucesso !'
    data['class'] = 'alert-success'
    context = {'professores': professores, 'data': data}

    #retornar os dados para a pagina
    return render(request,'professor/index.html',context)

@login_required
def selecionarProfessor(request):
    profid = request.POST.get('prof_id')

    professor = Professor.objects.get(prof_id=profid)
    statuss = Status.objects.all()
    professorturmas = ProfessorTurma.objects.filter(prof_turma_professor_id=profid)
    
    #turmas = Turma.objects.all()
    #NAO trazer para selecao turmas em que o professor ja esta cadastrado 
    turmas = Turma.objects.all()

    #Criando dict para retorno das informacoes ao form
    context = {'professor': professor, 'statuss': statuss ,'professorturmas':professorturmas ,'turmas':turmas}
    return render(request,'professor/alterar.html',context)

@login_required
def deletarProfessor(request):
    profid = request.POST.get('prof_id')
    professor = Professor.objects.get(prof_id=profid)
    professor.delete()

    data = {}
    professores = Professor.objects.all()
    data['msg'] = 'Exclusão realizada com sucesso !'
    data['class'] = 'alert-success'
    context = {'professores': professores, 'data': data}
    return render(request,'professor/index.html',context)

@login_required
def alterarProfessor(request):
    professor = retornarProfessorRequest(request)
    professor.save()

    data = {}
    professores = Professor.objects.all()
    data['msg'] = 'Alteração realizada com sucesso !'
    data['class'] = 'alert-success'
    context = {'professores': professores, 'data': data}
    return render(request,'professor/index.html',context)

########################### PROFESSOR TURMA ###########################

@login_required
def retornaProfessorTurma(request):
    professorturmalocalizado = ProfessorTurma.objects.filter(prof_turma_professor_id=request.POST.get('prof_id') ,prof_turma_turma_id=request.POST.get('turma_id'))
    print(professorturmalocalizado)
    return professorturmalocalizado

@login_required
def inserirProfessorTurma(request): 
    
    prof_turma_professor = retornarProfessorRequest(request)
    prof_turma_turma = retornarTurmaRequest(request)

    professorTurmaJaExistente = retornaProfessorTurma(request)

    #print('professorTurmaJaExistente')
    #print(professorTurmaJaExistente)

    if len(professorTurmaJaExistente) == 0:
        professorturma = ProfessorTurma()
        professorturma.prof_turma_professor = prof_turma_professor
        professorturma.prof_turma_turma = prof_turma_turma
        professorturma.save()

    professorturmas = ProfessorTurma.objects.filter(prof_turma_professor_id=prof_turma_professor.prof_id)
    
    statuss = Status.objects.all()
    turmas = Turma.objects.all()


    professor = Professor.objects.get(prof_id=prof_turma_professor.prof_id)

    data = {}
    data['msg'] = 'Operação realizada com sucesso !'
    data['class'] = 'alert-success'

    #Criando dict para retorno das informacoes ao form
    context = {'professor': professor, 'statuss': statuss ,'professorturmas':professorturmas ,'turmas':turmas,'data':data}
    return render(request,'professor/alterar.html',context)

def deletarProfessorTurma(request):
    profturma_id = request.POST.get('prof_turma_id')
    professorturma = ProfessorTurma.objects.get(prof_turma_id=profturma_id)
    professorturma.delete()

    professor = Professor.objects.get(prof_id=request.POST.get('prof_id'))
    professorturmas = ProfessorTurma.objects.filter(prof_turma_professor_id=professor.prof_id)
    statuss = Status.objects.all()
    turmas = Turma.objects.all()
    data = {}
    data['msg'] = 'Exclusão realizada com sucesso !'
    data['class'] = 'alert-success'

    context = {'professor': professor, 'statuss': statuss ,'professorturmas':professorturmas ,'turmas':turmas, 'data':data}
    return render(request,'professor/alterar.html',context)


########################### PRESENCA AULA ###########################

@login_required
def retornaPresencaAula(request):
    presencaaula = PresencaAula.objects.filter(pres_aluno_id=request.POST.get('aluno_id') ,pres_aula_id=request.POST.get('aula_id'))
    #print(presencaaula)
    return presencaaula

@login_required
def retornaPresencasDaAula(request):
    presencaaula = PresencaAula.objects.filter(pres_aula_id=request.POST.get('aula_id'))
    #print(presencaaula)
    return presencaaula


@login_required
def inserirPresencaAula(request): 
    print('inserirPresencaAula')
    
    pres_aula = Aula.objects.get(aula_id=request.POST.get('aula_id'))
    #print('criou pres_aula')
    pres_aluno = Aluno.objects.get(aluno_id=request.POST.get('aluno_id'))
    #print('criou pres_aluno')

    presencaJaExistente = retornaPresencaAula(request)

    #print('professorTurmaJaExistente')
    #print(professorTurmaJaExistente)

    if len(presencaJaExistente) == 0:
        presencaAula = PresencaAula()
        presencaAula.pres_aula = pres_aula
        presencaAula.pres_aluno = pres_aluno
        presencaAula.save()
    
    turmas = Turma.objects.all()
    alunosDaTurma = Aluno.objects.filter(aluno_turma_id=pres_aluno.aluno_turma_id)
    presencasDaAula  = retornaPresencasDaAula(request)

    professorturmas = ProfessorTurma.objects.filter(prof_turma_turma_id=pres_aluno.aluno_turma_id)
    #professorturmas = ProfessorTurma.objects.filter(prof_turma_professor_id=1)

    #print('professorturmas:')
    #print(professorturmas)

    data = {}
    data['msg'] = 'Operação realizada com sucesso !'
    data['class'] = 'alert-success'

    #Criando dict para retorno das informacoes ao form
    context = {'aula': pres_aula, 'turmas': turmas ,'presencasDaAula':presencasDaAula ,'alunosDaTurma':alunosDaTurma ,'professorturmas':professorturmas}
    return render(request,'aula/registrarPresenca.html',context)

def deletarPresencaAula(request):
    presid = request.POST.get('pres_id')
    presencaaula = PresencaAula.objects.get(pres_id=presid)
    presencaaula.delete()

    aula = Aula.objects.get(aula_id=request.POST.get('aula_id'))

    presencasaulas = PresencaAula.objects.filter(pres_aula_id=aula.aula_id)
    turmas = Turma.objects.all()
    data = {}
    data['msg'] = 'Exclusão realizada com sucesso !'
    data['class'] = 'alert-success'

    context = {'aula': aula, 'presencasaulas':presencasaulas ,'turmas':turmas, 'data':data}
    return render(request,'professor/alterar.html',context)

########################### AULA ###########################
@login_required
def homeAula(request):
    #Exibir aulas cadastradas
    aulas ={
        'aulas': Aula.objects.all()
    }
    #retornar os dados para a pagina
    return render(request,'aula/index.html',aulas)

@login_required
def inserirAula(request):
    
    #Exibir status cadastrados
    turmas ={
        'turmas': Turma.objects.all()
    }

    #retornar os dados para a pagina
    return render(request,'aula/inserir.html',turmas)

@login_required
def retornarAulaRequest(request):
    aulaid = request.POST.get('aula_id')
    
    if aulaid != None:
        objeto = Aula.objects.get(aula_id=aulaid)
    else:    
        objeto = Aula()

    objeto.aula_descricao = request.POST.get('aula_descricao')
    objeto.aula_data = request.POST.get('aula_data')
    objeto.aula_turma = Turma.objects.get(turma_id=request.POST.get('aula_turma_id'))

    #print('criado objeto aula com sucesso')

    return objeto

@login_required
def cadastrarAula(request):
    data = {}
    objeto = retornarAulaRequest(request)
    objeto.save()

    aulas = Aula.objects.all()
    #print(statuss)
    data['msg'] = 'Cadastro realizado com sucesso !'
    data['class'] = 'alert-success'
    context = {'aulas': aulas, 'data': data}

    #retornar os dados para a pagina
    #return render(request,'alunos/index.html',status)
    return render(request,'aula/index.html',context)

@login_required
def selecionarAula(request):
    aulaid = request.POST.get('aula_id')
    aula = Aula.objects.get(aula_id=aulaid)
    turmas = Turma.objects.all()

    presencasDaAula  = retornaPresencasDaAula(request)

    #Criando dict para retorno das informacoes ao form
    context = {'aula': aula, 'turmas': turmas ,'presencasDaAula':presencasDaAula}
    return render(request,'aula/alterar.html',context)

def registroPresenca(request):
    aulaid = request.POST.get('aula_id')
    aula = Aula.objects.get(aula_id=aulaid)
    turmas = Turma.objects.all()
    alunosDaTurma = Aluno.objects.filter(aluno_turma_id=aula.aula_turma.turma_id)
    presencasDaAula  = retornaPresencasDaAula(request)

    professorturmas = ProfessorTurma.objects.filter(prof_turma_turma_id=aula.aula_turma.turma_id)
    #professorturmas = ProfessorTurma.objects.filter(prof_turma_professor_id=1)

    #Criando dict para retorno das informacoes ao form
    context = {'aula': aula, 'turmas': turmas ,'presencasDaAula':presencasDaAula ,'alunosDaTurma':alunosDaTurma ,'professorturmas':professorturmas}
    return render(request,'aula/registrarPresenca.html',context)

@login_required
def alterarAula(request):
    #Se quer alterar turma tem que ter passado turma_id
    objeto = retornarAulaRequest(request)
    objeto.save()

    data = {}
    aulas = Aula.objects.all()
    data['msg'] = 'Alteração realizada com sucesso !'
    data['class'] = 'alert-success'
    context = {'aulas': aulas, 'data': data}
    return render(request,'aula/index.html',context)

@login_required
def deletarAula(request):
    aulaid = request.POST.get('aula_id')
    aula = Aula.objects.get(aula_id=aulaid)
    aula.delete()

    data = {}
    aulas = Aula.objects.all()
    data['msg'] = 'Exclusão realizada com sucesso !'
    data['class'] = 'alert-success'
    context = {'aulas': aulas, 'data': data}
    return render(request,'aula/index.html',context)

########################### TURMA ###########################
@login_required
def homeTurma(request):
    #Exibir turmas cadastradas
    turmas ={
        'turmas': Turma.objects.all()
    }
    #retornar os dados para a pagina
    return render(request,'turma/index.html',turmas)

@login_required
def inserirTurma(request):
    
    #Exibir status cadastrados
    statuss ={
        'statuss': Status.objects.all()
    }

    #retornar os dados para a pagina
    return render(request,'turma/inserir.html',statuss)

@login_required
def retornarTurmaRequest(request):
    turmaid = request.POST.get('turma_id')
    #print('Aqui turma_status_id:')
    #print(turma_status_id)
    
    if turmaid != None:
        objeto = Turma.objects.get(turma_id=turmaid)
        turma_status_id = objeto.turma_status_id
    else:    
        objeto = Turma()
        turma_status_id = request.POST.get('turma_status_id')

    #print('criado objeto turma')

    objeto.turma_descricao = request.POST.get('turma_descricao')
    objeto.turma_idade_limite = request.POST.get('turma_idade_limite')

    objeto.turma_status = Status.objects.get(status_id=turma_status_id)
    #print('criado objeto status da turma')

    return objeto

@login_required
def cadastrarTurma(request):
#try:
    data = {}
    objeto = retornarTurmaRequest(request)
    objeto.save()

    turmas = Turma.objects.all()
    #print(statuss)
    data['msg'] = 'Cadastro realizado com sucesso !'
    data['class'] = 'alert-success'
    context = {'turmas': turmas, 'data': data}

    #retornar os dados para a pagina
    #return render(request,'alunos/index.html',status)
    return render(request,'turma/index.html',context)
#except:
    turmas = Turma.objects.all()
    data['msg'] = 'Erro ao realizar operação !'
    data['class'] = 'alert-danger'
    context = {'turmas': turmas, 'data': data}
    #retornar os dados para a pagina
    return render(request,'turma/inserir.html',context)

@login_required
def selecionarTurma(request):
    turmaid = request.POST.get('turma_id')
    turma = Turma.objects.get(turma_id=turmaid)

    statuss = Status.objects.all()

    #Criando dict para retorno das informacoes ao form
    context = {'turma': turma, 'statuss': statuss}
    return render(request,'turma/alterar.html',context)

@login_required
def alterarTurma(request):
    #Se quer alterar turma tem que ter passado turma_id
    objeto = retornarTurmaRequest(request)
    objeto.save()

    data = {}
    turmas = Turma.objects.all()
    data['msg'] = 'Alteração realizada com sucesso !'
    data['class'] = 'alert-success'
    context = {'turmas': turmas, 'data': data}
    return render(request,'turma/index.html',context)

@login_required
def deletarTurma(request):
    turmaid = request.POST.get('turma_id')
    turma = Turma.objects.get(turma_id=turmaid)
    turma.delete()

    data = {}
    turmas = Turma.objects.all()
    data['msg'] = 'Exclusão realizada com sucesso !'
    data['class'] = 'alert-success'
    context = {'turmas': turmas, 'data': data}
    return render(request,'professor/index.html',context)

########################### ALUNOS ###########################

#Pagina de cadastro de alunos
@login_required
def home(request):
    #retornar os dados para a pagina
    return render(request,'components/modeloPrincipal.html')

@login_required
def homeAlunos(request):
    #Exibir alunos cadastrados
    alunos ={
        'alunos': Aluno.objects.all()
    }
    #retornar os dados para a pagina
    return render(request,'alunos/index.html',alunos)

@login_required
def registropresenca(request):
    #Exibir alunos cadastrados
    alunos ={
        'alunos': Aluno.objects.all()
    }
    #retornar os dados para a pagina
    return render(request,'alunos/presenca.html',alunos)


@login_required
def inserirAluno(request):
    statuss = Status.objects.all()
    turmas = Turma.objects.all()

    #Criando dict para retorno das informacoes ao form
    context = {'statuss': statuss, 'turmas':turmas}
    #retornar os dados para a pagina
    return render(request,'alunos/inserir.html',context)

@login_required
def listarAlunos(request):
    #Exibir alunos cadastrados
    alunos ={
        'alunos': Aluno.objects.all()
    }
    #retornar os dados para a pagina
    return render(request,'alunos/listaAlunos.html',alunos)

def retornarAlunoRequest(request):
    alunoid = request.POST.get('aluno_id')
    #print(alunoid)
    
    if alunoid != None:
        aluno = Aluno.objects.get(aluno_id=alunoid)
    else:    
        aluno = Aluno()

    aluno.aluno_nome = request.POST.get('aluno_nome')
    aluno.aluno_nascimento = request.POST.get('aluno_nascimento')
    aluno.aluno_nome_mae = request.POST.get('aluno_nome_mae')
    aluno.aluno_nascimento_mae = request.POST.get('aluno_nascimento_mae')
    aluno.aluno_nome_pai = request.POST.get('aluno_nome_pai')
    aluno.aluno_nascimento_pai = request.POST.get('aluno_nascimento_pai')
    aluno.aluno_cep = request.POST.get('aluno_cep')
    aluno.aluno_endereco = request.POST.get('aluno_endereco')
    aluno.aluno_bairro = request.POST.get('aluno_bairro')
    aluno.aluno_cidade = request.POST.get('aluno_cidade')
    aluno.aluno_estado = request.POST.get('aluno_estado')
    aluno.aluno_email = request.POST.get('aluno_email')
    aluno.aluno_telefone = request.POST.get('aluno_telefone')
    aluno.aluno_status = Status.objects.get(status_id=request.POST.get('aluno_status_id'))
    aluno.aluno_turma = Turma.objects.get(turma_id=request.POST.get('aluno_turma_id'))
    return aluno

#Criando novo aluno no BD
@login_required
def cadastrarAluno(request):
    #try:
    data = {}
    novo_aluno = retornarAlunoRequest(request)
    novo_aluno.save()

    #Exibir alunos cadastrados
    #alunos ={
    #    'alunos': Aluno.objects.all()
    #}

    alunos = Aluno.objects.all()
    data['msg'] = 'Cadastro realizado com sucesso !'
    data['class'] = 'alert-success'
    context = {'alunos': alunos, 'data': data}

    #retornar os dados para a pagina
    #return render(request,'alunos/index.html',alunos)
    return render(request,'alunos/index.html',context)
#except:
    alunos = Aluno.objects.all()
    data['msg'] = 'Erro ao realizar operação !'
    data['class'] = 'alert-danger'
    context = {'alunos': alunos, 'data': data}
    #retornar os dados para a pagina
    return render(request,'alunos/inserir.html',context)


def deletarAluno(request):
    aluno_id = request.POST.get('aluno_id')
    aluno = Aluno.objects.get(pk=aluno_id)
    aluno.delete()
    
    #Exibir alunos cadastrados
    #alunos ={'alunos': Aluno.objects.all()}
    #retornar os dados para a pagina
    #return render(request,'alunos/index.html',alunos)

    data = {}
    alunos = Aluno.objects.all()
    data['msg'] = 'Exclusão realizada com sucesso !'
    data['class'] = 'alert-success'
    context = {'alunos': alunos, 'data': data}
    return render(request,'alunos/index.html',context)

@login_required
def selecionarAluno(request):
    alunoid = request.POST.get('aluno_id')
    aluno = Aluno.objects.get(aluno_id=alunoid)
    statuss = Status.objects.all()
    turmas = Turma.objects.all()

    #Criando dict para retorno das informacoes ao form
    context = {'aluno': aluno, 'statuss': statuss, 'turmas':turmas}

    #aluno ={'aluno': Aluno.objects.get(aluno_id=alunoid)}
    return render(request,'alunos/alterar.html',context)

@login_required
def alterarAluno(request):
    aluno = retornarAlunoRequest(request)
    aluno.save()

    #Exibir alunos cadastrados
    #alunos ={'alunos': Aluno.objects.all()}
    #retornar os dados para a pagina
    #return render(request,'alunos/index.html',alunos)

    data = {}
    alunos = Aluno.objects.all()
    data['msg'] = 'Alteração realizada com sucesso !'
    data['class'] = 'alert-success'
    context = {'alunos': alunos, 'data': data}
    return render(request,'alunos/index.html',context)

########################### USUARIOS ###########################
@login_required
def homeUsuarios(request):
    #Exibir alunos cadastrados
    usuarios ={
        'usuarios': User.objects.all()
    }
    #retornar os dados para a pagina
    return render(request,'registration/index.html',usuarios)

def criarUsuario(request):
    return render(request, 'registration/inserir.html')

def cadastrarUsuario(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e Senha confirmada divergente !'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['password'])
        #user.first_name = request.POST['first_name'] #exemplo alimentando outros campos
        user.save()
        data['msg'] = 'Cadastro realizado com sucesso !'
        data['class'] = 'alert-success'
        
    return render(request, 'registration/inserir.html',data)

@login_required
def selecionarUsuario(request):
    user_id = request.POST.get('user_id')
    #Criando dict para retorno das informacoes ao form
    usuario ={
        'usuario': User.objects.get(id=user_id)
    }
    return render(request,'registration/alterar.html',usuario)
