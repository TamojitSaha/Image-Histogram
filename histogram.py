'''
BSD 3-Clause License
Copyright (c) 2017, Tamojit Saha All rights reserved.
Redistribution and use in source and binary forms, with or without modification, 
are permitted provided that the following conditions are met:
* Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.
* Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''


'''
Sample Usage
...........................................................
histogramImage('lena.tiff',4,8,600)
...........................................................
'''

import os
import cv2
from matplotlib import pyplot as plt
def histogramImage(file_name,image_height,image_width,DPI):
    img = cv2.imread(file_name)
    base = os.path.basename(file_name)
    name = os.path.splitext(base)[0]
    ext = os.path.splitext(base)[1]
    histb = cv2.calcHist([img],[0],None,[256],[0,256])
    histg = cv2.calcHist([img],[1],None,[256],[0,256])
    histr = cv2.calcHist([img],[2],None,[256],[0,256])
    f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
    
    plt.xlabel('Pixel intensity')
    plt.ylabel('Number of pixels',horizontalalignment='left',position=(1,1))    
    figure = plt.gcf() # get current figure
    ax1.fill(histr,'r');
    ax2.fill(histg,'g');
    ax3.fill(histb,'b');
    figure.set_size_inches(image_width, image_height)#in inches
    # when saving, specify the DPI
    new_file_name = "histogram_"+name+ext
    print "\nThe filename is: "+new_file_name
    plt.savefig(new_file_name, dpi = DPI, bbox_inches='tight')
    plt.setp([a.get_xticklabels() for a in f.axes[:-5]], visible=True)
    plt.show()
