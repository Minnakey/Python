# 2-2 切片操作

# 从类似于 http://www.something.com 的URL中提取区域名

Url = input('Please enter the URL：')

domain = Url[11:-4]

print ('Domain name:' + domain)