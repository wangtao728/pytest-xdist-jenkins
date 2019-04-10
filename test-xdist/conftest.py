# -*-coding:utf-8 -*-
#作者:        ZHIAN
#创建时间:    2019/4/10
import pytest

@pytest.fixture(scope="session")
def start():
    print("\n打开首页")
    return "yoyo"