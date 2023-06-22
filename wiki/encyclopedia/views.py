from django.shortcuts import render, reverse

from . import util
from . import parse_utils

#entrys = util.list_entries()

def index(request):
    entrys = util.list_entries()
    wiki_tuples = util.url_list(entrys)
    return render(request, "encyclopedia/index.html", {

        "entries": wiki_tuples
    })


def title(request, title):
    text = parse_utils.to_html(util.get_entry(title))
    return render(request, f"encyclopedia/page.html/", {"entry" : text, "title": title})

def _find_first(lst, condition):
    return next((x for x in lst if condition(x)), None)

def search(request):
    query = request.GET.get('q', '')
    entrys = util.list_entries()
    wiki_tuples = util.url_list(entrys)
    first =  _find_first(entrys, lambda x: x.lower() == query.lower())
    if first:
        return title(request, first)
    else:
        substrings = list(filter(lambda x: query in x[1], wiki_tuples))
        return render(request, 'encyclopedia/no_match.html', {'query': query, "substrings": substrings})