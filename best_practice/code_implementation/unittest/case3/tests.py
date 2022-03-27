"""
単体テストから外部環境への依存を排除する。
responsesを使ってrequestのmock化
"""
import responses
import json
from api import get_post, post_to_sns


class TestPostToSNS:
    @responses.activate
    def test_post(self):
        # 外部環境へのアクセスをmock化
        responses.add(responses.POST, "https://the-sns.example.com/posts",
                      json={"body": "レスポンス本文"})
        data = post_to_sns("投稿の本文")
        assert data['body'] == "レスポンス本文"

        # 外部アクセスが呼び出されたことの確認
        assert len(responses.calls) == 1
        assert json.loads(responses.calls[0].request.body) == {'body': '投稿の本文'}
