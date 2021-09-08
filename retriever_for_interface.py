import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
from msedge.selenium_tools import Edge, EdgeOptions

def get_tweet_data(card):
    '''Extract data from tweet data'''
    username = card.find_element_by_xpath('.//span').text
    handle = card.find_element_by_xpath('.//span[contains(text(), "@")]').text
    long_date = card.find_element_by_xpath('.//time').get_attribute('datetime')
    short_date = long_date[:10] 
    comment = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
    responding = card.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
    text = comment +" "+ responding    

    rough_tweet = username, handle, short_date, text
    tweet = []
    for char in rough_tweet:
        tweet.append(char.replace("\n", " "))
    
    return tweet


def get_info(user_name, password, search_term):
    '''Getting the user information and search phrase to be used'''
    global user, user_pass, search_data
    user = user_name
    user_pass = password
    search_data = search_term
    return user_name, user_pass, search_term

def main():
    user, user_pass, search_data
    # %%
    # Opening edge browser
    options = EdgeOptions()
    options.use_chromium = True
    driver = Edge(options=options)

    # navigating to twitter login page
    driver.get('https://twitter.com/login')
    driver.maximize_window()
    sleep(2.5)

    # username
    username = driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
    username.send_keys(user)

    #password
    password = driver.find_element_by_xpath('//input[@name="session[password]"]')
    password.send_keys(user_pass)
    password.send_keys(Keys.RETURN)
    sleep(2.5)

    driver.get('https://twitter.com/{}'.format(user))
    sleep(3)

    # %%
    data = []
    tweet_ids = set()
    last_position = driver.execute_script("return window.pageYOffset;")
    scrolling = True

    # allowing the bot to scroll till the end of the page
    while scrolling:
        page_cards = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
        for card in page_cards[-15:]:
            tweet = get_tweet_data(card)
            if tweet:
                tweet_id = ''.join(tweet)
                if tweet_id not in tweet_ids:
                    tweet_ids.add(tweet_id)
                    data.append(tweet)
                
        scroll_attempt = 0
        while True:
            # check scroll position
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(2)
            curr_position = driver.execute_script("return window.pageYOffset;")
            if last_position == curr_position:
                scroll_attempt += 1
                
                # end of scroll region
                if scroll_attempt >= 3:
                    scrolling = False
                    break
                else:
                    sleep(2) # attempt another scroll
            else:
                last_position = curr_position
                break

    # close the web driver
    driver.close()

    # %%
    # sorting the retrieved tweets into single list
    sorted_tweet_data = []
    for i in data:
        sorted_tweet_data.append(' || '.join(i).lower())


    # %%
    for tweet in sorted_tweet_data:
        if search_data in tweet:
            print(tweet + '\n')

if __name__=='__main__':
    main()