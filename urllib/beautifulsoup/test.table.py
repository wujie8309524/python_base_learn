#!/usr/bin/env python3.6
from bs4 import BeautifulSoup

html = '''
    <table>
        <tr><td>标题</td><td>内容</td><td>作者</td><td>时间</td></tr>
        <tr><td>测试1</td><td>测试1的内容</td><td>wj1</td><td>2018-01-01</td></tr>
        <tr><td>测试2 </td><td>测试1的内容</td><td>wj1</td><td>2018-01-01</td></tr>
        <tr>
            <td>测试3 <b> test </b> </td>
            <td>测试2的内容 <a href='www.baidu.com'>www.baidu.com<a></td>
            <td><div id ='test'>wj2</div></td>
            <td>2018-02-02</td>
        </tr>
    </table>
    
'''
# soup = BeautifulSoup(html_cont, 'html.parser',from_encoding='utf-8')

soup = BeautifulSoup(html,'lxml')

table = soup.find('table')
print(type(table))
print(table)

print("========== 开始解析 ========\n\r")
i = 1
for tr in table.find_all('tr'):
    print("\n\r======= 第%d行 =====" % i)
    for td in tr.find_all('td'):

        print("===== 结果 ======")
        # td.string 如果不是纯文本，包含子节点无法获取内容
        # td.get_text() 可以获取该节点下的文本内容，包括子节点的内容
        print(td.get_text())
        print("\n\r")

    i += 1

print("======== 放入 dict =======")

data_list = []

'''
获取内容：
    string
        navigablesString 对象不包括其他tag，可直接获取
        如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点:
        如果一个tag仅有一个子节点,那么这个tag也可以使用 .string 方法,输出结果与当前唯一子节点的 .string 结果相同:
        如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None :    
    get_text("|",strip=True)
        navigablesString 对象有子节点tag时，将各tag内容用 | 分割，并去除空格
    .contents 当没有子节点时报错
        navigablesString 对象有子节点tag时，返回一个tag list

'''

for index,tr in enumerate(soup.table.find_all('tr')):
    # 去掉标题
    if index != 0:
        tds = tr.find_all('td')
        print(tds[0].get_text("|",strip=True),tds[1].contents,tds[2].get_text())
        data_dict = dict(标题=tds[0].get_text(), 作者=tds[2].get_text())
        data_list.append(data_dict)


print(data_list)