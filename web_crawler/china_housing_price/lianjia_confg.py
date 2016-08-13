#-*- coding=utf-8 -*-
'''
Author: TianRan
Date: 7/23/16
Version:
This is the city - area mapping in lianjia website
'''

# differnet area map for different url in lianjia website
BEIJING_AREA_MAP = \
    {
        u'朝阳':u'chaoyang',u'昌平':u'changping',u'东城':u'dongcheng',
        u'大兴':u'daxing',u'房山':u'fangshan',u'丰台':u'fengtai',
        u'海淀':u'haidian',u'怀柔':u'huairou',u'门头沟':u'mentougou',
        u'密云':u'miyun',u'平谷':u'pinggu',u'石景山':u'shijingshan',
        u'顺义': u'shunyi',u'通州':u'tongzhou',u'西城':u'xicheng',
        u'延庆':u'yanqing',u'亦庄开发区':u'yizhuangkaifaqu',u'燕郊':u'yanjiao',
        u'安次':u'anci',u'广阳':u'guangyang'
    }
CHENGDU_AREA_MAP = \
    {
        u'锦江':u'jinjiang',u'青羊':u'qingyang',u'金牛':u'jinniu',u'武侯':u'wuhou',
        u'成华':u'chenghua',u'龙泉驿':u'longquanyi',u'青白江':u'qingbaijiang',
        u'新都':u'xindou',u'温江':u'wenjiang',u'金堂':u'jintang',u'双流':u'shuangliu',
        u'郫县':u'pixian',u'大邑':u'dayi',u'蒲江':u'pujiang',u'新津':u'xinjin',
        u'都江堰':u'doujiangyan',u'彭州':u'pengzhou',u'邛崃':u'qionglai',
        u'崇州':u'chongzhou1',u'高新':u'gaoxin7',u'天府新区':u'tianfuxinqu',
        u'彭山':u'pengshan'
    }
CHONGQING_AREA_MAP=\
    {
        u'万州':u'wanzhou',u'涪陵':u'fuling',u'万盛':u'wansheng',u'双桥':u'shuangqiao1',
        u'黔江':u'qianjiang',u'长寿':u'changshou1',u'江津':u'jiangjing',u'璧山':u'bishan',
        u'綦江':u'qijiang',u'南川':u'nanchuang',u'合川':u'hechuang',u'铜梁':u'tongliang',
        u'梁平':u'liangping',u'潼南':u'tongnan',u'云阳':u'yunyang',u'大足':u'dazu',
        u'武隆县':u'wulongxian',u'石柱':u'shizhu',u'高新':u'gaoxin2',u'渝中':u'yuzhong',
        u'江北':u'jiangbei',u'南岸':u'nanan',u'大渡口':u'dadukou',u'九龙坡':u'jiulongpo',
        u'沙坪坝':u'shapingba',u'巴南':u'banan',u'北碚':u'beibei',u'渝北':u'yubei',
        u'永川':u'yongchuan',u'丰都':u'fengdu1',
    }
CHANGSHA_AREA_MAP=\
    {
        u'望城':u'wangcheng',u'宁乡':u'ningxiang',u'浏阳':u'liuyang',u'雨花':u'yuhua',
        u'天心':u'tianxin',u'岳麓':u'yuelu',u'芙蓉':u'furong',u'开福':u'kaifu',u'长沙县':u'changshaxian',
    }
DALIAN_AREA_MAP=\
    {
        u'中山':u'zhongshan',u'西岗':u'xigang',u'沙河口':u'shahekou',u'甘井子':u'ganjingzi',
        u'旅顺口':u'lvshunkou',u'金州':u'jinzhou',u'长海':u'changhai',u'瓦房店':u'wafangdian',
        u'普兰店':u'pulandian',u'庄河':u'zhuanghe',u'高新园区':u'gaoxinyuanqu',u'开发区':u'kaifaqudl',
    }
