from pyecharts import Map 
value =[155, 10, 66, 78, 33, 80, 190, 53, 49.6]
attr =["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
map=Map("Map 结合 VisualMap 示例", width=1200, height=600)
map.add("", attr, value, maptype='china', is_visualmap=True, visual_text_color='#000')
#map.show_config()
map.render('Map.html')

from pyecharts import Bar 
bar =Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
#bar.show_config()
bar.render('Bar.html')

from pyecharts import Geo 
data =[ ("海门", 9),("鄂尔多斯", 12),("招远", 12),("舟山", 12),("齐齐哈尔", 14),("盐城", 15), ("赤峰", 16),("青岛", 18),("乳山", 18),("金昌", 19),("泉州", 21),("莱西", 21), ("日照", 21),("胶南", 22),("南通", 23),("拉萨", 24),("云浮", 24),("梅州", 25)...]
geo =Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center",width=1200, height=600, background_color='#404a59')
attr, value =geo.cast(data)
geo.add("", attr, value, visual_range=[0, 200], visual_text_color="#fff", symbol_size=15, is_visualmap=True)
#geo.show_config()
geo.render('Geo.html')

from pyecharts import Liquid 
liquid =Liquid("水球图示例")
liquid.add("Liquid", [0.6])
#liquid.show_config()
liquid.render('liquid.html')

from pyecharts import Geo
data =[ ("海门", 9),("鄂尔多斯", 12),("招远", 12),("舟山", 12),("齐齐哈尔", 14),("盐城", 15), ("赤峰", 16),("青岛", 18),("乳山", 18),("金昌", 19),("泉州", 21),("莱西", 21), ("日照", 21),("胶南", 22),("南通", 23),("拉萨", 24),("云浮", 24),("梅州", 25)...]
geo =Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center",width=1200, height=600, background_color='#404a59')
attr, value =geo.cast(data)
geo.add("", attr, value, visual_range=[0, 200], visual_text_color="#fff", symbol_size=15, is_visualmap=True)
geo.show_config()
geo.render('Geo.html')

from pyecharts import Geo
data =[("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15)]
geo =Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600, background_color='#404a59')
attr, value =geo.cast(data)
geo.add("", attr, value, type="effectScatter", is_random=True, effect_scale=5)
#geo.show_config()
geo.render('Geo_active.html')