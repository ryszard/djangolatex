# -*- coding: utf-8 -*-
'''
No warranty, express or implied.
We’ve done our best,
to debug and test.
Liability for damages denied.

Permission is granted hereby,
to copy, share, and modify.
Use as is fit,
free or for profit.
On this notice these rights rely.
'''

from subprocess import call, PIPE
from os import remove, rename
from os.path import dirname
from tempfile import NamedTemporaryFile
from django.template import loader, Context

def pdflatex(file, type='pdf'):
    call(['pdflatex', '-interaction=nonstopmode',
                      '-output-format', type, file],
         cwd=dirname(file), stdout=PIPE, stderr=PIPE)

def process_latex(source, type='pdf', outfile=None):
    """
    Processes a LaTeX source file.
    Output is either being returned or stored in outfile.
    At the moment only pdf output is supported.
    """

    tex = NamedTemporaryFile()
    tex.write(source)
    tex.flush()
    base = tex.name
    items = "log aux pdf dvi png".split()
    names = dict((x, '%s.%s' % (base, x)) for x in items)
    output = names[type]

    if type == 'pdf' or type == 'dvi':
        pdflatex(base, type)
    elif type == 'png':
        pdflatex(base, 'dvi')
        call(['dvipng', '-bg', '-transparent',
              names['dvi'], '-o', names['png']],
              cwd=dirname(base), stdout=PIPE, stderr=PIPE)

    remove(names['log'])
    remove(names['aux'])


    o = file(output).read()
    remove(output)
    if not outfile:
        return o
    else:
        outfile.write(o)


