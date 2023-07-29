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
baseUrl = "http://www.hao123.com/"

# 这儿定义的是请求的头部信息，复制当前请求中的数据即可。
header = {
    'connection': 'keep-alive',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'ft=1; BAIDUID=FEBA9AB27BF0D97EC0261B5913B2D946:FG=1; traceid=1_+FtATUeqXtAIugH578/w1z2edgMa7e7uxMRVaaxMDsjLk6esCCU+g4OM2GmQlO+1PAwKndK9zYqV+Cw/U+SdyQ; hide_top=1; org=1; s_ht_pageid=16; v_pg=normal; hz=0; Hm_lvt_22661fc940aadd927d385f4a67892bc3=1672129470,1672131537; hword=27; tnwhiteft=XzFYUBclcMPGIANCmytknWnBQaFYTzclnHmLnWD1nHR1rZY; __bsi=7963512770610437250_00_125_R_N_107_0303_c02f_Y; Hm_lpvt_22661fc940aadd927d385f4a67892bc3=1672132147'
}


def get_hao123():
    try:
        sleep(random.uniform(1, 2))  # 随机出现1-2之间的数，包含小数，休眠1-2秒
        try:
            response = requests.get(baseUrl, headers=header)
            if response.ok:
                re = response.text
                return re  # 返回解析内容
            else:
                print("请求失败，请重新请求！") # 网页重定向或者请求404
        except requests.ConnectionError as e:
            print('Error', e.args)  # 输出请求异常信息
    except(TimeoutError, Exception):
            print("请求失败，请重新请求！")

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
                    WebName_url = inline_block_wrapper.string +'   '+ inline_block_wrapper.attrs['href'] 
                    strig_list.append(WebName_url)
                except:
                    continue
            print("\n\r".join(strig_list))
            # file_handle = open(f'hao123daohang.txt', mode='w', encoding='utf-8')
            # file_handle.write(f"\n".join(strig_list))
    except:
        print("解析出错，请稍后再试！")


def main():
    html = get_hao123()
    deal_data(html)


if __name__ == '__main__':
    main()
