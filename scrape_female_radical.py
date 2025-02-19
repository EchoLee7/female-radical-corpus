import requests
from bs4 import BeautifulSoup
import json
import time

# 目标网站（以汉典为例）
BASE_URL = "https://www.zdic.net/hans/"

# 需要爬取的汉字列表（这里只是示例，后面可以爬取包含“女”部首的所有汉字）
characters = ["女", "妈", "婉", "妖", "娜", "嫉", "妒", "嬉", "媳", "娇", "媚"]

# 定义情感分类
positive_words = {"婉", "娴", "媛", "娜", "娇"}
negative_words = {"妖", "妒", "婪", "嫉"}
neutral_words = {"女", "妈", "姐", "媳"}

# 结果存储
data = []

for char in characters:
    url = BASE_URL + char
    response = requests.get(url)
    time.sleep(1)  
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")

        # 提取拼音（网站结构可能变化，需检查 HTML 结构）
        pinyin_tag = soup.find("span", class_="dicpy")
        pinyin = pinyin_tag.text.strip() if pinyin_tag else "未知"

        # 自动分类情感
        if char in positive_words:
            sentiment = "褒义"
        elif char in negative_words:
            sentiment = "贬义"
        else:
            sentiment = "中性"

        # 存储数据
        data.append({"字": char, "拼音": pinyin, "部首": "女", "情感分类": sentiment})
        print(f"✅ 已爬取：{char}（拼音：{pinyin}，分类：{sentiment}）")
    else:
        print(f"❌ 爬取失败：{char}")

# 保存到 JSON 文件
with open("female_radical_corpus.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("✅ 所有数据已保存到 female_radical_corpus.json！")
