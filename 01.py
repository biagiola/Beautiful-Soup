# import our libraies
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.request

# define the url we want to scrap
wiki_url = r"https://en.wikipedia.org/wiki/Eastern_Front_(World_War_II)"
response_object = urllib.request.urlopen(wiki_url)

# creating the soup
soup = BeautifulSoup( response_object, 'html.parser')
print(soup)

# find the first instance of an anchor tag
link = soup.find('a') # the first a tag
link = soup.find('a', href = True) # the first a tag with href in it
print(link)

# what is the type
print(type(link)) # output <class 'bs4.element.Tag'>

# define the name
print(link.name) # output a

# get the dictionary of all the attributes with its values
print(link.attrs) # output {'class': ['mw-jump-link'], 'href': '#mw-head'}

# get the attribute values 
print(link['href'])
print(link['class'])

header = soup.find('h1')
print(header.text) # print the text inside the header

# find all the paragraph in the document
paragraphAll = soup.find_all('p') 
print(paragraphAll)

# define the type
print(type(paragraphAll)) # output <class 'bs4.element.ResultSet'> (its not a list, its a ResultSet Obj that belongs to BeautifulSoup)

# the length of our result set object
print(len(paragraphAll)) # how many p tags are.








