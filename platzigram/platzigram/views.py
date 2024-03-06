
from django.http import HttpResponse

from datetime import datetime




def hello_world(request):
    """ return a greeeting """
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Hello world! {now}'.format(now=str(now)))


def hi(request):
    # import pdb; pdb.set_trace()
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    return HttpResponse(str(numbers), content_type='aplication/json')


def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Welcome {}, you are allowed here'.format(name)
    return HttpResponse(message)