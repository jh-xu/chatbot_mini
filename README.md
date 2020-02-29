# chatbot_mini
This is a mini web app built using django, javascript and css. 

It collects users' names, emails and information of the trucks they have. The users' information will be save in "name_email.csv" and the truck specifications will be save in "name_trucks.csv".

1. First page: ask for user's information. 
* Input the row: mark, model and quantity in the form by selecting in the drop-down lists and setting integer values (>0)
* Click "add" button which validates the input and indicates the invalid inputs at the bottom of the form.

**Note**: 
* The options of the drop-down list for "Model" updates after changing "Mark" according the relations in the file "truck_marks_models.csv". 
* If something is not in the the lists, select "Other" and then type in the new row appeared above. 
* Before "add" or "remove" this new row, the old "add" button is disabled.
* More options in the drop-down list are possible by adding more truck marks and models in the file "truck_marks_models.csv".
<img src="https://github.com/jh-xu/chatbot_mini/blob/master/chatbot_mini/chatbot_mini_Select_Add_Other.PNG" width=50% />


2. An added row can be removed using the "remove" button at the end of the row. 

3. By clicking the "Submit" button, the form will be submitted and data will be saved.
<img src="https://github.com/jh-xu/chatbot_mini/blob/master/chatbot_mini/chatbot_mini_Select_Add.PNG" width=50% />

4. After submit, it shows a summary of the users' input.
<img src="https://github.com/jh-xu/chatbot_mini/blob/master/chatbot_mini/submit.png" width=40% />
