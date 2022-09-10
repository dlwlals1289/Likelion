from unicodedata import category
import requests
import json

name = "홍대 꽃집" # 검색하고자 하는 영화 이름
url = f'https://dapi.kakao.com/v2/local/search/keyword.json?query={name}&page=4'
headers = {"Authorization": "KakaoAK 94624b34ab9e9fe38600293317e06fc3"}


response = requests.get(url, headers=headers) # 정보 받아오기

jsonObject = json.loads(response.text) # 정보는 str 타입인데 json.load 사용 시 dictionary 형태로 바꿔줌
# print(jsonObject)

save_file = open('./flowershops2.json','w')
# json.dump(jsonObject, save_file, ensure_ascii = False)
save_file.close()
min_print = len(jsonObject["documents"]) # if 영화 결과 값이 10개 이하일 경우 출력 개수를 영화 결과 값에 맞춰줌
data = {}
data['documents'] = []

for i in range(0, min_print):
    if(response.status_code == 200): # 정보를 잘 전달 받았다면
        address_name = jsonObject["documents"][i]["address_name"]
        phone = jsonObject["documents"][i]["phone"]
        place_name = jsonObject["documents"][i]["place_name"]
        road_address_name = jsonObject["documents"][i]["road_address_name"]
        x = jsonObject["documents"][i]["x"]
        y = jsonObject["documents"][i]["y"]

        data['documents'].append({
            "shopName": place_name,
            "x" : x,
            "y":y})

        with open('./shop3.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent="\t", ensure_ascii = False)
    else: # 실패일 때
        print("Error Code:" + response.status_code)