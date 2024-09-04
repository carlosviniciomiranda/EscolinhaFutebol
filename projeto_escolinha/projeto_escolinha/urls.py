from django.urls import path
from app_escolinha import views

#imports para uso de login
from django.urls import path, include 

urlpatterns = [
    #rota, view responsavel, nome de referencia
    
    path('', views.home,name='home'),

    #Status
    path('status/', views.homeStatus,name='indexStatus'),
    path('status/inserir', views.inserirStatus,name='telaInserirStatus'),
    path('status/selecionarStatus', views.selecionarStatus,name='selecionarStatus'),
    path('status/cadastrarstatus', views.cadastrarStatus,name='cadastroDeStatus'),
    path('status/alterarstatus', views.alterarStatus,name='alteracaoDeStatus'),
    path('status/deletarstatus', views.deletarStatus,name='deletarStatus'),

    #Aula
    path('aula/', views.homeAula,name='indexAula'),
    path('aula/inserir', views.inserirAula,name='telaInserirAula'),
    path('aula/selecionarTurma', views.selecionarAula,name='selecionarAula'),
    path('aula/cadastrarTurma', views.cadastrarAula,name='cadastroDeAula'),
    path('aula/alterarTurma', views.alterarAula,name='alteracaoDeAula'),
    path('aula/deletarTurma', views.deletarAula,name='deletarAula'),
    path('aula/registroPresenca', views.registroPresenca,name='registroPresenca'),

    #PresencaAula
    path('aula/inserirPresencaAula', views.inserirPresencaAula,name='inserirPresencaAula'),
    path('aula/deletarPresencaAula', views.deletarPresencaAula,name='deletarPresencaAula'),
    
    #Turma
    path('turma/', views.homeTurma,name='indexTurma'),
    path('turma/inserir', views.inserirTurma,name='telaInserirTurma'),
    path('turma/selecionarTurma', views.selecionarTurma,name='selecionarTurma'),
    path('turma/cadastrarTurma', views.cadastrarTurma,name='cadastroDeTurma'),
    path('turma/alterarTurma', views.alterarTurma,name='alteracaoDeTurma'),
    path('turma/deletarTurma', views.deletarTurma,name='deletarTurma'),

    #Professor
    path('professor/', views.homeProfessor,name='indexProfessor'),
    path('professor/inserir', views.inserirProfessor,name='telaInserirProfessor'),
    path('professor/selecionarProfessor', views.selecionarProfessor,name='selecionarProfessor'),
    path('professor/cadastrarProfessor', views.cadastrarProfessor,name='cadastroDeProfessor'),
    path('professor/alterarProfessor', views.alterarProfessor,name='alteracaoDeProfessor'),
    path('professor/deletarProfessor', views.deletarProfessor,name='deletarProfessor'),

    #Professor Turma
    path('professor/inserirProfessorTurma', views.inserirProfessorTurma,name='inserirProfessorTurma'),
    path('professor/deletarProfessorTurma', views.deletarProfessorTurma,name='deletarProfessorTurma'),
    
    #Usuarios
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', views.homeUsuarios,name='indexUsuario'),
    path('registration/inserir', views.criarUsuario,name='telaInserirUsuario'),
    path('registration/cadastrarUsuario', views.cadastrarUsuario,name='executarCadastroUsuario'),
    path('registration/selecionarUsuario', views.selecionarUsuario,name='selecionarUsuario'),

    #Alunos
    path('alunos/', views.homeAlunos,name='indexAluno'),
    path('alunos/inserir', views.inserirAluno,name='telaInserirAluno'),
    path('alunos/selecionarAluno', views.selecionarAluno,name='selecionarAluno'),
    #1 - Url, 2 - funcao criada em views.py ,3 - Nome para usar em formulario
    path('alunos/cadastrarAluno', views.cadastrarAluno,name='cadastroDeAluno'),
    path('alunos/alterarAluno', views.alterarAluno,name='alteracaoDeAluno'),
    path('alunos/deletarAluno', views.deletarAluno,name='deletarAluno'),

]
