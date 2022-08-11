from fake_useragent import UserAgent


class UserAgentDownloadMiddleware(object):
    def process_request(self, request, spider):
        # 设置动态UA.
        request.headers.setdefault(b'User-Agent', UserAgent().chrome)