DONGGUAN_AREA_MAP=\
    {
        u'中堂':u'zhongtang',u'企石':u'qishi',u'凤岗':u'fenggang',u'南城':u'nancheng',
        u'厚街':u'houjie',u'塘厦':u'tangxia',u'大岭山':u'dalingshan',u'大朗':u'dalang',
        u'寮步':u'liaobu',u'常平':u'changping',u'望牛墩':u'wangniudun',u'松山湖':u'songshanhu',
        u'桥头':u'qiaotou',u'樟木头':u'zhangmutou',u'横沥':u'hengli',u'沙田':u'shatian',
        u'洪梅':u'hongmei',u'清溪':u'qingxi',u'石排':u'shipai',u'石碣':u'shijie',
        u'石龙':u'shilong',u'茶山':u'chashan',u'莞城':u'guancheng',u'虎门':u'humen',
        u'道滘':u'daojiao',u'长安':u'changan',u'高埗':u'gaobu',u'麻涌':u'mayong',
        u'黄江':u'huangjiang',u'其他':u'qita',
    }
FOUSHAN_AREA_MAP=\
    {
        u'三水':u'sanshui',u'南海':u'nanhai',u'禅城':u'chancheng',u'顺德':u'shunde',
        u'高明':u'gaoming',u'其他':u'qita',
    }
GUANGZHOU_AREA_MAP=\
    {
        u'从化':u'conghua',u'佛冈':u'fogang',u'佛山':u'foshan',u'南沙':u'nansha',
        u'南海':u'nanhai',u'增城':u'zengcheng',u'天河':u'tianhe',u'海珠':u'haizhu',
        u'清远':u'qingyuan',u'番禺':u'panyu',u'白云':u'baiyun',u'花都':u'huadu',
        u'荔湾':u'liwan',u'越秀':u'yuexiu',u'顺德':u'shunde',u'黄埔':u'huangpu',u'其他':u'qita',
    }
HANGZHOU_AREA_MAP=\
    {
        u'上城':u'shangcheng',u'下城':u'xiacheng',u'江干':u'jianggan',u'拱墅':u'gongshu',
        u'西湖':u'xihu',u'滨江':u'binjiang',u'萧山':u'xiaoshan',u'余杭':u'yuhang',
        u'桐庐':u'tonglu1',u'淳安':u'chunan1',u'建德':u'jiande',u'富阳':u'fuyang',
        u'临安':u'linan',u'海宁市':u'hainingshi',
    }
HUIZHOU_AREA_MAP=\
    {
        u'仲恺':u'zhongkai',u'博罗':u'boluo',u'大亚湾':u'dayawan',u'惠东':u'huidong',
        u'惠城':u'huicheng',u'惠阳':u'huiyang',u'龙门':u'longmen',
    }
HAIKOU_AREA_MAP=\
    {
        u'海口市':u'haikoushi',
    }
JINAN_AREA_MAP=\
    {
        u'历下':u'lixia',u'市中':u'shizhong',u'槐荫':u'huaiyin',u'天桥':u'tianqiao',u'历城':u'licheng',
        u'长清':u'changqing',u'章丘':u'zhangqiu1',u'高新':u'gaoxin',u'济阳':u'jiyang',u'商河':u'shanghe',
    }
JIAXIN_AREA_MAP=\
    {
        u'中心城区':u'zhongxinchengqu',u'南湖新区':u'nanhuxinqu',u'嘉善':u'jiashan',u'国际商务区':u'guojishangwuqu',
        u'大麻镇':u'damazhen',u'平湖':u'pinghu',u'广陈镇':u'guangchenzhen',u'桐乡':u'tongxiang',u'海盐':u'haiyan',
        u'秀洲新区':u'xiuzhouxinqu',u'经济开发区':u'jingjikaifaqu',u'运河新区':u'yunhexinqu',
    }
LinXIN_AREA_MAP=\
    {
        u'临沭县':u'linshuxian',u'兰山区':u'lanshanqu',u'北城新区':u'beichengxinqu',u'沂南县':u'yinanxian',
        u'沂水县':u'yishuixian',u'河东区':u'hedongqu',u'经济开发区':u'jingjikaifaqu',u'罗庄区':u'luozhuangqu',
        u'苍山县':u'cangshanxian',u'蒙阴县':u'mengyinxian',u'费县':u'feixian',u'郯城县':u'tanchengxian',
        u'高新区':u'gaoxinqu',
    }
NANJING_AREA_MAP=\
    {
        u'玄武':u'xuanwu',u'秦淮':u'qinhuai',u'建邺':u'jianye',u'鼓楼':u'gulou',
        u'浦口':u'pukou',u'栖霞':u'qixia',u'雨花台':u'yuhuatai',u'江宁':u'jiangning',
        u'六合':u'liuhe',u'溧水':u'lishui',u'高淳':u'gaochun',
    }
