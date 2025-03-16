Userguide
=========

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

   # file: mcplot_test.py
   from mcplot import mcPlot

   if __name__ == '__main__':
       # make instance of mcPlot
       iplot = mcPlot(desc='Test mcPlot',
                      argstr='No argument wanted')
       # simple test plot with two sinusoidals
       iplot.plot_test()
       # finish
       iplot.close()

This script **mcplot_test.py** can be called on the command line. Just
calling the script opens a standard `Matplotlib`_ plotting window with
the test plot.

.. code-block:: bash

   python mcplot_test.py

Adding the command line option **-h** gives a short usage note:

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
     --dpi number          Dots Per inch (DPI) for non-vector output types or
                           rasterized maps in vector output (default: 300).
     --transparent         Transparent figure background
                           (default: black or white).
     --font name           Font name or LaTeX package name
                           (default: DejaVuSans or DejaVuSerif (serif) and
			   MyriadPro or ComputerModern (serif) if --usetex

Thus, the command line option **-t pdf** would write the plot into a
PDF file. The option **-o test1.pdf** would write it into the file named
**test1.pdf**:

.. code-block:: bash

   python mcplot_test.py -t pdf -o test1.pdf

This uses the sans-serif font **DejaVu Sans**, which is the standard
font of `Matplotlib`_. :class:`~mcplot.class_mcplot.mcPlot` will use
the serif font **DejaVue Serif** with the command line option
**-s**. It will use LaTeX to render text with the **-u** option (see
`Text rendering with LaTeX`_). **-u -s** uses LaTeX standard Computer
Modern font. It uses **MyriadPro** as sans-serif font in LaTeX, which
must be installed separately (see section `Myriad Pro`_ here). One can
chose the font with the **--font** option.

.. code-block:: python

   import matplotlib as mpl
   mpl.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')

prints all fonts available to Matplotlib. :mod:`mcplot` supports the
following LaTeX sans serif fonts with **-u**: **FiraSans**,
**Helvetica**, **Iwona**, **Kurier**, **Lato**, **MyriadPro**, and
**OpenSans**, or any other font that can be loaded in LaTeX with
`\usepackage{fontname}`. The respective LaTeX packages must be
installed. **FiraSans** is a good alternative to **MyriadPro** if the
latter is too difficult to install.

By default, ``mcPlot`` plots onto a DIN A4 page, which facilitates
choices of font sizes, etc. The output can be cropped with the utility
pdfcrop_ which can be acquired from CTAN_. The plot will be tightly
cropped if the output type is **png**. Plot resolution can be set for
**png** or rasterized maps in **pdf** (**--dpi**) with standard 300
dpi. PNG plots can also have transparent background
(**--transparent**), for example for use in presentations. Note that
**figsize** is reduced by 10/12 (ca. 80%) for on screen windows to fit
on laptop screens. If you are developing the plot on screen and the
final figure in PNG or PDF should have a textsize of 12 pt, it should
be developed on screen with 10 pt.

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
**-o**, **-u**), and make the same plot with dark background for
presentations (options **-t**, **-o**, **-u**, **-w**).


Extending the plotting class
----------------------------

The class :class:`~mcplot.class_mcplot.mcPlot` shall be extended. One
would normally have a method to read data from a file, and a routine
that produces a plot. This could give a script like
**mcplot_basic.py**:

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
           self.ifig += 1
           fig = plt.figure(self.ifig)
           ax = fig.add_subplot(3, 2, 1)

           # plot
           xx = self.dat / float(self.dat.size) * 4. * np.pi
           larr = ax.plot(xx, np.sin(xx))
           plt.setp(larr[-1], linestyle='-', linewidth=self.lw,
                    marker='', color=self.lcol1)

           # show plot or write in file
           self.plot_save(fig)

       def plot_fig_2(self):
           import matplotlib.pyplot as plt

           self.ifig += 1
           fig = plt.figure(self.ifig)
           ax = fig.add_subplot(3, 2, 1)

           xx = self.dat / float(self.dat.size) * 4. * np.pi
           larr = ax.plot(xx, np.cos(xx))
           plt.setp(larr[-1], linestyle='-', linewidth=self.lw,
                    marker='', color=self.lcol2)

           self.plot_save(fig)


   if __name__ == '__main__':
       # open plot
       iplot = myPlot(desc='Pass file to mcPlot',
                      argstr='input_file')
       # read data
       iplot.read_data()
       # plot two figures
       iplot.plot_fig_1()
       iplot.plot_fig_2()
       # close plot and possible output file
       iplot.close()

