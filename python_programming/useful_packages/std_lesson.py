import contextlib
import sys
import logging

# for line in sys.stdin:
#     print(line)
with open('stdout.log', 'w') as f:
    # stdoutのredirect先をconsole→fileに変更
    with contextlib.redirect_stdout(f):
        print('hello')
# print('hello')
# sys.stdout.write('hello')
with open('stderr.log', 'w')as f:
    with contextlib.redirect_stderr(f):    
        logging.error('Error!')
# sys.stderr.write('Error')
