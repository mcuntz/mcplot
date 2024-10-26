#!/usr/bin/env python
"""
Color palettes of Paul Tol at SRON - Netherlands Institute for Space
Research

These are the color maps of:
    https://personal.sron.nl/~pault/data/colourschemes.pdf

For details see:
    https://personal.sron.nl/~pault

The color maps are published under the licence: Standard 3-clause BSD

.. moduleauthor:: Matthias Cuntz

History
   * Written Nov 2021 from code *tol_colors.py*
     of Paul Tol, Matthias Cuntz
   * Use : instead of _ in colormap names, Oct 2024, Matthias Cuntz
   * Add sron:pale and sron:dark cmaps, Oct 2024, Matthias Cuntz
   * Add sron_named_colors, Oct 2024, Matthias Cuntz

"""


__all__ = ['sron_named_colors',
           'sron_colors', 'sron_colormaps', 'sron_functions']


sron_named_colors = {
    # All references to sron_colourschemes.pdf
    # Fig. 1
    'sron:bright:blue': '#4477AA',
    'sron:bright:cyan': '#66CCEE',
    'sron:bright:green': '#228833',
    'sron:bright:yellow': '#CCBB44',
    'sron:bright:red': '#EE6677',
    'sron:bright:purple': '#AA3377',
    'sron:bright:grey': '#BBBBBB',
    # Fig. 2
    'sron:high-contrast:white': '#FFFFFF',
    'sron:high-contrast:yellow': '#DDAA33',
    'sron:high-contrast:red': '#BB5566',
    'sron:high-contrast:blue': '#004488',
    'sron:high-contrast:black': '#000000',
    # Fig. 3
    'sron:vibrant:blue': '#0077BB',
    'sron:vibrant:cyan': '#33BBEE',
    'sron:vibrant:teal': '#009988',
    'sron:vibrant:orange': '#EE7733',
    'sron:vibrant:red': '#CC3311',
    'sron:vibrant:magenta': '#EE3377',
    'sron:vibrant:grey': '#BBBBBB',
    # Fig. 4
    'sron:muted:indigo': '#332288',
    'sron:muted:cyan': '#88CCEE',
    'sron:muted:teal': '#44AA99',
    'sron:muted:green': '#117733',
    'sron:muted:olive': '#999933',
    'sron:muted:sand': '#DDCC77',
    'sron:muted:rose': '#CC6677',
    'sron:muted:wine': '#882255',
    'sron:muted:purple': '#AA4499',
    'sron:muted:grey': '#DDDDDD',
    # Fig. 5
    'sron:medium-contrast:white': '#FFFFFF',
    'sron:medium-contrast:light yellow': '#EECC66',
    'sron:medium-contrast:light red': '#EE99AA',
    'sron:medium-contrast:light blue': '#6699CC',
    'sron:medium-contrast:dark yellow': '#997700',
    'sron:medium-contrast:dark red': '#994455',
    'sron:medium-contrast:dark blue': '#004488',
    'sron:medium-contrast:black': '#000000',
    # Fig. 6
    'sron:pale:blue': '#BBCCEE',
    'sron:pale:cyan': '#CCEEFF',
    'sron:pale:green': '#CCDDAA',
    'sron:pale:yellow': '#EEEEBB',
    'sron:pale:red': '#FFCCCC',
    'sron:pale:grey': '#DDDDDD',
    'sron:dark:blue': '#222255',
    'sron:dark:cyan': '#225555',
    'sron:dark:green': '#225522',
    'sron:dark:yellow': '#666633',
    'sron:dark:red': '#663333',
    'sron:dark:grey': '#555555',
    # Fig. 7
    'sron:light:blue': '#77AADD',
    'sron:light:cyan': '#99DDFF',
    'sron:light:mint': '#44BB99',
    'sron:light:pear': '#BBCC33',
    'sron:light:olive': '#AAAA00',
    'sron:light:yellow': '#EEDD88',
    'sron:light:orange': '#EE8866',
    'sron:light:pink': '#FFAABB',
    'sron:light:grey': '#DDDDDD',
}


