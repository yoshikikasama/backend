import sys
from pathlib import Path

# ルートディレクトリへのパスを追加
current_dir = Path(__file__).parent
root_dir = current_dir.parent
sys.path.append(str(root_dir))
from merge_sorted_array import Solution


def test_merge1():
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_merge2():
    solution = Solution()
    nums1 = [4, 0, 0, 0]
    m = 1
    nums2 = [1, 2, 3]
    n = 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 3, 4]


# Add more tests to cover edge cases
def test_merge_empty():
    solution = Solution()
    nums1 = []
    m = 0
    nums2 = []
    n = 0
    solution.merge(nums1, m, nums2, n)
    assert nums1 == []
