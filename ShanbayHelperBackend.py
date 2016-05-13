__author__ = 'Administrator'

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

class ShanbayHelperBackend(object):

    def __init__(self, GUI):
        '''

        :param GUI: ShanbayHelperGUI
        :return:
        '''
        self.gui = GUI

    def openChrome(self):
        self.browser = webdriver.Chrome()

    def exitChrome(self):
        self.browser.quit()


    def login(self, username, password):
        '''

        :param username: String
        :param password: String
        :return:
        '''
        try:
            self.browser.get(url="http://www.shanbay.com/accounts/login/")
            usr = self.browser.find_element_by_id('id_username')
            usr.clear()
            usr.send_keys(username)

            pw = self.browser.find_element_by_id('id_password')
            pw.clear()
            pw.send_keys(password)

            submitButton = self.browser.find_elements_by_xpath('//button[@type="submit"]')
            submitButton[0].click()
        except NoSuchElementException:
            self.gui.log('Failed to open the log url')
            return False

        try:
            self.browser.find_element_by_xpath("//a[contains(@href,'/listen/plan/')]")
        except NoSuchElementException:
            self.gui.log('Logged in failed with usr:' + username + ' pw:' + password)
            return False
        self.gui.log('Logged in successfully with usr:' + username + ' pw:' + password)
        return True

    def addWordList(self, wordList):
        '''

        :param wordList: List
        :return:
        '''
        add_url = 'https://www.shanbay.com/bdc/vocabulary/add/batch/'
        self.browser.get(add_url)
        words = []
        for word in wordList:
            if len(words) == 10:
                self.addTenWords(words)
                words.clear()
            words.append(word)
        self.addTenWords(words)
        self.gui.log('Successfully added ' + str(len(wordList)) + ' words')

    def addTenWords(self, words):
        if len(words) > 10:
            return
        s = ''
        for word in words:
            s += word + '\n'
        self.browser.find_elements_by_xpath('//textarea[@name="words"]')[0].send_keys(s)
        self.browser.find_elements_by_xpath('//input[@type="submit"]')[0].click()
        self.gui.log('Words Added: ' + s.replace('\n', ' '))
        time.sleep(1)