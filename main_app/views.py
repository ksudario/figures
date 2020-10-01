from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Figure, Weapon, Cleaning, Photo
from .forms import CleaningForm
import uuid
import boto3
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'figurecollector'

@login_required
def add_photo(request, figure_id):
    # Collect the photo asset from the request
    photo_file = request.FILES.get('photo-file', None)

    # check if a photo asset was provided
    if photo_file:
        # make the s3 utility available locally to this view function
        s3 = boto3.client('s3')
        # create a key that will be used to add a unique identifier to our photo asset
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]

        try:
            # attempt to upload the file to aws
            s3.upload_fileobj(photo_file, BUCKET, key)
            #create the unique photo asset url
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # create an instance the photo model in memory
            photo = Photo(url=url, figure_id=figure_id)
            # save the photo model
            photo.save()

        except:
            # something went wrong - gracefully do something else
            print('An error occurred uploading file to s3')
    
    return redirect('detail', figure_id=figure_id)



def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('figures')
    else:
      error_message = 'Invalid sign up, try again!'
  form = UserCreationForm()
  context = {'form' : form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'home.html')

@login_required
def figures_index(request):
    figures = Figure.objects.filter(user=request.user)
    return render(request, 'figures/index.html', { 'figures': figures})

@login_required
def figures_detail(request, figure_id):
    
    figure = Figure.objects.get(id=figure_id)
    cleaning_form = CleaningForm()
    weapons_figure_doesnt_have = Weapon.objects.exclude(id__in=figure.weapons.all().values_list('id'))

    return render(request, 'figures/detail.html', {
        'figure': figure,
        'cleaning_form': cleaning_form,
        'weapons': weapons_figure_doesnt_have
    })


class FigureCreate(LoginRequiredMixin, CreateView):
  model = Figure
  fields = ['name', 'type', 'cost']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class FigureUpdate(LoginRequiredMixin, UpdateView):
  model = Figure
  fields = ['name', 'type', 'cost']

class FigureDelete(LoginRequiredMixin, DeleteView):
  model = Figure
  success_url ='/figures/'


@login_required
def weapons_index(request):
    weapons = Weapon.objects.filter(user=request.user)
    return render(request,'weapons/index.html', {'weapons': weapons})

@login_required
def relate_weapon(request, figure_id, weapon_id):
  Figure.objects.get(id=figure_id).weapons.add(weapon_id)
  return redirect('detail', figure_id=figure_id)
@login_required
def disconnect_weapon(request, figure_id, weapon_id):
  Figure.objects.get(id=figure_id).weapons.remove(weapon_id)
  return redirect('detail', figure_id=figure_id)

class WeaponCreate(LoginRequiredMixin, CreateView):
  model = Weapon
  fields = ['name']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class WeaponUpdate(LoginRequiredMixin, UpdateView):
  model = Weapon
  fields = ['name']

class WeaponDelete(LoginRequiredMixin, DeleteView):
  model = Weapon
  success_url ='/weapons/'

def cleanings_index(request):
  cleanings = Cleaning.objects.all()
  return render(request,'cleanings/index.html', {'cleanings' : cleanings})

def add_cleaning(request, figure_id):
  form  = CleaningForm(request.POST)

  if form.is_valid():
    new_cleaning = form.save(commit=False)
    new_cleaning.figure_id=figure_id
    new_cleaning.save()
  return redirect('detail', figure_id=figure_id)

def assoc_weapon(request, figure_id, weapon_id):
  Figure.objects.get(id=figure_id).weapons.add(weapon_id)
  return redirect('detail', figure_id=figure_id)

def unassoc_weapon(request, figure_id, weapon_id):
  Figure.objects.get(id=figure_id).weapons.remove(weapon_id)
  return redirect('detail', figure_id=figure_id)

class CleaningUpdate(LoginRequiredMixin, UpdateView):
  model = Cleaning
  fields = ['name', 'date']

class CleaningDelete(LoginRequiredMixin, DeleteView):
  model = Cleaning
  success_url ='/cleanings/'