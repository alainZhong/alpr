#输入用户名或和密码，判断登录成功

name=input('请输入名称：')
password=input('请输入密码：')

if name=='alain' and password=='12345':
    print('登录成功')
else:
    print('不正确')

#注意在做判断时，需要使用==
#if else 后都用：