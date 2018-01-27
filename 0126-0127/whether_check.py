# coding:utf-8
import requests
import json


def main():
    apikey = "059ac9eebb3943137ade039ec4686de1"
    sapporo_id = 2128295
    url = "http://api.openweathermap.org/data/2.5/weather"
    getparam = "?appid={}&id={}".format(apikey, sapporo_id)
    response = requests.get(url + getparam)

    # responseステータスの確認
    if not response.raise_for_status():
        weather_data = json.loads(response.text)
        print("札幌の天気は: %s" % weather_data["weather"][0]["main"])


if __name__ == "__main__":
    main()
