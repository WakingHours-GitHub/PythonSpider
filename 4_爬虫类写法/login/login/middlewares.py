from fake_useragent import UserAgent

class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        request.headers.setdefault(b'User-Agent', UserAgent().chrome)


        return None