#!/usr/bin/env python
"""
Get, show, print color palettes

This module was written by Matthias Cuntz while at Institut National de
Recherche pour l'Agriculture, l'Alimentation et l'Environnement (INRAE), Nancy,
France.

:copyright: Copyright 2021- Matthias Cuntz, see AUTHORS.rst for details.
:license: MIT License, see LICENSE for details.

.. moduleauthor:: Matthias Cuntz

The following functions are provided:

.. autosummary::
   color_palette
   get_cmap
   get_color
   get_palette
   print_cmaps
   print_colors
   print_palettes
   show_cmaps
   show_colors
   show_palettes

History
   * Written Nov 2021, Matthias Cuntz
   * Change order of color maps, Dec 2021, Matthias Cuntz
   * More consistent docstrings, Jan 2022, Matthias Cuntz
   * Added 'order' keyword, Feb 2022, Matthias Cuntz
   * 'get_color', Mar 2022, Matthias Cuntz
   * 'cname' can be list of names in 'get_color', Apr 2022, Matthias Cuntz
   * Register ufz colors only once, Apr 2022, Matthias Cuntz
   * Added print_colors, Apr 2022, Matthias Cuntz
   * Use matplotlib.colormaps.get_cmap instead of deprecated
     matplotlib.cm.get_cmap, Dec 2022, Matthias Cuntz
   * Use matplotlib.colormaps[name] instead of
     matplotlib.colormaps.get_cmap(name) to work with matplotlib < v3.6,
     Jan 2023, Matthias Cuntz
   * Do not set_bad() for sron palettes, Jan 2023, Matthias Cuntz
   * Allow ncol=1 in get_cmap, Jun 2023, Matthias Cuntz
   * Added IPCC colors, Feb 2024, Matthias Cuntz
   * Use : instead of _ in colormap names, Oct 2024, Matthias Cuntz
   * Start Brewer colors after Matplotlib colors at new page in show_palettes,
     Oct 2024, Matthias Cuntz
   * Print named colors by using the predefined dictionaries,
     Oct 2024, Matthias Cuntz
   * Use color dictionaries directly in get_color, get_cmap, print_palettes,
     Oct 2024, Matthias Cuntz
   * Added show_colors, Oct 2024, Matthias Cuntz
   * Add alias get_palette = get_cmap, print_palettes = print_cmaps,
     show_palettes = show_cmaps, Oct 2024, Matthias Cuntz
   * Add alias color_palette = get_cmap as in seaborn, Oct 2024, Matthias Cuntz
   * Use named colors from matplotlib.colors rather than plt.cm.colors,
     Oct 2024, Matthias Cuntz
   * Only do case-insensitive search for cmaps of Matplotlib in get_cmap,
     Oct 2024, Matthias Cuntz
   * Order Matplotlib colormaps into categories, Oct 2024, Matthias Cuntz
   * Use helper functions _all_colors, _mpl_cmaps, and _all_cmaps,
     Oct 2024, Matthias Cuntz
   * Add sron_named_colors, Oct 2024, Matthias Cuntz
   * Tighter layout in show_colors, Nov 2024, Matthias Cuntz
   * Tight bounding box for non-pdf output of show_colors and show_cmaps,
     Nov 2024, Matthias Cuntz
   * Add freetone colors, Dec 2024, Matthias Cuntz

"""
import matplotlib as mpl
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from .brewer_palettes import (brewer_sequential, brewer_diverging,
                              brewer_qualitative)
from .freetone_palettes import freetone_colors
from .ipcc_palettes import (ipcc_categorical, ipcc_diverging,
                            ipcc_sequential)
from .mathematica_palettes import mathematica_rainbow
from .mcplot_palettes import mcplot_cmaps
from .ncl_palettes import ncl_large, ncl_small, ncl_meteo_swiss
from .oregon_palettes import (oregon_sequential, oregon_diverging,
                              oregon_qualitative)
