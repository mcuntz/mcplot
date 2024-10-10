#!/usr/bin/env python
"""
mcplot own color palettes

.. moduleauthor:: Matthias Cuntz

History
   * Written Apr 2022, Matthias Cuntz,
     added pyjams_amwg
   * Renamed pyjams_cmaps to mcplot_cmaps, and pyjams_amwg to mcplot_amwg,
     Oct 2024, Matthias Cuntz
   * Use : instead of _ in colormap names, Oct 2024, Matthias Cuntz

"""

__all__ = ['mcplot_cmaps']


# Toned down version of ncl_amwg w/o pink and rose,
# from Cernusak et al. (New Phyt 2022)
# This is the change from the New Phytology editorial office
# to our plots made with ncl_amwg.
# Must be some kind of conversion between RGB, sRGB or Adobe RGB.
mcplot_amwg = [
    (145, 45, 50),
    (213, 75, 40),
    (229, 153, 42),
    (244, 208, 43),
    (206, 172, 130),
    (239, 220, 182),
    (14, 132, 88),
    (141, 185, 66),
    (0, 152, 163),
    (155, 204, 213),
    (93, 136, 185),
    (36, 91, 153),
    (36, 33, 104),
    (124, 104, 157),
    (0, 0, 0),
    (255, 255, 255) ]
mcplot_amwg = [ (c[0] / 255, c[1] / 255, c[2] / 255)
                for c in mcplot_amwg ][::-1]

# mcplot color maps
mcplot_cmaps = {
    'mcplot:amwg': mcplot_amwg,
}


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
