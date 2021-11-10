# 在headers中带有字典
# 首先是登录你要爬取的网站
# 然后利用network抓包工具, 在请求头(request headers)抓取cookie
# 然后写成字典, 放入到headers里面去

# 这里访问github为例:
import requests

url = "https://github.com/"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44",
    # "cookie": "octo=GH1.1.1710039104.1633267756; _device_id=1ef39710a6404fd18719261525028132; "
    #           "user_session=iE9F-ID8zvORcUOUTaDgpEj4FtG2TjItZc5GLoqghwd2suWy; "
    #           "__Host-user_session_same_site=iE9F-ID8zvORcUOUTaDgpEj4FtG2TjItZc5GLoqghwd2suWy; logged_in=yes; "
    #           "dotcom_user=WakingHours-GitHub; has_recent_activity=1; "
    #           "color_mode=%7B%22color_mode%22%3A%22light%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C"
    #           "%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22"
    #           "%3A%22dark%22%7D%7D; tz=Etc%2FGMT-8; "
    #           "_gh_sess=Ts%2FMX"
    #           "%2Fm0Gi3au1WetGI7DyWfkHPVH8jy4i3OStcfyg7QxjTTnyP2Fp9i5GL40VOtJYIes5WyHldpVfDLtyFlj8RZyHfIX1cZXIiiksg4A5kx5lEvQa4bJU9HnrvGgKvEeLcQVuZVixbJpPBsI0woFdam8hkxvK2FCPSAh6OMrZIBq7S%2B9%2BlYQ7rCIDuEF%2Bk3--h7Ehrax7LPtehMcm--CFiYgnpaKYP7Lo8cLfia9Q%3D%3D "
}

resp = requests.get(url, headers=headers)

print(resp.text)
