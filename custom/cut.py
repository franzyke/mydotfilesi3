#!/usr/bin/env python3
# -*- coding: utf-8 -*-

while(1):
    s = str(input())
    if (len(s) > 100):
        s = s[:30] + '...' + s[-30:]
    print(s)