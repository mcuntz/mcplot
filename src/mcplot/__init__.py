#!/usr/bin/env python
"""
mcplot provides a class that combines methods to easily produce
publication-ready graphics on light or black background. It includes a
large number of colormaps collected from different sources. And there are
a number of functions that help to position plots, number plot panels,
or generally write text on a graph.

The package was extracted from general purpose library pyjams
https://github.com/mcuntz/pyjams

:copyright: Copyright 2021- Matthias Cuntz, see AUTHORS.rst for details.
:license: MIT License, see LICENSE for details.

Subpackages
===========
.. autosummary::
   argsort
   color
   class_mcplot
   position
   romanliterals
   str2tex
   text2plot

History
   * Written Oct 2024 by Matthias Cuntz (mc (at) macu (dot) de)
   * v1.0, first standalone version, Oct 2024, Matthias Cuntz
   * v2.0 use similar names and defaults as Matplotlib,
     Nov 2024, Matthias Cuntz
   * v2.1 adds the font option, Mar 2025, Matthias Cuntz
   * v2.2 cli option and color documentation, May 2025, Matthias Cuntz

"""
# version, author
try:  # pragma: no cover
    from ._version import __version__
except ImportError:  # pragma: no cover
    # package is not installed
    __version__ = "0.0.0.dev0"
__author__  = "Matthias Cuntz"

# sub-packages without dependencies to rest of mcplot
# color palettes and continuous color maps
from . import color

# argmax, argmin and argsort for array_like and Python iterables
from .argsort import argmax, argmin, argsort
# Matthias Cuntz' standard plotting class.
from .class_mcplot import mcPlot
# positions of subplots, used with add_axes
from .position import position
# Convert integer to and from Roman numerals
from .romanliterals import int2roman, roman2int
# Convert strings to LaTeX strings
from .str2tex import str2tex
# put text on plot (import after str2tex)
from .text2plot import text2plot, abc2plot, signature2plot


__all__ = ['__version__', '__author__',
           'argmax', 'argmin', 'argsort',
           'color',
           'mcPlot',
           'position',
           'int2roman', 'roman2int',
           'str2tex',
           'text2plot', 'abc2plot', 'signature2plot',
           ]
