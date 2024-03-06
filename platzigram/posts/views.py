from datetime import datetime
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



posts = [

    {
        'name': 'Mont Blanc',
        'user': ' Mynor',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        
    }
]


def list_posts(request):

    content = []
    for post in posts:
        content.append('<p>{name} <br> {user} <br> {timestamp} </p>'.format(**post))
    return HttpResponse(str(posts))