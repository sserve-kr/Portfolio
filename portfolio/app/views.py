from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import Project
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def projects(request):
    all_projects = Project.objects.all().order_by('start_commit')
    return render(request, 'app/projects.html', {
        "projects": all_projects
    })

def get_project(request, project_id):
    project = Project.objects.get(href=project_id)
    return JsonResponse(project.as_dictionary())

def get_project_list(request):
    all_projects = Project.objects.all().order_by('start_commit')
    return JsonResponse([project.href for project in all_projects], safe=False)

def contact_success(request):
    return render(request, "app/contact-thanks.html")

class ContactView(FormView):
    template_name = 'app/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy("app:thanks")

    def form_valid(self, form: ContactForm):
        form.send_mail()
        return super().form_valid(form)