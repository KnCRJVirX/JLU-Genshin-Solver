import requests
import time
import random
import json

from urllib.parse import quote

url = "https://virtualcourse.zhihuishu.com/report/saveReport"

# 随便提交一次，saveReport请求的body（“负载”选项卡）里的jsonStr字段内容中键名为uuid，&9734结尾的字符串
uuid = input("UUID: ")
# virtualcourse.zhihuishu.com的Cookies中的acw_tc字段
acw_tc = input("acw_tc: ")

# 构造原始数据
json_payload = None

with open('body.json', 'r', encoding='utf-8') as f:
    json_payload = json.load(f)

if json_payload is None:
    print("无法读取body.json文件内容，请检查文件是否存在且格式正确！")
    exit(1)

json_payload['uuid'] = uuid
json_payload['endTime'] = int(time.time()) * 1000 + random.randint(100, 900)
json_payload['timeUsed'] = random.randint(2800, 3100)
json_payload['startTime'] = json_payload['endTime'] - json_payload['timeUsed'] * 1000

# URL编码
quoted_payload = quote(str(json_payload))

# 构造请求
payload = f'jsonStr={quoted_payload}&ticket='
headers = {
  'sec-ch-ua-platform': '"Windows"',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
  'sec-ch-ua': '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
  'Content-Type': 'application/x-www-form-urlencoded',
  'sec-ch-ua-mobile': '?0',
  'Accept': '*/*',
  'Sec-Fetch-Site': 'same-site',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'host': 'virtualcourse.zhihuishu.com',
  'Cookie': f'acw_tc={acw_tc}'
}

response = requests.request("POST", url, headers=headers, data=payload)

json_response = response.json()
if (json_response.get("code") == 1) and (json_response.get("message") == "success"):
    print("提交成功！")
    print("原始返回：", response.text)
else:
    print("提交失败！")
    print("原始返回：", response.text)