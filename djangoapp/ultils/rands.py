import string
from random import SystemRandom
from django.utils.text import slugify


def randon_letters(k=5):
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits, k=k
    ))


def slugify_new(text):
    return slugify(text) + randon_letters()


print(slugify_new('Blá bla atenaçao'))