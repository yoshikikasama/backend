# 本来は別のテスト使うテストデータ生成関数をimport
# square_listという関数をテストするためにたまたま他のテストで用意した整数のリストを返す関数get_other_fixturesを利用している
# この状態で他の開発者が別のテストを修正する目的でget_other_fixtures関数の戻り値を変更したらTestSquareListのテストケースは失敗する

# from spam.tests.other_fixtrures import get_other_fixture


# class TestSquareList:
#     def test_square(self):
#         # Arrange
#         from spam import square_list

#         test_list = get_other_fixture()
#         # Act
#         actual = square_list(test_list)

#         # Assert
#         expected = [1, 4, 5]
#         assert actual == expected


# 個々のテストケースの中でのみ有効なfixtureを用意して他のテストには影響を与えないようにする
class TestSquareList:
    def test_square(self):
        # Arrange
        from spam import square_list

        test_list = [1, 2, 3]
        # Act
        actual = square_list(test_list)

        # Assert
        expected = [1, 4, 9]
        assert actual == expected


# factory-boyでもfixtureをテストケースの中で指定する
class TestSquareList:
    def test_square(self):
        # Arrange
        from spam.hoge import get_spam_by_name

        spam = SpamFactory(name="spam1")

        # Act
        actual = get_spam_by_name(spam.name)

        # Assert
        assert actual.name == "spam"


# 検証まで含めてデフォルト値を使って検証する方法もある。デフォルト値が変わってもテストは失敗しない。
class TestSquareList:
    def test_square(self):
        # Arrange
        from spam.hoge import get_spam_by_name

        spam = SpamFactory()

        # Act
        actual = get_spam_by_name(spam.name)

        # Assert
        assert actual.name == spam.name
