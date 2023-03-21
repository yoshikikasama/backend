from settings import CommonEnv, SpecialEnv


sample_a = 'test_a'
sample_b = 'test_b'
sample_c = 'test_c'


common_env = CommonEnv(sample_a, sample_b)
special_env = SpecialEnv(sample_c)

print("common_env.sample_a:", common_env.sample_a)
print("common_env.sample_b:", common_env.sample_b)
print("special_env.sample_c:", special_env.sample_c)

special_env.messages = 'test_1'
print("special_env.messages 1回目:", special_env.messages)
special_env.messages = 'test_2'
print("special_env.messages 2回目:", special_env.messages)
