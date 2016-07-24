#-*- coding=utf-8 -*-
'''
Author: TianRan
Date: 7/23/16
Version:
This is the city - area mapping in lianjia website
'''

# differnet area map for different url in lianjia website
BEIJING_AREA_MAP = {u'朝阳':u'chaoyang',u'昌平':u'changping',u'东城':u'dongcheng',
                u'大兴':u'daxing',u'房山':u'fangshan',u'丰台':u'fengtai',
                u'海淀':u'haidian',u'怀柔':u'huairou',u'门头沟':u'mentougou',
                u'密云':u'miyun',u'平谷':u'pinggu',u'石景山':u'shijingshan',
                u'顺义': u'shunyi',u'通州':u'tongzhou',u'西城':u'xicheng',
                u'延庆':u'yanqing',u'亦庄开发区':u'yizhuangkaifaqu',u'燕郊':u'yanjiao',
                u'安次':u'anci',u'广阳':u'guangyang'
                    }

LIANJIA_MAP = \
{
    u'Beijing':{
            u'website':u'http://bj.fang.lianjia.com',
            u'area_map':BEIJING_AREA_MAP
                }
}


if __name__ == '__main__':
    pass