The class :class:`~mcplot.class_mcplot.mcPlot` is extended by the
methods :meth:`read_data`, :meth:`plot_fig_1`, and
:meth:`plot_fig_2`. In the main section, an instance of the extended
class :class:`myPlot` is created, which prepares also any plotting
backend such as a Matplotlib window or a PDF file. The data is read
with the method :meth:`read_data`, which could also be called directly
in :meth:`__init__`. Two figures are created in the methods
:meth:`plot_fig_1` and :meth:`plot_fig_2`, which write the figures to
the backend with the method `plot_save(fig)`. Any open backend
such as a PDF file will be closed with the method :meth:`close`.

The script could be called giving the name of an input file
**input.csv** on the command line, which is then accessible through
**self.cargs**:

.. code-block:: bash

   python mcplot_basic.py -t png -o basic_ input.csv

Everytime **self.plot_save(fig)** is called, a figure is written to
the output file. A PDF file can have multiple pages. PNG files are
individual plots. Only the start of the output files is
hence given for PNG files and this start will be extended as
**f'{start}{self.ifig:04d}.png'**. The example would give the output
files **basic_0001.png** and **basic_0002.png**.


Class variables
---------------

The plotting methods :meth:`plot_fig_1` and :meth:`plot_fig_2` above
use the defined variables **self.lcol1** for line color number 1,
**self.lcol2** for line color number 2, and **self.lw** for the
width of the plotted line.

The are a large number of useful class variables defined, see
:meth:`~mcplot.class_mcplot.mcPlot.set_layout_options`. They can be
used in all plot methods such as different plotting functions to make
plots having the same appearance.

**Lines and markers**

* There are five line colors defined: **lcol1** to **lcol5** (dark
  blue, dark red, light blue, orange, dark green); the same for
  markers: **mcol1** to **mcol5**.
* The are two lists **lcols** and **mcols** with 13 colors (dark blue,
  medium blue, light blue, cyan, turquoise, light green, dark green,
  sand, beige, yellow, orange, light red, dark red), which uses
  :mod:`mcplot`'s own colormap, which is a toned down version of
  `amwg` from `NCAR`_'s `Atmosphere Model Working Group`_ available in
  `NCL`_, for example.
* The foreground color (**fgcolor**) is set to black, and the
  background color (**bgcolor**) is set to white. This is inverted
  with the **-w** command line option, which sets the variable
  **self.dowhite**.
* Linewidth of a plotting line (**lw**) is set to 1.5 while widths
  of axes (**alw**) and errorbars (**elw**) are set to 1.
* Marker size (**msize**) is set to 1.5 while the width of the marker
  edge (**mew**) is set to 1.
* **ldashes** gives seven dash sequences (solid, dashed,
  dash-dot-dash, dash-dot-dot-dash, ...).

**Text**

* Textsize (**textsize**) is set to 12 pt, which works well together
  with the assumed DIN A4 paper size.
* The command line option **-s** sets the variable **self.serif** to
  True and a serif ouput font is used.
* The command line option **-u** sets the variable **self.usetex** to
  True, which can be used with any text in Matplotlib. It then uses
  LaTeX for all text handling. One can also use the function
  :func:`~mcplot.str2tex.str2tex` for automatic conversion of any text
  string to its LaTeX equivalent.