from .sron2012_palettes import sron2012_colors, sron2012_functions
from .sron_palettes import sron_named_colors
from .sron_palettes import sron_colors, sron_colormaps, sron_functions
from .ufz_palettes import ufz_colors


__all__ = ['get_color', 'print_colors', 'show_colors',
           'get_cmap', 'print_cmaps', 'show_cmaps',
           'get_palette', 'print_palettes', 'show_palettes',
           'color_palette']


def _all_colors(collection=''):
    """
    Get all known named colors

    Parameters
    ----------
    collection : str or list of strings, optional
        Name(s) of color collection(s).
        Known collections are
        'base', 'css', 'freetone', 'sron', 'tableau', 'ufz', and 'xkcd'.

    Returns
    -------
    dict
        dict of dict. First keys: collection, 2nd keys: color names,
        values: colors

    Examples
    --------
    .. code-block:: python

       call = _all_colors(['tableau', 'ufz'])

    """
    if collection:
        if isinstance(collection, str):
            collects = [collection.lower()]
        else:
            collects = [ i.lower() for i in collection ]
    else:
        collects = ['base', 'tableau', 'sron', 'ufz', 'css', 'xkcd',
                    'freetone']

    dall = {}
    if 'base' in collects:
        dall.update({'base': mcolors.BASE_COLORS})
    if 'tableau' in collects:
        dall.update({'tableau': mcolors.TABLEAU_COLORS})
    if 'sron' in collects:
        dall.update({'sron': sron_named_colors})
    if 'ufz' in collects:
        dall.update({'ufz': ufz_colors})
    if 'css' in collects:
        dall.update({'css': mcolors.CSS4_COLORS})
    if 'xkcd' in collects:
        dall.update({'xkcd': mcolors.XKCD_COLORS})
    if 'freetone' in collects:
        dall.update({'freetone': freetone_colors})

    return dall


def _mpl_cmaps():
    """
    Get Matplotlib colormaps in categories of perception

    See
    https://matplotlib.org/stable/gallery/color/colormap_reference.html

    Returns
    -------
    dict
        dict of dict dict. First keys: categories, 2nd keys: colormap names,
        values: colors

    Examples
    --------
    .. code-block:: python

       cmaps = _mpl_cmaps()

    """
    mpl_palettes = {'perceptually uniform sequential':
                    ['viridis', 'plasma', 'inferno', 'magma', 'cividis'],
                    'sequential':
                    ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                     'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                     'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn',
                     'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone',
                     'pink', 'spring', 'summer', 'autumn', 'winter', 'cool',
                     'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper'],
                    'diverging':
                    ['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
                     'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr',
                     'seismic'],
                    'cyclic':
                    ['twilight', 'twilight_shifted', 'hsv'],
                    'qualitative':
                    ['Pastel1', 'Pastel2', 'Paired', 'Accent',
                     'Dark2', 'Set1', 'Set2', 'Set3',
                     'tab10', 'tab20', 'tab20b', 'tab20c'],
                    'miscellaneous':
                    ['flag', 'prism', 'ocean', 'gist_earth', 'terrain',
                     'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap',
                     'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet',
                     'turbo', 'nipy_spectral', 'gist_ncar']}

    mpl_cmaps = {}
    for pp in mpl_palettes:
        mpl_cmaps.update({pp: {}})
        for cc in mpl_palettes[pp]:
            cmap = mpl.colormaps[cc]
            try:
                colors = cmap.colors
            except AttributeError:
                colors = [ cmap(i) for i in range(cmap.N) ]
            mpl_cmaps[pp].update({cc: colors})

    return mpl_cmaps


