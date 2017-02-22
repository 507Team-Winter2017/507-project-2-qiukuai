#proj2.py
import requests
from bs4 import BeautifulSoup
import sys

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):

    enc = file.encoding

    if enc == 'UTF-8':

        print(*objects, sep=sep, end=end, file=file)

    else:

        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)

        print(*map(f, objects), sep=sep, end=end, file=file) 



#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)
 
count=0
for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a and count<10: 
        uprint(story_heading.get_text())
        count+=1


#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
base_url = 'http://www.michigandaily.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)
 
count=0
b=soup.find(class_="panel-pane pane-mostread")

c=b.find_all('a')
for d in c:
	print(d.get_text())
#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
base_url = 'http://newmantaylor.com/gallery.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)
 
count=0
b=soup.find_all('img')
#print(b)

for c in b:
	#print(c)
	if c.get('alt'):
		#print('yes')
		print(c.get('alt'))
	else:
		print('No alternative text provided!')
		


#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
base_url = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
page_link=[]
for count in range(6):
	page_url=base_url+'&page='+str(count)
	#print(page_url)
	r = requests.get(page_url,headers={'User-Agent': 'SI_CLASS'})
	soup = BeautifulSoup(r.text)
	#uprint(soup)	
	b=soup.find_all('a',string='Contact Details')
	#uprint(b)
	for c in b:
		page_link.append(c.get('href'))

count=1
for l in page_link:
	link_url ='https://www.si.umich.edu'+l
	#uprint(link_url)
	r = requests.get(link_url,headers={'User-Agent': 'SI_CLASS'})
	soup = BeautifulSoup(r.text)
	b=soup.find(class_="field field-name-field-person-email field-type-email field-label-inline clearfix")
	print(count,end=' ')
	count+=1
	uprint(b.a.get_text())
	

