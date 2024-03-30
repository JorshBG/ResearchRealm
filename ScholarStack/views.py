from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from ScholarStack.forms import SignUpForm, ThesisCreationForm
from ScholarStack.models import Thesis


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'pages/auth/login.html')


def sign_in(request):
    if request.method == 'POST':

        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            login(request, user)
            return redirect('home')
        return render(request, 'pages/auth/login.html', {
            'errors': 'Invalid username or password.'
        })

    return render(request, 'pages/auth/login.html')


@login_required(redirect_field_name='sign_in')
def sign_out(request):
    logout(request)
    return redirect('login')


def register(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'pages/auth/register.html', {'errors': form.errors})

    return render(request, 'pages/auth/register.html', {
        'errors': '',
    })


@login_required(redirect_field_name='login', login_url='login')
def home(request):

    if request.method == 'POST' and request.POST['action'] == 'delete':
        thesis = Thesis.objects.get(id=request.POST['thesis_id'])
        thesis.delete()

    theses = Thesis.objects.filter(user=request.user)

    return render(request, 'pages/protected/home.html', {
        'user': request.user,
        'theses': theses
    })


@login_required(redirect_field_name='login', login_url='login')
def explore(request):

    theses = Thesis.objects.all()

    return render(request, 'pages/protected/explore.html', {
        'user': request.user,
        'theses': theses
    })


@login_required(redirect_field_name='login', login_url='login')
def create_thesis(request):
    if request.method == 'POST' and request.FILES['content']:

        print(request.FILES, request.POST, sep='\n\n')

        thesis_form = ThesisCreationForm(request.POST, request.FILES)

        if thesis_form.is_valid():
            thesis_form.save()
            return redirect('home')
        return render(request, 'pages/protected/create_thesis.html', {
            'form': thesis_form,
            'errors': thesis_form.errors
        }, status=400)

    return render(request, 'pages/protected/create_thesis.html', {
        'form': ThesisCreationForm(),
        'title': 'Upload'
    })


@login_required(redirect_field_name='login', login_url='login')
def edit_thesis(request, id):
    thesis = Thesis.objects.get(id=id)
    print(thesis)
    print(request.FILES, request.POST, sep='\n\n')
    if request.method == 'POST' and request.FILES['content']:

        thesis = Thesis.objects.get(id=id)

        thesis.title = request.POST['title']
        thesis.content = request.FILES['content']
        thesis.description = request.POST['description']

        thesis.save()

        return redirect('home')

    return render(request, 'pages/protected/edith_thesis.html', {
        'thesis': thesis
    })


@login_required(redirect_field_name='login', login_url='login')
def show_thesis(request, id):

    thesis = Thesis.objects.get(id=id)

    return render(request, 'pages/protected/watch_thesis.html', {
        'thesis': thesis
    })


