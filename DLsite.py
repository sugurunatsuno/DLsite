import requests
from bs4 import BeautifulSoup


class Product:

    def __init__(self, url):
        request = requests.get(url, timeout=5)
        if request.status_code != 200:
            return

        self.__soup = BeautifulSoup(request.text, 'lxml')
        self.title = self.__soup.select_one(
            '#work_name').text.replace('\n', '')
        self.circle_name = self.__soup.find(
            class_='maker_name').text.replace('\n', '')
        self.description = self.__soup.find(
            class_='work_parts type_text').text.replace('\n', '').replace('\r', '\n')

        outline = self.__soup.find(id='work_outline')

        th = outline.find_all('th')
        td = outline.find_all('td')
        for i, label in enumerate(th):
            current_label = label.text
            current_value = td[i]

            if current_label == '販売日':
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
                elements = current_value.find_all('a')
                self.file_format = [e.text for e in elements]

            if current_label == 'イベント':
                self.event = current_value.text.replace('\n', '')

            if current_label == 'ジャンル':
                elements = current_value.find_all('a')
                self.genre = [e.text for e in elements]

            if current_label == 'ファイル容量':
                self.file_size = current_value.text.replace(
                    '\n', '').replace(' ', '')

            if current_label == 'シナリオ':
                self.scenario = current_value.text.replace('\n', '')

            if current_label == 'イラスト':
                self.illustrator = current_value.text.replace('\n', '')

            if current_label == 'シリーズ名':
                self.series = current_value.text.replace('\n', '')

            if current_label == '声優':
                elements = current_value.find_all('a')
                self.voice_actor = [e.text for e in elements]

    def __str__(self):
        maker = ','.join(self.author) if hasattr(
            self, 'author') else ','.join(self.voice_actor)
        return f"{self.title}: {maker}({self.circle_name})"

    def __repr__(self):
        return self.__str__()
