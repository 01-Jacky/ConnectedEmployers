from bs4 import BeautifulSoup

html_doc = open('connected_employer/test_data/dummy.html')

soup = BeautifulSoup(html_doc, 'html.parser')

li_elments = soup.findAll("li")

print len(li_elments)