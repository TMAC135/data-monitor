#-*- coding:utf-8 -*-
'''
Author: TianRan
Date: 12/10/16
Version:
'''

class MinneapolisCrimePrediction(object):

    def __init__(self,lat,lon,time):
        '''
        :param lat: latitude
        :param lon: longitude
        :param time: time
        '''
        pass

    def predict_from_lr(self):
        '''
        return top 2 predictions from logitic regression and corresponding probabilities.
        :return:
        '''
        pass

    def UCR_mapper(code):
        '''
        :return: the str of the crime for the given code
        '''
        hash_map = {1:"Criminal Homicide",2:"Sexual Assault",3:"Robbery", 4:"Aggravated Assault",
                    5:"Burglary",6:"Larceny",7:"Motor Vehicle Theft",8:"Arson",9:" Other Assaults",10:"Forgery And Counterfeiting"}
        return hash_map.get(code,"Motor Vehicle Theft")

if __name__ == '__main__':
    # pickle, load the object pickled from notebook
    import pickle
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

