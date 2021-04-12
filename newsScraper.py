# Write a short script tat takes information from google news and 
# outputputs to terminal with tile and link

from requests_html import HTMLSession
# create a session to open up the page
session = HTMLSession()
url = "https://news.google.com/topstories?hl=en-IE&gl=IE&ceid=IE:en"

r = session.get(url)

r.html.render(sleep=1, scrolldown=5)

articles = r.html.find("article")
#print(article) -----------------------------

newslist = []
for item in articles:
    try:
        newsitem = item.find('h3', first=True)
        news_article_info = {"title" : newsitem.text, "link" : newsitem.absolute_links}
        newslist.append(news_article_info)
        #print(title, link) -------------------------------
    except:
        pass

print(len(newslist))
