from bs4 import BeautifulSoup
import requests
from resume_gpt import resumegpt

def lect(url):
    link = url
    req = requests.get(link)
    if req.status_code == 200:
        html = req.content
        soup = BeautifulSoup(html, 'html5lib')
        try :
            article_brute = [tag.get_text() for tag in soup.find_all(['h1', 'h2', 'h3', 'p'])]
            article = str(article_brute)
            rr = resumegpt(article)
            return rr  # return the summary instead of printing it
        except:
            pass