def _all_cmaps(collection=''):
    """
    Get all known color palettes and continuous colormaps

    Parameters
    ----------
    collection : str or list of strings, optional
        Name(s) of color palette collection(s).
        Known collections are 'mcplot', 'sron', 'sron2012', 'mathematica',
        'oregon', 'ipcc', 'ncl', 'matplotlib', and 'brewer'.

    Returns
    -------
    dict
        dict of dict of dict. First keys: collection, 2nd keys: categories,
        3rd keys: colormap names, values: colors

    Examples
    --------
    .. code-block:: python

       cmaps = _all_cmaps(['mcplot', 'sron'])

    """
    if collection:
        if isinstance(collection, str):
            collects = [collection.lower()]
        else:
            collects = [ i.lower() for i in collection ]
    else:
        collects = ['mcplot', 'sron', 'sron2012', 'mathematica', 'oregon',
                    'ipcc', 'ncl', 'matplotlib', 'brewer']

    dall = {}
    if 'mcplot' in collects:
        dall.update({'mcplot': {'mcplot_cmaps': mcplot_cmaps}})
    if 'sron' in collects:
        dall.update({'sron': {'sron_colors': sron_colors,
                              'sron_colormaps': sron_colormaps,
                              'sron_functions': sron_functions}})
    if 'sron2012' in collects:
        dall.update({'sron2012': {'sron2012_colors': sron2012_colors,
                                  'sron2012_functions': sron2012_functions}})
    if 'mathematica' in collects:
        dall.update({'mathematica':
                     {'mathematica_rainbow': mathematica_rainbow}})
    if 'oregon' in collects:
        dall.update({'oregon_sequential':
                     {'oregon_sequential': oregon_sequential,
                      'oregon_diverging': oregon_diverging,
                      'oregon_qualitative': oregon_qualitative}})
    if 'ipcc' in collects:
        dall.update({'ipcc':
                     {'ipcc_categorical': ipcc_categorical,
                      'ipcc_diverging': ipcc_diverging,
                      'ipcc_sequential': ipcc_sequential}})
    if 'ncl' in collects:
        dall.update({'ncl':
                     {'ncl_small': ncl_small,
                      'ncl_large': ncl_large,
                      'ncl_meteo_swiss': ncl_meteo_swiss}})
    if 'matplotlib' in collects:
        dall.update({'matplotlib': _mpl_cmaps()})
    if 'brewer' in collects:
        dall.update({'brewer':
                     {'brewer_sequential': brewer_sequential,
                      'brewer_diverging': brewer_diverging,
                      'brewer_qualitative': brewer_qualitative}})

    return dall


def _rgb2rgb(col):
    """
    Transform RGB tuple with values 0-255 to tuple with values 0-1

    Parameters
    ----------
    col : iterable
        RGB tuple with values from 0-255

    Returns
    -------
    tuple
        RGB tuple with values from 0-1

    Examples
    --------
    .. code-block:: python

       col = (0, 126, 255)
       col = _rgb2rgb(col)

    """
    return tuple([ i / 255. for i in col ])


def _to_grey(col):
    """
    Transform RGB tuple to grey values

    Parameters
    ----------
    col : iterable
        RGB tuple

    Returns
    -------
    tuple
        RGB tuple with corresponding grey values

    Examples
    --------
    .. code-block:: python

       col = (0, 0.5, 1)
       col = _to_grey(col)

    """
    isgrey = 0.2125 * col[0] + 0.7154 * col[1] + 0.072 * col[2]
    return (isgrey, isgrey, isgrey)


def get_color(cname=''):
    """
    Return named color(s)

    Parameters
    ----------
    cname : str or iterable of str, optional
        Color name(s)

    Examples
    --------
    .. code-block:: python

       col1 = get_color('ufz:blue')
       col2 = get_color('xkcd:blue')
       cols = get_color(['blue', 'red'])

    """
    from collections.abc import Iterable

    call = _all_colors()
    dall = {}
    for cc in call:
        dall.update(call[cc])

    if cname:
        if isinstance(cname, Iterable) and (not isinstance(cname, str)):
            out = [ dall[i] for i in cname ]
            return out
        else:
            return dall[cname]


def print_colors(collection=''):
    """
    Print the known named colors

    Parameters
    ----------
    collection : str or list of strings, optional
        Name(s) of color collection(s).
        Known collections are
        'base', 'css', 'freetone', 'sron', 'tableau', 'ufz', and 'xkcd'.

    Returns
    -------
    None
        Prints list of known named colors to console.

    Examples
    --------
    .. code-block:: python

       print_colors()

    """
    dall = _all_colors(collection)

    for cc in dall:
        print('')
        print(cc)
        print('    ', sorted(list(dall[cc].keys())))


