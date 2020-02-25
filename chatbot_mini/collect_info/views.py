from django.shortcuts import render
from . import models
from .forms import InputForm, model_choices

import csv

# Create your views here.
def collect_info(request):
    return render(request, 'collect_info.html', {'form': InputForm})

def load_models(request):
    mark = request.GET.get('mark')
    models = model_choices[mark]
    return render(request, 'model_dropdown_list_options.html', {'models': models})

def int_each(string_list):
    return [int(x) for x in string_list]

def submit(request):
    name=request.POST['username']
    email=request.POST['email']
    print(name,request.POST)
    with open("name_email.csv", 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([name,email])

    input_rows = []
    if request.POST['mark_list'] !='':
        for mark, model, quantity in zip(request.POST['mark_list'].split(','), 
                                       request.POST['model_list'].split(','), 
                                       int_each(request.POST['quantity_list'].split(','))):

            with open("name_trucks.csv", 'a+', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow([name, mark, model, quantity])
                
            input_rows.append(dict(Mark=mark, Model=model, Quantity=quantity))        
   
    tag_lib = {"user_info": {"name":name,"email":email}, "input_rows": input_rows, "input_length": len(input_rows)}
    print(tag_lib)
    return render(request, 'submit.html', tag_lib)


def submit2database(request):
    name=request.POST['username']
    email=request.POST['email']
    new_user = models.users(name=name, email=email)
    new_user.save()
    print(name,request.POST)
    input_rows = []
    if request.POST['mark_list'] !='':
        for mark, model, quantity in zip(request.POST['mark_list'].split(','), 
                                       request.POST['model_list'].split(','), 
                                       int_each(request.POST['quantity_list'].split(','))):
            input_rows.append(dict(Mark=mark, Model=model, quantity=quantity))
            
            new_rec = models.Records(name=name, truck_mark=mark, truck_model=model, truck_nb=quantity)
            new_rec.save()
            
    tag_lib = {"user_info": {"name":name,"email":email}, "input_rows": input_rows, "input_length": len(input_rows)}
    
    return render(request, 'submit.html', tag_lib)
    