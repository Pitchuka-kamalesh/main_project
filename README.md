#
## Models must created for treatment :
[❌]  Task must complete 

[ ✔ ] Task complete 

- [❌]  create the treatement models with variables and fields
- [❌]  Then write the inner paremeters for the form 
- [❌]  then create the performance table and 
- [❌]  create the relaction between the tables 
- [❌] then makemigrations and migrate the table 
- [❌]  tables must be created
- [❌] create the views and urls for the models and data 
- [❌] create the selenium script 
- [❌] create the automate the data insection 

# 
## treatment model 
- name_variable	fields	Null	Relaction
- province_state 	Char_Field	FALSE	
- country 	Char_Field	FALSE	
- uwi 	Integer_Field	FALSE	Forienkey
- active_ind 	Char_Field	FALSE	
- source	Char_Field	FALSE	
- license_id	Char_Field	FALSE	
- dril_id	Integer_Field	FALSE	
- comp_source	Char_Field	FALSE	
- comp_obs_no	Char_Field	FALSE	
- changeby	Char_Field	FALSE	
- changedate	Date_Field	FALSE	
- created_by	Char_Field	FALSE	
- created_date	Date_Field	FALSE	
- treatment_obs_no	Integer_Field	FALSE	
- stageno	Integer_Field	FALSE	
- treatment_top	Integer_Field	FALSE	
- treatment_base	Integer_Field	FALSE	
- total_no_of_statges	Integer_Field	FALSE	
- casing_ind_type	Char_Field	FALSE	
- data_source	Char_Field	FALSE	
- line_ind	Integer_Field	FALSE	
- treatment_type	Char_Field	FALSE	
- simulaton_type	Char_Field	FALSE	
- pressure_pump_co	Integer_Field	FALSE	
- treatment_co	Char_Field	FALSE	
- top_strait_unit_id	Char_Field	FALSE	
- top_age	Integer_Field	FALSE	
- base_strait_unit_id	Char_Field	FALSE	
- base_age	Integer_Field	FALSE	
- treatment_remark	Char_Field	FALSE	










#
## first creating the project 

__code__  : ```django-admin startproject bot_project```
#
## second cd bot_project 
__code__ :  ```python manage.py startapp bot_app```

# 
## main when creating a django app 
@ first write app name in project settings 

__doc__ : 
        
        INSTALLED_APPS = [
        
            'django.contrib.admin',
        
            'django.contrib.auth',
        
            'django.contrib.contenttypes',
        
            'django.contrib.sessions',
        
            'django.contrib.messages',
        
            'django.contrib.staticfiles',
        
            'bot_app1' # this is the app name 
        
        ]