def get_cmap(palette, ncol=0, offset=0, upper=1,
             reverse=False, grey=False, order=None, as_cmap=False):
    """
    Get colors of defined palettes or continuous colormaps

    Parameters
    ----------
    palette : str
        Name of color palette or continuous colormap
    ncol : int, optional
        Number of desired colors.
        If 0, all colors defined by the specific palette will be returned.
        256 colors will be chosen for continuous colormaps.
        If > 0, existing color palettes will be subsampled to *ncol* colors.
        *ncol* colors will be produced from continuous colormaps.
    offset : float (0-1), optional
        Bottom fraction to exclude for subsample or continuous colormaps
    upper : float (0-1), optional
        Upper most fraction to include for subsample or continuous colormaps
    reverse : bool, optional
        Reverse colormap if True (default: False). This can also be achieved by
        adding '_r' to the palette name. Palettes that end with '_r' will not
        be reversed.
    grey : bool, optional
        Return grey equivalent colors if True (default: False).
    order : str, optional
        Order colors by 'hue', 'saturation', or 'value'.
        This is done before *reverse* and *grey*
        (default: order from color sources).
    as_cmap : bool, optional
        If True, returns matplotlib.colors.Colormap
        instead of list of RGB tuples

    Returns
    -------
    list or matplotlib.colors.Colormap
        List of RGB tuples or :class:`matplotlib.colors.Colormap`

    Notes
    -----
    `get_cmap` always returns a list of RGB tuples or a Matplotlib
    ListedColormap. You can use the *ncol*, *offset*, and *upper* keywords to
    subsample colormaps. To get smoothly-varying colormaps, you can use the
    method :meth:`matplotlib.colors.LinearSegmentedColormap.from_list`

       cols = get_cmap('sron:ylorbr')

       cmap = matplotlib.colors.LinearSegmentedColormap.from_list(cols)

    You can get the color tuples from a LinearSegmentedColormap like this

       colors = [ cmap(i) for i in range(cmap.N) ]

    Examples
    --------
    .. code-block:: python

       cols = get_cmap('mathematica:dark_rainbow_256', 15)

    """
    from mcplot import argsort

    # backwards compatibility - mcplot_amwg to mcplot:amwg
    palette_ = palette
    if ':' not in palette:
        palette = palette.replace('_', ':', 1)

    # _r at end of palette is same as reverse=True
    if palette.endswith('_r'):
        palette = palette[:-2]
        palette_ = palette_[:-2]
        reverse = True

    brewer_collects = {**brewer_sequential, **brewer_diverging,
                       **brewer_qualitative}  # concat dictionaries
    ipcc_collects = {**ipcc_categorical, **ipcc_diverging,
                     **ipcc_sequential}
    mathematica_collects = mathematica_rainbow
    mcplot_collects = mcplot_cmaps
    ncl_collects = {**ncl_large, **ncl_small, **ncl_meteo_swiss}
    oregon_collects = {**oregon_sequential, **oregon_diverging,
                       **oregon_qualitative}
    sron2012_collects = {**sron2012_colors, **sron2012_functions}
    sron_collects = {**sron_colors, **sron_colormaps, **sron_functions}

    found_palette = False
    nosubsample = False
    # miss = None

    # mcplot, mathematica, ncl
    simplepals = {**mcplot_collects, **mathematica_collects,
                  **ncl_collects}
    if not found_palette:
        if (palette in simplepals) or (palette_ in simplepals):
            found_palette = True
            if palette in simplepals:
                ipal = palette
            else:
                ipal = palette_
            colors = simplepals[ipal]

    # brewer, ipcc, oregon
    rgbpals = {**brewer_collects, **ipcc_collects, **oregon_collects}
    if not found_palette:
        if (palette in rgbpals) or (palette_ in rgbpals):
            found_palette = True
            if palette in rgbpals:
                ipal = palette
            else:
                ipal = palette_
            colors = [ _rgb2rgb(i) for i in rgbpals[ipal] ]

    # sron
    if not found_palette:
        if (palette in sron_collects) or (palette_ in sron_collects):
            found_palette = True
            if palette in sron_collects:
                ipal = palette
            else:
                ipal = palette_
            if ipal in sron_colors:
                colors = [ mcolors.colorConverter.to_rgb(i)
                           for i in sron_colors[ipal] ]
            elif ipal in sron_colormaps:
                colors = [ mcolors.colorConverter.to_rgb(i)
                           for i in sron_colormaps[ipal][0] ]
                # miss = mcolors.colorConverter.to_rgb(
                #            sron_functions[ipal][1])
            elif ipal in sron_functions:
                nosubsample = True
                if ncol == 0:
                    ncol1 = 23
                else:
                    ncol1 = ncol
                cols = sron_functions[ipal](ncol1)
                colors = [ mcolors.colorConverter.to_rgb(i)
                           for i in cols[0] ]
                # miss = mcolors.colorConverter.to_rgb(cols[1])

    # sron2012
    if not found_palette:
        if ( (palette in sron2012_collects) or
             (palette_ in sron2012_collects) ):
            found_palette = True
            if palette in sron2012_collects:
                ipal = palette
            else:
                ipal = palette_
            if ipal in sron2012_colors:
                colors = [ mcolors.colorConverter.to_rgb(i)
                           for i in sron2012_colors[ipal] ]
            elif ipal in sron2012_functions:
                nosubsample = True
                colors = []
                if ncol == 0:
                    ncol1 = 256
                else:
                    ncol1 = ncol
                for i in range(ncol1):
                    if ncol1 == 1:
                        x = offset
                    else:
                        x = (offset + float(i) / float(ncol1 - 1) *
                             (upper - offset))
                    colors.append(tuple(sron2012_functions[ipal](x)))

    # matplotlib
    if not found_palette:
        mplmaps = [ i for i in list(mpl.colormaps) if not i.endswith('_r') ]
        lmplmaps = [ i.lower() for i in mplmaps ]
        if (palette.lower() in lmplmaps) or (palette_.lower() in lmplmaps):
            if palette.lower() in lmplmaps:
                pal = palette
            else:
                pal = palette_
            found_palette = True
            ipalette = lmplmaps.index(pal.lower())
            cmap = mpl.colormaps[mplmaps[ipalette]]
            try:
                colors = cmap.colors
            except AttributeError:
                colors = [ cmap(i) for i in range(cmap.N) ]

    if not found_palette:
        raise ValueError(f'{palette} color palette not found.')

    if order is not None:
        hsv = ['hue', 'saturation', 'value']
        if order.lower() in hsv:
            oo = hsv.index(order.lower())
        else:
            raise ValueError('Sort order not known: ' + order)
        ii = argsort([ mcolors.rgb_to_hsv(cc)[oo]
                       for cc in colors ])
        colors = [ colors[i] for i in ii ]

    if reverse:
        colors = colors[::-1]

    if grey:
        colors = [ _to_grey(i) for i in colors ]

    # subsample
    if (ncol > 0) and not nosubsample:
        ncolors = len(colors)
        ocolors = [''] * ncol
        for i in range(ncol):
            if ncol == 1:
                x = offset
            else:
                # [0-1]
                x = offset + float(i) / float(ncol - 1) * (upper - offset)
            iicol = round(x * (ncolors - 1))  # [0-ncolor-1]
            ocolors[i] = colors[iicol]
        colors = ocolors

    if as_cmap:
        colors = mcolors.ListedColormap(colors)
        # if mpl.__version__ > '3.4.0':
        #     if miss is not None:
        #         colors.set_bad(miss)

    return colors


