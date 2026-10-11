


c = "牛逼666"
n = 67
m = 'GGBond'
print(type(c),type(n),type(m))
print(isinstance(c,str),isinstance(n,str),isinstance(m,str))
print('It\'s very good!') # 输出：It's very good!
print("\tGG\n\tBond")
print('我是'+c+'，我喜欢'+m+', 我喜欢'+str(n))
print('我是%s，我喜欢%s，我喜欢%d' % (c,m,n))
print('我是{0}，我喜欢{1}，我喜欢{2}'.format(c,m,n))
print(f'我是{c}, 我喜欢{m}, 我喜欢{n}')
a = input('请输入器官数字：')
b = 13
print('神秘数字：',b+int(a))