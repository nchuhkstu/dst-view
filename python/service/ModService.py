import os

from config.cluster_path import cluster_path
from config.databaseConnect import Session
import requests
from bs4 import BeautifulSoup
from pojo.Mod import Mod


class ModService:
    def __init__(self):
        self.session = Session()

    def get(self, mod_id):
        response = requests.get('https://steamcommunity.com/sharedfiles/filedetails/?id={}'.format(mod_id),
                                proxies={'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('div', class_='workshopItemTitle').text
        description = soup.find('div', id='highlightContent').prettify()
        author = next(soup.find('div', class_='friendBlockContent').stripped_strings)
        elements = soup.find('div', class_='detailsStatsContainerRight').find_all('div', class_='detailsStatRight')
        size = elements[0].text
        push_time = elements[1].text
        if len(elements) > 2:
            update_time = elements[2].text
        else:
            update_time = ""
        mod = Mod(mod_id, title, author, description, size, push_time, update_time)
        image_element = soup.find('img', id='previewImageMain')
        image_path = 'D:\\mod图片\\{}'.format(mod_id) + '.jpg'
        if image_element is not None:
            if os.path.exists(image_path):
                os.remove(image_path)
            self.save_image_from_url(image_element['src'], image_path)

        mod_original = self.session.query(Mod).filter(Mod.mod_id == mod_id).first()
        if mod_original is None:
            self.session.add(mod)
        else:
            mod_original.mod_id = mod.mod_id
            mod_original.mod_title = mod.mod_title
            mod_original.mod_author = mod.mod_author
            mod_original.mod_description = mod.mod_description
            mod_original.mod_size = mod.mod_size
            mod_original.mod_push_time = mod.mod_push_time
            mod_original.mod_update_time = mod.mod_update_time
        self.session.commit()
        self.session.close()
        return {'title': title, 'author': author, 'description': description, 'size': size, 'push_time': push_time,
                'update_time': update_time}

    def save_image_from_url(self, image_url, save_path):
        response = requests.get(image_url, proxies={'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'})
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print("图片已成功保存到", save_path)
        else:
            print("无法下载图片：", response.status_code)

    def getMain(self):
        mod_path = os.path.join(cluster_path, 'Master', 'modoverrides.lua')
        with open(mod_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        workshop_ids = [line.split('["workshop-')[1].split('"]')[0] for line in lines if
                        line.strip().startswith('["workshop-')]
        print(workshop_ids)
        mods = []
        mod_results = self.session.query(Mod).filter(Mod.mod_id.in_(workshop_ids)).all()
        mod_dict = {mod.mod_id: {
            'title': mod.mod_title,
            'author': mod.mod_author,
            'description': mod.mod_description,
            'modid': mod.mod_id,
            'size': mod.mod_size,
            'push_time': mod.mod_push_time,
            'update_time': mod.mod_update_time
        } for mod in mod_results}
        for workshop_id in workshop_ids:
            mod = mod_dict.get(workshop_id)
            if mod is not None:
                mods.append(mod)
            else:
                mods.append({
                    'title': '暂无信息',
                    'author': '暂无信息',
                    'description': '暂无信息',
                    'modid': '暂无信息',
                    'size': '暂无信息',
                    'push_time': '暂无信息',
                    'update_time': '暂无信息'
                })
        return mods