def color_palette(*args, **kwargs):
    """ Alias for get_cmap """
    return get_cmap(*args, **kwargs)


def get_palette(*args, **kwargs):
    """ Alias for get_cmap """
    return get_cmap(*args, **kwargs)


def print_cmaps(collection=''):
    """
    Print the known color palettes and continuous colormaps

    Parameters
    ----------
    collection : str or list of strings, optional
        Name(s) of color palette collection(s).
        Known collections are 'brewer', 'ipcc', 'mathematica', 'matplotlib',
        'mcplot', 'ncl', 'oregon', 'sron', and 'sron2012'.

    Returns
    -------
    None
        Prints list of known color palettes and continuous colormaps to
        console.

    Examples
    --------
    .. code-block:: python

       print_cmaps(collection=['mcplot', 'sron'])

    """
    dall = _all_cmaps(collection)

    for cc in dall:
        print('')
        print(cc)
        dd = dall[cc]
        for ii in dd:
            print('   ', ii)
            print('       ', list(dd[ii].keys()))


def print_palettes(*args, **kwargs):
    """ Alias for print_cmaps """
    return print_cmaps(*args, **kwargs)


#
# show colors and palettes
#

def _savefig(fig, ifig, outtype, outfile, pdf_pages):  # pragma: no cover
    """ Helper function for show_colors and show_palettes """
    if (outtype == 'pdf'):
        pdf_pages.savefig(fig)
        plt.close(fig)
    elif not (outtype == 'X'):
        ofile = (outfile[:outfile.rfind('.')] + '_' + '{:04d}'.format(ifig)
                 + '.' + outtype)
        fig.savefig(ofile, bbox_inches='tight', pad_inches=0.035)
        plt.close(fig)
    else:
        pass


