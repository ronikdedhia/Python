from selenium import webdriver
from email_validator import validate_email, EmailNotValidError
import csv

def LinkedInEmailScraper(userEmail, userPassword):
    emailList = {}

    browser = webdriver.Chrome()
    url = '[INSERT URL TO LINKEDIN POST]'
    browser.get(url)
    browser.implicitly_wait(5)
    commentDiv = browser.find_element_by_xpath(
        '/html/body/main/section[1]/section[1]/div/div[3]/a[2]'
    )
    loginLink = commentDiv.get_attribute('href')
    browser.get(loginLink)
    email = browser.find_element_by_xpath('//*[@id="username"]')
    password = browser.find_element_by_xpath('//*[@id="password"]')
    email.send_keys(userEmail)
    password.send_keys(userPassword)
    submit = browser.find_element_by_xpath(
        '//*[@id="app__container"]/main/div[3]/form/div[3]/button')
    submit.submit()
    browser.implicitly_wait(5)
    commentSection = browser.find_element_by_css_selector(
        '.comments-comments-list')
    for _ in range(
            3
    ):
        try:
            moreCommentsButton = commentSection.find_element_by_class_name(
                'comments-comments-list__show-previous-container'
            ).find_element_by_tag_name('button')
            moreCommentsButton.click()
            browser.implicitly_wait(5)
        except:
            print('End of checking comments')
            break
    browser.implicitly_wait(20)
    comments = commentSection.find_elements_by_tag_name(
        'article')
    for comment in comments:
        try:
            commenterName = comment.find_element_by_class_name(
                'hoverable-link-text')  # finds name of commenter
            commentText = comment.find_element_by_tag_name('p')
            commenterEmail = commentText.find_element_by_tag_name(
                'a').get_attribute('innerHTML')  # finds email of commenter
            # validates email address
            validEmail = validate_email(commenterEmail)
            commenterEmail = validEmail.email
        except:
            continue
        emailList[commenterName.get_attribute('innerHTML')] = commenterEmail
    browser.quit()
    return emailList

def DictToCSV(input_dict):
    with open('./LinkedIn Email Scraper/emails.csv', 'w') as f:
        f.write('name,email\n')
        for key in input_dict:
            f.write('%s,%s\n' % (key, input_dict[key]))
        f.close()

if __name__ == '__main__':
    userEmail = '[INSERT YOUR EMAIL ADDRESS FOR LINKEDIN ACCOUNT]'
    userPassword = '[INSERT YOUR PASSWORD FOR LINKEDIN ACCOUNT'
    emailList = LinkedInEmailScraper(userEmail, userPassword)
    DictToCSV(emailList)
