"""
factory-boyを使い、不要なフィクスチャーの作成を不要にする。
factory-boyを使うことでモデル作成に必要なデフォルト値を指定せずに済む。
テストに関係する値のみ指定することで、テストコードを最小限にできる。
"""

import pytest

from factories import OrganizationFactory, PostFactory, UserFactory

class TestPostDetailView:
    @pytest.mark.django_db
    def test_get(self, client):
        post = PostFactory(
            title="記事タイトル",
            body="記事本文",
            author__username="theusername"
        )

        res = client.get(f"/posts/{post.id}/")

        assert res.context_data["title"] == "ブログ記事のタイトル"
        assert res.context_data["body"] == "ブログ記事の本文"
        assert res.context_data["author_name"] == "theusername"