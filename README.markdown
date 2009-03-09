djangolatex
===========

djangolatex is a django package that allows you to produce PDF files
using Django Templates and pdflatex.

The main entry point is `djangolatex.views.direct_to_pdf_template`,
which is like direct_to_template except that the template is processed
by pdflatex after rendering and it takes an additional `filename`
argument (to be able to set the `Content-Disposition` HTTP header).

Authors
-------

Some code is taken from [this snippet](http://www.djangosnippets.org/snippets/102/),
authored by [blizz](http://www.djangosnippets.org/users/blizz/).


Licensing
---------

    No warranty, express or implied.
    We’ve done our best,
    to debug and test.
    Liability for damages denied.

    Permission is granted hereby,
    to copy, share, and modify.
    Use as is fit,
    free or for profit.
    On this notice these rights rely.