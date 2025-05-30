mcplot
======

A Python package with a plotting class and routines for publication-ready graphics.

|DOI| |PyPI version| |Conda version| |License| |Build Status| |Coverage Status|


About mcplot
------------

``mcplot`` provides a class that combines methods to easily produce
publication-ready graphics on light or black background. It includes a
large number of colormaps collected from different sources. There are
a number of functions that help to position plots, number plot panels,
or write text on a graph.

The complete documentation of ``mcplot`` is available at:

   https://mcuntz.github.io/mcplot/


Installation
------------

The easiest way to install is via `pip`:

.. code-block:: bash

   python -m pip install mcplot

or via `conda`:

.. code-block:: bash

   conda install -c conda-forge mcplot

Requirements
   * numpy_
   * matplotlib_
   * pandas_


Calling a plotting script from the command line
-----------------------------------------------

``mcplot`` provides a class that has methods for opening and closing
different plotting backends, setting layout options, as well as having
a command line interface. A most basic example is using the method
`plot_test`, which just plots two sinusoidal curves. A file
`mcplot_test.py` could be:

.. code-block:: python

   # file: mcplot_test.py
   from mcplot import mcPlot

   if __name__ == '__main__':
       iplot = mcPlot(desc='Test mcPlot',
                      argstr='No argument wanted')
       iplot.plot_test()
       iplot.close()

This script `mcplot_test.py` can be called on the command line. '-h'
gives a short help:

.. code-block:: bash

   python mcplot_test.py -h

gives the help message::

   usage: mcplot_test.py [-h] [-o plotname] [-s] [-t outtype] [-u]
                         [-w] [--dpi number] [--transparent] [args ...]

   Test mcPlot

   positional arguments:
     args                  No argument wanted

   options:
     -h, --help            show this help message and exit
     -o plot_filename, --output plot_filename,
     -p plot_filename, --plotname plot_filename
                           Name of plot output file for types pdf, html,
			   d3, or hvplot, and name basis for type png
			   (default: class_mcplot).
     -s, --serif           Use serif font; default sans serif.
     -t outtype, --type outtype
                           Output type is pdf, png, html, d3, or hvplot
                           (default: open screen windows).
     -u, --usetex          Use LaTeX to render text in pdf, png and html.
     -w, --white           White lines on transparent or black background;
                           default: black lines on transparent or
                           white background.
     --dpi number          Dots Per Inch (DPI) for non-vector output types or
                           rasterized maps in vector output (default: 300).
     --transparent         Transparent figure background
                           (default: black or white).
     --font name           Font name or LaTeX package name
                           (default: DejaVuSans or DejaVuSerif (serif) and
			   MyriadPro or ComputerModern (serif) if --usetex


.. code-block:: bash

   python mcplot_test.py

opens a standard Matplotlib plotting window with the test plot.
   
.. code-block:: bash

   python mcplot_test.py -t pdf -o test1.pdf

writes the plot into the PDF file `test1.pdf` using the sans-serif
font `DejaVuSans` that comes with Matplotlib. It will use the serif
font DejaVueSerif with the command line option `-s`. It will use LaTeX
to render text with the `-u` option. `-u -s` uses LaTeX's standard
Computer Modern font. It uses MyriadPro as sans-serif font in LaTeX,
which must be installed (see section `Myriad Pro`_).

By default, ``mcPlot`` plots onto a DIN A4 page, which facilitates
choices of font sizes, etc. The output can easily be cropped with the
utility pdfcrop_ which can be acquired from CTAN_. The standard
subplots are on a 2x3 grid. The plot will be tightly cropped if the
output type is `png`. Plot resolution can be set for `png` as well
(`--dpi`) with standard being 300 dpi. PNG plots can have transparent
background (`--transparent`), for example to use in presentations.

The command line switch `-w` swaps foreground and backgroud colors,
i.e. uses white lines on black background. This is used if you do
presentations with black background.

In summary, the standard command line options allow to use the same
script to design a plot using plotting windows on screen, produce the
publication ready plots in a PDF file (`-t`, `-o`, `-u` options), and
make the same plot with dark background for presentations (`-t`, `-o`,
`-u`, `-w` options).


Using the plotting class
------------------------

The class `mcPlot` can be extended. One normally would have at least a
method to read data from a file and a method that produces a
plot. This could give a script such as:

.. code-block:: python

   # file: mcplot_basic.py
   import numpy as np
   from mcplot import mcPlot


   class myPlot(mcPlot):

       def read_data(self):
           # reading one file would use self.cargs[0] such as
           # self.dat = np.loadtxt(self.cargs[0])
           self.dat = np.arange(100)

       def plot_fig_1(self):
           import matplotlib.pyplot as plt

           # make axes
           fig = plt.figure()
           ax = fig.add_subplot(3, 2, 1)

           # plot
           xx = self.dat / self.dat.size * 4. * np.pi
           line1 = ax.plot(xx, np.sin(xx))
           plt.setp(line1, linestyle='-', linewidth=self.lw,
                    marker='', color=self.lcol1)

           # show plot or write in file
           self.plot_save(fig)


   if __name__ == '__main__':
       # open plot
       iplot = myPlot(desc='A basic plot')
       # read data
       iplot.read_data()
       # plot
       iplot.plot_fig_1()
       # close plot and possible output file
       iplot.close()

The script could be called giving the name(s) of (an) input file(s) on
the command line, which is then accessible through `self.cargs`:

.. code-block:: bash

   python mcplot_basic.py -t png -o basic. input.csv

Every time `self.plot_save(fig)` is called, a figure is written to the
output file. A PDF file can have multiple pages. For PNG files, only
the start of the output files is given (here *basic.*) and will be
extended by `f'{start}{self.ifig:04d}.png'`. The example would give
the outputfile `basic.0001.png`.

See the complete documentation of ``mcplot`` at: https://mcuntz.github.io/mcplot/


License
-------

``mcplot`` is distributed under the MIT License. See the LICENSE_ file
for details.

Copyright (c) 2021- Matthias Cuntz


.. |DOI| image:: https://zenodo.org/badge/866240152.svg
   :target: https://doi.org/10.5281/zenodo.13893825
.. |PyPI version| image:: https://badge.fury.io/py/mcplot.svg
   :target: https://badge.fury.io/py/mcplot
.. |Conda version| image:: https://anaconda.org/conda-forge/mcplot/badges/version.svg
   :target: https://anaconda.org/conda-forge/mcplot
.. |License| image:: http://img.shields.io/badge/license-MIT-blue.svg?style=flat
   :target: https://github.com/mcuntz/mcplot/blob/master/LICENSE
.. |Build Status| image:: https://github.com/mcuntz/mcplot/actions/workflows/main.yml/badge.svg
   :target: https://github.com/mcuntz/mcplot/actions/workflows/main.yml
.. |Coverage Status| image:: https://coveralls.io/repos/github/mcuntz/mcplot/badge.svg?branch=main
   :target: https://coveralls.io/github/mcuntz/mcplot?branch=main

.. _CTAN: https://www.ctan.org/pkg/pdfcrop
.. _LICENSE: https://github.com/mcuntz/mcplot/blob/main/LICENSE
.. _Myriad Pro: https://github.com/mcuntz/setup_mac?tab=readme-ov-file#myriad-pro
.. _matplotlib: https://matplotlib.org/
.. _netCDF4: https://github.com/Unidata/netcdf4-python
.. _numpy: https://numpy.org/
.. _pandas: https://pandas.pydata.org/
.. _pdfcrop: https://github.com/ho-tex/pdfcrop
