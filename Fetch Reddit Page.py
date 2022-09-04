import requests
import csv
import time
import sqlite3
from bs4 import BeautifulSoup

def sql_connection():
    con = sqlite3.connect('SubredditDatabase.db')
    return con

def sql_table(con):
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS posts(SUBREDDIT text, TAG text, "
                " TITLE text, AUTHOR text, TIMESTAMP text, UPVOTES int, " 
                " COMMENTS text, URL text)")
    con.commit()

def sql_insert_table(con, entities):
    cur = con.cursor()
    cur.execute('INSERT INTO posts(SUBREDDIT, TAG, TITLE, AUTHOR, '
                'TIMESTAMP, UPVOTES, COMMENTS, URL) '
                'VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entities)
    con.commit()

def scraper():
    con = sql_connection()
    sql_table(con)
    while 1:
        subreddit = input('\n\nEnter the name of the subreddit: r/').lower()
        max_count = int(input('Enter the maximum number of entries to collect: '))
        select = int(input('Select tags to add for the search: \n1. hot\n2. new'
                            '\n3. rising\n4. controversial\n5. top\nMake your choice: '))
        if select == 1:
            tag = 'hot'
            tag_url = '/'
        elif select == 2:
            tag = 'new'
            tag_url = '/new/'
        elif select == 3:
            tag = 'rising'
            tag_url = '/rising/'
        elif select == 4:
            tag = 'controversial'
            tag_url = '/controversial/'
        elif select == 5:
            tag = 'top'
            tag_url = '/top/'
        url = 'https://old.reddit.com/r/' + subreddit
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = requests.get(url, headers=headers)
        if req.status_code == 200:
            soup = BeautifulSoup(req.text, 'html.parser')
            print(f'\nCOLLECTING INFORMATION FOR r/{subreddit}....')
            attrs = {'class': 'thing'}
            counter = 1
            full = 0
            reddit_info = []
            while 1:
                for post in soup.find_all('div', attrs=attrs):
                    try:
                        title = post.find('a', class_='title').text
                        author = post.find('a', class_='author').text
                        time_stamp = post.time.attrs['title']
                        comments = post.find('a', class_='comments').text.split()[0]
                        if comments == 'comment':
                            comments = 0
                        upvotes = post.find('div', class_='score likes').text
                        if upvotes == '•':
                            upvotes = "None"
                        link = post.find('a', class_='title')['href']
                        link = 'www.reddit.com' + link
                        entities = (subreddit, tag, title, author, time_stamp, upvotes, 
                                    comments, link)
                        sql_insert_table(con, entities)
                        if counter == max_count:
                            full = 1
                            break
                        counter += 1
                    except AttributeError:
                        continue
                if full:
                    break
                try:
                    next_button = soup.find('span', class_='next-button')
                    next_page_link = next_button.find('a').attrs['href']
                    time.sleep(2)
                    req = requests.get(next_page_link, headers=headers)
                    soup = BeautifulSoup(req.text, 'html.parser')
                except:
                    break
            print('DONE!\n')
            ans = input('Press (y) to continue or any other key to exit: ').lower()
            if ans == 'y':
                continue
            else:
                print('Exiting..')
                break
        else:
            print('Error fetching results.. Try again!')
if __name__ == '__main__':
    scraper()