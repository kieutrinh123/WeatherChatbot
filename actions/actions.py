
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


import json
import feedparser
import requests
from bs4 import BeautifulSoup

class WeatherLocation0(Action):

     def name(self) -> Text:
         return "action_weather_location0"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

             location0_entity = next(tracker.get_latest_entity_values('location0'),None)

             if location0_entity:
                # khai báo địa chỉ url lưu trữ thông tin
                url = requests.get('https://nchmf.gov.vn/Kttvsite/vi-VN/1/thoi-tiet-dat-lien-24h-12h2-15.html')
                #
                xuly = BeautifulSoup(url.text, 'html.parser')
                datas = xuly.find_all('div', {'class': 'text-weather-location fix-weather-location'})
                title = []
                for data in datas:
                    title.append(data.text.strip())

                dispatcher.utter_message(title[0])
             else:
                 dispatcher.utter_message(text='Không có dữ liệu')

             return []


class WeatherLocation1(Action):

    def name(self) -> Text:
        return "action_weather_location1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location1_entity = next(tracker.get_latest_entity_values('location1'), None)
        if location1_entity:
            # khai báo địa chỉ url lưu trữ thông tin
            url = requests.get('https://nchmf.gov.vn/Kttvsite/vi-VN/1/thoi-tiet-dat-lien-24h-12h2-15.html')
            #
            xuly = BeautifulSoup(url.text, 'html.parser')
            datas = xuly.find_all('div', {'class': 'text-weather-location fix-weather-location'})
            title = []
            for data in datas:
                title.append(data.text.strip())

            dispatcher.utter_message(title[1])
        else:
            dispatcher.utter_message(text='Không có dữ liệu')

        return []


class WeatherLocation2(Action):

    def name(self) -> Text:
        return "action_weather_location2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location2_entity = next(tracker.get_latest_entity_values('location2'), None)
        if location2_entity:
            # khai báo địa chỉ url lưu trữ thông tin
            url = requests.get('https://nchmf.gov.vn/Kttvsite/vi-VN/1/thoi-tiet-dat-lien-24h-12h2-15.html')
            #
            xuly = BeautifulSoup(url.text, 'html.parser')
            datas = xuly.find_all('div', {'class': 'text-weather-location fix-weather-location'})
            title = []
            for data in datas:
                title.append(data.text.strip())

            dispatcher.utter_message(title[2])
        else:
            dispatcher.utter_message(text='Không có dữ liệu')

        return []


class WeatherLocation3(Action):

    def name(self) -> Text:
        return "action_weather_location3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location3_entity = next(tracker.get_latest_entity_values('location3'), None)
        if location3_entity:
            # khai báo địa chỉ url lưu trữ thông tin
            url = requests.get('https://nchmf.gov.vn/Kttvsite/vi-VN/1/thoi-tiet-dat-lien-24h-12h2-15.html')
            #
            xuly = BeautifulSoup(url.text, 'html.parser')
            datas = xuly.find_all('div', {'class': 'text-weather-location fix-weather-location'})
            title = []
            for data in datas:
                title.append(data.text.strip())

            dispatcher.utter_message(title[3])
        else:
            dispatcher.utter_message(text='Không có dữ liệu')
        return []


class WeatherLocation4(Action):

    def name(self) -> Text:
        return "action_weather_location4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location4_entity = next(tracker.get_latest_entity_values('location4'), None)
        if location4_entity:
            # khai báo địa chỉ url lưu trữ thông tin
            url = requests.get('https://nchmf.gov.vn/Kttvsite/vi-VN/1/thoi-tiet-dat-lien-24h-12h2-15.html')
            #
            xuly = BeautifulSoup(url.text, 'html.parser')
            datas = xuly.find_all('div', {'class': 'text-weather-location fix-weather-location'})
            title = []
            for data in datas:
                title.append(data.text.strip())

            dispatcher.utter_message(title[4])
        else:
            dispatcher.utter_message(text='Không có dữ liệu')

        return []


class WeatherLocation5(Action):

    def name(self) -> Text:
        return "action_weather_location5"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location5_entity = next(tracker.get_latest_entity_values('location5'), None)
        if location5_entity:
            # khai báo địa chỉ url lưu trữ thông tin
            url = requests.get('https://nchmf.gov.vn/Kttvsite/vi-VN/1/thoi-tiet-dat-lien-24h-12h2-15.html')
            #
            xuly = BeautifulSoup(url.text, 'html.parser')
            datas = xuly.find_all('div', {'class': 'text-weather-location fix-weather-location'})
            title = []
            for data in datas:
                title.append(data.text.strip())

            dispatcher.utter_message(title[5])
        else:
            dispatcher.utter_message(text='Không có dữ liệu')
        return []


class WeatherLocation6(Action):

    def name(self) -> Text:
        return "action_weather_location6"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location6_entity = next(tracker.get_latest_entity_values('location6'), None)
        if location6_entity:
            # khai báo địa chỉ url lưu trữ thông tin
            url = requests.get('https://nchmf.gov.vn/Kttvsite/vi-VN/1/thoi-tiet-dat-lien-24h-12h2-15.html')
            #
            xuly = BeautifulSoup(url.text, 'html.parser')
            datas = xuly.find_all('div', {'class': 'text-weather-location fix-weather-location'})
            title = []
            for data in datas:
                title.append(data.text.strip())

            dispatcher.utter_message(title[6])
        else:
            dispatcher.utter_message(text='Không có dữ liệu')

        return []


