# 导包
import unittest
from unittest import mock

# 创建测试类
from samply import UserService, OrderPayService


class TestPay(unittest.TestCase):
    def test01(self):
        # 测试金额为2001时的支付结果
        # 由于用户余额查询接口出现了问题，所以不能正常返回的用户的余额，这个时候
        # 我们需要使用mock模块来替换用户余额查询接口的返回值，最后进行支付。
        UserService.get_user_amount = mock.Mock(return_value=2001)

        # 初始化支付接口
        ops = OrderPayService()
        # 进行支付
        result = ops.order_pay()
        print("支付结果为：", result)

        # 断言
        self.assertEqual(1, result.get('status'))
        self.assertEqual(1, result.get('account_remain'))

    # 测试金额为2001时的支付结果

    # 测试金额为1999时的支付结果

    # 测试抛出异常场景
