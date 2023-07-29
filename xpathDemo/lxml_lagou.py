from lxml import etree

def parse_lagou_file():
    parser = etree.HTMLParser(encoding='utf-8')
    htmlElement = etree.parse("lagou.html", parser=parser)
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))


if __name__ == '__main__':
    parse_lagou_file()
