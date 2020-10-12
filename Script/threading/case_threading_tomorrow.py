#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_threading_tomorrow.py
@Author: gentle.yu
@Date  : 2020/8/16 15:25
"""

from bs4 import BeautifulSoup
import requests
import os
import time
from tomorrow import threads

# 当前脚本所在的目录
cur_path = os.path.dirname(os.path.realpath(__file__))


def get_img_urls():
    r = requests.get("http://www.baidu.com/link?url=7Rh7uK3xkrBdF0d0IBjdwX23bCUPtFFUG9LFQmgbnpdth1dm21C9oCP2qDPjC1ttUO-vQPYnify8ks1ZvxKxBU2M4rAQE0O0rLQnrOT_ZVlVUWn8IYfAAuuVGL1nzejczQzwMMgV-blCK_SbdAOjSfaZiJdsBCfM11zP2N45MDxRKSpRyRlBCzn6U_mrZkfXc6XjnHf2URKDWhgB3hwW1bVu2QPy25f3QC0wgNaI6AI9c3Zs7yXdk5HJO3VqZQatUZl96vmVE3_t7uNvFvIRw0b8FGbPQ1Lf6Q0Qz85axZku-2PtM9-drKMwqU34ZI8srv5OGaeJ5zUbW-NXh9SpYCAGUZFn7eT_1nCFHUIMhTtd2lHykuiVtTdwQ5Q2bQTtOLpjcymt71FfduXGthos830RGlXPby3NM_UjtIHWxiAV6_gs84iDLsZpL1ErILxpkG3SvHnVfzKGC7eaka1q46j-EScpfzKSNYdiUHAuxuZcQ781ZuvU865_N4gmM4EMvo-P7aGE31bvv-vDsv8w2LfBM-TNVDLjq9sSiA5FGs1Ikcdn-lWuoXH9ZSUHO_LRqkbGN4X2zyvho0vusdVU410IUmkRkIpDNzZiX64Omu_&timg=&click_t=1597566642851&s_info=1519_722&wd=&eqid=803bd60300068ede000000035f38eeb0")
    fengjing = r.content
    soup = BeautifulSoup(fengjing, "html.parser")
    # 找出所有的标签
    images = soup.find_all(class_="lazy")
    return images


@threads(5)
def save_img(imgUrl):
    try:
        jpg_url = imgUrl["data-original"]
        title = imgUrl["title"]
        # print(title)
        # print(jpg_rl)
        # print("")
        # 判断是否有jpg文件夹，不存在创建一个
        save_file = os.path.join(cur_path, "jpg")
        if not os.path.exists(save_file): os.makedirs(save_file)

        with open(os.path.join(save_file, title + ".jpg"), "web") as f:
            f.write(requests.get(jpg_url).content)

    except:
        pass


if __name__ == '__main__':
    t1 = time.time()

    image_urls = get_img_urls()
    for i in image_urls:
        save_img(i)

    t2 = time.time()
    print("总耗时：% .2f秒" %(t2 - t1))
