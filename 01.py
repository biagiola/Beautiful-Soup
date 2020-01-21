# import our libraies
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.request

# define the url we want to scrap
wiki_url = r"https://en.wikipedia.org/wiki/Eastern_Front_(World_War_II)"
response_object = urllib.request.urlopen(wiki_url)

# creating the soup
soup = BeautifulSoup( response_object, 'html.parser')
print(soup) # it print all the tags from the url

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

# if we want just a list of the children we could use the Contents attribute
a_content = simple_soup.a.contents
# display the list
print(a_content)
# display the first child
print(a_content[0])

# if we want to create a generator to iterate over them vice a list we can use
# the `children` attribute
for child in simple_soup.a.children:
    print(child)
# same as above
for child in a_content
    print(child)

#*#

# count the number of elements in both the childre and the descendants
print(len(list(simple_soup.a.children)))
print(len(list(simple_soup.a.descendants)))

# loop through the descendants itarator
for descendant in simple_soup.a.descendants:
    print(descendant)

#*#

# get the parent of the a tag
print(simple_soup.a.parent)
# get the parent of the parent of the a tag
print(simple_soup.a.parent.parent) 
# Loop through all the parents of the 'a' tag
for parent in simple_soup.a.parents:
    print(parent)

#*#
# Siblings
# print b
print(simple_soup.b)
# does the b have a sibling?
print(simple_soup.b.next_sibling)
print(simple_soup.c.previous_sibling)

#*#
# we take the fifth table
my_table = soup.find_all('table')[5] 
# using next element
print(my_table.next_element)    
for child in my_table.children: # children is more direct
    print(child) 

#*#
# grab the body
print(simple_soup.body)
# go to the next element
print(simple_soup.body.next_element)
print('break')
for element in simple_soup.b.next_elements:
    print(element)

#*#
# find_parents()
# print('b', simple_soup.b)
# print('b parent', simple_soup.b.find_parent())
# print('b parents', simple_soup.b.find_parents())

# find_next_sibling()
print('b', simple_soup.b)
print('b sibling', simple_soup.b.find_next_sibling())
print('b siblings', simple_soup.b.find_next_siblings())
#same of previous_simbling()

# find_next()
print('a', simple_soup.a)
print('a next', simple_soup.a.find_next())
print('a nexts', simple_soup.a.find_all_next())
#same of find_previous()

#*#
# grab all the tables
table = soup.find_all('table')[5]
print(table.prettify())

#*#
# grab all the tables
table = soup.find_all('table')[5]
# grab the a tag
a_tag = table.a
print(a_tag)
print(a_tag['href'])
# adding a new attribute value
a_tag['style'] = 'background: blue' 
print(a_tag)

# print(table.prettify())

#*#
# it is like innerHTML from js
a_tag.string = "My new String"
print(a_tag)
# delete the inner text of a tag
a_tag.clear(); 
print(a_tag)

#*#
print('body', table.tbody)
# extract the first table header
th_tag = table.tbody.th.extract()
# display the extracted tag
print('th_tag', th_tag)

#*#
# grab the first string that you find in the table header tag
print('table.th.string: ', table.th.string)
# get all the strings that belong to a table body
# first we must to convert into a list a slice it for practical reasons
for string in list(table.tbody.strings)[0:10]:
    print(string)
print('--------')
# same as above but ignoring the line breaks
for string in list(table.tbody.stripped_strings)[0:10]:
    print(string)







