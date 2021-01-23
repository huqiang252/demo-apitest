#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from hogwarts_apitest.api import BaseApi


class ApiHttpbinGit(BaseApi):
    url = "http://httpbin.org/get"
    params = {}
    method = "GET"
    headers = {"accept": "application/json"}


class ApiHttpBinPost(BaseApi):
    url = "http://httpbin.org/post"
    params = {}
    method = "POST"
    headers = {"accept": "application/json"}
    data=""
    json = {"abc":123}