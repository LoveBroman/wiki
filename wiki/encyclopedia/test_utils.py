import util
from parse_utils import to_html
import util
html = """# *HTML*

HTML is a markup language that can be used to define the structure of a web page. HTML elements include

* headings

* paragraphs
* lists
* links
* *and more!*

The most recent major version of HTML is HTML5."""

CSS ="""# CSS

CSS is a language that can be used to add style to an [HTML](/wiki/HTML) page.
"""

django = """# Django Git(/)

Django is a web framework written using [Python](/wiki/Python) that allows for the design of web applications that generate [HTML](/wiki/HTML) dynamically.

klok
hoh

* stål 
* Kål
* Bål

"""

html_django = to_html(html)
#print(html_django)

#print(to_html(CSS))
dj = to_html(django)
print(util.list_entries())