import unittest
from asyncio import sleep
from unittest import mock
# 实现加法操作
def add(x, y):
    print("该方法还未完成...")
    sleep(1)
    return 0
class TestAdd(unittest.TestCase):
    def test_add(self):
# 使用mock模拟加法计算的方法，返回一个预定的结果
      add = mock.Mock(return_value=10)
      result = add(2, 8)
      print("result=", result)
      self.assertEqual(10, result)