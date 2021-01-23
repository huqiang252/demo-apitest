#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tests.api.httpbin import *


def test_version():
    from hogwarts_apitest import __version__
    assert isinstance(__version__, str)


def test_httpbin_get():
    ApiHttpbinGit().run()\
        .validate("status_code",200)\
        .validate("headers.server","gunicorn/19.9.0")\
        .validate("json().url","http://httpbin.org/get")\
        .validate("json().args",{})\
        .validate("json().headers.Accept","application/json")



def test_httpbin_get_with_prams():

    ApiHttpbinGit().set_params(abc=123,xyz=456).run()\
        .validate("status_code",200) \
        .validate("headers.server", "gunicorn/19.9.0")\
        .validate("json().url","http://httpbin.org/get?abc=123&xyz=456") \
        .validate("json().headers.Accept", "application/json")


def test_httpbin_post():
    ApiHttpBinPost()\
        .set_json({"yyy":999})\
        .run()\
        .validate("status_code",200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json().headers.Accept", "application/json")\
        .validate("json().json.yyy",999)


def test_httpbin_parameters_share():
    user_id = "adk129"

    ApiHttpbinGit().set_params(user_id=user_id).run() \
        .validate("status_code", 200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json().url", "http://httpbin.org/get?user_id={}".format(user_id)) \
        .validate("json().headers.Accept", "application/json")

    ApiHttpBinPost() \
        .set_json({"userid": user_id}) \
        .run() \
        .validate("status_code", 200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json().headers.Accept", "application/json") \
        .validate("json().json.userid", "adk129")