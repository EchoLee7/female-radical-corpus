import json

# 创建包含“女”部首的汉字数据
data = [
    {"字": "女", "拼音": "nǚ", "部首": "女", "情感分类": "中性"},
    {"字": "妈", "拼音": "mā", "部首": "女", "情感分类": "中性"},
    {"字": "婉", "拼音": "wǎn", "部首": "女", "情感分类": "褒义"},
    {"字": "妖", "拼音": "yāo", "部首": "女", "情感分类": "贬义"}
]

# 保存 JSON 文件
with open("female_radical_corpus.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("✅ JSON 文件已创建！")
