import scrapy
import time
from fangspider.items import FangItem,Fang1Item,Fang2Item

from scrapy_redis.spiders import RedisSpider

class Fang(RedisSpider):
    name = "fang"
    # start_urls=[
    #     'https://www.fang.com/SoufunFamily.htm',
    # ]
    redis_key = 'fang:start_urls'

    def newhouse(self,response):
        lilist=response.xpath("//div[@class='nhouse_list']/div[@class='nl_con clearfix']/ul/li")
        for li in lilist:
            try:
                house_image=li.xpath(".//div[@class='clearfix']/div[@class='nlc_img']/a/img/@src").getall()[-1].strip()
                house_detail=li.xpath(".//div[@class='clearfix']/div[@class='nlc_img']/a/@href").get().strip()
                house_name=li.xpath(".//div[@class='clearfix']/div[@class='nlc_details']/div[@class='house_value clearfix']/div/a/text()").get().strip()
                house_descript=li.xpath(".//div[@class='clearfix']/div[@class='nlc_details']/div[@class='house_type clearfix']/a/text()").getall()
                house_size=li.xpath(".//div[@class='clearfix']/div[@class='nlc_details']/div[@class='house_type clearfix']")[0].xpath('string(.)').get().replace('\t','').replace("\n","").split("－")[1]
                house_descript='/'.join(house_descript)
                house_address = li.xpath(".//div[@class='clearfix']/div[@class='nlc_details']/div[@class='relative_message clearfix']/div[@class='address']/a/@title").get().strip()
                house_phone = li.xpath(".//div[@class='clearfix']/div[@class='nlc_details']/div[@class='relative_message clearfix']/div[@class='tel']/p/text()").get().strip()
                try:
                    house_price=li.xpath(".//div[@class='clearfix']/div[@class='nlc_details']/div[@class='nhouse_price']/span/text()").get()+ \
                        li.xpath(".//div[@class='clearfix']/div[@class='nlc_details']/div[@class='nhouse_price']/em/text()").get()
                except:
                    house_price = li.xpath(".//div[@class='clearfix']/div[@class='nlc_details']/div[@class='nhouse_price']/span/text()").get()
                house_label= li.xpath(".//div[@class='clearfix']/div[@class='nlc_details']/div[contains(@class, 'fangyuan')]/span/text()").get()+'/' \
                    +'/'.join(li.xpath(".//div[@class='clearfix']/div[@class='nlc_details']/div[contains(@class, 'fangyuan')]/a/text()").getall())
            except:
                continue
            city_name=response.meta['city_name']
            area_name=response.meta['area_name']
            item=Fang2Item(flag=3,house_image=house_image,house_detail=house_detail,house_name=house_name,house_descript=house_descript,house_size=house_size,house_address=house_address,house_phone=house_phone,city_name=city_name,area_name=area_name,house_price=house_price,house_label=house_label)
            yield item
        last_url=response.xpath("//div[@class='page']/ul[@class='clearfix']/li[@class='fr']/a[@class='last']")
        if not last_url:
            return 0        #表示爬取完毕
        else:
            next_url=response.xpath("//div[@class='page']/ul[@class='clearfix']/li[@class='fr']/a[@class='active']/following-sibling::a[1]/@href").get()
            if next_url==None:
                return
            next_url=response.meta['area_url']+next_url
            yield scrapy.Request(next_url,self.newhouse,meta={'area_url':response.meta['area_url'],'city_name':city_name,'area_name':area_name})
    def esfhouse(self,response):
        pass
    def zuhouse(self,response):
        pass
    def parse(self, response):
        #得到tr标签的列表
        temp_name = ''
        trlist=response.xpath("//div[@class='mainContent']/div[@class='letterSelt']/div[@class='outCont']/table[@class='table01']/tr")
        for tr in trlist:
            tdlist=tr.xpath(".//td")
            if tdlist[1].xpath(".//strong/text()").get() != None and len(tdlist[1].xpath(".//strong/text()").get()) != 1:      #省份
                province = tdlist[1].xpath(".//strong/text()").get()
            else:
                province = temp_name
            areas=tdlist[2].xpath(".//a")
            for area in areas:          #表示一个省的城市
                area_name=area.xpath(".//text()").get()
                area_url=area.xpath(".//@href").get()

                items=FangItem(flag=1,province_name=province,city_name=area_name,city_url=area_url)
                yield items


                newhouse_url = "https://" + area_url.split("//")[1].split(".")[0] + ".newhouse.fang.com/house/s/"
                url_root="https://" + area_url.split("//")[1].split(".")[0] + ".newhouse.fang.com"
                yield scrapy.Request(newhouse_url, callback=self.area,meta={'province': province, 'area_name': area_name,'url':url_root})
            temp_name = province
    def area(self,response):
        province=response.meta['province']
        city_name=response.meta['area_name']
        url=response.meta['url']
        dd=response.xpath("//div[@class='choose main_1200 tf']/dl[@id='ax1'][1]/dd[@id='sjina_D03_05']/ul/li[@class='quyu_name dingwei']/a")
        for a in dd[1:]:
            area_name=a.xpath(".//text()").get()
            area_url=url+a.xpath(".//@href").get()
            item=Fang1Item(flag=2,province_name=province,city_name=city_name,area_url=area_url,area_name=area_name)
            yield item
            yield scrapy.Request(area_url, callback=self.newhouse,meta={'area_name':area_name,'province':province,'city_name':city_name,'area_url':url})
