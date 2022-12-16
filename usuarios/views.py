from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.files.storage import FileSystemStorage

from usuarios.forms import Cadastro_form
from usuarios.models import Usuario

from dnit_bi.models import Agente

User = get_user_model()

# Create your views here.
def cadastro(request):
        
    if request.method == 'POST':
        form = Cadastro_form(request.POST, request.FILES)
        confirma_senha = request.POST['password2']
        if form.is_valid():
            
            usuario = form.save(commit=False)
            
            # VERIFICA SE USUARIO JA EXISTE
            if User.objects.filter(email=usuario.email).exists():
                # messages.success(request, 'Usuario cadastrado com sucesso')
                messages.error(request, 'Email ja cadastrado')
                return redirect('cadastro')

            # VERIFICA SE SENHAS SAO IGUAIS
            if usuario.password != confirma_senha:
                messages.error(request, 'As senhas devem ser iguais!')
                return redirect('cadastro')
            
            
            usuario.username=f'{usuario.email}'
            
            usuario.set_password(usuario.password)
            
            usuario.save()
            
            return redirect('login')
        
        
        
    else:
        form = Cadastro_form()
    
    return render(request, 'usuarios/cadastro.html', {'form':form})

def login(request):   
    if request.method == 'POST':
        email = request.POST.get('email', False)
        senha = request.POST['password']
        
        if email == "" or senha == "":
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
        
        
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('tickets_freshdesk')   
    
    
    
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def dashboard(request):
    agentes = Agente.objects.all()
    
    context = {
        
        'agentes' : agentes,
        
    }
    
    return render(request, 'usuarios/agentes.html', context)