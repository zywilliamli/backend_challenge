# Backend Challenge

Follow the setup on this page to spin up your very own local graphql service that answers to one query:

### Setup:

##### clone this repo:

- `git clone https://github.com/zywilliamli/backend_challenge.git`
- `cd backend_challenge`

##### dependency setup:

- `virtualenv env`
- `source env/bin/activate` *(on Windows use `env\Scripts\activate`)*
- `pip install -r requirements.txt`

##### configure and run locally:

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py loaddata data`
- `python manage.py runserver`

### Usage:

##### visit [localhost:8000/graphql](localhost:8000/graphql) on your browser and try the following request:

```
query {
  person {
    email
    name
    address {
      number
      street
      city
      state
    }
  }
}
```