* **dxabc** and **dyabc** are used to place a), b), c), ... on the
  plot using :func:`~mcplot.text2plot.abc2plot`. These are 0-1 between
  axis minimum and maximum. They are set to 0.05 and 0.9,
  resp., i.e. default is the upper left corner.

**Plot layout**

The module :mod:`mcplot` includes a function
:func:`~mcplot.position.position` that is similar to
:class:`matplotlib.gridspec.GridSpec` but is used with
:meth:`matplotlib.figure.Figure.add_axes`. It returns the tuple
`(left, bottom, width, height)` for subplots with
:meth:`~matplotlib.figure.Figure.add_axes`.

* **nrow** is set to 3 by default and **ncol** to 2, which gives six
  plotting panels on a DIN A4 page, which has a ratio between 3/2 and
  4/3.
* The further class variables **left** (0.125), **right** (0.9),
  **bottom** (0.11), **top** (0.88), **hspace** (0.1), and **vspace**
  (0.1) are fractions of the figure width and height and the same as
  the current defaults of :class:`matplotlib.gridspec.GridSpec`
  (Matplotlib v3.9), except for **hspace** and **vspace**, which are
  half the corresponding GridSpec values (`wspace` and `hspace`,
  resp.). **hspace** and **vspace** are abbreviations for `horizontal
  space` and `vertical space` between subplots, which is more mnemonic
  for me than `wspace` for `width reserved for space between subplots`
  and `hspace` for `height reserved for space between subplots` in
  :class:`~matplotlib.gridspec.GridSpec`.
* It is good practice to increase the figure counter **ifig** if
  opening a new figure.

**Legend**

There are class variables for some of the main keywords of
:meth:`matplotlib.axes.Axes.legend` with defaults adapted for a
tighter layout:

* The length of lines in the legend (**handlelength**) is set to 1.5,
  and the padding to the text (**handletextpad**) is set to 0.4.
* The vertical space between label rows (**labelspacing**) is set to
  0, and the horizontal space between label columns
  (**columnspacing**) is set to 1.
* **frameon** for the frame around the legend is set to False.
* **loc** is set to 'upper right'. **xbbox** and **ybbox**, to be
  used with `bbox_to_anchor`, and are set to 1.0 so that the legend is
  in the upper right corner with these defaults.

**Savefig**

Some keywords of :meth:`matplotlib.figure.Figure.savefig` are given as
class variables:

* The command line options **--dpi** and **--transparent** set the
  equivalent keywords in
  :meth:`~matplotlib.figure.Figure.savefig`. They are 300 and False by
  default, respectively.
* **bbox_inches** is set to 'tight' with a very small padding
  **pad_inches** of 0.035.

After fiddling with any of the class variables, it is a good idea to
call **set_matplotlib_rcparams()** again (see example below), which
sets some defaults such as setting the color of the boxplot whiskers
to the foreground colour, of which one might not have thought
themselves.

