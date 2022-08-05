import requests
from fake_useragent import UserAgent
from lxml import etree
import pymysql

url = "http://datachart.500.com/ssq/"

# 提取数据
resp = requests.get(url, headers={
    "User-Agent": UserAgent().chrome
})
# resp.encoding = 'gbk'

# 链接数据库:
client = pymysql.connect(
    host="127.0.0.1",
    port=3306,  # 与你安装时设置的端口数一样
    user='root',
    password='root',
    charset='utf-8',
    db=''  # 链接哪个数据库, 一定要已经创建好了数据库
)
cursor = client.cursor()

# 创建sql语句.
sql = 'insert into t_ball values(0, %s, %s, %s)'  # 插入的基础sql语句, t_ball是表名, 然后使用占位符进行占位
select_sql = "select * from t_ball where date_time = %s"


# 解析数据
e = etree.HTML(resp.text)
tr_list = e.xpath('//tbody[@id="tdata"]/tr[not(@class="tdbck")]')
for tr in tr_list:
    date_time = tr.xpath('td[1]/text()')
    red_ball = tr.xpath('td[@class="chartBall01"]/text()')  # 不要在前面加上/, 因为我们不是从根选取
    blue_ball = tr.xpath('td[@class="chartBall02"]/text()')
    print(date_time, red_ball, blue_ball)

    # 对其进行处理 -> 均处理成为字符串
    date_time = date_time[0]
    red_ball = '-'.join(red_ball)
    blue_ball = blue_ball[0]

    # 执行插入语句.
    cursor.execute(sql, [date_time, red_ball, blue_ball])
    # 提交
    client.commit()

    # break

# 结束资源时候的原则: 先创建的后关闭
cursor.close()
client.close()
resp.close()
