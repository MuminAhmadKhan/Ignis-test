from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json
class eventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['event_name','date','time','location','image']
        """widget = {
           'event_name' : forms.TextInput(attrs = {'class':'form-control'}),
           'date' : forms.SelectDateWidget(attrs={'class':'form-control','placeholder':'yyyy-mm-dd'}),
           'time' : forms.TimeInput(attrs={'class':'form-control'}),
           'location' : forms.TextInput(attrs={'class':'form-control'}),
           'image': forms.FileInput(attrs={'class':'form-control-file'}),
        }"""
        widgets = {
            'event_name': forms.TextInput(attrs={'class':'form-control'}),
            'date' : forms.DateInput(attrs={'class':'form-control','placeholder':'yyyy-mm-dd'}),
            'time' : forms.TimeInput(attrs={'class':'form-control'}),
           'location' : forms.TextInput(attrs={'class':'form-control'}),
           'image': forms.FileInput(attrs={'class':'form-control-file'}),
        }
def index(request):
    events=Events.objects.all()
    if request.method =='POST':
        print("ki")
        form=eventForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            print("yes")
            data =  Events()
            form = eventForm(request.POST,request.FILES, instance=data)
            print(form)
            
            form.save()
            return HttpResponseRedirect(reverse('index'),form)
        else:
            return render(request,"event/index.html",{
        "form":form,})

    form=eventForm()
    return render(request,"event/index.html",{
        "form":form,
        "events":events,
    })

def likes(request):
    events=Events.objects.filter(is_liked=True)
    return render(request,"event/likes.html",{
        "events":events,

    })
@csrf_exempt
def like(request):
    if request.method =="PUT":
        
        data=json.loads(request.body)
        
        event=Events.objects.get(pk=data['p_id'])
        print( data['is_liked'])     
        if data['is_liked']:   
            
            event.is_liked=True
        else:
            
          event.is_liked=False
        event.save()
        
        return JsonResponse({"message":"succesful",})