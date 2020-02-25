from django import forms
import csv

# mark_choices = [('0', '----'),('1','VW'),('2','Benz'), ('3','Other')]

# model_choices = {'VW': [('1','VW1'),('2','VW2'),('3','VW3'),('4','Other')], 
                # 'Benz': [('1','BZ1'), ('2','BZ2'), ('3','BZ3'), ('4','BZ4'), ('5','BZ5'),('6','Other')],
                # 'Other': [('1','Other')]}
                
mark_choices = [('0', '----')]
model_choices = {}

# Loading marks and models from csv into lists of tuples (idx, item) with sorting
with open('truck_marks_models.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    mark_list = []
    for row in csv_reader:
        items = row
        mark_list.append(items[0])
                    
        model_choices_list = []
        
        for idx, item in enumerate(sorted(items[1:])):
            model_choices_list.append((str(idx+1), item))           
        model_choices_list.append((str(idx+2), 'Other'))

        model_choices[items[0]] = model_choices_list
        
    for idx, item in enumerate(sorted(mark_list)):
        mark_choices.append((str(idx+1), item))    
    mark_choices.append((str(idx+2), 'Other'))   

#print(mark_choices)
#print(model_choices)

# Loading marks and models from csv into lists of tuples (idx, item) without sorting
# with open('truck_marks_models.csv') as csv_file:
    # csv_reader = csv.reader(csv_file, delimiter=',')
    
    # for idx0, row in enumerate(csv_reader):
        # items = row
        # mark_choices.append((str(idx0+1), items[0]))
        
        # model_choices_list = []
        # for idx1, item in enumerate(items[1:]):
            # model_choices_list.append((str(idx1+1), item))  
        # model_choices_list.append((str(idx1+2), 'Other'))
        
        # model_choices[items[0]] = model_choices_list
    # mark_choices.append((str(idx0+2), 'Other'))   


class InputForm(forms.Form):
    mark = forms.ChoiceField(widget=forms.Select, choices=mark_choices)
    model = forms.ChoiceField(widget=forms.Select,initial='0',choices=[('0', '----')])
    quantity = forms.IntegerField(min_value=1)
