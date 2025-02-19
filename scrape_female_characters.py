import requests
from bs4 import BeautifulSoup
import json
import time

# 部首查询页面（示例：从汉典或其他部首查询网站获取）
ROOT_URL = "https://bihua.51240.com/nv__bihuachaxun/"

# 目标网站（汉典，每个汉字单独查询）
DETAIL_URL = "https://www.zdic.net/hans/"

# 定义情感分类
POSITIVE_WORDS = {"婉", "娴", "媛", "娜", "娇"}
NEGATIVE_WORDS = {"妖", "妒", "婪", "嫉"}
NEUTRAL_WORDS = {"女", "妈", "姐", "媳"}

# 结果存储
data = []

# 1️⃣ **获取所有含“女”部首的汉字**
print("⏳ 正在获取含‘女’部首的汉字...")
response = requests.get(ROOT_URL)
soup = BeautifulSoup(response.text, "lxml")

# 提取所有汉字（网页结构可能会变化，需要手动检查）
characters = []
for char_link in soup.find_all("a"):
    char = char_link.text.strip()
    if len(char) == 1:  # 只保留单个汉字
        characters.append(char)

print(f"✅ 找到 {len(characters)} 个含‘女’部首的汉字：{characters}")

# 2️⃣ **遍历汉字，获取拼音、释义**
for char in characters:
    url = DETAIL_URL + char
    response = requests.get(url)
    time.sleep(1)  # 避免请求过快被封
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")

        # 提取拼音
        pinyin_tag = soup.find("span", class_="dicpy")
        pinyin = pinyin_tag.text.strip() if pinyin_tag else "未知"

        # 自动分类情感
        if char in POSITIVE_WORDS:
            sentiment = "褒义"
        elif char in NEGATIVE_WORDS:
            sentiment = "贬义"
        else:
            sentiment = "中性"

        # 存储数据
        data.append({"字": char, "拼音": pinyin, "部首": "女", "情感分类": sentiment})
        print(f"✅ 已爬取：{char}（拼音：{pinyin}，分类：{sentiment}）")
    else:
        print(f"❌ 爬取失败：{char}")

# 3️⃣ **保存到 JSON 文件**
with open("female_radical_corpus.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("✅ 所有数据已保存到 female_radical_corpus.json！")
