from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'index.html'

class SendEmailView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # ✅ Save form to DB
        form.save()

        # ✅ Send Email
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        send_mail(
            subject=f'Contact Form Message from {name}',
            message=message,
            from_email=email,
            recipient_list=['adityajha240220@gmail.com'],
            fail_silently=False,
        )

        messages.success(self.request, "Message sent successfully.")
        return super().form_valid(form)
