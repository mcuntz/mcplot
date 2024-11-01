#!/usr/bin/env python
"""
Write text on a plot

This module was written by Matthias Cuntz while at Department of Computational
Hydrosystems, Helmholtz Centre for Environmental Research - UFZ, Leipzig,
Germany, and continued while at Institut National de Recherche pour
l'Agriculture, l'Alimentation et l'Environnement (INRAE), Nancy, France.

:copyright: Copyright 2014- Matthias Cuntz, see AUTHORS.rst for details.
:license: MIT License, see LICENSE for details.

.. moduleauthor:: Matthias Cuntz

The following functions are provided:

.. autosummary::
   text2plot
   abc2plot
   signature2plot

History
   * Written Nov 2021 by Matthias Cuntz (mc (at) macu (dot) de)
     combining abc2plot and signature2plot
   * Written abc2plot, May 2012, Matthias Cuntz
   * Added parenthesis option to abc2plot, Feb 2013, Arndt Piayda
   * Ported to Python 3, Feb 2013, Matthias Cuntz
   * Added opening and closing parentheses, brackets, braces,
     Feb 2013, Matthias Cuntz
   * Options usetex and mathrm, Feb 2013, Matthias Cuntz
   * Options mathbf, large and making medium the default,
     Feb 2013, Matthias Cuntz
   * Added string option, Nov 2013, Matthias Cuntz
   * Corrected bug in medium as default, Nov 2013, Matthias Cuntz
   * Make usetex work with fontsize keyword of axis.text()
     of matplotllib v1.1.0, Nov 2013, Matthias Cuntz
   * Written signature2plot, Jan 2014, Matthias Cuntz
   * Assert that small or large is set if medium is not None (abc2plot),
     Feb 2014, Matthias Cuntz
   * Replace horizontalalignment='left' and verticalalignment='bottom'
     by kwargs mechanism (abc2plot), May 2014, Matthias Cuntz
   * Added option italic (abc2plot), May 2014, Matthias Cuntz
   * Added options xlarge, xxlarge, xsmall, xxsmall (abc2plot),
     Oct 2015, Matthias Cuntz
   * Make numpy docstring format (abc2plot), Nov 2020, Matthias Cuntz
   * Ported into pyjams, Nov 2021, Matthias Cuntz
   * dx, dy, and name mandatory parameters (signature2plot),
     Nov 2020, Matthias Cuntz
   * Change option name parenthesis -> parentheses, Nov 2021, Matthias Cuntz
   * Written text2plot, Nov 2021, Matthias Cuntz
   * Use text2plot for signature2plot, Nov 2021, Matthias Cuntz
   * Use text2plot for abc2plot, Nov 2021, Matthias Cuntz
   * More consistent docstrings, Jan 2022, Matthias Cuntz
   * Added upper keyword in abc2plot, Jun 2024, Matthias Cuntz
   * Use f-strings and flake8 compliant, Oct 2024, Matthias Cuntz
   * Use backslash with braces only if usetex not if only pdf output in
     abc2plot, Oct 2024, Matthias Cuntz
   * Put $...$ around a, b, c only if mathrm in abc2plot,
     Oct 2024, Matthias Cuntz
   * Pass italic and bold along to str2tex in text2plot,
     Oct 2024, Matthias Cuntz

"""
import time as ptime
from .str2tex import str2tex
from .romanliterals import int2roman
# from mcplot.str2tex import str2tex
# from mcplot.romanliterals import int2roman


__all__ = ['text2plot', 'abc2plot', 'signature2plot']


