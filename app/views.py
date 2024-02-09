from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.

class templatehtml(TemplateView):
    template_name='templatehtml.html'
    #TemplateView has a method of get_context_data which accepts **Kwargs and is used to create Empty Context Dict Obj
    def get_context_data(self,**kwargs):
        #we are inheriting the parent view properties to the child so use super()
        #Overriding the parent class properties and add new properties in child class
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='Sravani'
        ECDO['City']='Bangalore'
        #return the Object
        return ECDO


class insertobj_byTV(TemplateView):
    template_name='insertobj_byTV.html'
    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['CFO']=CompanyForm
        return ECDO
        
    def post(self,request):
        CFDO=CompanyForm(request.POST)
        if CFDO.is_valid():
            CFDO.save()
            return  HttpResponse('INserting object by TemplateView')


class insertobj_btFV(FormView):
    template_name='insertobj_btFV.html'
    form_class=CompanyForm #form_class will be used to context object,form class object and send to FrontEnd

    def form_valid(self,form): #form_valid will check POST is activate or not ,collect the data also validate it.
        form.save()
        return HttpResponse('Inserting through FormView ')