NANTONG_AREA_MAP=\
    {
        u'启东':u'qidong',u'如东':u'rudong',u'如皋':u'rugao',u'崇川区':u'chongchuanqu',
        u'开发区':u'kaifaqu',u'海安':u'haian',u'海门':u'haimen',
        u'港闸区':u'gangzhaqu',u'通州区':u'tongzhouqu',
    }
QINGDAO_AREA_MAP=\
    {
        u'市南':u'shinan',u'市北':u'shibei',u'四方':u'sifang',u'黄岛':u'huangdao',
        u'崂山':u'laoshan',u'李沧':u'licang',u'城阳':u'chengyang',u'胶州':u'jiaozhou',
        u'即墨':u'jimo',u'平度':u'pingdu',u'胶南':u'jiaonan',u'莱西':u'laixi',
        u'高新':u'gaoxin6',
    }
SHANGHAI_AREA_MAP=\
    {
        u'浦东':u'pudongxinqu',u'嘉定':u'jiading',u'松江':u'songjiang',u'宝山':u'baoshan',
        u'闵行':u'minhang',u'青浦':u'qingpu',u'普陀':u'putuo',u'徐汇':u'xuhui',
        u'杨浦':u'yangpu',u'闸北':u'zhabei',u'黄浦':u'huangpu',u'奉贤':u'fengxian',
        u'长宁':u'changning',u'虹口':u'hongkou',u'静安':u'jingan',u'金山':u'jinshan',
        u'崇明':u'chongming',u'上海周边':u'shanghaizhoubian',
    }
SHENZHEN_AREA_MAP=\
    {
        u'宝安':u'baoan',u'大鹏新区':u'dapengxinqu',u'福田':u'futian',u'光明新区':u'guangmingxinqu',
        u'龙岗':u'longgang',u'龙华新区':u'longhuaxinqu',u'罗湖':u'luohu',u'南山':u'nanshan',
        u'坪山新区':u'pingshanxinqu',u'盐田':u'yantian',u'惠州':u'huizhou',
    }
SOUZHOU_AREA_MAP=\
    {
        u'吴中':u'wuzhong',u'相城':u'xiangcheng',u'高新':u'gaoxin1',u'姑苏':u'gusu',
        u'工业园区':u'gongyeyuan',u'吴江':u'wujiang',
    }
SHIJIAZHUANG_AREA_MAP=\
    {
        u'新华':u'xinhua',u'长安':u'changan',u'裕华':u'yuhua1',u'桥西':u'qiaoxi',
        u'行唐':u'xingtang',u'正定':u'zhengding',u'栾城':u'luancheng',
        u'平山':u'pingshan1',u'新乐':u'xinle',u'无极县':u'wujixian',u'辛集市':u'shenzexian',
        u'赞皇县':u'zanhuangxian',u'赵县':u'zhaoxian',u'鹿泉':u'luquan',
        u'藁城':u'gaocheng',u'元氏县':u'yuanshixian',u'高邑县':u'gaoyixian',
        u'晋州市':u'jinzhoushi',u'井陉县':u'jingxingxian',u'灵寿县':u'lingshouxian',
        u'开发区':u'kaifaqu1',
    }
SHENYANG_AREA_MAP=\
    {
        u'于洪':u'yuhong',u'和平':u'heping',u'大东':u'dadong',u'康平':u'kangping',
        u'抚顺市':u'fushunshi',u'新民':u'xinmin',u'本溪市':u'benxishi',u'沈北新区':u'shenbeixinqu',
        u'沈河':u'shenhe',u'浑南区':u'hunnanqu',u'皇姑':u'huanggu',u'苏家屯':u'sujiatun',
        u'辽中':u'liaozhong',u'铁岭':u'tieling',u'铁西':u'tiexi',u'其他':u'qita',
    }
TIANJIN_AREA_MAP=\
    {
        u'和平':u'heping',u'河东':u'hedong',u'河西':u'hexi',u'南开':u'nankai',
        u'河北':u'hebei',u'红桥':u'hongqiao',u'塘沽':u'tanggu',u'东丽':u'dongli',
        u'西青':u'xiqing',u'津南':u'jinnan',u'北辰':u'beichen',u'武清':u'wuqing',
        u'滨海新区':u'binhaixinqu',u'开发区':u'kaifaqutj',u'宝坻':u'baodi',
        u'宁河':u'ninghe',u'静海':u'jinghai',u'蓟县':u'jixian',
    }
