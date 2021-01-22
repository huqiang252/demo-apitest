#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

    def set_data(self, data):
        self.data = data
        return self

    def set_json(self, json_data):
        self.json = json_data
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