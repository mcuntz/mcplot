"""
Collection of color palettes and continuous color maps

:copyright: Copyright 2021- Matthias Cuntz, see AUTHORS.md for details.
:license: MIT License, see LICENSE for details.

Subpackages
===========
.. autosummary::
   brewer_palettes
   freetone_palettes
   ipcc_palettes
   mathematica_palettes
   ncl_palettes
   oregon_palettes
   mcplot_palettes
   sron2012_palettes
   sron_palettes
   ufz_palettes
   color

"""
# colour palettes
from .brewer_palettes import brewer_sequential, brewer_diverging
from .brewer_palettes import brewer_qualitative
from .freetone_palettes import freetone_colors
from .ipcc_palettes import ipcc_categorical, ipcc_diverging, ipcc_sequential
from .mathematica_palettes import mathematica_rainbow
from .mcplot_palettes import mcplot_cmaps
from .ncl_palettes import ncl_large, ncl_small, ncl_meteo_swiss
from .oregon_palettes import oregon_sequential, oregon_diverging
from .oregon_palettes import oregon_qualitative
from .sron2012_palettes import sron2012_colors, sron2012_functions
from .sron_palettes import sron_named_colors
from .sron_palettes import sron_colors, sron_colormaps, sron_functions
from .ufz_palettes import ufz_colors
# get, show, print colors and color palettes
from .color import get_color, print_colors, show_colors
from .color import get_cmap, print_cmaps, show_cmaps
from .color import get_palette, print_palettes, show_palettes
from .color import color_palette


__all__ = ['brewer_sequential', 'brewer_diverging', 'brewer_qualitative',
           'ipcc_categorical', 'ipcc_diverging', 'ipcc_sequential',
           'freetone_colors'
           'mathematica_rainbow',
           'mcplot_cmaps',
           'ncl_large', 'ncl_small', 'ncl_meteo_swiss',
           'oregon_sequential', 'oregon_diverging', 'oregon_qualitative',
           'sron2012_colors', 'sron2012_functions',
           'sron_named_colors',
           'sron_colors', 'sron_colormaps', 'sron_functions',
           'ufz_colors',
           'get_color', 'print_colors', 'show_colors',
           'get_cmap', 'print_cmaps', 'show_cmaps',
           'get_palette', 'print_palettes', 'show_palettes',
           'color_palette'
           ]
