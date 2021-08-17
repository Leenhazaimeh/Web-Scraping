import requests
from bs4 import BeautifulSoup

#Your web scraper should report the number of citations needed
def get_citations_number(link): 
    History_of_Mexico= requests.get(link)
    soup = BeautifulSoup(History_of_Mexico.content , 'html.parser')
    data=soup.find_all('a' , title="Wikipedia:Citation needed")

    return int(len(data))


#Your web scraper should identify those cases AND include the relevant passage.
def get_citations_passage(link): 
    
    History_of_Mexico= requests.get(link)
    soup = BeautifulSoup(History_of_Mexico.content , 'html.parser')
    text=soup.find_all( 'p') 
    out_put=[]
    for passege in text : 
        result=passege.find_all('a' , title="Wikipedia:Citation needed")
        if len(result) >0 : 
            for i in result : 
                out_put.append(passege.text.strip())
    return ('\n').join(out_put)

    
if __name__ == "__main__" : 
    link = 'https://en.wikipedia.org/wiki/History_of_Mexico'
print('my first step in Web Scraping')
print (get_citations_number(link))
print (get_citations_passage(link))
print ('\n thanx ^_^' )

