Named Colors
============

:mod:`mcplot` provides a large number of named colors from a variety
of public sources, which can be retrieved with
:func:`mcplot.color.get_color()`.

Next to `Matplotlib`_'s `Base Colors`_, the `Tableau palette`_, the
`CSS Colors`_, and the `XKCD Colors`_, there are `Paul Tol`_'s
qualitative colors named `SRON Colors`_, `Stuart Semple`_'s `Freetone
Colors`_, and the named `UFZ Colors`_ of the `Helmholtz Centre for
Environmental Research`_.

The named colors can be printed with
:func:`mcplot.color.print_colors()` and plotted on screen or into a
file with :func:`mcplot.color.show_colors()` with the categories
`base`, `css`, `freetone`, `sron`, `tableau`, `ufz`, and `xkcd`. A PDF
file with all named colors is given here: `mcplot_colors.pdf`_.

..
   for i in images/mcplot_colors-*.png ; do echo $i ; magick identify ${i} ; done

Base Colors
-----------

.. image:: ../images/mcplot_colors-base.png
   :width: 350 px
   :align: center
   :alt: Matplotlib base colors

Tableau Palette
---------------

.. image:: ../images/mcplot_colors-tableau.png
   :width: 550 px
   :align: center
   :alt: Matplotlib tableau palette

SRON Colors
-----------

.. image:: ../images/mcplot_colors-sron.png
   :width: 800 px
   :align: center
   :alt: Paul Tol's named colors

UFZ Colors
----------

.. image:: ../images/mcplot_colors-ufz.png
   :width: 600 px
   :align: center
   :alt: UFZ corporate colors

CSS Colors
----------

.. image:: ../images/mcplot_colors-css.png
   :width: 800 px
   :align: center
   :alt: Matplotlib css colors

XKCD Colors
-----------

.. image:: ../images/mcplot_colors-xkcd_01.png
   :width: 800 px
   :align: center
   :alt: Matplotlib XKCD colors #1

.. image:: ../images/mcplot_colors-xkcd_02.png
   :width: 800 px
   :align: center
   :alt: Matplotlib XKCD colors #2

.. image:: ../images/mcplot_colors-xkcd_03.png
   :width: 800 px
   :align: center
   :alt: Matplotlib XKCD colors #3

.. image:: ../images/mcplot_colors-xkcd_04.png
   :width: 800 px
   :align: center
   :alt: Matplotlib XKCD colors #4

.. image:: ../images/mcplot_colors-xkcd_05.png
   :width: 800 px
   :align: center
   :alt: Matplotlib XKCD colors #5

.. image:: ../images/mcplot_colors-xkcd_06.png
   :width: 800 px
   :align: center
   :alt: Matplotlib XKCD colors #6

.. image:: ../images/mcplot_colors-xkcd_07.png
   :width: 800 px
   :align: center
   :alt: Matplotlib XKCD colors #7

Freetone Colors
---------------

.. image:: ../images/mcplot_colors-freetone_13.png
   :width: 800 px
   :align: center
   :alt: Stuart Semple's Freetone colors #1

.. image:: ../images/mcplot_colors-freetone_14.png
   :width: 800 px
   :align: center
   :alt: Stuart Semple's Freetone colors #2

.. image:: ../images/mcplot_colors-freetone_15.png
   :width: 800 px
   :align: center
   :alt: Stuart Semple's Freetone colors #3

.. image:: ../images/mcplot_colors-freetone_16.png
   :width: 800 px
   :align: center
   :alt: Stuart Semple's Freetone colors #4

.. image:: ../images/mcplot_colors-freetone_17.png
   :width: 800 px
   :align: center
   :alt: Stuart Semple's Freetone colors #5

.. image:: ../images/mcplot_colors-freetone_18.png
   :width: 800 px
   :align: center
   :alt: Stuart Semple's Freetone colors #6

.. image:: ../images/mcplot_colors-freetone_19.png
   :width: 800 px
   :align: center
   :alt: Stuart Semple's Freetone colors #7

.. image:: ../images/mcplot_colors-freetone_20.png
   :width: 800 px
   :align: center
   :alt: Stuart Semple's Freetone colors #8

.. image:: ../images/mcplot_colors-freetone_21.png
   :width: 800 px
   :align: center
   :alt: Stuart Semple's Freetone colors #9


.. _Helmholtz Centre for Environmental Research: https://www.ufz.de/
.. _Matplotlib: https://matplotlib.org/stable/gallery/color/named_colors.html
.. _Paul Tol: https://personal.sron.nl/~pault/
.. _Stuart Semple: https://culturehustle.com/products/freetone
.. _mcplot_colors.pdf: https://mcuntz.github.io/mcplot/images/mcplot_colors.pdf
