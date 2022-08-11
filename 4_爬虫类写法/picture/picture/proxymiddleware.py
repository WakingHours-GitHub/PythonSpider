

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        # 查看下载中间件的源码:
        # request.meta['proxy'] = 'http://ip:port'
        # request.meta['proxy'] = 'http://user:password@id:port'
        request.meta['proxy'] = 'http://27.42.168.46:55481'
        # 我们也可以设置一堆的ip放到Settings中, 然后在这里自己去选择即可.