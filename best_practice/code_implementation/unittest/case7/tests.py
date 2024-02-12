from unittest import mock


def test_is_enough_spam(self):
    from hoge.tests.factories import SpamFactory

    piyo_id = 9
    SpamFactory(piyo_id=piyo_id)
    SpamFactory(piyo_id=piyo_id)

    # NUM_OF_SPAM = 1として置き換えられる
    with mock.patch('hoge.NUM_OF_SPAM', new=1):
        from hoge import is_enough_spam

        actual = is_enough_spam(piyo_id=piyo_id)
    
    self.assertTrue(actual)