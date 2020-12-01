import requests
from bs4 import BeautifulSoup

url = 'http://codewithharry.com'

#Step-1 Get the html -----------------------------------------

r = requests.get(url)
htmlcontent = r.content
# print(htmlcontent)

#Step-2 parse the html---------------------------------------

soup = BeautifulSoup(htmlcontent,'html.parser')
# print(soup.prettify)


#Step-3 html tree traversal --------------------------------


# commonly use type of object
# 1 Tag
# 2 NavigableString
# 3 BeautifulSoup
# 4 Comment


# title = soup.title
# print(type(title))
# print(type(title.string))
# print(type(soup))

#Get the title of the html page
title = soup.title

# get all the paragraph from the page 
paras = soup.find_all('p')
# print(paras)

# get all the anchor tag from the page
anchor = soup.find_all('a')
# print(anchor)


# it will find the first paragraph tag from the page
# or 
# get the first element of the html page
print(soup.find('p')) 


# it will find the first paragraph tag class name from the page 
# or 
# get class of element of html page 
print(soup.find('p')['class']) 


# find all the element of class = lead
print(soup.find_all('p',class_='lead'))


#Get the text from the tags/soup
print(soup.find('p').get_text())  

print(soup.get_text())




# Get all the link of the anchor tag

anchors = soup.find_all('a')

all_link = set()
for link in anchors:
    if link.get('href') != '#':
        all_link.add('https://codewithharry.com' + link.get('href'))

print(all_link)

markup =  "<p><!--This is comment --></p>"
soup2 = BeautifulSoup(markup)
print(soup2.p)
print(soup2.p.string)
print(type(soup2.p.string))




# .contents = A tags children are available in list
# .children = A tags children are available in gernerator




navbarSupportedContent =  soup.find(id='navbarSupportedContent')

for ele in navbarSupportedContent.children:
    print(ele)



for ele in navbarSupportedContent.strings:
    print(ele)


for ele in navbarSupportedContent.stripped_strings:
    print(ele)

print(navbarSupportedContent.parent)
print('-------------------------------------------------------------------------------------')
for item in navbarSupportedContent.parents:
    print(item.name)

print('-------------------------------------------------------------------------------------------------')
print(navbarSupportedContent.next_sibling.next_sibling)
print(navbarSupportedContent.previous_sibling.previous_sibling)

print('-------------------------------------------------------------------------------------------------')
ele = soup.select('#loginModal')
print(ele)
ele = soup.select('.modal-title')
print(ele)

print(' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ')

ele = soup.select('.modal-footer')
print(ele)

print('+')