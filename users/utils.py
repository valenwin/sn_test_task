import clearbit
from django.conf import settings
from pyhunter import PyHunter
from requests import exceptions
from rest_framework import serializers

hunter = PyHunter(settings.EMAIL_HUNTER_API_KEY)
clearbit.key = settings.CLEARBIT_API_KEY


def email_verify(email):
    try:
        response = hunter.email_verifier(email)
        if response['result'] == 'undeliverable':
            raise serializers.ValidationError('The email address is not valid.')
    except exceptions.HTTPError:
        raise serializers.ValidationError
    return True


def clearbit_signup(email):
    person = clearbit.Person.find(email=email, stream=True)
    if person is not None:
        name = str(person['name']['fullName'])
        return name
    return None
