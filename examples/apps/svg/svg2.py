# -*- coding: utf-8 -*-
from pymt import *

# PYMT Plugin integration
IS_PYMT_PLUGIN = True
PLUGIN_TITLE = 'SVG Viewer'
PLUGIN_AUTHOR = 'Nathanaël Lécaudé'
PLUGIN_DESCRIPTION = 'This is an example of Scalable Vector Graphics using the Squirtle library for pyglet.'

svgdata = """<?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 13.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 14948)  -->
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.0//EN" "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg version="1.0" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 width="128px" height="128px" viewBox="0 0 128 128" enable-background="new 0 0 128 128" xml:space="preserve">
<polygon fill="#F1E323" points="26.318,46.295 64.821,19.125 110.014,42.609 112.881,96.541 67.961,111.15 26.045,92.309 "/>
<polygon fill="#F8F191" points="64.957,22.128 108.238,43.974 110.969,95.312 99.637,50.392 "/>
<polyline points="82.844,51.822 77.109,44.931 73.285,53.273 78.809,57.082 "/>
<polyline points="59.072,54.47 52.683,47.113 48.422,56.019 54.576,60.084 "/>
<polygon points="45.979,75.24 44.887,70.871 39.016,79.201 44.477,78.518 59.223,89.441 77.246,90.807 92.674,77.973 96.77,77.152
	90.898,70.734 90.217,75.787 76.836,87.529 59.769,86.164 "/>
<polygon fill="#404040" points="52.942,48.89 57.584,54.215 53.352,51.757 "/>
<polygon fill="#404040" points="77.109,46.159 81.479,51.757 77.518,49.846 "/>
<polygon fill="#404040" points="44.478,72.783 45.569,75.924 58.95,86.301 44.341,76.469 "/>
<polygon fill="#404040" points="91.172,71.691 95.814,76.742 92.4,74.967 "/>
<polyline fill="#CFC31E" points="27.547,47.115 27.273,91.354 68.098,109.785 30.687,89.168 "/>
<polygon fill="#F1E323" points="116.173,58.063 145.789,54.59 147.251,77.99 119.646,77.259 "/>
<polygon fill="#F1E323" points="103.376,31.92 80.341,19.854 96.063,-3.363 114.893,5.778 "/>
<polygon fill="#F1E323" points="53.833,21.134 33.723,-6.288 10.688,7.24 27.507,33.383 "/>
<polygon fill="#F1E323" points="21.292,58.611 -11.25,57.697 -11.25,80.549 19.281,79.817 "/>
<polygon fill="#F1E323" points="28.604,98.647 13.065,124.059 34.637,133.383 52.736,110.348 "/>
<polygon fill="#F1E323" points="84.18,110.348 104.473,103.035 113.979,130.092 92.955,133.748 "/>
<polygon fill="#F8F191" points="96.978,-1.352 112.882,6.875 102.827,29.727 108.86,7.789 "/>
<polygon fill="#F8F191" points="118.55,59.342 144.326,56.6 145.789,76.161 141.401,60.622 "/>
<polygon fill="#F8F191" points="33.906,-3.729 51.09,20.585 38.111,11.262 "/>
<polygon fill="#F8F191" points="-9.056,59.891 19.098,60.622 18.001,77.989 15.807,63.364 "/>
<polygon fill="#F8F191" points="103.741,105.778 112.15,128.63 104.29,117.844 "/>
<polygon fill="#F8F191" points="29.518,101.757 48.714,111.812 35.368,130.458 44.326,113.64 "/>
<polygon fill="#CFC31E" points="95.5,1 83.75,18.5 101.5,28.75 87.75,18.25 "/>
<polygon fill="#CFC31E" points="118.75,62.25 121,76 143.5,76.25 123.25,74 "/>
<polygon fill="#CFC31E" points="85.75,111.25 93.5,132.75 91.5,120 "/>
<polygon fill="#CFC31E" points="27.75,103 14.75,123.5 32.5,131.5 18.25,122.75 "/>
<polygon fill="#CFC31E" points="16.25,78.5 -10.5,79.25 -10,60.5 -8.75,77 "/>
<polygon fill="#CFC31E" points="28.25,31.25 13,8 23.75,17.5 "/>
</svg>""";


def pymt_plugin_activate(w, ctx):
    sun = MTScatterSvg(filename = 'sun', pos = (200,200), rawdata=svgdata)
    ctx.c = MTKinetic()
    ctx.c.add_widget(sun)
    w.add_widget(ctx.c)

def pymt_plugin_deactivate(w, ctx):
    w.remove_widget(ctx.c)

if __name__ == '__main__':
    w = MTWindow()
    ctx = MTContext()
    pymt_plugin_activate(w, ctx)
    runTouchApp()
    pymt_plugin_deactivate(w, ctx)