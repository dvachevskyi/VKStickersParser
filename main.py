import requests

from bs4 import BeautifulSoup

def default_headers() -> dict:
    return {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "upgrade-insecure-requests" : "1",
        "cookie" : ""
    }

def main():
    response = requests.get('https://vk.com/stickers')
    response.encoding = 'windows-1251'
    soup = BeautifulSoup(response.text, 'lxml')
    array_a = soup.find_all('a', class_='im_sticker_bl')
    for a in array_a:
        name_a = a.find('div', class_='im_sticker_bl_name').text
        id_sticker = a.find('div', class_='im_sticker_bl_demo im_sticker_bl_demo_background')
        if id_sticker:
            id_sticker = str(id_sticker).split("<div class=\"im_sticker_bl_demo im_sticker_bl_demo_background\" style=\"background-image: url(https://vk.com/images/store/stickers/")
            id_sticker = id_sticker[1].split('/background.png)"> <div class="sticker_animatio')
            id_sticker = id_sticker[0]
            pass
        else:
            id_sticker = a.find('img', class_='im_sticker_bl_demo_thumb')
            id_sticker = str(id_sticker).split("<img class=\"im_sticker_bl_demo_thumb\" height=\"188\" src=\"https://vk.com/images/store/stickers/")
            id_sticker = id_sticker[1].split('/preview1_296.jpg"')
            id_sticker = id_sticker[0]
            pass
        responseq = requests.get('https://m.vk.com/stickers?stickers_id='+id_sticker, headers=default_headers());
        response.encoding = 'windows-1251'
        if "Получить за" in responseq.text:
            soupq = BeautifulSoup(responseq.text, 'lxml')
            vfivj = soupq.find_all('div', class_='op_block')
            price = str(vfivj[1]).split(">Получить за ")[1].split(" голос")[0]
            print(name_a+' : '+id_sticker+' : '+price)
            f = open('stickers.txt' , 'a')
            f.write(name_a+' : '+id_sticker+' : '+price+"\n")
            f.close()
    return

if __name__ == '__main__':
    main()
