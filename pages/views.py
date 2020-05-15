from django.views import generic

class HomePage(generic.TemplateView):
    template_name = 'index.html'

class AboutPage(generic.TemplateView):
    template_name = 'html/about.html'

class ContactPage(generic.TemplateView):
    template_name = 'html/contact.html'