from bs4 import BeautifulSoup
import urllib
import time
import sys


category = sys.argv[1]
categories = {}
categories['203'] = "earring"
categories['202'] = "ring"
categories['208'] = "hat"
categories['215'] = "watch"
categories['216'] = "glass"
categories['101'] = "shoes_woman"
categories['102'] = "shoes_man"
categories['103'] = "coin_bag"
categories['105'] = "clutch_bag"
categories['111'] = "backpack"
categories['117'] = "suitcase"
categories['6'] = "dresses"
categories['3'] = "skirt"
categories['4'] = "pant"
categories['20'] = "jacket"
categories['10'] = "sock"
categories['15'] = "hoodies"
categories['225'] = "belt"


Url = "http://www.pinkoi.com/browse?subcategory=%s&p=1" % category
filename = categories[category] + ".txt"
web_url = "http://www.pinkoi.com"


def DiveToSoup(url):
    f = urllib.urlopen(url)
    html = f.read()
    soup = BeautifulSoup(html)
    return soup


def get_photo_url(url):
    time.sleep(0.3)
    page = DiveToSoup(url)
    photo_url = page.select('div.photo-holder > a')[0].get('href')
    return [url, photo_url]


def get_photo_list(url):
    page = DiveToSoup(url)
    photo_list = page.select('div.item.g-fav-wrap > a')
    photo_list = map(lambda x: web_url+x.get('href'), photo_list)
    return photo_list


def write_into_file(file_name, _list):
    filename = "url_list/%s" % file_name
    _file = open(filename, 'a')
    for urls in _list:
        photo_name = urls[1].split("/")[4]
        _file.write(",".join(urls) + "," + photo_name + "," + category + "\n")
        get_photo(urls[1])


def get_photo(url):
    time.sleep(0.1)
    photo_name = url.split('/')[4]+".jpg"
    dir_name = "image_detail/"
    urllib.urlretrieve(url, dir_name+photo_name)


def create_url(url):
    url_list = []
    for index in range(1, 21):
        url_list.append(url[:-1]+str(index))
    return url_list

if __name__ == "__main__":
    url_list = create_url(Url)
    for url in url_list:
        lists = map(lambda x: get_photo_url(x), get_photo_list(url))
        write_into_file(filename, lists)
