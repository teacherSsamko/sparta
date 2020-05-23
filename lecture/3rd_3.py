import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()['RealtimeCityAir']


gus = rjson['row']

# for gu in gus:
#     if gu['IDEX_MVL'] < 90:
#         print(gu['MSRSTE_NM'], gu['IDEX_MVL'])

def gu_o3(gu_name):
    if rjson['RESULT']['CODE'] == 'INFO-000':
        for gu in gus:
            if gu['MSRSTE_NM'] == gu_name:
                return gu['O3']

print(gu_o3('용산구'))