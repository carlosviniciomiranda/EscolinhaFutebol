from django.forms import ModelForm
from app_escolinha.models import Aluno

# Create the form class.
class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['aluno_nome', 'aluno_nascimento', 'aluno_nome_mae', 'aluno_nascimento_mae','aluno_nome_pai', 'aluno_nascimento_pai', 'aluno_cep', 'aluno_endereco','aluno_bairro', 'aluno_cidade', 'aluno_estado', 'aluno_status']
