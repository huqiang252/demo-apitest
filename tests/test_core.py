#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test_version():
    from hogwarts_apitest import __version__
    assert isinstance(__version__,str) #校验其是一个字符串
