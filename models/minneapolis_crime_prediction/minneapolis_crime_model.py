#-*- coding:utf-8 -*-
'''
Author: TianRan
Date: 12/10/16
Version:
'''
import pickle
import numpy as np
import arrow as ar


from utils import PROJECT_DIR
class MinneapolisCrimePrediction(object):

    def __init__(self):
        # load the scaler and lr_model from the pickle object
        with open(PROJECT_DIR + '/models/minneapolis_crime_prediction/crime_scaler_rf.pkl',
                  'rb') as input:
            self.scaler = pickle.load(input)
            self.rf_model = pickle.load(input)

    def predict_from_lr(self,lat,lon,date,time,k):
        '''
        :param lat: latitude
        :param lon: longitude
        :param date: the date,"2016-12-10" the default value is the current date
        :param time: time, "13:00", the default value is current time
        :param k: top k result we want to return
        return top k predictions from logitic regression and corresponding probabilities.

        Notice:
            The features are [lat,long,one-hot-hour-feature,one-hot-day-feature,one-hot-month-feature]
        '''
        if not date:
            date_obj = ar.now().date()
        else:
            date_obj = ar.get(date).date()
        if not time:
            time = str(ar.now().datetime)[11:16]

        # get the one hot for time and date
        one_hot_time = self.get_one_hot_time(time)
        one_hot_month_day = self.get_one_hot_month_day(date_obj)

        #form the features and normlize
        features_unnormed = [lat,lon]
        features_unnormed.extend(one_hot_time)
        features_unnormed.extend(one_hot_month_day)

        features_normed = self.scaler.fit_transform(np.array(features_unnormed))
        predict_proba_list = self.lr_model.predict_proba(features_normed)[0]

        # form the result, choose the top two result and corresponding probability
        return self.form_result_from_proba(predict_proba_list,k)


    def predict_from_rf(self,lat,lon,date,time,k):
        '''
        :param lat: latitude
        :param lon: longitude
        :param date: the date,"2016-12-10" the default value is the current date
        :param time: time, "13:00", the default value is current time
        :param k: top k result we want to return
        return top k predictions from logitic regression and corresponding probabilities.

        Notice:
            The features are [lat,long,one-hot-hour-feature,one-hot-day-feature,one-hot-month-feature]
        '''
        if not date:
            date_obj = ar.now().date()
        else:
            date_obj = ar.get(date).date()
        if not time:
            time = str(ar.now().datetime)[11:16]

        # get the one hot for time and date
        one_hot_time = self.get_one_hot_time(time)
        one_hot_month_day = self.get_one_hot_month_day(date_obj)

        #form the features and normlize
        features_unnormed = [lat,lon]
        features_unnormed.extend(one_hot_time)
        features_unnormed.extend(one_hot_month_day)

        features_normed = self.scaler.transform(np.array(features_unnormed))
        predict_proba_list = self.rf_model.predict_proba(features_normed)[0]

        # form the result, choose the top two result and corresponding probability
        return self.form_result_from_proba(predict_proba_list,k)

    def form_result_from_proba(self,predict_proba_list,k):
        '''
        return the top k result and corresponding proba
        :param predict_proba_list:
        :param k:
        :return:
        '''
        # if predict_proba_list:
        #     return None
        if k > len(predict_proba_list):
            return None
        index_code_map = {0:1,1:3,2:4,3:5,4:6,5:7,6:8,7:10}
        arg_index_list = predict_proba_list.argsort()
        res = []
        for i in range(1,k+1):
            index = arg_index_list[-i]
            res.append([predict_proba_list[index], self.UCR_mapper(index_code_map[index]) ])
        return res


    def get_one_hot_time(self,time):
        '''
        form the one hot list from time
        :param time:  str, like "12:12"
        :return:
        '''
        hour = int(time.split(":")[0])
        hour %= 24
        if 0 <= hour <= 5:
            return [1,0,0,0]
        elif 6 <= hour <= 11:
            return [0,1,0,0]
        elif 12 <= hour <= 17:
            return [0,0,1,0]
        else:
            return [0,0,0,1]

    def get_one_hot_month_day(self,date_obj):
        '''
        get the one hot list for month and day
        :param date_obj: date object
        :return: [day_list,month_list]
        '''
        month = int(date_obj.month)
        if 1 <= month <= 3:
            month_list = [1,0,0,0]
        elif 4 <= month <= 6:
            month_list = [0,1,0,1]
        elif 7 <= month <= 9:
            month_list = [0,0,1,0]
        else:
            month_list = [0,0,0,1]

        day = int(date_obj.day)
        if 1 <= day <= 8:
            day_list =  [1,0,0,0]
        elif 9 <= day <= 16:
            day_list = [0,1,0,1]
        elif 17 <= day <= 23:
            day_list = [0,0,1,0]
        else:
            day_list = [0,0,0,1]
        day_list.extend(month_list)
        return day_list


    def UCR_mapper(self,code):
        '''
        :return: the str of the crime for the given code
        '''
        hash_map = {1:"Criminal Homicide",2:"Sexual Assault",3:"Robbery", 4:"Aggravated Assault",
                    5:"Burglary",6:"Larceny",7:"Motor Vehicle Theft",8:"Arson",9:" Other Assaults",10:"Forgery And Counterfeiting"}
        return hash_map.get(code,"Motor Vehicle Theft")

if __name__ == '__main__':
    # pickle, load the object pickled from notebook
    with open('/Users/TianRan/PycharmProjects/data_monitor/models/minneapolis_crime_prediction/crime_scaler_lr.pkl',
              'rb') as input:
        scaler = pickle.load(input)
        lr_model = pickle.load(input)

    import numpy as np
    test = np.array([ 45.04451 , -93.310883,   0,   0,   1,
         0.      ,   0.      ,   0.      ,   1.      ,   0.      ,
         1.      ,   0.      ,   0.      ,   0.      ])

    print scaler.fit_transform(test)
    prob_list = lr_model.predict_proba(scaler.fit_transform(test))
    print prob_list

    # deal with date
    # time = "2016-12-23"
    # date =  ar.get(time).date()
    # print date.year
    # print date.month
    # print date.day
    # print str(ar.now().datetime)[11:16]

    # one hot generators