TANGSHAN_AREA_MAP=\
    {
        u'丰南':u'fengnan',u'丰润':u'fengrun',u'乐亭县':u'laotingxian',u'古冶':u'guye',
        u'开平':u'kaiping',u'曹妃甸新区':u'caofeidianxinqu',u'汉沽管理区':u'hanguguanliqu',
        u'海港开发区':u'haigangkaifaqu',u'滦南县':u'luannanxian',u'滦县':u'luanxian',
        u'玉田县':u'yutianxian',u'路北':u'lubei',u'路南':u'lunan',u'迁安市':u'qiananshi',
        u'迁西县':u'qianxixian',u'遵化市':u'zunhuashi',u'高新区':u'gaoxinqu',
    }
TAIYUAN_AREA_MAP=\
    {
        u'万柏林':u'wanbolin',u'小店':u'xiaodian',u'尖草坪':u'jiancaoping',
        u'晋源':u'jinyuan',u'杏花岭':u'xinghualing',u'榆次':u'yuci',
        u'迎泽':u'yingze',u'阳曲':u'yangqu',
    }
WUHAN_AREA_MAP=\
    {
        u'汉南':u'hannan',u'蔡甸':u'caidian',u'江夏':u'jiangxia',u'黄陂':u'huangbei',
        u'新洲':u'xinzhou',u'江岸':u'jiangan',u'江汉':u'jianghan',u'武昌':u'wuchang',
        u'硚口':u'qiaokou',u'汉阳':u'hanyang',u'洪山':u'hongshan',u'东西湖':u'dongxihu',
        u'青山':u'qingshan',
    }
WUXI_AREA_MAP=\
    {
        u'北塘区':u'beitangqu',u'南长区':u'nanchangqu',u'崇安区':u'chonganqu',u'惠山区':u'huishanqu',
        u'新区':u'xinqu',u'滨湖区':u'binhuqu',u'锡山区':u'xishanqu',u'其他':u'qita',
    }
WEIFANG_AREA_MAP=\
    {
        u'临朐县':u'linquxian',u'坊子':u'fangzi',u'奎文':u'kuiwen',u'安丘市':u'anqiushi',
        u'寒亭':u'hanting',u'寿光市':u'shouguangshi',u'峡山经济开发区':u'xiashanjingjikaifaqu',
        u'昌乐县':u'changlexian',u'昌邑市':u'changyishi',u'滨海经济开发区':u'binhaijingjikaifaqu',
        u'潍城':u'weicheng',u'经济开发区':u'jingjikaifaqu',u'诸城市':u'zhuchengshi',
        u'青州市':u'qingzhoushi',u'高密市':u'gaomishi',u'高新技术开发区':u'gaoxinjishukaifaqu',
    }
WEIZHOU_AREA_MAP=\
    {
        u'乐清市':u'yueqingshi',u'平阳县':u'pingyangxian',u'文成县':u'wenchengxian',
        u'永嘉县':u'yongjiaxian',u'泰顺县':u'taishunxian',u'洞头县':u'dongtouxian',
        u'瑞安市':u'ruianshi',u'瓯海':u'ouhai',u'苍南县':u'cangnanxian',u'鹿城':u'lucheng',
        u'龙湾':u'longwan',
    }
XIAN_AREA_MAP=\
    {
        u'高陵':u'gaoling1',u'西咸':u'xixian',u'城内':u'chengnei',u'经开':u'jingkai',
        u'城南':u'chengnan',u'城北':u'chengbei',u'浐灞':u'chanba',u'城东':u'chengdong',
        u'临潼':u'lintong',u'阎良':u'yanliang',u'长安':u'changan1',u'曲江':u'qujiang',
        u'城西':u'chengxi',u'高新':u'gaoxin4',u'蓝田':u'lantian',u'户县':u'huxian',
        u'周至':u'zhouzhi',u'渭南':u'weinan',
    }
XIAMEN_AREA_MAP=\
    {
        u'云霄县':u'yunxiaoxian',u'同安':u'tongan',u'思明':u'siming',u'海沧':u'haicang',
        u'湖里':u'huli',u'漳州':u'zhangzhou',u'翔安':u'xiangan',u'集美':u'jimei',
        u'其他':u'qita',
    }
