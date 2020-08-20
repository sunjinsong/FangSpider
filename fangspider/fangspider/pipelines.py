# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from fangspider.items import FangItem,Fang1Item,Fang2Item
import pymysql
class FangPipeline:
    def open_spider(self,spider):
        self.conn = pymysql.connect(host='127.0.0.1', user ='root', password ='', database ='', charset ='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if item['flag']==1:
            province=item['province_name']
            city_name=item['city_name']
            city_url=item['city_url']
            sql1="select province_name from province_table where province_name='%s'"%(province)
            sql2 = "insert into province_table(province_name) values('"+province+"')"
            self.cursor.execute(sql1)
            result=self.cursor.fetchone()

            if result==None:
                self.cursor.execute(sql2)
                self.conn.commit()
                self.cursor.execute("select id from province_table where province_name='%s'"%(province))
                id=self.cursor.fetchone()[0]
                sql3="insert into city_table(city_name,city_url,Province_table_id ) values('%s','%s',%d)"%(city_name,city_url,int(id))
                self.cursor.execute(sql3)
                self.conn.commit()
            else:
                self.cursor.execute("select id from province_table where province_name='%s'"%(province))
                id=self.cursor.fetchone()[0]
                sql3="insert into city_table(city_name,city_url,Province_table_id ) values('%s','%s',%d)"%(city_name,city_url,int(id))
                self.cursor.execute(sql3)
                self.conn.commit()

            newhouse_url = ''
            if city_url == "http://bj.fang.com/":  # 北京的房子例外
                newhouse_url = "https://newhouse.fang.com/house/s/"
            else:
                # https://hf.fang.com/
                newhouse_url = "https://" + city_url.split("//")[1].split(".")[0] + ".newhouse.fang.com/house/s/"

            esfhouse_url = ''
            if city_url == "http://bj.fang.com/":  # 北京的房子例外
                esfhouse_url = "https://esf.fang.com/"
            else:
                # https://hf.fang.com/
                esfhouse_url = "https://" + city_url.split("//")[1].split(".")[0] + ".esf.fang.com"

            zuhouse_url = ''
            if city_url == "http://bj.fang.com/":  # 北京的房子例外
                zuhouse_url = "https://zu.fang.com/"
            else:
                # https://hf.fang.com/
                zuhouse_url = "https://" + city_url.split("//")[1].split(".")[0] + ".zu.fang.com"
            self.cursor.execute("select id from city_table where city_name='%s'" % (city_name))
            id = self.cursor.fetchone()[0]                  #城市的主键
            for url in [newhouse_url]:   #,esfhouse_url,zuhouse_url]:
                sql3 = "insert into typeofhouse_table (house_type,house_url,City_table_id) values('%s','%s',%d)" % (city_name, url, int(id))
                self.cursor.execute(sql3)
                self.conn.commit()
        elif item['flag']==2:
            province_name=item['province_name']
            city_name=item['city_name']
            area_url=item['area_url']
            area_name=item['area_name']
            self.cursor.execute("select id from typeofhouse_table where house_type='%s'" % (city_name))
            id = self.cursor.fetchone()[0]      #得到区域所在的城市
            sql="insert into area_table(area_name,area_url,TypeOfHouse_table_id ) values('%s','%s',%d)"%(area_name,area_url,int(id))
            self.cursor.execute(sql)
            self.conn.commit()
        elif item['flag']==3:
            house_image=item['house_image']
            house_detail=item['house_detail']
            house_name=item['house_name']
            house_descript=item['house_descript']
            if isinstance(house_descript,list):
                house_descript=house_descript[0]
            house_size=item['house_size']
            house_address=item['house_address']
            house_phone=item['house_phone']
            city_name=item['city_name']
            area_name=item['area_name']
            house_price=item['house_price']
            house_label=item['house_label']
            self.cursor.execute("select id from typeofhouse_table where house_type='%s'" % (city_name))
            print(city_name)
            id = self.cursor.fetchone()[0]      #得到区域所在的城市
            self.cursor.execute("select id from area_table where area_name='%s' and TypeOfHouse_table_id=%d" % (area_name,int(id)))
            id = self.cursor.fetchone()[0]      #得到区域id
            try:
                sql="insert into newhouseinfo_table(house_image,house_detail,house_name,house_descript,house_size,house_address,house_phone,Area_table_id,house_price,house_label) values('%s','%s','%s','%s','%s','%s','%s',%d,'%s','%s')"%(house_image.replace("'",""),house_detail.replace("'",""),house_name.replace("'",""),house_descript.replace("'",""),house_size.replace("~","-"),house_address.replace("'",""),house_phone.replace("'",""),int(id),house_price,house_label)
            except:
                print (house_image,house_detail,house_name,house_descript,house_size,house_address,house_phone,house_price,house_label)

            self.cursor.execute(sql)
            self.conn.commit()

    def cloase_spider(self,spider):
        self.cursor.close()
        self.conn.close()
