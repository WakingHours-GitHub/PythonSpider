import requests
import zipfile
import re
import jsonpath
import pandas as pd
import os
import numpy as np

requests.adapters.DEFAULT_RETRIES = 5
TEMP_ROOT = "./temp/zip"


def test_DPT() -> None:
    # URL = "https://data.worldbank.org.cn/indicator/SH.IMM.IDPT?locations=CN"
    URL = "https://api.worldbank.org/v2/zh/indicator/SH.IMM.IDPT?downloadformat=csv"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32",
        "referer": "https://data.worldbank.org.cn/",

    }
    resp = requests.get(URL, headers=headers)
    # print(resp)
    with open(os.path.join(TEMP_ROOT, "DPT.zip"), "wb") as write:
        write.write(resp.content)
    with zipfile.ZipFile(os.path.join(TEMP_ROOT, "DPT.zip"), 'r') as zip:
        for file in zip.namelist():
            zip.extract(file, os.path.join(TEMP_ROOT, "unzip"))
    file_path = os.path.join(os.path.join(TEMP_ROOT, "unzip"), "API_SH.IMM.IDPT_DS2_zh_csv_v2_4035423.csv")
    # print(file_path)
    file_csv = pd.read_csv(file_path, skiprows=3).loc[:, ["Country Name", '2010', '2011', '2012', '2013',
                                                          '2014', '2015', '2016', '2017', '2018', '2019', '2020',
                                                          ]]
    # print(file_csv.columns)
    """
    Index(['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code',
       '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968',
       '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977',
       '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
       '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004',
       '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
       '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021',
       'Unnamed: 66'],"""

    # file_csv = file_csv[file_csv.loc[:, "Country Name"] == ["中国", "美国"]]
    log = np.array(file_csv["Country Name"] == '美国') | np.array(file_csv["Country Name"] == '中国')
    print(log)


    # print(file_csv[log])
    file_csv[log].to_csv("./DPT.csv", encoding='gb2312')


if __name__ == '__main__':
    test_DPT()
