from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView,FormView
from app.forms import *
# Create your views here.


## By using TemplateView inserting data

class insert_data(TemplateView):
    template_name = 'insert_data.html'
    
    def get_context_data(self,**kwargs):
        ECDO = super().get_context_data(**kwargs)   ## ECDO --> empty context dictionary object
        SFO = StudentForm()
        ECDO['SFO'] = SFO
        return ECDO

    def post(self, request):
        SFD = StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('<center><h1>Data Inserted by using TemplateView</h1></center>')



## By using FormView inserting data

class StudentFormView(FormView):
    template_name = 'StudentFormView.html'
    form_class = StudentForm    ## form_class --> it will perform all the operation

    def form_valid(self, form): ## form_valid()--> it will perform post method/collect_data/validation
                                ## form --> we pass a argument to store the data
        form.save()
        return HttpResponse('<center><h1>Data Inserted by using FormView</h1></center>')