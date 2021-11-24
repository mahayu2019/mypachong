#!/usr/bin/env python
# coding=utf-8

'''
目标页
https://bbs.mihoyo.com/dby/home/47?type=2
'''

import requests
import time


# 封装requests
def get_requests(url, ret_type='text', timeout=5, encoding='utf-8', host="bbs-api.mihoyo.com"):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Origin": "https://bbs.mihoyo.com",
        "Referer": "https://bbs.mihoyo.com/",
        "Host": host
    }

    res = requests.get(url=url, headers=headers, timeout=timeout)
    res.encoding = encoding

    # 三种返回类型???
    if ret_type == 'text':
        return res.text

    elif ret_type == 'image':
        return res.content

    elif ret_type == 'json':
        return res.json()


# 抓取函数
def main(last_id):
    # 起始页
    if last_id != 0:
        url = f'https://bbs-api.mihoyo.com/post/wapi/getForumPostList?' \
              f'forum_id=47&gids=5&is_good=false&is_hot=false&last_id={last_id}&page_size=20&sort_type=2'
    else:
        url = f'https://bbs-api.mihoyo.com/post/wapi/getForumPostList?' \
              f'forum_id=47&gids=5&is_good=false&is_hot=false&page_size=20&sort_type=2'
    res_json = get_requests(url, ret_type='json', timeout=5)
    # print(res_json)
    if res_json['retcode'] == 0:
        for item in res_json['data']['list']:
            post_id = item['post']['post_id']
            detail(post_id)

    # 回调函数,利用last_id往下翻页检索数据
    # if res_json['data']['last_id'] != '':
    #     return main(res_json['data']['last_id'])


# 内页获取
def detail(post_id):
    url = f'https://bbs-api.mihoyo.com/post/wapi/getPostFull?' \
          f'gids=5&post_id={post_id}&read=1'
    res_json = get_requests(url, ret_type='json', timeout=5)
    if res_json['retcode'] == 0:
        image_list = res_json['data']['post']['image_list']
        for img in image_list:
            img_url = img['url']
            if (img_url.find('weigui')) < 0:
                # print(img_url)
                save_image(img_url)


# 保存
def save_image(img_url):
    content = get_requests(img_url, 'image', host='upload-bbs.mihoyo.com')
    # with open(f'{str(time.time())}.jpg', 'wb') as f:
    #     f.write(content)
    #     global total
    #     total += 1
    #     print(f'保存{total}张图片')


if __name__ == '__main__':
    global total
    total = 0
    main(0)  # 初始翻页last_id
