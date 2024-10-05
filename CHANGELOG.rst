Changelog
---------

v1.0 (Oct 2024)
    * First standalone release of ``mplot``, extracting all plotting
      routines from ``pyjams``.
    * Rudimentary documentation with README.rst.

v0.18 (Aug 2024)
    * Argument 'parents' to `mcPlot` to pass extra command line
      arguments.
    * Added upper keyword in `abc2plot`.
    * Use DejaVuSans and DejaVueSerif as standard fonts if not LaTeX
      in `mcPlot`.
    * Add `mcPlot` method `print_layout_options`.
    * Added IPCC WG1 colours.
    * Set default options for `mcPlot` if not given on command line.

v0.17 (Jun 2023)
    * Set filename without suffix as default plot name in `mcPlot`.
    * Allow ncol=1 in `color.get_cmap`.

v0.16 (May 2023)
    * Replace plotly with hvplot in `mcPlot`.
    * Add unicode symbol degree \u00B0, which gets replaced by ^\circ
      if usetex==True in str2tex.
    * Do not escape % if not usetex in str2tex.

v0.15 (Jan 2023)
    * Do not set color for missing data; only existed for sron palettes.
    * Add --dpi as a standard option in `mcPlot`.
    * Use mpl.colormaps[name] instead of mpl.colormaps.get_cmap(name)
      to replace mpl.cm.get_cmap(name) to work with matplotlib < v3.6.

v0.14 (Dec 2022)
    * Changed matplotlib.cm.get_cmap to matplotlib.colormaps.get_cmap in
      color module and tests.

v0.13 (Jul 2022)
    * Add left, bottom, top to standard layout options in `mcPlot`.
    * Documented as_cmap keyword of `get_cmap`.

v0.12 (Jun 2022)
    * Use I/O type helpers in `str2tex`.
    * Add kwargs mechanism to `plot_save` in `mcPlot` to pass arguments
      to save_file.
    * Add --transparent as a standard option in `mcPlot`.

v0.11 (May 2022)
    * Change from NCL amwg to pyjams amwg as the default color palette in
      `mcPlot`.

v0.10 (Apr 2022)
    * Added `pyjams_amwg` color map.
    * `get_color` can get list of colors and not only single colors.
    * Register ufz colors only once with `get_color`.
    * Add `print_colors` to print known named colors to console.

v0.9 (Mar 2022)
    * Add `get_color` to get value of named colors known to Matplotlib.
    * Added named colors of the guidelines of the Helmholtz Centre for
      Environmental Research - UFZ, Leipzig, Germany.

v0.8 (Mar 2022)
    * Added 'order' keyword to `get_cmap`.

v0.7 (Dec 2021)
    * Changed order of color maps in printing and plotting.
    * Edited docstrings of color module to follow closer numpydoc.

v0.6 (Nov 2021)
    * Use `text2plot` in `abc2plot` and `signature2plot`.
    * Better handling of linebreaks in Matplotlib and LaTeX mode in `str2tex`.
    * Added `text2plot`, adding text onto a plot.
    * Added `int2roman` and `roman2int`, converting integer to and from
      Roman literals.
    * Combine `abc2plot` and `signature2plot` in one file `text2plot.py`.
    * Added `abc2plot`, adding a, B, iii), etc. onto a plot.
    * Added `signature2plot`, adding a copyright notice onto a plot.
    * Added 'pyjams_color.pdf' as reference to available colormaps.

v0.5 (Nov 2021)
    * Added tests for `color`.
    * Added 'pragma: no cover' to plot and MPI sections of codes so that they
      are not included in coverage report.
    * Cleaned mcPlot docstrings.
    * Added current colors of Paul Tol, i.e. sron color palettes.

v0.4 (Nov 2021)
    * Add `position`, which positions arrays of subplots to be used with
      Matplotlib's add_axes.

v0.3 (Nov 2021)
    * Write standard output file of mcPlot into current folder.
    * Add `str2tex`, converting strings to LaTeX strings
    * Added `color`, a collection of color palettes and continuous color maps.

v0.2 (Nov 2021)
    * Add `mcPlot`, the standard plotting class of Matthias Cuntz.
        - It currently assumes that MyriadPro is installed for LaTeX if one
          wants to typeset with latex (-u, --usetex). For installing MyriadPro
          on macOS see https://github.com/mcuntz/setup_mac#myriad-pro This
          should be similar on Linux.
        - There are no tests for mcPlot yet.

v0.1 (Oct 2021)
    * Create ``pyjams`` from routines of JAMS package
      https://github.com/mcuntz/jams_python