def text2plot(handle, dx, dy, itext,
              small=False, medium=False, large=False,
              xsmall=False, xxsmall=False, xlarge=False, xxlarge=False,
              bold=False, italic=False,
              usetex=False, mathrm=False,
              **kwargs):  # pragma: no cover
    """
    Write text on plot

    Parameters
    ----------
    handle : :class:`matplotlib.axes` subclass
        Matplotlib axes handle
    dx : float
        % of xlim from min(xlim)
    dy : float
        % of ylim from min(ylim)
    itext : str
        String to write on plot
    small : bool, optional
        fontsize='small' if True (default: False)
    medium : bool, optional
        fontsize='medium' if True (default: False).
        Medium is taken if no other fontsize is chosen.
    large : bool, optional
        fontsize='large' if True (default: False)
    xlarge : bool, optional
        fontsize='x-large' if True (default: False)
    xsmall : bool, optional
        fontsize='x-small' if True (default: False)
    xxlarge : bool, optional
        fontsize='xx-large' if True (default: False)
    xxsmall : bool, optional
        fontsize='xx-small' if True (default: False)
    bold : bool, optional
        fontweight='bold' if True, else fontsize='normal' (default)
    italic : bool, optional
        fontstyle='italic' if True, else fontstyle='normal' (default)
    usetex : bool, optional
        Embed into LaTeX math environment if True,
        else no LaTeX math mode (default)
    mathrm : bool, optional
        If True, put text into appropriate LaTeX mathrm/mathit/mathbf
        environment if *usetex==True* and *italic==True* or *bold==True*.
        If False, use standard math font if *usetex==True* (default).
    string : bool, optional
        Treat *iplot* as literal string and not as integer if True (default:
        False). *integer*, *roman* and *lower* are disabled then.
    **kwargs : dict, optional
        All additional parameters are passed passed to
        :meth:`matplotlib.axes.Axes.text()`

    Returns
    -------
    String on plot

    Examples
    --------
    .. code-block:: python

       text2plot(ax, 0.7, 0.6, r'CO$_2$', large=True,
                 usetex=usetex, mathrm=False)

    """
    # Check input
    ifont = small + medium + large + xsmall + xxsmall + xlarge + xxlarge
    assert ifont <= 1, ('only one of small, medium, large, xsmall, xxsmall'
                        ' xlarge, or xxlarge font size can be chosen.')
    if ifont == 0:
        medium = True
    if usetex and mathrm:
        assert (bold + italic) <= 1, ('if usetex and mathrm: then bold and'
                                      ' italic are mutually exclusive.')

    # Size
    if small:
        fs = 'small'
    elif medium:
        fs = 'medium'
    elif large:
        fs = 'large'
    elif xsmall:
        fs = 'x-small'
    elif xxsmall:
        fs = 'xx-small'
    elif xlarge:
        fs = 'x-large'
    elif xxlarge:
        fs = 'xx-large'
    else:  # just for security
        fs = 'medium'

    # Weight
    if bold:
        fw = 'bold'
    else:
        fw = 'normal'

    # Style
    if italic:
        fst = 'italic'
    else:
        fst = 'normal'

    # usetex
    istr = str2tex(itext, bold=bold, italic=italic, usetex=usetex)

    if usetex:
        if mathrm:
            if bold:
                istr = istr.replace('mathrm', 'mathbf')
            elif italic:
                istr = istr.replace('mathrm', 'mathit')

    # x/y position
    xmin, xmax = handle.get_xlim()
    ymin, ymax = handle.get_ylim()
    idx = xmin + dx * (xmax - xmin)
    if 'transform' in kwargs:
        if kwargs['transform'] is handle.transAxes:
            idx = dx
    idy = ymin + dy * (ymax - ymin)
    if 'transform' in kwargs:
        if kwargs['transform'] is handle.transAxes:
            idy = dy

    handle.text(idx, idy, istr,
                fontsize=fs, fontweight=fw, fontstyle=fst,
                **kwargs)


