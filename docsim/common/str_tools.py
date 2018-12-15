
def is_chinese(c):
    """
    判断一个unicode字符是否为中文
    :param c: 要判断的字符
    :return:
        True： 表示字符c是中文字符
        False：表示字符c不是中文字符
    """
    l = len(c)
    if l != 1:
        return False

    if '\u4e00' <= c <= '\u9fff':
        return True
    else:
        return False


def decode(content_bin):
    """
    将二进制串转化为unicode字符串，支持utf-8和gb18030编码
    :param content_bin: 二进制串
    :return: 转换后的unicode字符串
    """
    content = ''
    try:
        content = content_bin.decode('utf-8')
    except UnicodeDecodeError:
        content = content_bin.decode('gb18030')
    return content


