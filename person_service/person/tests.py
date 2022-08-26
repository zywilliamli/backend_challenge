from person_service.schema import Query
from person_service.person.models import Person, Address
from django.test.testcases import TestCase
import graphene


class PersonServiceTest(TestCase):

    def setUp(self):
        super().setUp()
        self.query = """
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
        """

    def test_fetch_person(self):
        Person.objects.create(email='random.person@gmail.com', name='William Billy Wilson',
                              address=Address.objects.create(number=1, street='George Street', city='Sydney',
                                                             state='New South Wales'))

        schema = graphene.Schema(query=Query)
        result = schema.execute("""
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
        """)
        self.assertIsNone(result.errors)
        self.assertDictEqual({
            "person": [
                {
                    "email": "random.person@gmail.com",
                    "name": "William Billy Wilson",
                    "address": {
                        "number": 1,
                        "street": "George Street",
                        "city": "Sydney",
                        "state": "NEW_SOUTH_WALES"
                    }
                }
            ]
        }, result.data)
