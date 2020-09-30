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
    path('figures/<int:figure_id>/add_activity/', views.add_activity, name='activities_create'),
    path('figures/<int:figure_id>/relate_weapon/<int:weapon_id>/', views.relate_weapon, name='relate_weapon'),
    path('figures/<int:figure_id>/disconnect_weapon/<int:weapon_id>/', views.disconnect_weapon, name='disconnect_weapon'),
    path('weapons/', views.weapons_index, name='weapons_index'),
    path('weapons/create/', views.WeaponCreate.as_view(), name='weapons_create'),
    path('weapons/<int:pk>/update/', views.WeaponUpdate.as_view(), name='weapons_update'),
    path('weapons/<int:pk>/delete/', views.WeaponDelete.as_view(), name='weapons_delete'),
    path('activity/', views.activities_index, name='activities_index'),
    path('activity/<int:pk>/update/', views.ActivityUpdate.as_view(), name='activity_update'),
    path('activity/<int:pk>/delete/', views.ActivityDelete.as_view(), name='activity_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('figures/<int:figure_id>/add_photo/', views.add_photo, name='add_photo'),

]
    
