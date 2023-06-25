from django.template import Library
from Fruitipedia.fruits.models import Profile

register = Library()


@register.simple_tag()
def get_profile():
    return Profile.objects.first()