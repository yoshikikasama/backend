import re

RE_STACK_ID = re.compile(r"""
    arn:aws:cloudformation:
    (?P<region>[\w-]+):
    (?P<account_id>[\d]+)
    :stack/
    (?P<stack_name>[\w]+)""", re.VERBOSE)

s1 = ('arn:aws:cloudformation:us-east-2:1234568:stack/'
     'dsdfkdngkdnglkdnfgld')
s2 = ('arn:aws:cloudformation:us-east-2:1234568:stack/'
     'dsdfkdngkdngfdfdddffffgld')

# m = re.match(
#     (r'arn:aws:cloudformation:(?P<region>[\w-]+):(?P<account_id>[\d]+)'
#      ':stack/(?P<stack_name>[\w]+)'), s)
for s in [s1, s2]:
    m = RE_STACK_ID.match(s)
    if m:
        print(m.group('region'))
        print(m.group('account_id'))
        print(m.group('stack_name'))

    else:
        raise Exception('Error!')
