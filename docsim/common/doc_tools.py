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


def load_stopwords(path):
    """
    从指定的路径加载停用词，目录中的停用词文件需要时utf-8编码
    :param path: 存放停用词文件的目录
    """
    import os
    stopwords.clear()
    if not(path.endswith('/') or path.endswith('\\')):
        path = path + '/'
    stopwords_files = os.listdir(path)
    for filename in stopwords_files:
        full_filename = path + filename
        with open(full_filename, encoding='utf-8') as f:
            for line in f.readlines():
                line = line.strip()
                if line not in stopwords:
                    stopwords.append(line)





if __name__ == '__main__':
    stopwords.append('的')
    stopwords.append('是')
    stopwords.append('一位')
    content = '小明的父亲是一位著名大学里的物理老师'
    words = content_to_words(content)
    print(words)
