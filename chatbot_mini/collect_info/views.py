from django.shortcuts import render
from . import models

import csv

# Create your views here.
def collect_info(request):
    return render(request, 'collect_info.html')

def int_each(string_list):
    return [int(x) for x in string_list]

def submit(request):
    #print(name,request.POST)
    name=request.POST['username']
    email=request.POST['email']
    with open("name_email.csv", 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([name,email])

    input_rows = []
    if request.POST['Mark_list'] !='':
        for mark, model, number in zip(request.POST['Mark_list'].split(','), 
                                       request.POST['Model_list'].split(','), 
                                       int_each(request.POST['Number_list'].split(','))):

            with open("name_trucks.csv", 'a+', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow([name, mark, model, number])
                
            input_rows.append(dict(Mark=mark, Model=model, Number=number))        
   
    tag_lib = {"user_info": {"name":name,"email":email}, "input_rows": input_rows, "input_length": len(input_rows)}
    return render(request, 'submit.html', tag_lib)


def submit2database(request):
    name=request.POST['username']
    email=request.POST['email']
    new_user = models.users(name=name, email=email)
    new_user.save()
    print(name,request.POST)
    input_rows = []
    if request.POST['Mark_list'] !='':
        for mark, model, number in zip(request.POST['Mark_list'].split(','), 
                                       request.POST['Model_list'].split(','), 
                                       int_each(request.POST['Number_list'].split(','))):
            input_rows.append(dict(Mark=mark, Model=model, Number=number))
            
            new_rec = models.Records(name=name, truck_mark=mark, truck_model=model, truck_nb=number)
            new_rec.save()
            
    tag_lib = {"user_info": {"name":name,"email":email}, "input_rows": input_rows, "input_length": len(input_rows)}
    
    return render(request, 'submit.html', tag_lib)
    