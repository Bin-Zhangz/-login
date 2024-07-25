import requests
def loginid():
    cookies = {
        'select_city': '110000',
        'lianjia_uuid': '06242536-3879-4fb9-ac05-7f384d3ddd92',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22190dfc9aa0c6aa-04a8fcffc212b5-26001f51-947870-190dfc9aa0d1058%22%2C%22%24device_id%22%3A%22190dfc9aa0c6aa-04a8fcffc212b5-26001f51-947870-190dfc9aa0d1058%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
        'lianjia_ssid': 'fc28697d-9881-4025-ab4a-7fcce175e60e',
        'ak_bmsc': 'ACC1C7FC7D4B4CD5680FB12D5D29552D~000000000000000000000000000000~YAAQh+8ZuCcvU92QAQAAuRxg4hg3JxK9kolyFFz3fWfg61zq2LN3I9LIkeQvWwwF4BWBiRyP6SnSmQ4N06idn873uII3J19yChOtzORVtIL2EqGiAcx7JJp8auJCZ4bi7btdz6WHWKJrEGiqhNugEXCoRFM3wvC8hlbz4YKlL5jD4nMXQL3NNvP+iOJRfHnUgpSsEudGZg7GUO74Nt/IBke2vBmALU8lnKwaPVbTLP224Awb/KsDJfQUbaYt9G9qfTaBbHIMg4iet95fuYssBpulcMHhZ+0KRDh+mK41PUwjiS/C4M30xshaFEbkYBpsJlNUxPVG93QVpEeDaOxmmZ9/Hji0q/pSbaRrGWXxPMIUF1W7e2oXu6eQPf4tuZooZ1ewhGJ8HlLNE2BIenCQYEkGwWnwQ9k1pfl0ANme3Zz5hkl2vC1GZu3yjOn/Z7EHCdU=',
        'digv_extends': '%7B%22utmTrackId%22%3A%22%22%7D',
        'crosSdkDT2019DeviceId': '-a0w2nz-8hfeq2-qwhqmcpganz3u6r-mggfwhox1',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'select_city=110000; lianjia_uuid=06242536-3879-4fb9-ac05-7f384d3ddd92; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22190dfc9aa0c6aa-04a8fcffc212b5-26001f51-947870-190dfc9aa0d1058%22%2C%22%24device_id%22%3A%22190dfc9aa0c6aa-04a8fcffc212b5-26001f51-947870-190dfc9aa0d1058%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; lianjia_ssid=fc28697d-9881-4025-ab4a-7fcce175e60e; ak_bmsc=ACC1C7FC7D4B4CD5680FB12D5D29552D~000000000000000000000000000000~YAAQh+8ZuCcvU92QAQAAuRxg4hg3JxK9kolyFFz3fWfg61zq2LN3I9LIkeQvWwwF4BWBiRyP6SnSmQ4N06idn873uII3J19yChOtzORVtIL2EqGiAcx7JJp8auJCZ4bi7btdz6WHWKJrEGiqhNugEXCoRFM3wvC8hlbz4YKlL5jD4nMXQL3NNvP+iOJRfHnUgpSsEudGZg7GUO74Nt/IBke2vBmALU8lnKwaPVbTLP224Awb/KsDJfQUbaYt9G9qfTaBbHIMg4iet95fuYssBpulcMHhZ+0KRDh+mK41PUwjiS/C4M30xshaFEbkYBpsJlNUxPVG93QVpEeDaOxmmZ9/Hji0q/pSbaRrGWXxPMIUF1W7e2oXu6eQPf4tuZooZ1ewhGJ8HlLNE2BIenCQYEkGwWnwQ9k1pfl0ANme3Zz5hkl2vC1GZu3yjOn/Z7EHCdU=; digv_extends=%7B%22utmTrackId%22%3A%22%22%7D; crosSdkDT2019DeviceId=-a0w2nz-8hfeq2-qwhqmcpganz3u6r-mggfwhox1',
        'Origin': 'https://bj.ke.com',
        'Pragma': 'no-cache',
        'Referer': 'https://bj.ke.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'service': 'https://ajax.api.ke.com/login/login/getuserinfo',
        'version': '2.0',
    }

    response = requests.post('https://clogin.ke.com/authentication/initialize', cookies=cookies, headers=headers, json=json_data)

    return response.json()['loginTicketId']
    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"service":"https://ajax.api.ke.com/login/login/getuserinfo","version":"2.0"}'
    #response = requests.post('https://clogin.ke.com/authentication/initialize', cookies=cookies, headers=headers, data=data)