from django.urls import path
from .views import HomeView, SendEmailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Home page (index.html)
    path('send-email/', SendEmailView.as_view(), name='send_email'),  # Contact form POST
]
