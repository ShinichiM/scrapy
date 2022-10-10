import requests
from bs4 import BeautifulSoup

URL = "https://www.reddit.com/r/news/"
# URL = "https://www.indeed.com/"
# URL = "https://www.indeed.com/jobs?q=software+developer&l=&from=searchOnHP&vjk=8acc01383db49893"
HEADERS ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=HEADERS);
soup = BeautifulSoup(page.text, "html.parser")
results = soup.find_all('h3')
data_str = [] 
for item in results:
    print(' - - - Item - - ', item, ' - - - - text - - - ', item.text)
    data_str.append(item.get_text())

print(data_str)

# Run every hour, to get top 7 news postings on reddit 
# Cataegorize post titles and then map general public intersest in news?