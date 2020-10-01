from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('figures/', views.figures_index, name='figures'),
    path('figures/<int:figure_id>/', views.figures_detail, name='detail'),
    path('figures/create/', views.FigureCreate.as_view(), name='figures_create'),
    path('figuresfigures/<int:pk>/update/', views.FigureUpdate.as_view(), name='figures_update'),
    path('figures/<int:pk>/delete/', views.FigureDelete.as_view(), name='figures_delete'),
    path('figures/<int:figure_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),
    path('figures/<int:figure_id>/assoc_weapon/<int:weapon_id>/', views.assoc_weapon, name='assoc_weapon'),
    path('figures/<int:figure_id>/unassoc_weapon/<int:weapon_id>/', views.unassoc_weapon, name='unassoc_weapon'),
    path('weapons/', views.weapons_index, name='weapons_index'),
    path('weapons/create/', views.WeaponCreate.as_view(), name='weapons_create'),
    path('weapons/<int:pk>/update/', views.WeaponUpdate.as_view(), name='weapons_update'),
    path('weapons/<int:pk>/delete/', views.WeaponDelete.as_view(), name='weapons_delete'),
    path('cleaning/', views.cleanings_index, name='cleanings_index'),
    path('cleaning/<int:pk>/update/', views.CleaningUpdate.as_view(), name='cleaning_update'),
    path('cleaning/<int:pk>/delete/', views.CleaningDelete.as_view(), name='cleaning_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('figures/<int:figure_id>/add_photo/', views.add_photo, name='add_photo'),

]
    
