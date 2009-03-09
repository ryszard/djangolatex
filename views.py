# -*- coding: utf-8 -*-
"""
No warranty, express or implied.
We’ve done our best,
to debug and test.
Liability for damages denied.

Permission is granted hereby,
to copy, share, and modify.
Use as is fit,
free or for profit.
On this notice these rights rely.
"""

from latex import process_latex
from django.template import loader, RequestContext
from django.http import HttpResponse

def direct_to_pdf_template(request, template, filename, extra_context=None, **kwargs):
    """
    Render a given template with any extra URL parameters in the
    context as ``{{ params }}``, and then process it with `pdflatex`
    ``filename`` is used to set the Content-Disposition header.
    """
    if extra_context is None: extra_context = {}
    dictionary = {'params': kwargs}
    for key, value in extra_context.items():
        if callable(value):
            dictionary[key] = value()
        else:
            dictionary[key] = value

    c = RequestContext(request, dictionary)
    t = loader.get_template(template)
    latex = t.render(c)
    print latex
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=%s.pdf' % filename
    process_latex(latex, outfile=response)
    return response
