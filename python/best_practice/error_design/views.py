from sys import exc_info
from best_practice.error_design.exceptions import MailReceivingError
import exceptions
import datetime


def get_newest_mail(user):
    """
    ユーザーのメールアドレスに届いている一時間以内の最新のメールを取得する。
    直近一時間以内のメールがない場合、Noneを返す。
    """
    mail_service = service.get_mail_service()

    # MailConnectionError, MailAuthError等が発生する可能性がある
    mail_service.login(user.email, user.password)

    # MailConnectionError, MailHeaderError等が発生する可能性がある
    mail = mail_service.get_newest_mail()

    if mail.date < datetime.now() - datetime.timedelta(hours=1):
        return None
    return mail


def newmail(request):
    try:
        mail = get_newest_mail(request.user)
    except exceptions.MailReceivingError as e:
        # 自作した例外の基底クラスでexceptしているため、継承している3つの例外クラスどれでも捕まえられる
        # ログにWARNINGレベルで例外発生時のトレースバック出力
        logger.warning('Mail Receiving Error', exc_info=True)
        # 異常系専用のテンプレートを使って、発生したエラーのメッセージを画面表示
        return render(request, 'mail-receiving-error.html',
                      context={'message': str(e)})
    else:
        if mail is None:
            # 正常系のメッセージをわかりやすく表示
            return render(request, 'no-mail.html',
                          context={'message': '一時間以内のメールはありません'})
    context = {
        'from': mail.from_,
        'to': mail.to,
        'date': mail.date,
        'subject': mail.subject,
        'except': mail.body[:100]
    }
    return render(request, 'new-mail.html', context=context)
