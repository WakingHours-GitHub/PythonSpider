from fake_useragent import UserAgent



def main() -> None:
    ua = UserAgent() # 创建对象
    print(ua.chrome) # 随机生成chrome的ua信 息
    print(ua.edge) # 随机生成edge的ua信息

    print(ua.random) # 随机产生ua信息。



if __name__ == '__main__':
    main()
