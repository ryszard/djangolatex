# -*- coding: utf-8 -*-
from latex import process_latex
from django.template import loader, RequestContext
from django.http import HttpResponse

def direct_to_latex_template(request, template, filename, extra_context=None, **kwargs):
    """
    Render a given template with any extra URL parameters in the context as
    ``{{ params }}``.
    """
    if extra_context is None: extra_context = {}
    dictionary = {'params': kwargs}
    for key, value in extra_context.items():
        if callable(value):
            dictionary[key] = value()
        else:
            dictionary[key] = value
    print dictionary
    c = RequestContext(request, dictionary)
    t = loader.get_template(template)
    latex = t.render(c)
    print latex
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=%s.pdf' % filename
    process_latex(latex, outfile=response)
    return response
