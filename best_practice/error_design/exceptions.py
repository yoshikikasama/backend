

class MailReceivingError(Exception):
    pretext = ''

    def __init__(self, message, *args):
        if self.pretext:
            message = f"{self.pretext}: {message}"
        super().__init__(message, *args)


class MailConnectionError(MailReceivingError):
    pretext = '接続エラー'


class MailAuthError(MailReceivingError):
    pretext = '認証エラー'


class MailHeaderError(MailReceivingError):
    pretext = 'メールヘッダーエラー'
