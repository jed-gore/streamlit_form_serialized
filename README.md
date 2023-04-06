# Streamlit Form Serialized

The goal of this rep is to demonstrate the usage of Marshmallow, Streamlit Forms, and SQL Alchemy to persist python objects in SQL and use Streamlit as an input engine.

Run "streamlit run app.py" to launch the input app.  Enter a user name and submit.

![image](https://user-images.githubusercontent.com/39496491/230428284-a669b5d2-5e3d-45ca-8418-566cb0057529.png)

Then, run "streamlit run sql_admin.py" and in the dropdown and type "select * from users;" to see your input.

![image](https://user-images.githubusercontent.com/39496491/230428074-1c6eda01-5e77-4c7f-81b8-1a84ce3c5a7f.png)

Future work on this project will have the ability to edit / delete entries in the original Form, as well as one-to-many relationships between "user" and other objects.
