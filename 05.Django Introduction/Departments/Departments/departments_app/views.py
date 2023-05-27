from django.shortcuts import render


def sample_view(request, *args, **kwargs):
    print(args)
    print(kwargs)