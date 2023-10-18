from logging import exception
from tkinter.messagebox import RETRY
from turtle import ht
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import random
import requests
from time import sleep
from lxml import etree  # lxml为第三方网页解析库，强大且速度快

# 这儿是真实指向的url地址
baseUrl = "https://www.hao123.com/"

# 这儿定义的是请求的头部信息，复制当前请求中的数据即可。
header = {
    'connection': 'keep-alive',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 's_ht_pageid=16; ft=1; v_pg=normal; hz=0; BAIDUID=F580818A3B0B40C0DC445AB3B548156E:FG=1; traceid=1_JiTey9fZ140Rk%2BvhZt1tOAWKzTLYFNu%2B9qohikA3pEVcvmW%2Fur%2BGBaM%2F3XN79m%2BQ31iHqx1ZjcCwPxa3%2FJy3DQ; Hm_lvt_22661fc940aadd927d385f4a67892bc3=1696773634; Hm_lpvt_22661fc940aadd927d385f4a67892bc3=1696773634; hword=8; tnwhiteft=XzFYUBclcMPGIANCmytknWnBQaFYTzclnHm4PWTLn1m1nMY; hide_top=1; org=1; __bsi=8395199245813335183_00_34_N_N_728_0303_c02f_Y'
}


def get_hao123():
    try:
        response = requests.get(baseUrl, headers=header)
        if response.status_code==200:
            re = response.text
            return re  # 返回解析内容
        else:
            print("请求失败，请重新请求！") # 网页重定向或者请求404
    except requests.ConnectionError as e:
        print('Error', e.args)  # 输出请求异常信息

def deal_data(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        # print(soup.find('div',class_='coolsites-wrapper')) # 打印div 标签为coolsites-wrapper的
        a_eles = soup.select('.coolsites-wrapper > div > ul')
        # print(a_eles)
        for els in a_eles:
            url_type = els.select('li > a')[0]
            # print(url_type.string)   # 类别
            sitm_item = els.select('li > div > a')
            strig_list = [url_type.string]
            for inline_block_wrapper in sitm_item:
                # print(inline_block_wrapper)
                try:
                    # print(inline_block_wrapper.string +'   '+ inline_block_wrapper.attrs['href'])
                    # WebName_url = inline_block_wrapper.string +'   '+ inline_block_wrapper.attrs['href']
                    WebName_url = inline_block_wrapper.attrs['href']
                    print(WebName_url)
                    strig_list.append(WebName_url)
                except:
                    continue
            # print("\n\r".join(strig_list))
            # file_handle = open(f'hao123daohang.txt', mode='w', encoding='utf-8')
            # file_handle.write(f"\n".join(strig_list))
    except:
        print("解析出错，请稍后再试！")


def main():
    html = get_hao123()
    deal_data(html)


if __name__ == '__main__':
    main()
