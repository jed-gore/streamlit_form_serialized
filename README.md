# Streamlit Form Serialized

The goal of this repo is to 1) demonstrate the simplified usage of [Marshmallow](https://github.com/marshmallow-code/marshmallow-sqlalchemy) and Streamlit Forms to persist python objects in SQL and use Streamlit as an input engine. and 2) to demonstrate the use of an editable Streamlit dataframe as another alternative for i/o to SQL.

There are two streamlit apps.  One is app.py the second is editable_dataframe_streamlit.py

APP.PY

From a Terminal in VSCode run "streamlit run app.py" to launch the input app.  Enter a user name and an associated object and submit.

![image](https://user-images.githubusercontent.com/39496491/230500778-b32934d1-0b94-41e3-be18-82b4f1783b8c.png)

Then, close the app in Terminal and run "streamlit run sql_admin.py" and in the dropdown and type "select * from users;" or "select * from user_objects" to see your input.

![image](https://user-images.githubusercontent.com/39496491/230428074-1c6eda01-5e77-4c7f-81b8-1a84ce3c5a7f.png)

Future work on this project will have the ability to edit / delete entries in the original Form, as well as one-to-many relationships better displayed (perhaps in an editable dataframe?) between "user" and other objects.

Credit: https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/ for the sql_admin.py file.

EDITABLE_DATAFRAME_STREAMLIT.PY

From a Terminal in VSCode run "streamlit run editable_dataframe_streamlit.py" to launch the input app.

You'll see a dataframe you can edit by clicking on it.  And then you can save the edited dataframe to SQL or download to CSV.

![image](https://user-images.githubusercontent.com/39496491/230629816-2e06bfd4-f83e-4fac-a778-3e01c13e627d.png)

Feel free to contact me with questions.
