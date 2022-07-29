# 测试验证码登录url
import requests
from fake_useragent import UserAgent

log_url = "https://login.sina.com.cn/sso/prelogin.php"
code_url = "https://login.sina.com.cn/cgi/pin.php"
info_url = "https://s.weibo.com/weibo?q=%E7%A6%BB%E8%B0%B1"
# 因为要登录和获取本次登录的code, 所以要使用session保持会话.
session = requests.session()
headers = {
    'User-Agent': UserAgent().random,
    'referer': "https://weibo.com/"
}

def main() -> None:

    log_resp = session.get(log_url, headers=headers)

    code_resp = session.get(code_url, headers=headers)
    with open("temp_code.png", 'wb') as f:
        f.write(code_resp.content) # 保存, 方便后续识别.

def info_url_test():
    resp = session.get(info_url, headers=headers)
    session.cookies='SINAGLOBAL=9480666690576.453.1658799436663; UOR=,,cn.bing.com; PC_TOKEN=cab63d1f5c; login_sid_t=a198aad36a52d7d43261f8caaf311b20; cross_origin_proto=SSL; _s_tentry=weibo.com; Apache=1114494078458.7742.1659064689066; ULV=1659064689070:3:3:3:1114494078458.7742.1659064689066:1659009551392; appkey=; WBtopGlobal_register_version=2022072911; ALF=1690602234; SSOLoginState=1659066234; SUB=_2A25P5ycqDeRhGeNK7lUX9ibKzD6IHXVslR_irDV8PUNbmtB-LWfEkW9NSU_QhWWbuge7tbsxILpRpoOluXJPFicT; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWWdSamvN.9ELP5sRjLJ2.H5JpX5KzhUgL.Fo-XSKMcSoncS0z2dJLoIXnLxKqL1hnL1K2LxKML1-2L1hBLxKnL1heLB.BLxK-L122L1-zLxK-LBKBLBKMLxKBLB.2L12-LxKnLB.qL1K5LxKqLBo5L1KBt'
    resp.encoding = 'gb2312'
    print(resp.text)

if __name__ == '__main__':
    # main()
    info_url_test()
