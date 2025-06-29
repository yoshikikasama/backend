# typedDictを使用すれば、引数に期待するデータをより明確にできる
from typing import TypedDict, List


class IdListDict(TypedDict):
    ids: List[int]


def validate(data: IdListDict):
    """data['ids']を検査して、含まれる不正なidの一覧を返す。
    """
    pass