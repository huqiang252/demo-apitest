#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test_version():
    from hogwarts_apitest import __version__
    assert isinstance(__version__, str)  # 校验其是一个字符串


import requests

class BaseApi(object):
    method="GET"
    url=""
    params= {}
    headers= {}
    data = {}
    json = {}

    def set_params(self,**params):
        self.params=params
        return self


    def run(self):
        self.response = requests.request(self.method,
                                         self.url,
                                         params=self.params,
                                         headers=self.headers,
                                         data=self.data,
                                         json=self.json
                                         )
        return self  # 为了链式调用

    def validate(self,key,expected_value):
        actual_value= getattr(self.response,key)  #getattr() 函数用于返回一个对象属性值
        assert actual_value==expected_value
        return self



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
        # .validate("headers.server","gunicorn/19.9.0")\
        # .validate("json.url","http://httpbin.org/get")


def test_httpbin_get_with_prams():

    ApiHttpbinGit().set_params(abc=123,xyz=456).run()\
        .validate("status_code",200)


def test_httpbin_post():

    ApiHttpBinPost().run()\
        .validate("status_code",200)

