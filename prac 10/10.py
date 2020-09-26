
import csv 
import requests 
import xml.etree.ElementTree as ET 

def loadRSS(): 
	url = 'https://www.news18.com/rss/books.xml'
	resp = requests.get(url) 
	with open('books.xml', 'wb') as f: 
		f.write(resp.content) 
	
def parseXML(xmlfile): 
	tree = ET.parse(xmlfile) 
	root = tree.getroot() 
	newsitems = [] 
	for item in root.findall('./channel/item'):  
		news = {} 
		for child in item: 
			if child.tag == '{https://search.yahoo.com/mrss/}content': 
				news['media'] = child.attrib['url'] 
			elif child.text is not None: 
				news[child.tag] = child.text.encode('utf8')
				newsitems.append(news)
	return newsitems 

def savetoCSV(newsitems, filename): 
	fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media'] 
	with open(filename, 'w') as csvfile: 
		writer = csv.DictWriter(csvfile, fieldnames = fields) 
		writer.writeheader() 
		writer.writerows(newsitems) 
loadRSS() 
newsitems = parseXML('books.xml') 
savetoCSV(newsitems, 'topnews.csv') 
def generate_edges(graph):
        edges=[]
        for node in graph:
                for neighbour in graph[node]:
                        edges.append((node,neighbour))
                return edges
