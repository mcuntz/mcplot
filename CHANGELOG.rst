Changelog
---------

v2.2 (May 2025)
   - Added option `cli` to bypass command line if False, e.g. if class
     initiated from within Python. Supersedes old logic that bypassed
     the command line if no desc or argstr was given.
   - Cleaner commented example in documentation.
   - Documentation of font option.
   - Documentation of colors and color palettes.

v2.1 (Mar 2025)
   - Add font option.
   - Add Stuart Semple's Freetone colors.
   - Changed build and coverage status to main branch.
   - Slight amendments to documentation. 

v2.0 (Nov 2024)
   - Tighter layout in `show_colors` and tight bounding box for
     non-pdf output of `show_colors` and `show_cmaps`.
   - Use class variables in test plot of `mcPlot`.
   - Pass italic and bold along to `str2tex` in `text2plot`.
   - Put $...$ around a, b, c only if mathrm=True in `abc2plot`.
   - Use backslash with braces only if `usetex` not if only pdf
     output in `abc2plot`.  * Removed trailing > in html output.
   - Add sron named colors.
   - Add pale and dark colors to sron_colors.
   - Use helper functions for all colors and colormaps.
   - Order Matplotlib colormaps into categories.
   - Use named colors from `matplotlib.colors` rather than
     `plt.cm.colors`.
   - Add `color_palette` = `get_cmap` to have a very similar function
     as seaborn.
   - Add alias `get_palette` = `get_cmap`, `print_palettes` =
     `print_cmaps`, `show_palettes` = `show_cmaps` to have both
     notations, `Matplotlib` and `seaborn`, respectively.
   - Added `show_colors` to plot known named colors.
   - Directly use color dictionaries in `get_cmap`, `get_color`,
     `print_colors`, and `print_palettes`.
   - Print named colors using predefined dictionaries.
   - Rename `print_layout_options` to `print_class_variables`,
     using `self.__dict__` to access all variables.
   - Remove `desc`, `argstr`, and `parents` keyword arguments from
     `get_command_line_arguments` to not interfere with possible
     child method.
   - If nor `desc` nor `argstr` given, the command line will be
     bypassed in order to use the class `mcPlot` without the command
     line from within Python.
   - Use 10/12 instead of 4/5 to reduce figsize on screen windows.
   - Also `-o` and `--output` for `-p output_plot_filename` possible.
   - Prefix IPCC colors with ipcc:.
   - Use : instead of _ in colormap names.
   - Start Brewer colors after Matplotlib colors at new page in
     `show_palettes`.
   - Renamed file `mcplot.py` to `class_mcplot.py`.
   - Change class variables `lwidth` to `lw`, `alwidth` to `alw`,
     `elwidth` to `elw`, `msize` to `ms`, `mwidth` to `mew` in
     `mcPlot`.
   - Added `loc` and set `xbbox` and `ybbox` in `mcPlot` so that
     legend is in upper right corner.
   - Change `llxbbox` to `xbbox`, `llybbox` to `ybbox`, `llrspace` to
     `labelspacing`, `llcspace` to names of Matplotlib's `Axes.legend`.
   - Reorder `ldashes` from little to more dots between dashes.
   - Set `dxabc` and `dyabc` to upper left corner of plot in
     `mcPlot`.
   - Use same left, right, bottom, top as GridSpec of Matplotlib in
     `mcPlot`.

v1.0 (Oct 2024)
   - First standalone release of ``mplot``, extracting all plotting
     routines from ``pyjams``.
   - Rudimentary documentation with README.rst.

v0.18 (Aug 2024)
   - Argument 'parents' to `mcPlot` to pass extra command line
     arguments.
   - Added upper keyword in `abc2plot`.
   - Use DejaVuSans and DejaVueSerif as standard fonts if not LaTeX
     in `mcPlot`.
   - Add `mcPlot` method `print_layout_options`.
   - Added IPCC WG1 colors.
   - Set default options for `mcPlot` if not given on command line.

