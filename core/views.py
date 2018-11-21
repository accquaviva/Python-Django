from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

from django.shortcuts import render

def home (request):
    return  render(request,'core/index.html')

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    dados = {'pessoas':pessoas,'form':form}
    return render(request,'core/lista_pessoas.html',dados)

def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('core_lista_pessoas')

def pessoas_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data ['form'] = form
    data ['pessoa'] = pessoa

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request,'core/update_pessoa.html',data)

def pessoas_delete(request,id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html',{'obj':pessoa})

def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    dados = {'veiculos':veiculos,'form':form}
    return render(request,'core/lista_veiculos.html',dados)

def veiculos_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def veiculos_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data ['form'] = form
    data ['veiculo'] = veiculo

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request,'core/update_veiculos.html',data)

def veiculos_delete(request,id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request,'core/delete_confirm.html',{'obj':veiculo})

def lista_movrotativos(request):
    form = MovrotativosForm()
    movrotativos = MovRotativo.objects.all()
    dados = {'movrotativos':movrotativos,'form':form}
    return render(request,'core/lista_movrotativos.html',dados)

def movrotativos_novo(request):
    form = MovrotativosForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')



def movrotativos_update(request,id):
    data = {}
    movrotativos = MovRotativo.objects.get(id=id)
    form = MovrotativosForm(request.POST or None, instance=movrotativos)
    data['movrotativos'] = movrotativos
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        return render(request,'core/update_movrotativos.html',data)

def movrotativos_delete(request,id):
    movrottivos = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        movrottivos.delete()
        return redirect('core_lista_movrotativos')
    else:
        return render (request,'core/delete_confirm.html',{'obj':movrottivos})

def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    dados = {'mensalistas':mensalistas,'form':form}
    return render(request,'core/lista_mensalistas.html',dados)

def mensalistas_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')

def mensalistas_update(request,id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance= mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request,'core/update_mensalistas.html',data)

def mensalistas_delete(request,id):
    mensalistas = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalistas.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request,'core/delete_confirm.html',{'obj':mensalistas})


def lista_movmensalitas(request):
    movmensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    dados = {'movmensalistas':movmensalistas,'form':form}
    return  render(request,'core/lista_movmensalitas.html',dados)

def movmensalitas_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalitas')

def movmensalitas_update(request,id):
    data = {}
    movmensalitas = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=movmensalitas)
    data['movmensalitas'] = movmensalitas
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalitas')
    else:
        return render(request,'core/updata_movmensalitas.html',data)




def movmensalitas_delete(request,id):
    movmensalitas = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        movmensalitas.delete()
        return redirect('core_lista_movmensalitas')
    else:
        return render(request,'core/delete_confirm.html',{'obj':movmensalitas})