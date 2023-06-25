from django import template
from CarCollectionApp.car.models import Profile


register = template.Library()


@register.simple_tag
def get_profile():
    return Profile.objects.first()