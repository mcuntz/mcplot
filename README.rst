mcplot
======
..
  pandoc -f rst -o README.html -t html README.rst

A Python package with a plotting class and routines for publication-ready graphics.

|DOI| |PyPI version| |Conda version| |License| |Build Status| |Coverage Status|


About pyjams
------------

``mcplot`` provides a class that combines methods to easily produce
publication-ready graphics on light or black background. It includes a
large number of colormaps collected from different sources. And there are
a number of functions that help to position plots, number plot panels,
or generally write text on a graph.

The complete documentation of ``mcplot`` is available at:

   https://mcuntz.github.io/mcplot/


Installation
------------

The easiest way to install is via `pip`:

.. code-block:: bash

   pip install mcplot

or via `conda`:

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

.. |DOI| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.13851994.svg
   :target: https://doi.org/10.5281/zenodo.13851994
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

.. _LICENSE: https://github.com/mcuntz/mcplot/blob/main/LICENSE
.. _matplotlib: https://matplotlib.org/
.. _netCDF4: https://github.com/Unidata/netcdf4-python
.. _numpy: https://numpy.org/