sron_colors = {
    # All references to sron_colourschemes.pdf
    # Fig. 1 - but order given below Fig. 7
    'sron:bright': ['#4477AA', '#EE6677', '#228833', '#CCBB44', '#66CCEE',
                    '#AA3377', '#BBBBBB', '#000000'],
    # Fig. 2 - but order given below Fig. 7
    'sron:high-contrast': ['#004488', '#DDAA33', '#BB5566', '#000000'],
    # Fig. 3 - but order given below Fig. 7
    'sron:vibrant': ['#EE7733', '#0077BB', '#33BBEE', '#EE3377', '#CC3311',
                     '#009988', '#BBBBBB', '#000000'],
    # Fig. 4 - but order given below Fig. 7
    'sron:muted': ['#CC6677', '#332288', '#DDCC77', '#117733', '#88CCEE',
                   '#882255', '#44AA99', '#999933', '#AA4499', '#DDDDDD',
                   '#000000'],
    # Fig. 5 - but order given below Fig. 7
    'sron:medium-contrast': ['#6699CC', '#004488', '#EECC66', '#994455',
                             '#997700', '#EE99AA', '#000000'],
    # Fig. 6
    'sron:pale': ['#BBCCEE', '#CCEEFF', '#CCDDAA', '#EEEEBB', '#FFCCCC',
                  '#DDDDDD'],
    'sron:dark': ['#222255', '#225555', '#225522', '#666633', '#663333',
                  '#555555'],
    # Fig. 7 - but order given below Fig. 7
    'sron:light': ['#77AADD', '#EE8866', '#EEDD88', '#FFAABB', '#99DDFF',
                   '#44BB99', '#BBCC33', '#AAAA00', '#DDDDDD', '#000000'],
}


sron_colormaps = {
    # All references to sron_colourschemes.pdf
    # tuple([colors], missing value)
    # Fig. 12
    'sron:sunset': (['#364B9A', '#4A7BB7', '#6EA6CD', '#98CAE1', '#C2E4EF',
                     '#EAECCC', '#FEDA8B', '#FDB366', '#F67E4B', '#DD3D2D',
                     '#A50026'], '#FFFFFF'),
    # Fig. 13
    'sron:burd': (['#2166AC', '#4393C3', '#92C5DE', '#D1E5F0', '#F7F7F7',
                   '#FDDBC7', '#F4A582', '#D6604D', '#B2182B'], '#FFEE99'),
    # Fig. 14
    'sron:prgn': (['#762A83', '#9970AB', '#C2A5CF', '#E7D4E8', '#F7F7F7',
                   '#D9F0D3', '#ACD39E', '#5AAE61', '#1B7837'], '#FFEE99'),
    # Fig. 17
    'sron:ylorbr': (['#FFFFE5', '#FFF7BC', '#FEE391', '#FEC44F', '#FB9A29',
                     '#EC7014', '#CC4C02', '#993404', '#662506'], '#888888'),
    # Fig. 17 variant
    'sron:whorbr': (['#FFFFFF', '#FFF7BC', '#FEE391', '#FEC44F', '#FB9A29',
                     '#EC7014', '#CC4C02', '#993404', '#662506'], '#888888'),
    # Fig. 18
    'sron:iridescent': (['#FEFBE9', '#FCF7D5', '#F5F3C1', '#EAF0B5', '#DDECBF',
                         '#D0E7CA', '#C2E3D2', '#B5DDD8', '#A8D8DC', '#9BD2E1',
                         '#8DCBE4', '#81C4E7', '#7BBCE7', '#7EB2E4', '#88A5DD',
                         '#9398D2', '#9B8AC4', '#9D7DB2', '#9A709E', '#906388',
                         '#805770', '#684957', '#46353A'], '#999999'),
    # Fig. 19 top
    'sron:rainbow_purd': (['#6F4C9B', '#6059A9', '#5568B8', '#4E79C5',
                           '#4D8AC6', '#4E96BC', '#549EB3', '#59A5A9',
                           '#60AB9E', '#69B190', '#77B77D', '#8CBC68',
                           '#A6BE54', '#BEBC48', '#D1B541', '#DDAA3C',
                           '#E49C39', '#E78C35', '#E67932', '#E4632D',
                           '#DF4828', '#DA2222'], '#FFFFFF'),
    # Fig. 19 bottom
    'sron:rainbow_pubr': (['#6F4C9B', '#6059A9', '#5568B8', '#4E79C5',
                           '#4D8AC6', '#4E96BC', '#549EB3', '#59A5A9',
                           '#60AB9E', '#69B190', '#77B77D', '#8CBC68',
                           '#A6BE54', '#BEBC48', '#D1B541', '#DDAA3C',
                           '#E49C39', '#E78C35', '#E67932', '#E4632D',
                           '#DF4828', '#DA2222', '#B8221E', '#95211B',
                           '#721E17', '#521A13'], '#FFFFFF'),
    # Fig. 20 variant 1
    'sron:rainbow_whrd': (['#E8ECFB', '#DDD8EF', '#D1C1E1', '#C3A8D1',
                           '#B58FC2', '#A778B4', '#9B62A7', '#8C4E99',
                           '#6F4C9B', '#6059A9', '#5568B8', '#4E79C5',
                           '#4D8AC6', '#4E96BC', '#549EB3', '#59A5A9',
                           '#60AB9E', '#69B190', '#77B77D', '#8CBC68',
                           '#A6BE54', '#BEBC48', '#D1B541', '#DDAA3C',
                           '#E49C39', '#E78C35', '#E67932', '#E4632D',
                           '#DF4828', '#DA2222'], '#666666'),
    # Fig. 20 variant 2
    'sron:rainbow_whbr': (['#E8ECFB', '#DDD8EF', '#D1C1E1', '#C3A8D1',
                           '#B58FC2', '#A778B4', '#9B62A7', '#8C4E99',
                           '#6F4C9B', '#6059A9', '#5568B8', '#4E79C5',
                           '#4D8AC6', '#4E96BC', '#549EB3', '#59A5A9',
                           '#60AB9E', '#69B190', '#77B77D', '#8CBC68',
                           '#A6BE54', '#BEBC48', '#D1B541', '#DDAA3C',
                           '#E49C39', '#E78C35', '#E67932', '#E4632D',
                           '#DF4828', '#DA2222', '#B8221E', '#95211B',
                           '#721E17', '#521A13'], '#666666'),
}


