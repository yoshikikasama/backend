"""
戻り値がリストの関数のテストで要素数をテストする。
"""
from items import load_items


class TestLoadItems:
    def test_load(self):
        actual = load_items()

        assert len(actual) == 2
        assert actual[0] == {"id": 1, "name": "Coffee"}
        assert actual[1] == {"id": 2, "name": "Cake"}