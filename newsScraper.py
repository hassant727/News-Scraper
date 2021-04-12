# Write a short script tat takes information from google news and 
# outputputs to terminal with tile and link

from requets_html import HTMLSession
# create a session to open up the page
session = HTMLSession()
url = "https://news.google.com/topstories?hl=en-IE&gl=IE&ceid=IE:en"

article = session.get(url)
