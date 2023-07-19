import requests
import json

def make_request(img_type, prompt=None, img_id=None, num=None):
    url = "http://midjourney-api.ai-des.com/func2api/Imagine"

    # UUID应当被设置为实际的值
    uuid = "afd22831-6e9e-c4e4-2477-825a3328a178"

    headers = {
        "Content-Type": "application/json",
        "UUID": uuid
    }

    data = {
        "type": img_type
    }

    if img_type == "P":
        data["prompt"] = prompt
    elif img_type == "U":
        data["imgId"] = img_id
        data["num"] = num 

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("请求成功, 返回数据为:")
        return response.json()
    else:
        print(f"请求失败, 错误码为: {response.status_code}")
        return response.status_code

# Example usage:
# Generate image from prompt
make_request("P", prompt="一个企鹅，骑着摩托")