.. code-block:: python

   # file: mcplot_variables.py
   from mcplot import mcPlot


   class myPlot(mcPlot):

       def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           # Set some user-defined layout options overwriting the defaults
           self.set_extra_layout_options()
           # It is a good idea to update the rcParams as well then.
           self.set_matplotlib_rcparams()

       def set_extra_layout_options(self):
           """
           Set some class variables that can be used for plotting.

           """
           from mcplot.color import get_cmap, get_color

           # Set layout and spaces
           self.nrow = 2       # # of rows of subplots per figure
           self.ncol = 1       # # of columns of subplots per figure
           self.hspace = 0.09  # x-space between subplots
           self.vspace = 0.04  # y-space between subplots
           self.textsize = 20  # standard text size
           if self.usetex:
               self.font = 'Fira'

           # Set come line and marker properties
           self.lw = 3.5   # linewidth
           self.ms = 5.0   # marker size
           self.mew = 0.3  # marker edge width

           # Set come colors
           if self.dowhite:
               # delete starting white, black, and pink from palette
               self.mcols = get_cmap('ncl_amwg')[3:]
           else:
               # delete starting white, black, and pink from palette
               self.mcols = get_cmap('mcplot_amwg')[3:]
           self.mcol1 = self.fgcolor       # black or white
           self.mcol2 = self.mcols[-1]     # red
           self.mcol3 = get_color('grey')  # grey
           self.mcol4 = self.mcols[2]      # light blue
           self.mcol5 = self.mcols[-3]     # orange
           self.lcol1 = self.mcol1
           self.lcol2 = self.mcol2
           self.lcol3 = self.mcol3
           self.lcol4 = self.mcol4
           self.lcol5 = self.mcol5
           self.lcols = self.mcols

           # Set legend properties
           self.loc = 'upper left'
           self.xbbox = 0.  # x-data of corner of self.loc
           self.ybbox = 1.  # y-data of corner of self.loc
           self.labelspacing  = 0.2  # spacing between rows in legend
           self.columnspacing = 1.   # spacing between columns in legend
           self.handletextpad = 0.4  # pad between the legend handle and text
           self.handlelength  = 1.0  # length of the legend handles


   if __name__ == '__main__':
       iplot = myPlot(desc='Change some class variables')
       iplot.plot_test()
       iplot.close()


More command line options
-------------------------

You can replace the method
:meth:`~mcplot.class_mcplot.mcPlot.get_command_line_arguments` of
:class:`~mcplot.class_mcplot.mcPlot` with your own method if you want
completely different command line arguments. Or you can extend the
existing arguments using the `parents`_ keyword to Python's
:class:`argparse.ArgumentParser`. For the latter, you create an
:class:`~argpase.ArgumentParser` with the extra arguments you want and
then parse it to :class:`~mcplot.class_mcplot.mcPlot` with the
**parents** keyword:

.. code-block:: python

   if __name__ == '__main__':
       import argparse

       desc = 'Example to add missing value command line argument'
       argstr = 'input_file'

       parser = argparse.ArgumentParser(add_help=False)

       miss = -9999.
       parser.add_argument('-m', '--missing', action='store',
                           default=miss, dest='miss', type=float,
                           metavar='missing_value',
                           help=(f'Data treated as missing value in'
                                 f' input file (default: {miss}).'))

       iplot = myPlot(desc, argstr, parents=parser)

       iplot.read_data()
       iplot.plot_fig_1()
       iplot.plot_fig_2()
       iplot.close()

You have to set **add_help=False** in the instance of
:class:`argpase.ArgumentParser` because otherwise
:class:`~argpase.ArgumentParser` will see two **-h/--help** options
and raise an error.

An extended and commented example is given in :doc:`Commented Example
<full_example>`, which uses most of the class and functions of
:mod:`mcplot`.


.. _Atmosphere Model Working Group: https://www.cesm.ucar.edu/working-groups/atmosphere
.. _CTAN: https://www.ctan.org/pkg/pdfcrop
.. _LICENSE: https://github.com/mcuntz/mcplot/blob/main/LICENSE
.. _Matplotlib: https://matplotlib.org/
.. _Myriad Pro: https://github.com/mcuntz/setup_mac?tab=readme-ov-file#myriad-pro
.. _NCAR: https://ncar.ucar.edu
.. _NCL: https://www.ncl.ucar.edu
.. _Text rendering with LaTeX: https://matplotlib.org/stable/users/explain/text/usetex.html#usetex
.. _matplotlib: https://matplotlib.org/
.. _netCDF4: https://github.com/Unidata/netcdf4-python
.. _numpy: https://numpy.org/
.. _parents: https://docs.python.org/3/library/argparse.html#parents
.. _pdfcrop: https://github.com/ho-tex/pdfcrop
