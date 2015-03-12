from bs4 import BeautifulSoup
import urllib
import time

Url = "http://www.pinkoi.com/browse/%E9%85%8D%E4%BB%B6%E9%A3%BE%E5%93%81?category=2&archive=0&sortby=rank&order=desc&p=3"
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
    _file = open(filename, 'w')
    for urls in _list:
        _file.write(','.join(urls)+"\n")
        get_photo(urls[1])


def get_photo(url):
    time.sleep(0.1)
    photo_name = url.split('/')[4]+".jpg"
    dir_name = "image/"
    urllib.urlretrieve(url, dir_name+photo_name)


if __name__ == "__main__":
    lists = map(lambda x: get_photo_url(x), get_photo_list(Url))
    write_into_file("accessory.txt", lists)