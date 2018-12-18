import unittest
import common.doc_tools as doc_tools


class TestDocTools(unittest.TestCase):
    def test_content_to_words(self):
        doc_tools.stopwords.append('的')
        doc_tools.stopwords.append('是')
        doc_tools.stopwords.append('一位')
        content = '小明的父亲是一位著名大学里的物理老师'
        words = doc_tools.content_to_words(content).split()

        self.assertIn('父亲', words)
        self.assertIn('著名', words)
        self.assertIn('大学', words)
        self.assertIn('物理', words)
        self.assertIn('老师', words)

        self.assertNotIn('的', words)
        self.assertNotIn('是', words)
        self.assertNotIn('一位', words)

    def test_load_stopwords(self):
        doc_tools.load_stopwords('D:\\Study\\gongwen\\data\\stopwords')
        self.assertIn('具体说来', doc_tools.stopwords)
        self.assertIn('一则', doc_tools.stopwords)
        self.assertIn('allow', doc_tools.stopwords)
        self.assertIn('打开天窗说亮话', doc_tools.stopwords)
        self.assertIn('难道说', doc_tools.stopwords)
