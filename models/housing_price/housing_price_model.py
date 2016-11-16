# -*- coding:utf-8 -*-
'''
Created November 16, 2016
version:1.0
Qi Mo


'''

from dao.mysql.housing_price_mysql import HousingPriceMysqlDao

def divide_zero(a, b):
    a = float(a)
    b = float(b)
    if b == 0:
        return 0
    return a / b

class HousingPriceModel():
    def __init__(self):
        self.dao = HousingPriceMysqlDao('housing_price')

    def get_housing_price_list(self,date_end,date_begin,smooth_days,city_name):
        result = self.dao.get_city_housing_price(date_end,date_begin,city_name)

        # all_area_average
        city_all_area = [{'name': 'all_area', 'data': {}}]

        # resort the data by time
        re_dict = dict()
        for x in result:
            date = str(x['date_time'])
            re_dict[date] = dict()
        for x in result:
            date = str(x['date_time'])
            re_dict[date]['avg(value)'] = x['avg(value)']

        re_dict_sorted = sorted(re_dict.iteritems(), reverse=False)

        # deal the smooth
        if smooth_days ==0:
            for k in range(len(re_dict_sorted)):
                date = re_dict_sorted[k][0]
                t = round(float(re_dict_sorted[k][1]['avg(value)']),2)
                if t>0:
                    city_all_area[0]['data'][date] = str(t)
        else:
            housing_price = 0
            cnt =0

            for k in range(len(re_dict_sorted)):
                if k % smooth_days == 0:
                    if k > 0:
                        t = round(divide_zero(float(housing_price), float(cnt)), 2)
                        if t>0:
                            city_all_area[0]['data'][date] = str(t)

                    date = re_dict_sorted[k][0]
                    housing_price = 0
                    cnt = 0
                else:
                    housing_price += float(re_dict_sorted[k][1]['avg(value)'])
                    cnt+=1

            t = round(divide_zero(float(housing_price), float(cnt)), 2)
            if t > 0:
                city_all_area[0]['data'][date] = str(t)

        return city_all_area