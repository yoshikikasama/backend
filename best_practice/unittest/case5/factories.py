import factory

from models import Organaization, Post, User


class OrganizationFactory(factory.django.DjangoModelFactory):
    name = 'beproud'

    class Meta:
        model = Organaization


class UserFactory(factory.django.DjangoModelFactory):
    username = 'foobar'

    organaization = factory.SubFactory(OrganizationFactory)

    class Meta:
        model = User


class PostFactory(factory.django.DjangoModelFactory):
    title = '記事タイトル'
    body = '記事本文'
    author = factory.Subfactory(UserFactory)
    published_at = None