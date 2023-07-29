from lxml import etree
import requests

BASE_URL = "https://dytt8.net/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}


def get_detali_url(url):
    resp = requests.get(url, headers=HEADERS)
    html = resp.text
    html_text = etree.HTML(html)
    detali_urls = html_text.xpath("//table[@class='tbspan']//a[@class='ulink']/@href")
    detali_urls = map(lambda url: BASE_URL + url, detali_urls)
    return detali_urls

def parse_datali_url(url):
    movie = {}
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['title'] = title
    ZooEs = html.xpath("//div[@id='Zoom']")[0]
    cover = ZooEs.xpath(".//img/@src")[0]
    download = ZooEs.xpath(".//a/@href")[0]
    movie['cover'] = cover
    movie['download'] = download

    def parse_info(info, rule):
        return info.replace(rule, "").strip()
    infos = ZooEs.xpath(".//text()")
    for index, info in enumerate(infos):
        if info.startswith("◎年　　代"):
            info = parse_info(info, "◎年　　代")
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = parse_info(info, "◎产　　地")
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info, "◎类　　别")
            movie['category'] = info
        elif info.startswith("◎豆瓣评分"):
            info = parse_info(info, "◎豆瓣评分")
            movie['douban_rating'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info, "◎片　　长")
            movie['durating'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info, "◎导　　演")
            movie['director'] = info
        elif info.startswith("◎演　　员"):
            info = parse_info(info, "◎演　　员")
            actors = [info]
            for x in range(index+1, len(infos)):
                actor = infos[x]
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie['actors'] = actors
        elif info.startswith("◎简　　介"):
            info = parse_info(info, "◎简　　介")
            for x in range(index+1, len(infos)):
                profile = infos[x].strip()
                if profile.startswith("◎获奖情况"):
                    break

    return movie


def spider():
    base_url = "https://dytt8.net/html/gndy/dyzz/list_23_{}.html"
    movies = []
    for x in range(1, 8):
        url = base_url.format(x)
        # 这儿的url只是获取到当前第几页
        detali_urls = get_detali_url(url)
        for detali_url in detali_urls:
            # 第二个for获取到的电影的详情页
            # print(detali_url)
            movie = parse_datali_url(detali_url)
            movies.append(movie)
            print(movie)
            break
        break


if __name__ == '__main__':
    spider()
