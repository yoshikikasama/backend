import enum


# Permission
class Perm(enum.IntFlag):
    # Read
    R = 4
    # Write
    W = 2
    # Execute
    X = 1


# linux系のファイル操作権限の確認に使用
print(Perm.R | Perm.W)
print(repr(Perm.R | Perm.W | Perm.X))
RWX = Perm.R | Perm.W | Perm.X
print(Perm.W in RWX)

db = {
    'stack1': 1,
    'stack2': 2
}


# @enum.unique
class Status(enum.IntEnum):
    ACTIVE = 1
    INACTIVE = 2
    RUNNING = 3


# 文字列の比較よりintの比較が処理速度が速い
if db['stack1'] == Status.ACTIVE:
    print('shutdown')
elif db['stack2'] == Status.INACTIVE:
    print('terminate')


# print(Status.ACTIVE)

# for s in Status:
#     print(s)
#     print(type(s))