# -*-coding:utf-8 -*-
#作者:        ZHIAN
#创建时间:    2019/4/10
import pytest

@pytest.fixture(scope="function")
def open_blog():
    print("打开blog页面_function")