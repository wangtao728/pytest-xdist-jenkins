# -*-coding:utf-8 -*-
#作者:        ZHIAN
#创建时间:    2019/4/10
import pytest

@pytest.fixture(scope="session")
def open_baidu():
    print("打开百度页面_session")
