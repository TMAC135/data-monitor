#-*- coding=utf-8 -*-
'''
Author: TianRan
Date: 7/17/16
Version:
'''
import requests
from bs4 import BeautifulSoup
import re
import json


class SpiderCnnNews(object):
    '''
    crawer the contends of the CNN news。
    '''

    def __init__(self, url):
        '''
        '''
        self.url = url  # the website we want to craw
        self.news_urls = []  # urls for the news for given website url
        self.htmls = []  # strings of htmls for the urls
        self.s_all = []  # strings of contends of generate_htmls

    def generate_news_urls(self):
        '''
        Get the urls from the index page and store them to a list -- self.urls
        '''

        try:
            response = requests.get(self.url)
            html = response.text
        except Exception, e:
            print e

        soup = BeautifulSoup(html, 'lxml')
        if self.news_urls:
            return
        else:
            pattern = re.compile('http://')
            for i in soup.find_all('h3'):
                if not re.search(pattern, i.a['href']):
                    # add regular expression to judge if the the href already start with 'http://edition.cnn.com'
                    self.news_urls.append('http://edition.cnn.com' + i.a['href'])
                else:
                    self.news_urls.append(i.a['href'])
                    #         print self.news_urls

    def generate_htmls(self):
        '''
        Given the urls of news, we get the strings of htmls and store to a list -- self.htmls
        '''
        if self.htmls:
            return

        if not self.news_urls:
            raise Error('Please generate urls firstly, call generate_urls() directly')

        for url in self.news_urls:
            try:
                response = requests.get(url)
                self.htmls.append(response.text)
            except Exception, e:
                print e

    def extract_contends(self):
        '''
        Given the htmls we get from generate_htmls(), we extract the contends of each html
        and store them in self.s_all
        '''

        if self.s_all:
            return

        if not self.htmls:
            raise Error('Please generate urls and htmls firstly')

        # debug = 0
        for html in self.htmls:

            soup = soup = BeautifulSoup(html, 'lxml')
            s_tmp = ''

            ## if we find the specific module in the html, we will extract it, otherwise we
            # ignore this html
            if soup.find_all('section', class_=re.compile('zn-body-text')):
                for contend in soup.find_all('section', class_=re.compile('zn-body-text'))[0].strings:
                    # i is a generator and we need to pass through it
                    for j in contend:
                        s_tmp += j
                        #                 debug += 1
                        #                 print 'the news of ',debug,'is done'
                self.s_all.append(s_tmp)


class StringAnalysis(object):
    '''
    Analyze the news strings from the crawer result
    '''

    def __init__(self, news_strings):
        '''
        Constructor: input is the list of all news strings from the result of crawer
        '''
        if not news_strings:
            raise Error('please input nonempty string list  strings when initilizing')
        self.news_strings = news_strings
        self.words = []  # list of words for every news
        self.frequency = []  # list of dictionary which contains the frequency of words
        self.top_frequency = []  # list of top 10 words based on TF-IDF standard for each news

    def extract_words(self):
        '''
        Extract words of every new string, store words in a list.
        '''

        for each_new in self.news_strings:
            # split the string with space
            words_list = each_new.split(' ')
            # we need to refine the each word, eliminate special characters like ,.'"/ etc
            pattern = re.compile('([a-zA-Z]+)')
            words_list = [re.search(pattern, i).group() for i in words_list if re.search(pattern, i)]
            self.words.append(words_list)

    def count_frequency(self):
        '''
        Count the frequency of words in each news, store them in dictionary then append them
        to a list - frequency
        '''

        if not self.words:
            raise Error('please extract words for news firstly, call extract_words before this function')

        for word_each in self.words:
            # use the most naive method, any method to speed up this? list comprehensive?
            tmp = {}
            for word in word_each:
                if word in tmp:
                    tmp[word] += 1
                else:
                    tmp[word] = 1
            self.frequency.append(tmp)
            # get the frequency of the word
        #         self.frequency = [{key: word[key]/length*1.0 for key in word} for word in self.frequency]
        for each in self.frequency:
            length = len(each.keys())
            for key in each.keys():
                each[key] /= (length * 1.0)

    def TF_IDF(self):
        '''
        Given the frequency of words for all new list, store the top-10 words for
        every news in the list.

        Since the TF-IDF is proportional to the 1/(word appear in other files) and we only need to
        sort them instead of computing them, I just count the word appear in other files in helper function.
        '''

        if not self.frequency:
            return

        for i in range(len(self.frequency)):
            # here I  calulate the TF-IDF value of each word and sort them to pick the top
            # 10 to store, for big data, use heap to choose the top 10 instead of sort to get rid of nlog(n) complexity.
            items = self.frequency[i]
            for key in items.keys():
                items[key] /= self.helper(key, i)
            # sort the items and pick the top 10 words
            self.top_frequency.append(sorted(items, key=items.get, reverse=True)[:10])

    def helper(self, key, num):
        '''
        Helper function for TF-IDF function.
        Input:
            key: the word we are intereted
            i: the number of current file
        Output:
            A int number.
        Functionality:
            Given the key in this and current file i, count the number of files which this key
            appears in other than current file - i.
        '''
        result = 1
        for i in range(len(self.frequency)):
            if i == num:
                continue
            else:
                if key in self.frequency[i]:
                    result += 1
        return result


def save_to_jason(data, address=None):
    '''
    save the data in python to a json file
    '''
    with open('hot_words.json', 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    # here is the news website we want to craw
    CNN_url = 'http://edition.cnn.com'

    # get the string contends first with class SpiderCnnNews
    spider = SpiderCnnNews(CNN_url)
    spider.generate_news_urls()
    spider.generate_htmls()
    spider.extract_contends()

    # analyze the contends above with StringAnalysis
    analysis = StringAnalysis(spider.s_all)
    analysis.extract_words()
    analysis.count_frequency()
    analysis.TF_IDF()

    # print analysis.top_frequency
    # save_to_jason(analysis.top_frequency)

    from datetime import date
    from utils.path_util import PROJECT_DIR
    json_out_path = PROJECT_DIR + '/data/json/crawler/news/{0}_cnn_news.json'.format(str(date.today()))

    with open(json_out_path,'w') as f:
        json.dump(analysis.top_frequency, f)
