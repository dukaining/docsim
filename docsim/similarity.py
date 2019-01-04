from gensim import corpora, models, similarities
from config import Config

def calculate(document):
    content = document.content
    title = document.title

