import requests as HTTP
from bs4 import BeautifulSoup as SOUP
import re
import random

print("Emotions:")

fruits = ["normal", "hatred", "depressed"]
for x in fruits:
    print(x)
    

def main(emotion):
    if(emotion == "normal"):
        urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
        
    elif(emotion == "hatred"):
        urlhere = 'https://imdb.to/3YK9W2R'
        urlhere = 'https://imdb.to/3lNx8yw'
        urlhere = 'https://imdb.to/3IMPMjk'
        
    elif(emotion == "depressed"):
        urlhere = 'https://www.imdb.com/search/title/?genres=action,comedy&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=a581b14c-5a82-4e29-9cf8-54f909ced9e1&pf_rd_r=RECJWPYW3DX970XH8R33&pf_rd_s=center-5&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr5_i_2'
        urlhere = 'https://www.imdb.com/search/title/?genres=comedy&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=RECJWPYW3DX970XH8R33&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1'
        
    elif(emotion == "joy"):
        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
    else:
        return "Invalid"
    
    # HTTP request to get the data of the whole page
    response = HTTP.get(urlhere)
    data = response.text

    # Parsing the data using BeautifulSoup
    soup = SOUP(data, "lxml")

    # Extract movie titles from the data using regex
    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
    movie_list = []
    for i in title:
        tmp = str(i).split('>')
        if(len(tmp) == 3):
            movie_list.append(tmp[1][:-3])
    
    if len(movie_list) > 0:
        return random.choice(movie_list)
    else:
        return "No movies found for this emotion"

if __name__ == '__main__':
    
 while True:
    print("")
    emotion = input("Do you even feel something?: ")
    print(main(emotion))

