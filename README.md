# backend_challenge
### run the following commands in order to spin up your very own local graphql service that answers to one query:
- `virtualenv env`
- `source env/bin/activate`
- `pip install -r requirements.txt`  
- `python manage.py makemigrations`  
- `python manage.py migrate`  
- `python manage.py loaddata william`  
- `python manage.py runserver`  