# https://newsapi.org/
import requests
import html
import datetime
import os
from twilio.rest import Client

news_url = 'https://newsapi.org/v2/everything'
stock_url = 'https://www.alphavantage.co/query'


def get_news(stock_name, company_name , top = 3, percent_diff = 0.05):
       stock_params = {
              "function" : "TIME_SERIES_DAILY_ADJUSTED" , 
              "symbol" : stock_name,
              "apikey" : os.environ['API_KEY_alpha'],
       }
       response = requests.get(stock_url,params=stock_params)
       yesterday = datetime.date.today() - datetime.timedelta(days=1)

       data = response.json()['Time Series (Daily)']

       data_list = [value for (key,value) in data.items()]

       yesterday_closing_price = data_list[0]['4. close']

       # print(yesterday_closing_price)

       day_before_yesterday_stock_closing_price = data_list[1]['4. close']

       # print(day_before_yesterday_stock_closing_price)

       difference = abs(float(day_before_yesterday_stock_closing_price)-float(yesterday_closing_price))

       up_down = "+"
       if(float(day_before_yesterday_stock_closing_price) > float(yesterday_closing_price)):
              up_down="-"
       percentage_difference = (difference/float(yesterday_closing_price)) * 100

       # print(percentage_difference)

       if(percentage_difference >= percent_diff):
              # print("GET NEWS !!")
              news_param = {
                     "apiKey" : os.environ['API_KEY'],
                     "qInTitle" : company_name,
              }
              data_re = requests.get(news_url,params=news_param)
              top_Articles = data_re.json()['articles'][:top]
              formatted_articles = [f"{stock_name}{up_down}{percentage_difference}\% Header:{articles['title']}. \nBrief:{articles['content']}" for articles in top_Articles]
              

              # Find your Account SID and Auth Token in Account Info and set the environment variables.
              # See http://twil.io/secure
              account_sid = os.environ['TWILIO_ACCOUNT_SID']
              # account_sid = TWILIO_ACCOUNT_SID
              auth_token = os.environ['TWILIO_AUTH_TOKEN']
              # auth_token = TWILIO_AUTH_TOKEN
              client = Client(account_sid, auth_token)

              for i in formatted_articles:
                     message = client.messages.create(
                     body=i,
                     from_= os.environ['Twilio_Number'],
                     to=os.environ['personal_number']
                     )

                     print(message.sid)
       else:
              print("Not sufficient percentage!!")


get_news("TSLA","Tesla Inc" , 1 , 0.01)