def _newfig_colors(ifig, ititle, *,
                   cell_width_base=212,
                   cell_width=212, cell_height=22,
                   swatch_width=48, sidemargin=12,
                   topmargin=36,
                   ncols=37, nrows=4, dpi=72,
                   width=872, height=838,
                   textsize=10):  # pragma: no cover
    """ Helper function for show_colors """
    fig, ax = plt.subplots(num=ifig,
                           figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(sidemargin / width, topmargin / height,
                        (width - sidemargin) / width,
                        (height - topmargin) / height)
    ax.set_xlim(0, cell_width * ncols)
    ax.set_ylim(cell_height * (nrows - 0.5),
                -cell_height / 2.)

    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()

    fig.suptitle(ititle, fontsize=1.5 * textsize)

    return fig, ax


# https://matplotlib.org/stable/gallery/color/named_colors.html
def _plot_colors(ifig, table, colors, *, ncols=4, sort_colors=True,
                 textsize=10, outtype='X', outfile='', pdf_pages=None):
    """ Helper function for show_colors """
    from matplotlib.patches import Rectangle
    import math

    # n = len(colors)
    # nrows = math.ceil(n / ncols)
    nrowsmax = math.ceil(len(mcolors.CSS4_COLORS) / ncols)
    nrows = min(math.ceil(len(colors) / ncols), nrowsmax)
    cell_width_base = 212
    cell_height = 22
    swatch_width = 48
    sidemargin = 36
    topmargin = 48
    dpi = 72

    if table == 'base':
        cell_width = 89
    elif table == 'tableau':
        cell_width = 142
    elif table == 'sron':
        cell_width = 282
    elif table == 'ufz':
        cell_width = 159
    elif table == 'freetone':
        cell_width = 282
    else:
        cell_width = cell_width_base

    width = cell_width * ncols + 2 * sidemargin
    height = cell_height * nrows + 2 * topmargin

    ckw = {'cell_width_base': cell_width_base,
           'cell_width': cell_width,
           'cell_height': cell_height,
           'swatch_width': swatch_width,
           'sidemargin': sidemargin,
           'topmargin': topmargin,
           'ncols': ncols,
           'nrows': nrows,
           'dpi': dpi,
           'height': height,
           'width': width,
           'textsize': textsize}

    # Sort colors by hue, saturation, value and name.
    if sort_colors is True:
        if table == 'ufz':
            names = sorted(
                colors, key=lambda c:
                tuple(mcolors.rgb_to_hsv(colors[c])))
        elif table == 'freetone':
            # freetone has his own sorting
            names = colors
        elif table == 'sron':
            # do not sort but keep in categories,
            # which are already sorted by hue (or luminance for high-
            # and medium-contrast)
            names = list(colors)
        else:
            names = sorted(
                colors, key=lambda c:
                tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(c))))
    else:
        names = list(colors)

    nplots = nrows * ncols
    nnames = len(names)
    for i, name in enumerate(names):
        row = i % nrows
        col = (i // nrows) % ncols
        if (row == 0) and (col == 0):
            ifig += 1
            fig, ax = _newfig_colors(ifig, table, **ckw)
        y = row * cell_height

        swatch_start_x = cell_width * col
        text_pos_x = cell_width * col + swatch_width + 7

        ax.text(text_pos_x, y, name, fontsize=textsize,
                horizontalalignment='left',
                verticalalignment='center')

        ax.add_patch(
            Rectangle(xy=(swatch_start_x, y - 9), width=swatch_width,
                      height=18, facecolor=colors[name], edgecolor='0.7')
        )

        if (i == (nnames - 1)) or (((i + 1) % nplots) == 0):
            _savefig(fig, ifig, outtype, outfile, pdf_pages)

    return ifig


def show_colors(outfile='', collection=''):
    """
    Show the known named colors

    Parameters
    ----------
    outfile : str, optional
        Output file name. Output type will be determined from file suffix.
    collection : str or list of strings, optional
        Name(s) of color collection(s).
        Known collections are
        'base', 'css', 'freetone', 'sron', 'tableau', 'ufz', and 'xkcd'.

    Returns
    -------
    None
        Plots known names colors in file or on plotting window.

    Examples
    --------
    .. code-block:: python

       show_colors(outfile='mcplot_colors.pdf',
                   collection=['ufz', 'tableau'])

    """
    # outtype
    if '.' in outfile:
        outtype = outfile[outfile.rfind('.') + 1:]
        if outtype == 'pdf':
            mpl.use('PDF')  # set directly after import matplotlib
            from matplotlib.backends.backend_pdf import PdfPages
            textsize = 12
        else:
            mpl.use('Agg')  # set directly after import matplotlib
            textsize = 12
    else:
        outtype = 'X'
        textsize = 12

    # plot setup
    if outfile:
        mpl.rc('figure', figsize=(8.27, 11.69))  # a4 portrait
        if not (outtype == 'pdf'):
            mpl.rc('savefig', dpi=300, format=outtype)
    else:
        mpl.rc('figure', figsize=(8.27 * 0.75, 11.69 * 0.75))
    # figsize = mpl.rcParams['figure.figsize']
    mpl.rc('font', size=textsize)

    # plotting
    ifig = 0
    if (outtype == 'pdf'):
        pdf_pages = PdfPages(outfile)
    else:
        pdf_pages = None

    dall = _all_colors(collection)
    for cc in dall:
        ifig = _plot_colors(ifig, cc, dall[cc], sort_colors=True,
                            textsize=textsize, outtype=outtype,
                            outfile=outfile, pdf_pages=pdf_pages)

    if outtype == 'pdf':
        pdf_pages.close()
    elif outtype == 'X':
        plt.show()
    else:
        pass


def _newfig_cmaps(ifig, ititle):  # pragma: no cover
    """ Helper function for show_cmaps """
    fig = plt.figure(ifig)
    fig.suptitle(ititle)
    plt.subplots_adjust(left=0.3, bottom=0.1,
                        right=0.95, top=0.95,
                        wspace=0.05, hspace=0.5)
    return fig


def _newsubplot_cmaps(nrow, ncol, iplot, iname,
                      ncolors=0):  # pragma: no cover
    """ Helper function for show_cmaps """
    import numpy as np

    ax = plt.subplot(nrow, ncol, iplot)
    ax.axis('off')
    cmap = get_cmap(iname, ncolors, as_cmap=True)
    ax.imshow(np.outer(np.ones(cmap.N), np.arange(cmap.N)),
              aspect='auto', cmap=cmap, origin="lower")
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    dx = -0.01
    dy = 0.5
    if ncolors:
        iiname = f'{iname}({ncolors})'
    else:
        iiname = iname
    ax.text(xmin + dx * (xmax - xmin), ymin + dy * (ymax - ymin), iiname,
            ha='right', va='center')
    # return ax


# https://matplotlib.org/stable/gallery/color/colormap_reference.html
def show_cmaps(outfile='', collection=''):  # pragma: no cover
    """
    Show the known color palettes and continuous colormaps

    Parameters
    ----------
    outfile : str, optional
        Output file name. Output type will be determined from file suffix.
    collection : str or list of strings, optional
        Name(s) of color palette collection(s).
        All palettes will be shown if collection is empty or 'all'.
        Known collections are: 'brewer', 'ipcc', 'mathematica', 'matplotlib',
        'mcplot', 'ncl', 'oregon', 'sron', and 'sron2012'.

    Returns
    -------
    None
        Plots known color palettes and continuous colormaps in file or on
        plotting window.

    Examples
    --------
    .. code-block:: python

       show_cmaps(outfile='mcplot_cmaps.pdf',
                     collection=['mathematica', 'matplotlib'])

    """
    import mcplot.color as mc  # used in eval

    # outtype
    if '.' in outfile:
        outtype = outfile[outfile.rfind('.') + 1:]
        if outtype == 'pdf':
            mpl.use('PDF')  # set directly after import matplotlib
            from matplotlib.backends.backend_pdf import PdfPages
            textsize = 10
        else:
            mpl.use('Agg')  # set directly after import matplotlib
            textsize = 10
    else:
        outtype = 'X'
        textsize = 8

    # plot setup
    if outfile:
        mpl.rc('figure', figsize=(8.27, 11.69))  # a4 portrait
        if not (outtype == 'pdf'):
            mpl.rc('savefig', dpi=300, format=outtype)
    else:
        mpl.rc('figure', figsize=(8.27 * 0.75, 11.69 * 0.75))
    # figsize = mpl.rcParams['figure.figsize']
    mpl.rc('font', size=textsize)
    nrow = 35

    # plotting
    ifig = 0
    if (outtype == 'pdf'):
        pdf_pages = PdfPages(outfile)
    else:
        pdf_pages = None

    dall = _all_cmaps(collection)
    ipanel = 0
    for dd in dall:
        collname = dd
        call = dall[dd]
        for cc in call:
            if collname == 'matplotlib':
                catname = f'{collname} - {cc}'
            else:
                catname = cc
            icoll = call[cc]
            for iname in icoll:
                if ipanel == 0:
                    ifig += 1
                    fig = _newfig_cmaps(ifig, catname)
                ipanel += 1
                _newsubplot_cmaps(nrow, 1, ipanel, iname)

                if catname == 'sron_functions':
                    for ncolors in range(1, 24):
                        ipanel += 1
                        _newsubplot_cmaps(nrow, 1, ipanel, iname, ncolors)
                    # new page after each function
                    _savefig(fig, ifig, outtype, outfile, pdf_pages)
                    ipanel = 0

                if ipanel == nrow:  # new page if enough rows per page
                    _savefig(fig, ifig, outtype, outfile, pdf_pages)
                    ipanel = 0

            if ipanel != 0:  # new page after each category
                _savefig(fig, ifig, outtype, outfile, pdf_pages)
                ipanel = 0

    if ipanel != 0:  # finish at end of all cmaps
        _savefig(fig, ifig, outtype, outfile, pdf_pages)

    if outtype == 'pdf':
        pdf_pages.close()
    elif outtype == 'X':
        plt.show()
    else:
        pass


def show_palettes(*args, **kwargs):
    """ Alias for show_cmaps """
    return show_cmaps(*args, **kwargs)


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
