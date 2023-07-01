from bs4 import BeautifulSoup
import requests
import re
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
def fun(user):
    if user == 1:
        url = "https://www.imdb.com/search/title/?genres=Action&explore=title_type%2Cgenres&ref_=ft_popular_0"
    elif user == 2:
        url = "https://www.imdb.com/search/title/?genres=Sci-Fi&explore=title_type%2Cgenres&ref_=ft_popular_10"
    elif user == 3:
        url = "https://www.imdb.com/search/title/?genres=drama&sort=num_votes,desc&explore=title_type,genres"
    elif user == 4:
        url = "https://www.imdb.com/search/title/?genres=Thriller&explore=title_type%2Cgenres&ref_=ft_popular_11"
    elif user == 5:
        url = "https://www.imdb.com/search/title/?genres=comedy&sort=num_votes,desc&explore=title_type,genres"
    elif user == 6:
        url = "https://www.imdb.com/search/title/?genres=crime&sort=num_votes,desc&explore=title_type,genres"
    
    q = requests.get(url,headers=headers)
    soup = BeautifulSoup(q.text,'html.parser')
    s = soup.find_all('a',{'href':re.compile(r'\/title\/tt\d*\/')})
    return s

a = "1"
while a == "1":
    print("\n1)Action \n2)Sci-Fi \n3)Drama \n4)Thriller \n5)Comedy \n6)Crime\n")
    user = int(input("Enter your choice:"))
    top_10 = fun(user)
    count = 0
    for i in top_10:
        if i.string == "X" or i.string == None:
            continue
        else:
            print(i.string)
        if count > 8:
            break
        count +=1
    a = input("To continue press 1 or press enter to exit: ")
    if a != "1":
        exit
