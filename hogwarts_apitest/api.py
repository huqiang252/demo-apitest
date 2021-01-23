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
        return self

    def validate(self,key,expected_value):
        value = self.response
        for _key in key.split("."):
            # print("调试前==>", _key, value,type(value), expected_value)
            if isinstance(value,requests.Response):
                if _key=="json()":
                    value=self.response.json()
                else:
                    value = getattr(value, _key)
            elif isinstance(value,(requests.structures.CaseInsensitiveDict,dict)):
                value=value[_key]


        assert value==expected_value
        return self