"""
以下の単体テストはテスト対象に関係しないOrganizationのデータまで作成している。
UserがOrganizationに依存しているので仕方無く用意するが、検証したい項目には関係しないので省いたほうが良い。
"""


# from pytest
# from .models import Organization, Post, User

# class TestPostDetailView:
#     @pytest.mark.django_db
#     def test_get(self, client):
#         organization = Organization.objects.create(
#             name="beproud",
#         )
# author = User.objects.create(
#     title="ブログ記事のタイトル",
#     body="ブログ記事の本文",
#     author=author,
#     published_at="2018-11-05T00:00:00+0900",
# )


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
            title="記事タイトル", body="記事本文", author__username="theusername"
        )

        res = client.get(f"/posts/{post.id}/")

        assert res.context_data["title"] == "ブログ記事のタイトル"
        assert res.context_data["body"] == "ブログ記事の本文"
        assert res.context_data["author_name"] == "theusername"