XUZHOU_AREA_MAP=\
    {
        u'丰县':u'fengxian',u'云龙区':u'yunlongqu',u'新城区':u'xinchengqu',u'新沂市':u'xinyishi',
        u'梁寨镇':u'liangzhaizhen',u'沛县':u'peixian',u'泉山区':u'quanshanqu',
        u'睢宁县':u'suiningxian',u'贾汪区':u'jiawangqu',u'邳州市':u'pizhoushi',
        u'金山桥开发区':u'jinshanqiaokaifaqu',u'铜山区':u'tongshanqu',
        u'鼓楼区':u'gulouqu',
    }
YANTAI_AREA_MAP=\
    {
        u'招远市':u'zhaoyuanshi',u'栖霞':u'xixia',u'海阳':u'haiyang',u'牟平':u'muping',
        u'福山':u'fushan',u'芝罘':u'zhifu',u'莱山':u'laishan',u'莱州市':u'laizhoushi',
        u'莱阳市':u'laiyangshi',u'蓬莱':u'penglai',u'长岛县':u'changdaoxian',u'高新区':u'gaoxinqu',
        u'龙口':u'longkou',
    }
YANGZHOU_AREA_MAP=\
    {
        u'仪征市':u'yizhengshi',u'宝应市':u'baoyingshi',u'广陵区':u'guanglingqu',
        u'开发区':u'kaifaqu',u'江都区':u'jiangduqu',u'邗江区':u'hanjiangqu',
        u'高邮市':u'gaoyoushi',u'其他':u'qita,'
    }
ZHONGSHAN_AREA_MAP=\
    {
        u'三乡镇':u'sanxiangzhen',u'三角镇':u'sanjiaozhen',u'东凤镇':u'dongfengzhen',
        u'东区':u'dongqu',u'东升镇':u'dongshengzhen',u'五桂山镇':u'wuguishanzhen',
        u'南区':u'nanqu',u'南头镇':u'nantouzhen',u'南朗镇':u'nanlangzhen',u'古镇镇':u'guzhenzhen',
        u'坦洲镇':u'tanzhouzhen',u'大涌镇':u'dayongzhen',u'小榄镇':u'xiaolanzhen',u'板芙镇':u'banfuzhen',
        u'横栏镇':u'henglanzhen',u'民众镇':u'minzhongzhen',u'沙溪镇':u'shaxizhen',
        u'港口镇':u'gangkouzhen',u'火炬开发区':u'huojukaifaqu',u'石岐区':u'shiqiqu',
        u'神湾镇':u'shenwanzhen',u'西区':u'xiqu',
        u'阜沙镇':u'fushazhen',u'黄圃镇':u'huangpuzhen',
    }
ZHUHAI_AREA_MAP=\
    {
        u'中山市':u'zhongshanshi',u'斗门':u'doumen',u'横琴':u'hengqin',
        u'金湾':u'jinwan',u'香洲':u'xiangzhou',u'高栏港经济区':u'gaolangangjingjiqu',
        u'其他':u'qita',
    }

