# chatbot_mini
This is a mini web app built using django, javascript and css. 

It collects users' names, emails and information of the trucks they have. The users' information will be save in "name_email.csv" and the truck specifications will be save in "name_trucks.csv".

* First page: ask for user's information. 
1. Input the row: mark, model and quantity in the form by selecting in the drop-down lists and setting integer values (>0)
2. Click "add" button which validates the input and indicates the invalid inputs at the bottom of the form.

**Note**: 
1. The options of the drop-down list for "Model" updates after changing "Mark" according the relations in the file "truck_marks_models.csv". 
2. If something is not in the the lists, select "Other" and then type in the new row appearing. 
3. Before "add" or "remove" this new row, the old "add" button is disabled.
4. More options in the drop-down list are possible by adding more truck marks and models in the file "truck_marks_models.csv".

* An added row can be removed using the "remove" button at the end of the row. 

* By clicking the "Submit" button, the form will be submitted and data will be saved.
<img src="https://github.com/jh-xu/chatbot_mini/blob/master/chatbot_mini/input_info.png" width=40% />

* After submit, it shows a summary of the users' input.
<img src="https://github.com/jh-xu/chatbot_mini/blob/master/chatbot_mini/submit.png" width=40% />
