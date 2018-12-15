import jieba


stopwords = []


def content_to_words(content):
    """
    将一段文本分词，去掉停用词，返回用空格隔开的词
    :param content:
    :return:
    """
    words = ''
    for word in jieba.cut(content):
        if word not in stopwords:
            if word != ' ':
                words = words + word + ' '
    return words.strip()


if __name__ == '__main__':
    stopwords.append('的')
    stopwords.append('是')
    stopwords.append('一位')
    content = '小明的父亲是一位著名大学里的物理老师'
    words = content_to_words(content)
    print(words)
