from bs4.element import Tag
from bs4 import BeautifulSoup

html = """
	<div class="box">
		<div>
			<p>第零行数据</p>
		</div>
		<p class="line1">第一行数据</p>
		<p class="line1">第二行数据</p>
		<p id="line3">第三行数据</p>
		<a href="www.baidu.com">百度</a>
	</div>
	<p class="line4">第四行数据</p>
	<form>
		<input type="text" name="username"><p></p>
		<input type="password" name="password">
	</form>
	<div>这是一个div</div>
"""

soup = BeautifulSoup(html, "lxml")
div = soup.find("div")
for element in div.children:
    print(element)
    print("=" * 30)
