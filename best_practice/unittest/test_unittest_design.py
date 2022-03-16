"""ユニットテスト

■テストにテスト対象と同等の実装を書かない

■1つのテストメソッドでは1つの項目のみ確認する
"""
import main
import pytest


def test_calc_md5():
    actual = main.calc_md5('This is Content ')
    assert actual == "e61994e96b20e3965b61de16077e18c7"


class TestValidate:
    # 変数と結果をパラメータでテストコードに渡すことで、1つのテストメソッドで複数パターンのテストを行うことができる
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
