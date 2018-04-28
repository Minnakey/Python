# 2-4 序列成员资格

# 检查用户名和PIN码

database = [
    ['albert', '1234'],
    ['dilbert','4242'],
    ['simth','7542'],
    ['jones','9843']
]

username = input('User name: ')
pin = input('PIN code：')

if [username,pin] in database : print('Access granted.')