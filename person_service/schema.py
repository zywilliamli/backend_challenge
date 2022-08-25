import graphene
from graphene_django import DjangoObjectType

from person_service.person.models import Person, Address


class AddressType(DjangoObjectType):
    class Meta:
        model = Address
        fields = ("number", "street", "city", "state")


class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        fields = ("email", "name", "address")


class Query(graphene.ObjectType):
    person = graphene.List(PersonType)
    address = graphene.Field(AddressType, name=graphene.String(required=True))

    def resolve_person(root, info):
        return Person.objects.select_related("address").all()

    def resolve_address(root, info):
        return Address.objects.get()


schema = graphene.Schema(query=Query)
