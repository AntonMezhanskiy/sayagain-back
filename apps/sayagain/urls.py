from django.urls import path
from . import views

app_name = 'sayagain'

urlpatterns = [
    path('words/', views.WordListView.as_view(), name='words_list'),
    path('words/create/', views.WordCreateView.as_view(), name='word_create_view'),
    path('words/<int:pk>/edit/', views.WordEditView.as_view(), name='word_edit_view'),
]
