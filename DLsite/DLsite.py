import requests
from bs4 import BeautifulSoup


class Product:
    def __init__(self, url):
        request = requests.get(url)
        if request.status_code != 200:

            return
        self.__soup = BeautifulSoup(request.text, 'lxml')

        self.title = self.__soup.select_one('h1 a').text.replace('\n', '')
        self.circle_name = self.__soup.find(class_='maker_name').text
        self.description = self.__soup.find(class_='work_article work_story').text.replace('<br>', '')
        outline = self.__soup.find(id='work_outline')
        th = outline.find_all('th')
        td = outline.find_all('td')
        for i in range(len(th)):
            current_label = th[i].text
            current_value = td[i]

            if current_label == '発売日':
                self.release_date = current_value.text.replace('\n', '')
            if current_label == '最終更新日':
                self.last_updated = current_value.text.replace('\n', '')
            if current_label == '作者':
                elements = current_value.find_all('a')
                self.author = [e.text for e in elements]
            if current_label == '年齢指定':
                self.rate = current_value.text.replace('\n', '')
            if current_label == '作品形式':
                self.product_format = current_value.text.replace('\n', '')
            if current_label == 'ファイル形式':
                self.file_format = current_value.text.replace('\n', '')
            if current_label == 'イベント':
                self.event = current_value.text.replace('\n', '')
            if current_label == 'ジャンル':
                elements = current_value.find_all('a')
                self.genre = [e.text for e in elements]
            if current_label == 'ファイル容量':
                self.file_size = current_value.text.replace('\n', '')
            if current_label == 'シナリオ':
                self.scenario = current_value.text.replace('\n', '')
            if current_label == 'イラスト':
                self.illustrator = current_value.text.replace('\n', '')
            if current_label == '声優':
                elements = current_value.find_all('a')
                self.voice_actor = [e.text for e in elements]

    def __str__(self):
        maker = ','.join(self.author) if hasattr(self, 'author') else ','.join(self.voice_actor)
        return "{}: {}({})".format(self.title, maker, self.circle_name)

    def __repr__(self):
        return self.__str__()
