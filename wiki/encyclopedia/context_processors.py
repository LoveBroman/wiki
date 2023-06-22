import random
from django.urls import reverse
from . import util

def random_url(request):
    #urls = list(map(lambda x: "wiki/" + x, util.list_entries())) # List of URLs
    urls = util.list_entries() # List of URLs

    return {'random_url': reverse('title', args=[random.choice(urls)])}