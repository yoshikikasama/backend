"""
テストをしやすいように条件となる数値を引数として用意する。テストの時に数値を変えて実行する。
"""

NUM_OF_SPAM = 100000

def is_enough_spam(piyo_id):
    if Spam.objects.filter(piyo_id=piyo_id).count() > NUM_OF_SPAM:
        return True
    else:
        return False