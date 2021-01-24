#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from hogwarts_apitest.api import BaseApi


class ApiHttpbinGit(BaseApi):
    url = "http://httpbin.org/get"
    method = "GET"
    params = {}
    headers = {"accept": "application/json"}


class ApiHttpBinPost(BaseApi):
    url = "http://httpbin.org/post"
    method = "POST"
    params = {}
    headers = {"accept": "application/json"}
    data=""
    json = {"abc":123}


class ApiHttpBinGetCookies(BaseApi):
    url = "http://httpbin.org/cookies"
    method = "GET"
    params = {}
    headers = {"accept": "application/json"}


class ApiHttpBinGetSetCookies(BaseApi):
    url = "http://httpbin.org/cookies/set"
    method = "GET"
    params = {}
    headers = {"accept": "text/plain"}
