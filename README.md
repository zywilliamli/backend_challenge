# Backend Challenge

Follow the setup on this page to spin up your very own local graphql service that answers to one query. This service
uses `Django` and `Graphene-Django` to implement a simple GraphQL service.

The service exposes a GraphQL endpoint at `/graphql`, and consist of a single query, `person`, which returns a `Person`
object.

A `Person` object has the following fields:

- `email` (string)
- `name` (string)
- `address` (Address)
    - `number` (integer)
    - `street` (string)
    - `city` (string)
    - `state` (GraphQL enum)

# Setup:

### clone this repo:

```
git clone https://github.com/zywilliamli/backend_challenge.git
cd backend_challenge
```

### dependency setup:

The first two commands are for using virtual environment, this is recommended but not necessary  
(you'll need python and pip for the next steps, if you are having trouble with pip try running `pip install --upgrade pip`)
```
virtualenv env
(mac) source env/bin/activate, (windows) env\Scripts\activate
pip install -r requirements.txt
```

### configure local service with mock data:

```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata data
```

### (optional) run test to verify service is working as intended:

```
python manage.py test
```

# Usage:

```
python manage.py runserver
```

### visit [localhost:8000/graphql](localhost:8000/graphql) on your browser and try the following request:

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