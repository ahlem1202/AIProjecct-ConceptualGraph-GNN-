# myapp/urls.py
from django.urls import path
from .views import search_word
from myapp.views import gradio_integration
from myapp.views import gradio_integration

urlpatterns = [
    path('search/', search_word, name='search_word'),
   
    path('gradio/', gradio_integration, name='gradio_integration'),
]
