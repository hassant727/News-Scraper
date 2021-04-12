# Write a short script tat takes information from google news and 
# outputputs to terminal with tile and link

from requests_html import HTMLSession
# create a session to open up the page
session = HTMLSession()
url = "https://news.google.com/topstories?hl=en-IE&gl=IE&ceid=IE:en"

r = session.get(url)

r.html.render(sleep=1, scrolldown=0)

articles = r.html.find("article")
#print(article) -----------------------------

for item in articles:
    try:
        newsitem = item.find('h3', first=True)
        title = newsitem.text
        link = newsitem.absolute_links
        print(title, link)
    except:
        pass
