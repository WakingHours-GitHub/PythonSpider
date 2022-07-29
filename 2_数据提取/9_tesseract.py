"""
解决验证码问题
步骤:
    获取登录页面
    获取验证码
    处理验证码
    发送登录请求 -> 处理好请求头

    保证是一个session. 必须是同一个会话.

处理验证码的几种方案:
    手打
    图像识别 -> 参考我自己的深度学习项目
    云打码平台

图像识别工具: Tesseract介绍
一个谷歌支持的开源项目. 支持ocr识别.
不过识别率不是很高, 需要手动训练. 

"""
import pytesseract
from PIL import Image # 读取, 展示图像


img = Image.open("./code.png")  # 读取图片
code = pytesseract.image_to_string(img)
print(code)





