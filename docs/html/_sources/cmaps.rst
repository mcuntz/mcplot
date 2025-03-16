Colormaps
=========

:mod:`mcplot` provides a large number of colormaps (in the jargon of
`Matplotlib`_) or color palettes (in the jargon of `Seaborn`_ ) from a
variety of public sources. They can be chosen with
:func:`mcplot.color.get_cmap()` (or the aliases
:func:`mcplot.color.get_palette()` and
:func:`mcplot.color.color_palette()` as in `Seaborn`_).

Next to `Matplotlib`_'s colormaps, there are the colormaps of the
`IPCC Visual Style Guide for WG1 Authors`_, `Paul Tol`_'s 2021 as well
his 2012 colors and colormaps, Mathematica's `DarkRainbow`_ color
scheme, color schemes from the `Department of Geography, University of
Oregon`_, the color tables from the `NCAR Command Language`_ (NCL),
and the color schemes from Cynthia Brewer's `Colorbrewer 2.0`_. Most
collections come with sequential, diverging, and qualitative or
categorical colormaps.

Colormap names can be printed with :func:`mcplot.color.print_cmaps()`
and plotted on screen or into a file with
:func:`mcplot.color.show_cmaps()` with the categories `brewer`,
`ipcc`, `mathematica`, `matplotlib`, `mcplot`, `ncl`, `oregon`,
`sron`, and `sron2012`. A PDF file with all colormaps is given here:
`mcplot_cmaps.pdf`_.

All colormaps can be reversed by appending `_r` to the name or using
the `reverse=True` keyword of :func:`mcplot.color.get_cmap()`.

:func:`~mcplot.color.get_cmap()` returns a list of RGB tuples. One can
use :meth:`matplotlib.colors.ListedColormap()` or
:meth:`matplotlib.colors.LinearSegmentedColormap.from_list` to get
Matplotlib colormaps, for example:

.. code-block:: python

   ncolors = 7
   cmap = mcplot.color.get_cmap(f'sron2012:buylrd_{ncolors + 2}')
   cmap = matplotlib.colors.ListedColormap(cmap[1:-1])
   cmap.set_under(cmap[0])
   cmap.set_over(cmap[-1])

If the keyword `as_cmap` is set, :func:`~mcplot.color.get_cmap()` uses
:meth:`~matplotlib.colors.ListedColormap()` to convert the list of RGB
tuples to a colormap.


mcplot Colormap
---------------

.. image:: ../images/mcplot_cmaps-mcplot_cmaps.png
   :width: 800 px
   :align: center
   :alt: toned down amwg colormap

SRON Colors
-----------

.. image:: ../images/mcplot_cmaps-sron_colors.png
   :width: 800 px
   :align: center
   :alt: Paul Tol's colors

SRON Colormaps
--------------

.. image:: ../images/mcplot_cmaps-sron_colormaps.png
   :width: 800 px
   :align: center
   :alt: Paul Tol's colormaps

SRON Functions
--------------

.. image:: ../images/mcplot_cmaps-sron_functions.png
   :width: 800 px
   :align: center
   :alt: Paul Tol's colormap functions

SRON 2012 Colors
----------------

.. image:: ../images/mcplot_cmaps-sron2012_colors_01.png
   :width: 800 px
   :align: center
   :alt: Paul Tol's 2012 colors #1

.. image:: ../images/mcplot_cmaps-sron2012_colors_02.png
   :width: 800 px
   :align: center
   :alt: Paul Tol's 2012 colors #2

SRON 2012 Functions
-------------------

.. image:: ../images/mcplot_cmaps-sron2012_functions.png
   :width: 800 px
   :align: center
   :alt: Paul Tol's 2012 colormap functions

Mathematica
-----------

.. image:: ../images/mcplot_cmaps-mathematica_rainbow.png
   :width: 800 px
   :align: center
   :alt: Mathematica's DarkRainbow color scheme

Oregon Sequential
-----------------

.. image:: ../images/mcplot_cmaps-oregon_sequential.png
   :width: 800 px
   :align: center
   :alt: Department of Geography, University of Oregon sequential color schems

Oregon Diverging
----------------

.. image:: ../images/mcplot_cmaps-oregon_diverging.png
   :width: 800 px
   :align: center
   :alt: Department of Geography, University of Oregon diverging color schemes

Oregon Qualitative
------------------

.. image:: ../images/mcplot_cmaps-oregon_qualitative.png
   :width: 800 px
   :align: center
   :alt: Department of Geography, University of Oregon qualitative color schemes

IPCC Categorical
----------------

.. image:: ../images/mcplot_cmaps-ipcc_categorical.png
   :width: 800 px
   :align: center
   :alt: IPCC WG1 categorical colormaps

IPCC Diverging
--------------

.. image:: ../images/mcplot_cmaps-ipcc_diverging_01.png
   :width: 800 px
   :align: center
   :alt: IPCC WG1 diverging colormaps #1

.. image:: ../images/mcplot_cmaps-ipcc_diverging_02.png
   :width: 800 px
   :align: center
   :alt: IPCC WG1 diverging colormaps #2

.. image:: ../images/mcplot_cmaps-ipcc_diverging_03.png
   :width: 800 px
   :align: center
   :alt: IPCC WG1 diverging colormaps #3

.. image:: ../images/mcplot_cmaps-ipcc_diverging_04.png
   :width: 800 px
   :align: center
   :alt: IPCC WG1 diverging colormaps #4

IPCC Sequential
---------------

