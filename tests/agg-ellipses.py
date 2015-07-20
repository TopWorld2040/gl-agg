#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (C) 2013 Nicolas P. Rougier. All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY NICOLAS P. ROUGIER ''AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL NICOLAS P. ROUGIER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# The views and conclusions contained in the software and documentation are
# those of the authors and should not be interpreted as representing official
# policies, either expressed or implied, of Nicolas P. Rougier.
# -----------------------------------------------------------------------------
from agg_setup import *

radius = 255.0
theta = 0
dtheta = 5.5/180.0*math.pi
for i in range(500):
    x = 256+radius*math.cos(theta);
    y = 256+32+radius*math.sin(theta);
    rx = 10.1-i*0.02
    ry = 1.5*rx
    patch = Ellipse( xy=(x,y), width=2*rx, height=2*ry, angle=90+180*theta/math.pi,
                     lw=1.0, color='None', ec='k', fc='None' )
    axes.add_patch(patch)
    radius -= 0.45
    theta += dtheta

for i in range(0,39):
    thickness = (i+1)/10.0
    rx, ry = 4, 8
    x = 20 - rx +i*12.5
    y = 16 
    patch = Ellipse( xy=(x,y), width=2*rx, height=2*ry, angle=0,
                     lw=thickness, color='None', ec='k', fc='None' )
    axes.add_patch(patch)

fig.savefig('agg-ellipses.png')
plt.show()