# LianJia map for different cities and websites
LIANJIA_MAP = \
{
    u'Beijing':
        {
            u'website':u'http://bj.fang.lianjia.com',
            u'area_map':BEIJING_AREA_MAP
        },
    u'Chengdu':
        {
            u'website':u'http://cd.fang.lianjia.com/',
            u'area_map':CHENGDU_AREA_MAP
        },
    u'Chongqing':
        {
            u'website':u'http://cq.fang.lianjia.com/',
            u'area_map':CHONGQING_AREA_MAP
        },
    u'Changsha':
        {
            u'website': u'http://cs.fang.lianjia.com/',
            u'area_map': CHANGSHA_AREA_MAP
        },
    u'Dalian':
        {
            u'website': u'http://dl.fang.lianjia.com/',
            u'area_map': DALIAN_AREA_MAP
        },
    u'Dongguan':
        {
            u'website': u'http://dg.fang.lianjia.com/',
            u'area_map': DONGGUAN_AREA_MAP
        },
    u'Foushan':
        {
            u'website': u'http://fs.fang.lianjia.com/',
            u'area_map': FOUSHAN_AREA_MAP
        },
    u'Guangzhou':
        {
            u'website': u'http://gz.fang.lianjia.com/',
            u'area_map': GUANGZHOU_AREA_MAP
        },
    u'Hangzhou':
        {
            u'website': u'http://hz.fang.lianjia.com/',
            u'area_map': HANGZHOU_AREA_MAP
        },
    u'Huizhou':
        {
            u'website': u'http://hui.fang.lianjia.com/',
            u'area_map': HUIZHOU_AREA_MAP
        },
    u'Haikou':
        {
            u'website': u'http://hk.fang.lianjia.com/',
            u'area_map': HAIKOU_AREA_MAP
        },
    u'Jinan':
        {
            u'website': u'http://jn.fang.lianjia.com/',
            u'area_map': JINAN_AREA_MAP
        },
    u'Jiaxin':
        {
            u'website': u'http://jx.fang.lianjia.com/',
            u'area_map': JIAXIN_AREA_MAP
        },
    u'Linxin':
        {
            u'website': u'http://lin.fang.lianjia.com/',
            u'area_map': LinXIN_AREA_MAP
        },
    u'Nanjing':
        {
            u'website': u'http://nj.fang.lianjia.com/',
            u'area_map': NANJING_AREA_MAP
        },
    u'Nantong':
        {
            u'website': u'http://nt.fang.lianjia.com/',
            u'area_map': NANTONG_AREA_MAP
        },
    u'Qingdao':
        {
            u'website': u'http://qd.fang.lianjia.com/',
            u'area_map': QINGDAO_AREA_MAP
        },
    u'Shanghai':
        {
            u'website': u'http://sh.fang.lianjia.com',
            u'area_map': SHANGHAI_AREA_MAP
        },
    u'Shenzhen':
        {
            u'website': u'http://sz.fang.lianjia.com/',
            u'area_map': SHENZHEN_AREA_MAP
        },
    u'Souzhou':
        {
            u'website': u'http://su.fang.lianjia.com/',
            u'area_map': SOUZHOU_AREA_MAP
        },
    u'Shijiazhuang':
        {
            u'website': u'http://sjz.fang.lianjia.com/',
            u'area_map': SHIJIAZHUANG_AREA_MAP
        },
    u'Shenyang':
        {
            u'website': u'http://sy.fang.lianjia.com/',
            u'area_map': SHENYANG_AREA_MAP
        },
    u'Tianjin':
        {
            u'website': u'http://tj.fang.lianjia.com/',
            u'area_map': TIANJIN_AREA_MAP
        },
    u'Tangshan':
        {
            u'website': u'http://ts.fang.lianjia.com/',
            u'area_map': TANGSHAN_AREA_MAP
        },
    u'Taiyuan':
        {
            u'website': u'http://ty.fang.lianjia.com/',
            u'area_map': TAIYUAN_AREA_MAP
        },
    u'Wuhan':
        {
            u'website': u'http://wh.fang.lianjia.com/',
            u'area_map': WUHAN_AREA_MAP
        },
    u'Wuxi':
        {
            u'website': u'http://wx.fang.lianjia.com/',
            u'area_map': WUXI_AREA_MAP
        },
    u'Weifang':
        {
            u'website': u'http://wf.fang.lianjia.com/',
            u'area_map': WEIFANG_AREA_MAP
        },
    u'Weizhou':
        {
            u'website': u'http://wz.fang.lianjia.com/',
            u'area_map': WEIZHOU_AREA_MAP
        },
    u'Xian':
        {
            u'website': u'http://xa.fang.lianjia.com/',
            u'area_map': XIAN_AREA_MAP
        },
    u'Xiamen':
        {
            u'website': u'http://xm.fang.lianjia.com/',
            u'area_map': XIAMEN_AREA_MAP
        },
    u'Xuzhou':
        {
            u'website': u'http://xz.fang.lianjia.com/',
            u'area_map': XUZHOU_AREA_MAP
        },
    u'Yantai':
        {
            u'website': u'http://yt.fang.lianjia.com/',
            u'area_map': YANTAI_AREA_MAP
        },
    u'Yanzhou':
        {
            u'website': u'http://yz.fang.lianjia.com/',
            u'area_map': YANGZHOU_AREA_MAP
        },
    u'Zhongshan':
        {
            u'website': u'http://zs.fang.lianjia.com/',
            u'area_map': ZHONGSHAN_AREA_MAP
        },
    u'Zhuhai':
        {
            u'website': u'http://zh.fang.lianjia.com/',
            u'area_map': ZHUHAI_AREA_MAP
        },

}


if __name__ == '__main__':
    from utils.path_util import PROJECT_DIR

    json_out_path = PROJECT_DIR + '/data/json/crawler/housing/2016-08-07_lianjia_housing.json'
    import json
    import uniout

    with open(json_out_path,'r') as f:
        json_dict = json.load(f)
        print json_dict