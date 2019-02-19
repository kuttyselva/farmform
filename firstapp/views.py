from django.shortcuts import render
from django.http import HttpResponse
from django_tables2.tables import Table
import csv
import pandas as pd
from . import forms
def index(request):
    return render(request,'index.html')
def Formnameview(request):
    path='E:/udemy/first_project/firstapp/farmbook.csv'
    data = pd.read_csv(path)

    season=''
    district=''
    soil=''
    def compute(Season,district,soil):
        data_season = data[data['Season'].str.contains(season)]
        data_district=data_season[data_season['District'].str.contains(district)]
        data_soil=data_district[data_district['soiltype'].str.contains(soil)]
        ts=data_soil[['Crop']]
        return ts[['Crop']].head(8)
    form=forms.Formname()
    if request.method=='POST':
        form=forms.Formname(request.POST)
        if form.is_valid():
            season=form.cleaned_data['user']
            district=form.cleaned_data['password']
            soil=form.cleaned_data['text']


    da=compute(season,district,soil)
    data_html = da.to_html(index=False)
    context = {'loaded_data': data_html,'form':form}
    # return render(request,'form_page.html',{'form':form})
    print(context)
    return render(request, "form_page.html", context)

    # print(ts)
# Create your views here.
# def index(request):
#     if request.method == "POST":
#       #Get the posted form
#       MyLoginForm = LoginForm(request.POST)
#
#       if MyLoginForm.is_valid():
#          username = MyLoginForm.cleaned_data['username']
#       else:
#          MyLoginForm = Loginform()
#
#       return render(request, 'loggedin.html', {"username" : username})
    # path='E:/udemy/first_project/firstapp/wea.csv'
    # uf=UserForm(request.POST)
    # if uf.is_valid():
    #      user=uf.cleaned_data['username']
    #      data = pd.read_csv(path)
    #      data_html = data.to_html()
    #      context={"username":user}
    # #context = {'loaded_data': data_html}
    # #print(data)
    #      return render(request, "index.html", context)
    # # df_table = Table(data.to_dict(orient='list'))
    # # context = {'df_table': df_table}
    # # print(context['df_table'])
    # # return render(request, "index.html", context)
# def login(request):
#    username = "not logged in"
#
#    if request.method == "POST":
#       #Get the posted form
#       MyLoginForm = LoginForm(request.POST)
#
#       if MyLoginForm.is_valid():
#          username = MyLoginForm.cleaned_data['username']
#    else:
#          MyLoginForm = Loginform()
#
#    return render(request, 'loggedin.html', {"username" : username})
def help(request):
    return HttpResponse("hii")
