#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test_version():
    from hogwarts_apitest import __version__
    assert isinstance(__version__, str)  # 校验其是一个字符串


import requests


class ApiHttpbinGit:
    url = "http://httpbin.org/get"
    params = {}
    method = "GET"
    headers = {"accept": "application/json"}

    def set_params(self,**params):
        self.params=params
        return self

    def run(self):
        self.response=requests.get(self.url,
                                   params=self.params,
                                   headers=self.headers)
        return self  #为了链式调用

    def validate(self,key,expected_value):
        actual_value= getattr(self.response,key)  #getattr() 函数用于返回一个对象属性值
        assert actual_value==expected_value
        return self

class ApiHttpBinPost:
    url = "http://httpbin.org/post"
    params = {}
    method = "POST"
    headers = {"accept": "application/json"}
    json = {"abc":123}

    def run(self):
        self.response = requests.post(self.url,
                                      headers=self.headers,
                                      json=self.json)
        return self

    def validate(self,key,expected_value):
        actual_value= getattr(self.response,key)
        assert actual_value==expected_value
        return self


def test_httpbin_get():
    ApiHttpbinGit().run()\
        .validate("status_code",200)\
        # .validate("headers.server","gunicorn/19.9.0")\
        # .validate("json.url","http://httpbin.org/get")


def test_httpbin_get_with_prams():

    ApiHttpbinGit().set_params(abc=123,xyz=456).run()\
        .validate("status_code",200)


def test_httpbin_post():
    # resp = requests.post(
    #     "http://httpbin.org/post",
    #     headers={"accept": "application/json"},
    #     json={"abc": 123}
    # )
    # assert resp.status_code == 200
    # assert resp.headers["server"] == "gunicorn/19.9.0"
    # assert resp.json()['url'] == "http://httpbin.org/post"
    # assert resp.json()['json']['abc']== 123

    ApiHttpBinPost().run()\
        .validate("status_code",200)

