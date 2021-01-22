#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from hogwarts_apitest.api import BaseApi


def test_version():
    from hogwarts_apitest import __version__
    assert isinstance(__version__, str)  # 校验其是一个字符串



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


def test_httpbin_get():
    ApiHttpbinGit().run()\
        .validate("status_code",200)\
        .validate("headers.server","gunicorn/19.9.0")\
        # .validate("json.url","http://httpbin.org/get")


def test_httpbin_get_with_prams():

    ApiHttpbinGit().set_params(abc=123,xyz=456).run()\
        .validate("status_code",200) \
        .validate("headers.server", "gunicorn/19.9.0")

def test_httpbin_post():
    ApiHttpBinPost()\
        .set_data({"yyy":999})\
        .run()\
        .validate("status_code",200) \
        .validate("headers.server", "gunicorn/19.9.0")

