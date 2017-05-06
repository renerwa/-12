# _*_ coding: gbk _*_
import requests
import time
import re


sdate='2017-04-13'

edate='2017-04-29'

dvice=[]

#sdate=raw_input('请按照2017-04-12的格式输入开始日期：')
#edate=raw_input('请按照2017-04-12的格式输入结束日期：')

print("正在读取数据……")

date={'device[]':dvice,'start_time':sdate,'end_time':'2017-04-29','type':0,'show':1}

raw_cookies='PHPSESSID=6vbuga3vefb3h0d7ajb00q6h76; user_info=LxH9Zvcr7RMZFWTcfrR9xBdz%2FVvlk9%2F1a1AgINWym8jPucmzqh0NUEZJ6xSTLx2MX9pbX3Di3Vl2OdZi6%2B8ZSwuPQAGcr7b8coQke%2Bah%2FA5CrxSP1%2F4HAZDn8%2B7ZERAnrnoDSEMQsWsK6VAXtr9WbMEqOC5AB6OYoCmxJNe8VTNCJdkp3rfSCPq713kpN%2BfJlq%2BQTFHbWQRuXKAuMdNrz82OYgE%2BSkq4fUskmap6AnJ2m5EvPit2qooQDeq3BZPC2hEzXQm0wiMYnR2tiJT%2BYPWB%2FRnPs3%2FsZH%2BxXwOepEcgIXRPfDQS93A%2Br3UUUC%2FbUYh%2B%2Bwirg2mu1IP8Db7YNeEErrJfzhc1QZi1oagDWoWGGAASl%2FfryNRTNkExc19V6%2B7hYpcIq%2FSn%2BAl0PPPi4n5TOnv1diPwlQ4ehtnxjBEShKe4oKgWWtk%2B%2FI0G4WxZf1E3Fz0IqilP3mi0LlJJoSOimGAY6Z8bD1hdUJ6Q6ZNQ8L9vHmauEfP723k49%2FllgPJCF9O7VMCS0qBvlhbOn0TsiR9gHzsqBl02M2YSm1giIyTYTvsWOH7hb3V3ZUE7zxdt%2FawUWtnfO0X0I2Ph4KWqf8Ekb9yIS1PmCXXaxlyTQUVLbLIMFfKp7txMcU%2F2TnBkxYLZAZueRQRYomqpGl14tWqQ3NzJkD%2BIx5CIS4GmW2Crh90rUU3XLFF5WNSYMcP0tRLGuAbmMAPRQjQX5OucoLuqpa0CSIcRIYKlYc4dypFUPyz3DLKfEel6wZus70s%2B9EiDlWnj4yRIxub%2FBAvMl4XIDORXZq95SovS5WNuFZ1vYJ4ibkHLHtIEtGDSiRec9yFa25d03nrdYzJFsYWQ091vFTudDGWV91E8DQPDZ%2Fb2omiR53cYQHrFU4hfsUHIf63ovhiGEUMkKB4Y0kur3mUemrQdPTXS1jn7SUm4v4OgVOnd46NG74Ed00lziSehPLRGzckUcUW1wzMDgQXJF8fv0oLa5HA7xaQ1rWWEUHmPG%2BuSpB4xMtfQEd1pHfIHkmGbbHEH%2Bu3MPnPRT6SctAH5%2BLCy7SQX5lxtdH1Az3BoLNO6Pj3ZazdiUkgaQ%2FL6DWobuSup4DAHJmW1raIicW75lT2ztCvhTmpFs0hWZbiIT5%2BrPestVYGcPc8vvd17TfzV0G5jD7bxZg4AL9fH%2F0SZTNX6JoovfuXQ0DbaozHJuqvPd6s%2Fh5e6FeV0q55%2FaclBc0uFhVbpx4NoTBG0ayLUDebOzFgL63TqZ%2BBJHEcnwKq4zBBIkveDmmTuh%2F5AseTzPOHeUtqoceliH01hJkjpzys6uWmNUb%2BbZSaUx4%2FNiAA2oxbJ9pyMl4c5EIpKNQQsAGaMH1%2FCiqjNJ9pjiytcB3bwEYlP2gmGsU0JfEFFSaDOGPTaw%2F5832g%2FgplLZtbRr8Hlv0tBzhqgtbX6xoWFIAfCwsLFj4%2FdYrjIS5N3viJKRNuFQ3CxmX2bHqL9ZVz4Duu1P80lKNy%2BEieJ0DX98aWpgMxm%2BWE9qsUs%2FghMOfgoc7%2FxQI3NoR4wjZK6nQNYzA5mUWkUKfW%2BJXFEUwrDNv8BjY9PlOh1Gv21kHMa7JIkskaXmoQi1I92geZtPlxZMl2iyPkeru6X2wtWAdiF3MrXDj9l4zEDRM217kQykzbqatdn4jQOZo%2FY1DnVV8ycUam%2BmqluLtZPm8LzwoptjQSQ8fqEBrfpFXhKuaGkGL3JZSQuDXtaOWInUBQfcqKLqiHkiEG9Jx2JFJVkM%2FvIkWsRZyX1JquFqfqTTEXsZZayzfFRXeu7kHLaGorRkdhaL7FZSfo1p7p5ADM7dWkvJP2TSEVYGJco3YA3rwE9zSDgnJ9GyVMeb6%2BRkZs39q%2Fxlbep4uY3RyNOr%2B2tQJu6GPGbHWgN%2FnxRL%2FY56uqgz8GxY4yr%2BKly5WgOqKKrdVlLrtMnVVfekzhgxHHLd9XW8K%2FNYzuFC880IhrplXbYVKHk%2FT6avbZjczdUqpYH1baI89XuYsBLlwdrWZEiD7v2wia8uU3C%2B0LVcWhX3o991l50x9t9r5gWoHXRnPAswVpTrxBJv8Abu2IH5QJHPuF6OLqKC5olKYZFlcWc%2BOR%2BtoTTy1S62CeVvSNvyQyXJpuqFVTHHKcRBX%2FC61cdoaJ2JoKaRO7H22YO9ipfuJQNxGlNxZ79fhJomF%2Bt2a85W6U9pqtBwOAydCZeLxeVdhPbwkHLehGLTWtZiwKrej4eN3SAXyUnUpg6yJUVa%2B8N38sO3WkbZZB10Bl%2Fp4mBYWCswV0yuB3WtkdfhaJGAfKc%2BVcnT7VE2xJcDAVP%2F9jLCLwJj2vuvXsN6neMEWOiBNXb%2FjRuTHcdWVqWQWAzunaB%2B5N8KZEWOdUfE1do3zzR0jcaELyKX%2FXAP%2Fxbt8Aihcxz618gKuwU6%2BHPFWfgB6p8AnLNuJvcBkKGsZF%2F8ieewFbAF2xfMa0lILGowAHOIEnCB6vTB4nzaL8wWwqsGEM%2F%2FxuO%2FdIRbMF5trzJKULv%2B3iv6NXvJuF%2BMjQ%2FhzmTVdfNkq7NqNZcaVXvD5tvAhshtql0NEUC66oEOak8V%2FPPJ6kxxcYmTjeR7Bt5vPIrXMxAZg0q9PDpypQQoHWsF0Z4fC3XFJnEjVfT3zSRjJSNhbjYTWiy39gU9Qbc3QwFqyAfc07FhZEHF3zIb%2F4GMmkExONU6dprRW0vWkt9ov9Hq8WWPbBhJBwXwJqx9LTUoK5c21P0uJKalvB2vCypH7fPI5egYiH8cHFQOyWyqF1YaljbZpC8YnqvzTuyar3rY27NwjZNywFMbJJXQk4G2ugM5VS9KgQpTkwsDpEtfyFhXxjSFk6ZGCTLVOo1hNW15%2BFwwijSN0QSoRjh%2FQwIjUCj33KkR%2FtdmTE4iD2z7rlwcIAWGV%2BSXO4JxLW7Z1FrUR%2B%2FA%2FH8XoR5Ricv3UrRBBgKBsH382sOOes55NypuKgi%2FA9LRNaMoK%2FylPl8LYae6fCmolKBuFYB0eHylNglqfxPYgYkUrPFo%2FggYQXzlv%2Fjno3a%2FMCbsKjVp11h119JCvQb0Vqsw8MIdJ5AyPb2MamLjODq5M17PIzPZxMPKOVGNHkZPp7rYMkhrp%2BeOMsi9AeXffDmUePGQtey5tT7oDqbHp50SaXeDTf6fVeJbCu27%2FYwiGts0BR7Navz6IPF8WSTFOXY7%2BZSw8KZguQ7MeGW71lapyJ8%2BrqMJEQkc%2FRMDOQhv5OWKyYwGzfmaBGRvj42scvExan6RjBqZecQkGAhv0cU3f8WWWUIQUT1jF0msTz9F19CNTzXDBesFKhKKqL8UJckRFebnAgQVlyOhOiy5MQ3dBfbbMfIU6sbom6%2FE%2BIN6dNpKnZmpwT8vIc4d85CxtvsdGC%2BOeX%2FHqy7fgHWWMrozS4ArXsJAc5oK8xCwcCQ1hbCi1jiQIRy7rBPDcQcOQqCLxIF%2BiSZlDoVbQSuXTlWovoR%2FEYwhn0G'

cookies={}

for line in raw_cookies.split(';'):
    key=line.split('=')[0]
    value=line.split('=')[1]
    cookies[key]=value

#print(cookies)    

r=requests.post('http://47.88.1.57:8090/data/user',cookies=cookies,data=date)

pat=re.compile('wooplus\"\:\{\"\d{4}[\d\-\:\"\,]+')

a=pat.findall(r.text)

pat2=re.compile(r'\"\d{4}.*\d')

a2=pat2.findall(a[0])

wooplus=[]

for line in a2[0].split(','):
    date=eval(line.split(':')[0])
    num=line.split(':')[1]
    wooplus.append([date , num])

tplt="{:10}\t{:60}"
new_file=open("num.TXT",'w')
new_file.write(tplt.format('date','num'))
new_file.write('\n')
for s in wooplus:
    #new_file.write(tplt.format(s[0],s[1]))
    new_file.write(s[0])
    new_file.write('\t')
    new_file.write(s[1])
    new_file.write('\n')
print('done')
new_file.close()


'''

print(tplt.format('date','num'))
i=0
for i in wooplus:
    print(tplt.format(i[0],i[1]))


'''
