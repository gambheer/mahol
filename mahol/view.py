from django.http import HttpResponse


def ping():
    return HttpResponse("ok.")
