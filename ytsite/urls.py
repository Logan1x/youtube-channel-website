from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('upload/', views.create_form, name='upload'),
    path('created/', views.created, name = "created"),
    # playlist starts here
    path('solidworks/', views.solidworks, name = "solidworks"),
    path('needhelp/', views.needhelp, name = "needhelp"),
    path('ors/', views.ors, name = "ors"),
    path('tech/', views.tech, name = "tech"),
    path('gci/', views.gci, name = "gci"),
    path('slomo/', views.slomo, name = "slomo"),
    path('methermo/', views.methermo, name = "methermo"),
    path('gatecs/', views.gatecs, name = "gatecs"),
    path('memechanical/', views.memechanical, name = "memechanical"),
    path('som/', views.som, name = "som"),
    path('bloging/', views.bloging, name = "bloging"),
    path('python/', views.python, name = "python"),
]