v0.17 (Jun 2023)
   - Set filename without suffix as default plot name in `mcPlot`.
   - Allow ncol=1 in `color.get_cmap`.

v0.16 (May 2023)
   - Replace plotly with hvplot in `mcPlot`.
   - Add unicode symbol degree \u00B0, which gets replaced by ^\circ
     if usetex==True in str2tex.
   - Do not escape % if not usetex in str2tex.

v0.15 (Jan 2023)
   - Do not set color for missing data; only existed for sron palettes.
   - Add --dpi as a standard option in `mcPlot`.
   - Use mpl.colormaps[name] instead of mpl.colormaps.get_cmap(name)
     to replace mpl.cm.get_cmap(name) to work with matplotlib < v3.6.

v0.14 (Dec 2022)
   - Changed matplotlib.cm.get_cmap to matplotlib.colormaps.get_cmap in
     color module and tests.

v0.13 (Jul 2022)
   - Add left, bottom, top to standard layout options in `mcPlot`.
   - Documented as_cmap keyword of `get_cmap`.

v0.12 (Jun 2022)
   - Use I/O type helpers in `str2tex`.
   - Add kwargs mechanism to `plot_save` in `mcPlot` to pass arguments
     to save_file.
   - Add --transparent as a standard option in `mcPlot`.

v0.11 (May 2022)
   - Change from NCL amwg to pyjams amwg as the default color palette in
     `mcPlot`.

v0.10 (Apr 2022)
   - Added `pyjams_amwg` color map.
   - `get_color` can get list of colors and not only single colors.
   - Register ufz colors only once with `get_color`.
   - Add `print_colors` to print known named colors to console.

v0.9 (Mar 2022)
   - Add `get_color` to get value of named colors known to Matplotlib.
   - Added named colors of the guidelines of the Helmholtz Centre for
     Environmental Research - UFZ, Leipzig, Germany.

v0.8 (Mar 2022)
   - Added 'order' keyword to `get_cmap`.

v0.7 (Dec 2021)
   - Changed order of color maps in printing and plotting.
   - Edited docstrings of color module to follow closer numpydoc.

v0.6 (Nov 2021)
   - Use `text2plot` in `abc2plot` and `signature2plot`.
   - Better handling of linebreaks in Matplotlib and LaTeX mode in `str2tex`.
   - Added `text2plot`, adding text onto a plot.
   - Added `int2roman` and `roman2int`, converting integer to and from
     Roman literals.
   - Combine `abc2plot` and `signature2plot` in one file `text2plot.py`.
   - Added `abc2plot`, adding a, B, iii), etc. onto a plot.
   - Added `signature2plot`, adding a copyright notice onto a plot.
   - Added 'pyjams_color.pdf' as reference to available colormaps.

v0.5 (Nov 2021)
   - Added tests for `color`.
   - Added 'pragma: no cover' to plot and MPI sections of codes so that they
     are not included in coverage report.
   - Cleaned mcPlot docstrings.
   - Added current colors of Paul Tol, i.e. sron color palettes.

v0.4 (Nov 2021)
   - Add `position`, which positions arrays of subplots to be used with
     Matplotlib's add_axes.

v0.3 (Nov 2021)
   - Write standard output file of mcPlot into current folder.
   - Add `str2tex`, converting strings to LaTeX strings
   - Added `color`, a collection of color palettes and continuous color maps.

v0.2 (Nov 2021)
   - Add `mcPlot`, the standard plotting class of Matthias Cuntz.
   - It currently assumes that MyriadPro is installed for LaTeX if one
     wants to typeset with latex (-u, --usetex). For installing MyriadPro
     on macOS see https://github.com/mcuntz/setup_mac#myriad-pro This
     should be similar on Linux.
   - There are no tests for mcPlot yet.

v0.1 (Oct 2021)
   - Create ``pyjams`` from routines of JAMS package
     https://github.com/mcuntz/jams_python