def abc2plot(handle, dx, dy, iplot,
             integer=False, roman=False, lower=False, upper=None,
             parentheses=None, brackets=None, braces=None,
             bold=False, italic=False,
             usetex=False, mathrm=False, string=False,
             **kwargs):  # pragma: no cover
    """
    Write a, B, iii, IV, e), etc. on plots

    Parameters
    ----------
    handle : :class:`matplotlib.axes` subclass
       Matplotlib axes handle
    dx : float
        % of xlim from min(xlim)
    dy : float
        % of ylim from min(ylim)
    iplot : int or str
        Number of plot starting with 1, or string if 'string==True'
    integer : bool, optional
        Use integers instead of a, b, c if True (default: False)
    roman : bool, optional
        Use Roman literals instead of a, b, c if True (default: False)
    lower : bool, optional
        Use lowercase letters for a, b, c if True,
        else use uppercase letters (default).
        lower=True and upper=True are mutually exclusive.
    upper : bool, optional
        Use uppercase letters for A, B, C if True (default),
        else use lowercase letters.
        lower=True and upper=True are mutually exclusive.
    parentheses : str or None, optional
        Parentheses before or after the letter/number. Possible values are
        'open', 'close', 'both', 'None', and *None*.
        'open' puts opening parentheses in front of the letter/number.
        'close' puts closing parentheses after the letter/number.
        'both' puts opening and closing parentheses around the letter/number.
        'None' and *None* do not put any parentheses before or after the
        letter/number (default).
    brackets : str or None, optional
        Brackets before or after the letter/number. Possible values are
        'open', 'close', 'both', 'None', and *None*.
        'open' puts opening brackets in front of the letter/number.
        'close' puts closing brackets after the letter/number.
        'both' puts opening and closing brackets around the letter/number.
        'None' and *None* do not put any brackets before or after the
        letter/number (default).
    braces : str or None, optional
        Braces before or after the letter/number. Possible values are
        'open', 'close', 'both', 'None', and *None*.
        'open' puts opening braces in front of the letter/number.
        'close' puts closing braces after the letter/number.
        'both' puts opening and closing braces around the letter/number.
        'None' and *None* do not put any braces before or after the
        letter/number (default).
    bold : bool, optional
        fontweight='bold' if True, else fontsize='normal' (default)
    italic : bool, optional
        fontstyle='italic' if True, else fontstyle='normal' (default)
    usetex : bool, optional
        Embed into LaTeX math environment if True,
        else no LaTeX math mode (default)
    mathrm : bool, optional
        If True, put text into appropriate LaTeX mathrm/mathit/mathbf
        environment if *usetex==True* and *italic==True* or *bold==True*.
        If False, use standard math font if *usetex==True* (default).
    string : bool, optional
        Treat *iplot* as literal string and not as integer if True (default:
        False). *integer*, *roman* and *lower* are disabled then.
    **kwargs : dict, optional
        All additional parameters are passed passed to :func:`text2plot()`

    Returns
    -------
    Letter/number or string on plot

    Notes
    -----
    If output is a letter then iplot > 26 gives unexpected results.

    Examples
    --------
    .. code-block:: python

       abc2plot(ax, 0.7, 0.6, 2, large=True, parentheses='both',
                usetex=usetex, mathrm=False)

    """
    import matplotlib.pyplot as plt

    # Check input
    assert not (roman and integer), (
        'either Roman literals or integers can be chosen.')
    iparentheses = False
    if parentheses is not None:
        if parentheses != 'None':
            iparentheses = True
    ibrackets = False
    if brackets is not None:
        if brackets != 'None':
            ibrackets = True
    ibraces = False
    if braces is not None:
        if braces != 'None':
            ibraces = True
    ibrack = iparentheses + ibrackets + ibraces
    assert ibrack <= 1, ('only one of parentheses, brackets, or braces'
                         ' can be chosen.')
    if upper is not None:
        assert not (upper and lower), (
            'either uppercase or lowercase can be chosen.')
        # assure correct lower keyword if upper=False given
        if upper:
            lower = False
        else:
            lower = True

    # Number or letter
    if string:
        t = str(iplot)
    else:
        if roman:
            t = int2roman(iplot, lower=lower)
        elif integer:
            t = str(iplot)
        else:
            if lower:
                t = chr(96 + iplot)
            else:
                t = chr(64 + iplot)

    # parentheses
    if iparentheses:
        if parentheses.lower() == 'open':
            t = f'({t}'
        elif parentheses.lower() == 'close':
            t = f'{t})'
        elif parentheses.lower() == 'both':
            t = f'({t})'
        elif parentheses.lower() == 'none':
            pass
        else:
            raise ValueError("parentheses must be either 'open', 'close',"
                             " 'both', or 'none'.")

    if ibrackets:
        if brackets.lower() == 'open':
            t = f'[{t}' + t
        elif brackets.lower() == 'close':
            t = f'{t}]'
        elif brackets.lower() == 'both':
            t = f'[{t}]'
        elif brackets.lower() == 'none':
            pass
        else:
            raise ValueError("brackets must be either 'open', 'close',"
                             " 'both', or 'none'.")

    if ibraces:
        if braces.lower() == 'open':
            if usetex:  # or (plt.get_backend() == 'pdf'):
                t = r'\{' + t
            else:
                t = '{' + t
        elif braces.lower() == 'close':
            if usetex:  # or (plt.get_backend() == 'pdf'):
                t = t + r'\}'
            else:
                t = t + '}'
        elif braces.lower() == 'both':
            if usetex:  # or (plt.get_backend() == 'pdf'):
                t = r'\{' + t + r'\}'
            else:
                t = '{' + t + '}'
        elif braces.lower() == 'none':
            pass
        else:
            raise ValueError("braces must be either 'open', 'close',"
                             " 'both', or 'none'.")

    if usetex:
        if mathrm:
            if bold:
                t = r'\mathbf{' + t + '}'
            elif italic:
                t = r'\mathit{' + t + '}'
            else:
                t = r'\mathrm{' + t + '}'
            t = fr'${t}$'

    text2plot(handle, dx, dy, t,
              bold=bold, italic=italic,
              usetex=False, mathrm=False,
              **kwargs)


def signature2plot(handle, dx, dy, itext,
                   **kwargs):  # pragma: no cover
    """
    Write a copyright notice on a plot

    The notice is: '(C) YYYY *itext*', where YYYY is the current 4-digit year.

    Parameters
    ----------
    handle : :class:`matplotlib.axes` subclass
       Matplotlib axes handle
    dx : float
        % of xlim from min(xlim).
        The text is 'horizontalalignment' = 'right' by default
        if not given otherwise in **kwargs.
    dy : float
        % of ylim from min(ylim)
    itext : str
        Text after '(C) YYYY', where YYYY is the current 4-digit year
    **kwargs : dict, optional
        All additional parameters are passed passed to :func:`text2plot()`

    Returns
    -------
    '(C) YYYY itext' or '(C) YYYY' on plot, where YYYY is the 4-digit year

    Notes
    -----
    Signature will be right-aligned horizontally if horizontalalignment or
    ha are not given in kwargs.

    Examples
    --------
    .. code-block:: python

       signature2plot(ax, 0., 0.05, 'M Cuntz, INRAE',
                      small=True, italic=True,
                      usetex=usetex, mathrm=True)

    """
    year = str(ptime.localtime().tm_year)
    if itext.strip():
        otext = fr'$\copyright$ {year} {itext.strip()}'
    else:
        otext = fr'$\copyright$ {year}'

    if ('horizontalalignment' not in kwargs) and ('ha' not in kwargs):
        kwargs['horizontalalignment'] = 'right'

    text2plot(handle, dx, dy, otext, **kwargs)


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
