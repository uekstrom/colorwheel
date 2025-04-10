# Copyright (C) Ulf Ekstrom <uekstrom@gmail.com> 2025
# Permission is hereby granted, free of charge, to any person obtaining a copy of this 
# software and associated documentation files (the “Software”), to deal in the Software 
# without restriction, including without limitation the rights to use, copy, modify, merge, 
# publish, distribute, sublicense, and/or sell copies of the Software, and to permit 
# persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or 
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
# BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# This is the Colorwheel color map in sRGB float format
colors = [[9.65246549e-01, 8.13827873e-01, 3.54995481e-02],
       [1.00000000e+00, 7.54400671e-01, 5.96369855e-08],
       [1.00000000e+00, 6.89975121e-01, 3.70155717e-07],
       [1.00000000e+00, 6.24055810e-01, 2.89885028e-07],
       [1.00000000e+00, 5.56388222e-01, 2.37011569e-02],
       [1.00000000e+00, 4.88310276e-01, 1.07342654e-01],
       [1.00000000e+00, 4.14139317e-01, 1.45399871e-01],
       [9.96733205e-01, 3.32898008e-01, 1.83204421e-01],
       [9.55860966e-01, 2.67691368e-01, 2.29196088e-01],
       [9.16812299e-01, 2.29007900e-01, 3.16986609e-01],
       [8.74115199e-01, 2.12576460e-01, 4.00747900e-01],
       [8.26373747e-01, 2.15992904e-01, 4.79921197e-01],
       [7.73442962e-01, 2.35149069e-01, 5.55273021e-01],
       [7.13797072e-01, 2.68304699e-01, 6.22764084e-01],
       [6.46284947e-01, 3.14257459e-01, 6.70179364e-01],
       [5.75826839e-01, 3.55350643e-01, 7.13045820e-01],
       [4.97736406e-01, 3.92601178e-01, 7.47614002e-01],
       [4.07784381e-01, 4.29442504e-01, 7.68234303e-01],
       [2.99426780e-01, 4.68016769e-01, 7.71232221e-01],
       [1.61515156e-01, 5.11441924e-01, 7.57959971e-01],
       [0.00000000e+00, 5.61134848e-01, 7.38655511e-01],
       [0.00000000e+00, 6.06702393e-01, 7.07289110e-01],
       [0.00000000e+00, 6.48146935e-01, 6.65693542e-01],
       [1.29865957e-02, 6.80804928e-01, 6.03421641e-01],
       [1.89447215e-01, 7.08723329e-01, 5.34681691e-01],
       [3.15812031e-01, 7.34579462e-01, 4.62348754e-01],
       [4.21580101e-01, 7.60995139e-01, 3.86226481e-01],
       [5.21205993e-01, 7.90186326e-01, 3.12525366e-01],
       [6.34918907e-01, 8.12483129e-01, 2.36750831e-01],
       [7.50249701e-01, 8.27893673e-01, 1.66742811e-01],
       [8.62790551e-01, 8.34388326e-01, 1.05388198e-01],
       [9.65246549e-01, 8.13827873e-01, 3.54995481e-02]]

colormap = LinearSegmentedColormap.from_list("Wheel", colors)
