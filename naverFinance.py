import requests
from bs4 import BeautifulSoup
from save import save_to_file

URL = "https://finance.naver.com/research/company_list.nhn"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    links = soup.find("table", {"class": "Nnavi"}).find_all("a")
    pages = [];
    for link in links[:-2]:
        pages.append(int(link.string))

    max_page = pages[-1]
    # print(max_page)
    return max_page


def get_finance_data(html):
    # print(html)
    date_created = html.find_all("td", {"style": "padding-left:5px"})

    # 작성일
    dates = []
    for date in date_created:
        # print(date.string)
        dates.append(date.string)

    # 회사이름, 리포트 제목
    contents = []
    company = []
    report_title = []
    find_content = html.find_all("a")
    for content in find_content:
        # print(content.get_text())
        if (content.get_text()) is not '':
            contents.append(content.get_text())

    for i in range(0, len(contents)):
        if (i % 2) is 0:
            company.append(contents[i])
        else:
            report_title.append(contents[i])

    # print(company[0])
    # print(report_title)
    # print(dates)
    total = []
    for i in range(0, len(company)):
        diction_data = {
            "company": company[i],
            "report_title": report_title[i],
            "date": dates[i]
        }
        total.append(diction_data)
    return total
    # print(len(contents))


def get_finance_datas(last_page):
    datas = []
    for page in range(last_page):
        print(f"Scrapping Naver Finance Page:{page + 1}")
        result = requests.get(f"{URL}?&page={page + 1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("table", {"class": "type_1"})
        for result in results:
            data = get_finance_data(result)
            datas.append(data)

    return datas

def get_data():
    last_page = get_last_page()
    datas = get_finance_datas(last_page)
    return datas