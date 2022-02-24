from django.urls import path

from .views import TemplateView;

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name = 'index'),
    path('signup/', TemplateView.as_view(template_name='signup.html'), name = 'signup'),
    path('teamCreate/', TemplateView.as_view(template_name='teamCreate.html'), name = 'teamCreate'),
    path('profile/', TemplateView.as_view(template_name='profile.html'), name = 'profile'),
    path('team/', TemplateView.as_view(template_name='team.html'), name = 'team'),
]