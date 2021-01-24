#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import requests

@pytest.fixture(scope='function')
def init_session():
    return requests.sessions.Session()