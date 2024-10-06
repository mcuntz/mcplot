mcplot guide
============

A Python package with a plotting class and routines for
publication-ready graphics.

|DOI| |PyPI version| |Conda version| |License| |Build Status| |Coverage Status|


About mcplot
------------

:mod:`mcplot` provides a class that combines methods to easily produce
publication-ready graphics on light or black background. It includes a
large number of colormaps collected from different sources. There are
a number of functions that help to position plots, number plot panels,
or generally write text on a graph.


Calling plotting scripts from the command line
----------------------------------------------

:mod:`mcplot` provides the class :class:`~mcplot.class_mcplot.mcPlot`
that has methods for opening and closing different plotting backends,
setting layout options, as well as having a command line interface. A
most basic example is using the method
:meth:`~mcplot.class_mcplot.mcPlot.plot_test`, which just plots two
sinusoidal curves as an example. A file **mcplot_test.py** could be:

.. code-block:: python

   from mcplot import mcPlot

   if __name__ == '__main__':
       iplot = mcPlot(desc='Test mcPlot',
                      argstr='No argument wanted')
       iplot.plot_test()
       iplot.close()

This script **mcplot_test.py** can be called on the command line.

Just calling the script opens a standard `Matplotlib`_ plotting window
with the test plot.

.. code-block:: bash

   python mcplot_test.py

Adding the command line option **-h** gives a short usage note:

.. code-block:: bash

   python mcplot_test.py -h

gives the help message::

   usage: mcplot_test.py [-h] [-p plotname] [-s] [-t outtype] [-u]
                         [-w] [--dpi number] [--transparent] [args ...]

   Test mcPlot

   positional arguments:
     args                  No argument wanted

   options:
     -h, --help            show this help message and exit
     -p plotname, --plotname plotname
                           Name of plot output file for types pdf, html, d3, or
                           hvplot, and name basis for type png (default: mcplot).
     -s, --serif           Use serif font; default sans serif.
     -t outtype, --type outtype
                           Output type is pdf, png, html, d3, or hvplot
                           (default: open screen windows).
     -u, --usetex          Use LaTeX to render text in pdf, png and html.
     -w, --white           White lines on transparent or black background;
                           default: black lines on transparent or
                           white background.
     --dpi number          Dots Per inch (DPI) for non-vector output types or
                           rasterized maps in vector output (default: 300).
     --transparent         Transparent figure background
                           (default: black or white).

Thus, the command line option **-t pdf** would write the plot into a
PDF file. The option '-p test1.pdf' would write it into the file named
**test1.pdf**:

.. code-block:: bash

   python mcplot_test.py -t pdf -p test1.pdf

This uses the sans-serif font **DejaVuSans** that comes with
`Matplotlib`_. It will use the serif font **DejaVueSerif** with the
command line option **-s**. It will use LaTeX to render text with the
**-u** option. **-u -s** uses LaTeX standard Computer Modern font. It
uses **MyriadPro** as sans-serif font in LaTeX, which must be
installed (see section `Myriad Pro`_).

By default, ``mcPlot`` plots onto a DIN A4 page, which facilitates
choices of font sizes, etc. The output can be cropped with the utility
pdfcrop_ which can be acquired from CTAN_. The plot will be tightly
cropped if the output type is **png**. Plot resolution can be set for
**png** or rasterized maps in **pdf** (**--dpi**) with standard 300
dpi. PNG plots can also have transparent background
(**--transparent**), for example for use in presentations.

The command line switch **-w** swaps foreground and backgroud colours,
i.e. it plots white lines on black background. This is used if you do
presentations with black background.

``mcplot`` reads all remaining strings on the command line into the
list **self.cargs**, which can be used to read input files, etc.

How to add your own options to the command line is explained in the
section `More command line options`_ below.

In summary, the standard command line options allow you to use the
same script to design a plot using plotting windows on screen, produce
the publication ready plot writing into a PDF file (options **-t**,
**-p**, **-u**), and make the same plot with dark background for
presentations (options **-t**, **-p**, **-u**, **-w**).


Extending the plotting class
----------------------------

The class :class:`~mcplot.class_mcplot.mcPlot` shall be extended. One
would normally have a method to read data from a file, and a routine
that produces a plot. This could give a script **mcplot_basic.py**:

.. code-block:: python

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
           self.ifig += 1
           fig = plt.figure(self.ifig)
           ax = fig.add_axes([0.125, 0.667, 0.3375, 0.233])

           # plot
           xx = self.dat / float(self.dat.size) * 4. * np.pi
           larr = ax.plot(xx, np.sin(xx))
           plt.setp(larr[-1], linestyle='-', linewidth=self.lwidth,
                    marker='', color=self.lcol1)

           # show plot or write in file
           self.plot_save(fig)

       def plot_fig_2(self):
           import matplotlib.pyplot as plt

           self.ifig += 1
           fig = plt.figure(self.ifig)
           ax = fig.add_axes([0.125, 0.667, 0.3375, 0.233])

           xx = self.dat / float(self.dat.size) * 4. * np.pi
           larr = ax.plot(xx, np.cos(xx))
           plt.setp(larr[-1], linestyle='-', linewidth=self.lwidth,
                    marker='', color=self.lcol2)

           self.plot_save(fig)

   if __name__ == '__main__':
       # open plot
       iplot = myPlot(desc='Pass file to mcPlot',
                      argstr='input_file')
       # read data
       iplot.read_data()
       # plot data
       iplot.plot_fig_1()
       iplot.plot_fig_2()
       # close plot and possible output file
       iplot.close()

