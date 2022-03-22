"""
変数と結果をパラメータでテストコードに渡すことで、1つのテストメソッドで複数パターンのテストを行うことができる

"""

import main
import pytest


def test_calc_md5():
    actual = main.calc_md5('This is Content ')
    assert actual == "e61994e96b20e3965b61de16077e18c7"


class TestValidate:
    @pytest.mark.parametrize('text', ['a', 'a' * 50, 'a' * 100])
    def test_valid(self, text):
        """検証が正しい場合
        """
        # Trueでreturnされるかどうか
        assert main.validate(text)

    @pytest.mark.parametrize('text', ['', 'a' * 101])
    def test_invalid(self, text):
        """検証が正しくない場合
        """
        # Falseでreturnされるかどうか
        assert not main.validate(text)


# 読みやすくするためにテストコードを準備(Arrange)と実行(Act)と検証(Assert)に
class TestSignupAPIView:

    # fixture：テストの前処理を行うための機能
    @pytest.fixture
    def target_api(self):
        return '/api/signup'

    def test_do_signup(self, target_api, django_app):
        # 準備
        from account.models import User

        params = {
            "email": "signup@example.com",
            "name": "yamadataro",
            "password": "xxxxxx"
        }
        # 実行
        res = django_app.post_json(target_api, params=params)

        # 検証
        user = User.objects.all()[0]
        expected = {
            "status_code": 201,
            "user_email": "signup@example.com"
        }
        actual = {
            "status_code": res.status_code,
            "user_email": user.email
        }
        assert expected == actual
