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

links = soup.find_all('a', href = True)
# loop through the result set 
for link in links[0:10]:
    print('href attr = ', link['href'])
    try:
        print('title attr = ', link['title']) # if it has title
    except:
        continue # else continue

# search for tables and a tags
h1_and_small_tags = soup.find_all(['h1', 'small'])
print(h1_and_small_tags)

# tables header with a particular style
table_headers = soup.find_all('th', style="width: 10%")

wiki_tables = soup.find_all('table', class_="wikitable") 
print(wiki_tables)

# define a function to find the items
def list_withlinks(tag):
    return tag.name == 'li' and len(tag.find_all('a'))>20

# list items with a tags
list_with_a = soup.find_all(list_withlinks)
print(list_with_a)

# define the simple tree we see above.
simple_tree = """<html><body><a><b>text1</b><c>text2</c></a></body></html>"""
# pass the simple tree into our Parser to create some simple soup.
simple_soup = BeautifulSoup(simple_tree, 'html.parser')
# we can always print it in a familiar structure.
print(simple_soup.prettify())