.. image:: ../images/mcplot_cmaps-ipcc_sequential_01.png
   :width: 800 px
   :align: center
   :alt: IPCC WG1 sequential colormaps #1

.. image:: ../images/mcplot_cmaps-ipcc_sequential_02.png
   :width: 800 px
   :align: center
   :alt: IPCC WG1 sequential colormaps #2

.. image:: ../images/mcplot_cmaps-ipcc_sequential_03.png
   :width: 800 px
   :align: center
   :alt: IPCC WG1 sequential colormaps #3

.. image:: ../images/mcplot_cmaps-ipcc_sequential_04.png
   :width: 800 px
   :align: center
   :alt: IPCC WG1 sequential colormaps #4

.. image:: ../images/mcplot_cmaps-ipcc_sequential_05.png
   :width: 800 px
   :align: center
   :alt: IPCC WG1 sequential colormaps #5

NCL Small
---------

.. image:: ../images/mcplot_cmaps-ncl_small.png
   :width: 800 px
   :align: center
   :alt: NCL's small color tables

NCL Large
---------

.. image:: ../images/mcplot_cmaps-ncl_large_01.png
   :width: 800 px
   :align: center
   :alt: NCL's large color tables #1

.. image:: ../images/mcplot_cmaps-ncl_large_02.png
   :width: 800 px
   :align: center
   :alt: NCL's large color tables #2

NCL Meteo Swiss
---------------

.. image:: ../images/mcplot_cmaps-ncl_meteo_swiss.png
   :width: 800 px
   :align: center
   :alt: NCL's Meteo Swiss color tables

Matplotlib Perceptually Uniform Sequential
------------------------------------------

.. image:: ../images/mcplot_cmaps-matplotlib_perceptually_uniform_sequential.png
   :width: 800 px
   :align: center
   :alt: Matplotlib's perceptually uniform sequential colormaps

Matplotlib Sequential
---------------------

.. image:: ../images/mcplot_cmaps-matplotlib_sequential.png
   :width: 800 px
   :align: center
   :alt: Matplotlib's sequential colormaps

Matplotlib Diverging
--------------------

.. image:: ../images/mcplot_cmaps-matplotlib_diverging.png
   :width: 800 px
   :align: center
   :alt: Matplotlib's diverging colormaps

Matplotlib Cyclic
-----------------

.. image:: ../images/mcplot_cmaps-matplotlib_cyclic.png
   :width: 800 px
   :align: center
   :alt: Matplotlib's cyclic colormaps

Matplotlib Qualitative
----------------------

.. image:: ../images/mcplot_cmaps-matplotlib_qualitative.png
   :width: 800 px
   :align: center
   :alt: Matplotlib's qualitative colormaps

Matplotlib Miscellaneous
------------------------

.. image:: ../images/mcplot_cmaps-matplotlib_miscellaneous.png
   :width: 800 px
   :align: center
   :alt: Miscellaneous colormaps of Matplotlib

Brewer Sequential
-----------------

.. image:: ../images/mcplot_cmaps-brewer_sequential_01.png
   :width: 800 px
   :align: center
   :alt: Cynthia Brewer's sequential color schemes #1

.. image:: ../images/mcplot_cmaps-brewer_sequential_02.png
   :width: 800 px
   :align: center
   :alt: Cynthia Brewer's sequential color schemes #2

.. image:: ../images/mcplot_cmaps-brewer_sequential_03.png
   :width: 800 px
   :align: center
   :alt: Cynthia Brewer's sequential color schemes #3

.. image:: ../images/mcplot_cmaps-brewer_sequential_04.png
   :width: 800 px
   :align: center
   :alt: Cynthia Brewer's sequential color schemes #4

Brewer Diverging
----------------

.. image:: ../images/mcplot_cmaps-brewer_diverging_01.png
   :width: 800 px
   :align: center
   :alt: Cynthia Brewer's diverging color schemes #1

.. image:: ../images/mcplot_cmaps-brewer_diverging_02.png
   :width: 800 px
   :align: center
   :alt: Cynthia Brewer's diverging color schemes #2

.. image:: ../images/mcplot_cmaps-brewer_diverging_03.png
   :width: 800 px
   :align: center
   :alt: Cynthia Brewer's diverging color schemes #3

Brewer Qualitative
------------------

.. image:: ../images/mcplot_cmaps-brewer_qualitative_01.png
   :width: 800 px
   :align: center
   :alt: Cynthia Brewer's qualitative color schemes #1

.. image:: ../images/mcplot_cmaps-brewer_qualitative_02.png
   :width: 800 px
   :align: center
   :alt: Cynthia Brewer's qualitative color schemes #3


.. _Colorbrewer 2.0: https://colorbrewer2.org/
.. _Department of Geography, University of Oregon: https://pjbartlein.github.io/datagraphics/color_scales.html
.. _IPCC Visual Style Guide for WG1 Authors: https://www.ipcc.ch/site/assets/uploads/2019/04/IPCC-visual-style-guide.pdf
.. _DarkRainbow: https://reference.wolfram.com/language/guide/ColorSchemes.html
.. _Matplotlib: https://matplotlib.org/stable/gallery/color/colormap_reference.html
.. _NCAR Command Language: https://www.ncl.ucar.edu/Document/Graphics/color_table_gallery.shtml
.. _Paul Tol: https://personal.sron.nl/~pault/
.. _mcplot_cmaps.pdf: https://mcuntz.github.io/mcplot/images/mcplot_cmaps.pdf
.. _Seaborn: https://seaborn.pydata.org/tutorial/color_palettes.html
