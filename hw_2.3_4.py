import chardet
import json
from collections import Counter


def get_file():
    file = input()
    with open(file, 'rb') as f:
        data = f.read()
        res = chardet.detect(data)
        decoded_string = data.decode(res['encoding'])
    json_news = json.loads(decoded_string)
    return json_news


def get_top_10():
    news = get_file()['rss']['channel']['items']
    words = []
    for news_item in news:
        news_words = news_item['description'].split()
        words = words + news_words
    long_words = []
    for word in words:
        if len(word) > 6:
            long_words.append(word)
    words_count = Counter(long_words)
    top10 = words_count.most_common(10)
    for item in top10:
        print(item[0] + ', ' + '%d раз(а)' % (item[1]))

get_top_10()