The class :class:`~mcplot.class_mcplot.mcPlot` is extended by the
methods :meth:`read_data`, :meth:`plot_fig_1`, and
:meth:`plot_fig_2`. In the main section, an instance of the extended
class :class:`myPlot` is created, which prepares also any plotting
backend such as a Matplotlib window or a PDF file. The data is read
with the method :meth:`read_data`. Two figures are created in the
methods :meth:`plot_fig_1` and :meth:`plot_fig_2`, which write the
figures to the backend with the method :meth:`plot_save`. Any open
backend such as a PDF file will be closed with the method
:meth:`close`.

The plotting methods :meth:`plot_fig_1` and :meth:`plot_fig_2` use the
defined variables **self.lcol1** for line color number 1,
**self.lcol2** for line color number 2, and **self.lwidth** for the
width of the plotted line.

To be continued ...


There are **self.lcol1** to **self.lcol5** defined as well as
the list of colours **self.lcols** with standard 13 colours. This can
easily be changed using the **mcplot.color** sub-module. The above code
uses also **self.lwidth** for linewidth of the plotted line.

After fiddling with colours, it is a good idea to call
**set_matplotlib_rcparams()** again, which sets some defaults such as
the colour of the boxplot whiskers of which one might not have thought
themselves.

The script could be called giving the name of an input file **input.csv** on
the command line, which is then accessible through **self.cargs**:

.. code-block:: bash

   python mcplot_basic.py -t png -p basic_ input.csv

Everytime **self.plot_save(fig)** is called, a figure is written to the output file. A PDF file can have multiple pages. For PNG files, only the start of the output files is given and will be extended by **f'{start}{self.ifig:04d}.png'**. The example would give the outputfile **basic_0001.png**.


More command line options
-------------------------

You can replace the method
:meth:`~mcplot.class_mcplot.mcPlot.get_command_line_arguments` of
:class:`~mcplot.class_mcplot.mcPlot` with your own method if you want
completely different command line arguments. Or you can extend the
existing arguments using the `parents`_ keyword to Python's
:class:`argpase.ArgumentParser`. For the latter, you simply create an
:class:`~argpase.ArgumentParser` with the extra arguments you want and
then parse it to :class:`~mcplot.class_mcplot.mcPlot` with the
**parents** keyword:

.. code-block:: python

   if __name__ == '__main__':
       import argparse

       desc = 'Example to add missing value command line argument'
       argstr = 'input_file'

       parser = argparse.ArgumentParser(
           formatter_class=argparse.RawDescriptionHelpFormatter,
           add_help=False)
       miss = -9999.
       parser.add_argument('-m', '--missing', action='store',
                           default=miss, dest='miss', type=float,
                           metavar='missing_value',
                           help=(f'Data treated as missing value in
                                 f'input file (default: {miss}).'))

       iplot = PlotIt(desc, argstr, parents=parser)
       iplot.read_data()
       iplot.plot_fig_1()
       iplot.close()

You have to set **add_help=False** in the instance of
:class:`argpase.ArgumentParser` because otherwise :class:`~argpase.ArgumentParser`
will see two **-h/--help** options and raise an error.


Installation
------------

The easiest way to install is via **pip**:

.. code-block:: bash

   pip install mcplot

or via **conda**:

.. code-block:: bash

   conda install -c conda-forge mcplot


Requirements
   * numpy_
   * matplotlib_


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
.. |Build Status| image:: https://github.com/mcuntz/mcplot/workflows/Continuous%20Integration/badge.svg?branch=master
   :target: https://github.com/mcuntz/mcplot/actions
.. |Coverage Status| image:: https://coveralls.io/repos/github/mcuntz/mcplot/badge.svg?branch=master
   :target: https://coveralls.io/github/mcuntz/mcplot?branch=master

.. _CTAN: https://www.ctan.org/pkg/pdfcrop
.. _LICENSE: https://github.com/mcuntz/mcplot/blob/main/LICENSE
.. _Matplotlib: https://matplotlib.org/
.. _Myriad Pro: https://github.com/mcuntz/setup_mac?tab=readme-ov-file#myriad-pro
.. _matplotlib: https://matplotlib.org/
.. _netCDF4: https://github.com/Unidata/netcdf4-python
.. _numpy: https://numpy.org/
.. _parents: https://docs.python.org/3/library/argparse.html#parents
.. _pdfcrop: https://github.com/ho-tex/pdfcrop
