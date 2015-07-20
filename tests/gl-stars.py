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
import sys
import fbo
import numpy as np
import OpenGL.GL as gl
import OpenGL.GLUT as glut

# -------------------------------------
def on_display():
    gl.glClearColor(1,1,1,1);
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    collection.draw()
    glut.glutSwapBuffers()
    
# -------------------------------------
def on_reshape(width, height):
    gl.glViewport(0, 0, width, height)


# -------------------------------------
def on_keyboard(key, x, y):
    if key == '\033': sys.exit()
    if key == ' ': fbo.save( on_display, "gl-stars.png")

# -------------------------------------
def star( r1=0.5, r2=1.0, n=5):
    points = []
    n *= 2
    for i in np.arange(n):
        if i%2: r = r1
        else:   r = r2
        theta = np.pi/12 + 2*np.pi * i/float(n)
        x = r*np.cos(theta)
        y = r*np.sin(theta)
        points.append( [x,y])
    return np.array(points).reshape(n,2)


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    from glagg import PathCollection

    glut.glutInit(sys.argv)
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
    glut.glutCreateWindow("OpenGL antialiased stars")
    glut.glutReshapeWindow(512, 512+32)
    glut.glutDisplayFunc(on_display)
    glut.glutReshapeFunc(on_reshape)
    glut.glutKeyboardFunc(on_keyboard)

    collection = PathCollection()
    s = star()
    radius = 255.0
    theta, dtheta = 0, 5.5/180.0*np.pi
    for i in range(500):
        theta += dtheta
        x = 256+radius*np.cos(theta)
        y = 256+32+radius*np.sin(theta)
        r = 10.1-i*0.02
        radius -= 0.45
        collection.append( s*r + (x,y), closed=True, linejoin='miter')

    for i in range(0,39):
        linewidth = (i+1)/20.0
        x = 20+i*12.5 - r
        y = 16
        collection.append( s*4 + (x,y), closed=True,
                           linewidth=linewidth, linejoin='miter')

    glut.glutMainLoop()
