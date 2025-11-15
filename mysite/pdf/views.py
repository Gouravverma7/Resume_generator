from django.shortcuts import render, redirect
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
import mysite
import shutil

WKHTMLTOPDF_CMD = shutil.which("wkhtmltopdf")


def home(request):
    return render(request, 'pdf/home.html')


def accept(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        summary = request.POST.get('summary','')
        degree = request.POST.get('degree','')
        school = request.POST.get('school','')
        university = request.POST.get('university','')
        previous_work = request.POST.get('previous_work','')
        projects = request.POST.get('projects','')
        skills = request.POST.get('skills','')

        profile = Profile(name=name,email=email,phone=phone, summary=summary, degree=degree, school=school, university=university, previous_work=previous_work,projects=projects,skills=skills)
        profile.save()
        return redirect("/resume-list")

    return render(request,'pdf/accept.html')

def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html') 
    html = template.render({"user_profile":user_profile})
    options = {
        'page-size':'Letter',
        'encoding': 'UTF-8',
    }

    config = pdfkit.configuration(wkhtmltopdf=mysite.settings.WKHTMLTOPDF_CMD)

    pdf = pdfkit.from_string(html,False,options=options,configuration=config)
    response = HttpResponse(pdf,content_type="application/pdf")
    # response['Content-Disposition'] = 'attachment'
    response['Content-Disposition'] = f'attachment; filename="{user_profile.name}.pdf"'
    # filename = "resume.pdf"
    return response

def list(request):
    profiles = Profile.objects.all()
    return render(request,'pdf/list.html',{'profiles':profiles})