def _rainbow_discrete(n=23):
    """ Function __rainbow_discrete of tol_colors.py """
    assert n <= 23
    colors = ['#E8ECFB', '#D9CCE3', '#D1BBD7', '#CAACCB', '#BA8DB4',
              '#AE76A3', '#AA6F9E', '#994F88', '#882E72', '#1965B0',
              '#437DBF', '#5289C7', '#6195CF', '#7BAFDE', '#4EB265',
              '#90C987', '#CAE0AB', '#F7F056', '#F7CB45', '#F6C141',
              '#F4A736', '#F1932D', '#EE8026', '#E8601C', '#E65518',
              '#DC050C', '#A5170E', '#72190E', '#42150A']
    indexes = [[9],
               [9, 25],
               [9, 17, 25],
               [9, 14, 17, 25],
               [9, 13, 14, 17, 25],
               [9, 13, 14, 16, 17, 25],
               [8, 9, 13, 14, 16, 17, 25],
               [8, 9, 13, 14, 16, 17, 22, 25],
               [8, 9, 13, 14, 16, 17, 22, 25, 27],
               [8, 9, 13, 14, 16, 17, 20, 23, 25, 27],
               [8, 9, 11, 13, 14, 16, 17, 20, 23, 25, 27],
               [2, 5, 8, 9, 11, 13, 14, 16, 17, 20, 23, 25],
               [2, 5, 8, 9, 11, 13, 14, 15, 16, 17, 20, 23, 25],
               [2, 5, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25],
               [2, 5, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25, 27],
               [2, 4, 6, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25, 27],
               [2, 4, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25, 27],
               [2, 4, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25, 26,
                27],
               [1, 3, 4, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25,
                26, 27],
               [1, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 19, 21, 23,
                25, 26, 27],
               [1, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 20, 22,
                24, 25, 26, 27],
               [1, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 20, 22,
                24, 25, 26, 27, 28],
               [0, 1, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 20, 22,
                24, 25, 26, 27, 28]]
    cols = [ colors[i] for i in indexes[n - 1] ]
    if n == 23:
        return (cols, '#777777')
    else:
        return (cols, '#FFFFFF')


sron_functions = {
    # Fig. 22
    'sron:rainbow_discrete': _rainbow_discrete,
}


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
