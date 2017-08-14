#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 10:38:36 2017

@author: cheng-xili
"""

from subprocess import Popen,PIPE

def subprocess_cmd(dr,cmd1,cmd2):
    p1 = Popen(cmd1.split(),stdout=PIPE,cwd=dr)
    p2 = Popen(cmd2.split(),stdin=p1.stdout,stdout=PIPE,cwd=dr)
    p2 = Popen(cmd2.split(),stdout=PIPE,cwd=dr)
    p1.stdout.close()
    return p2.communicate()[0]

subprocess_cmd(dr,cmd1,cmd2):
