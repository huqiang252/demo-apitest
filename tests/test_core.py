#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tests.api.httpbin import *


def test_version():
    from hogwarts_apitest import __version__
    assert isinstance(__version__, str)


def test_httpbin_get():
    ApiHttpbinGit().run() \
        .validate("status_code", 200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json().url", "http://httpbin.org/get") \
        .validate("json().args", {}) \
        .validate("json().headers.Accept", "application/json")


def test_httpbin_get_with_prams():
    ApiHttpbinGit().set_params(abc=123, xyz=456).run() \
        .validate("status_code", 200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json().url", "http://httpbin.org/get?abc=123&xyz=456") \
        .validate("json().headers.Accept", "application/json")


def test_httpbin_post():
    ApiHttpBinPost() \
        .set_json({"yyy": 999}) \
        .run() \
        .validate("status_code", 200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json().headers.Accept", "application/json") \
        .validate("json().json.yyy", 999)


def test_httpbin_parameters_share():
    '''参数共享'''
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


def test_httpbin_extract():
    api_run = ApiHttpbinGit().run()
    '''参数提取'''
    status_code = api_run.extract("status_code")
    assert status_code == 200

    server = api_run.extract("headers.server")
    assert server == "gunicorn/19.9.0"

    accept_type = api_run.extract("json().headers.Accept")
    assert accept_type == "application/json"


def test_httpbin_setcookies():
    api_run = ApiHttpBinGetCookies() \
        .set_cookies("freeform1", "123") \
        .set_cookies("freeform2", "456") \
        .run()

    freeform1 = api_run.extract("json().cookies.freeform1")
    freeform2 = api_run.extract("json().cookies.freeform2")

    assert freeform1 == "123"
    assert freeform2 == "456"


def test_httpbin_parameters_extract():
    '''参数关联'''
    #step 1: get value
    freeform = ApiHttpBinGetCookies()\
        .set_cookies("freeform","123")\
        .run()\
        .extract("json().cookies.freeform")
    assert freeform == "123"
    #step2: use value as parameter
    ApiHttpBinPost() \
        .set_json({"freeform": freeform}) \
        .run() \
        .validate("status_code", 200) \
        .validate("headers.server", "gunicorn/19.9.0") \
        .validate("json().headers.Accept", "application/json") \
        .validate("json().json.freeform", freeform)

def test_httpbin_login_status():
    #step1: 登录 和 获取cookie
    ApiHttpBinGetSetCookies().set_params(freeform="567").run()

    #step2: 期望 第一个设置的cookie 在 第二个请求中也带上
    resp=ApiHttpBinPost() \
        .set_json({"abc": 123}) \
        .run().get_response()

    request_headers = resp.request.headers
    assert "freeform=567" in request_headers["Cookie"]