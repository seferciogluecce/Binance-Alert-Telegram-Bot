
import json 
import time

import requests

TOKEN = "yourBotToken"  #write your Bot Token inside brackets
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    
    
    
    '''BELOW IS IMPORTANTE'''
    
maFollowCoin=[]  
    
def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
     
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    if text[0]=='A' and (text, chat_id) != last_textchat:
        textx=text.split(' ')
        maFollowCoin.append([textx[a].upper() for a in range(1,4)])
        send_message("New follow added for " + textx[1].upper(),chat_id)
    elif text[0]=='D' and (text, chat_id) != last_textchat:
        textx=text.split(' ')
        for c in maFollowCoin:
            if c[0]==textx[1].upper():
                maFollowCoin.remove(c)
                send_message("Follow deleted for " + textx[1].upper(),chat_id)
                break

    elif (text, chat_id) != last_textchat and text[0]=='O' :
        send_message("--- ORDERS START ---" , chat_id)     
        index =1
        for order in maFollowCoin:
            print("O")
            send_message(order[0]+" : "+order[2]+" than "+order[1] , chat_id)    
            index+=1
        send_message("--- ORDERS END ---" , chat_id)     

    elif (text, chat_id) != last_textchat:
        send_message("Excusez moi! Anata no request is not in mein dictionary." , chat_id)     

    return (text, chat_id)
from binance.client import Client

api_key='yourBinanceAPIkey'   #write your Binance API Key inside brackets
api_secret= 'yourBinanceAPIsecret' #write your Binance API secret inside brackets
client = Client(api_key, api_secret)


def sendUpdates(chat_id):
    prices = client.get_all_tickers() #current pricelar   
    for a in prices:
        for b in maFollowCoin:
            if a['symbol'] == b[0]:
                currPrice=float(a['price'])
                targetPrice=float(b[1])
                if b[2]=='L'and currPrice<targetPrice:
                    send_message("ALERT: \nPrice for " +a['symbol']+" is "+a['price']+" LOWER than target " + b[1] , chat_id)
                elif b[2]=='H'and currPrice>targetPrice:
                    send_message("ALERT: \nPrice for " +a['symbol']+" is "+a['price']+" HIGHER than target " + b[1] , chat_id)                
                else: 
                    send_message("Info: Price for " +a['symbol']+" is "+a['price'] , chat_id)                
                    

def main():
    global last_textchat 
    last_textchat = (None, None)

    messageFreq=15 #inSeconds
    dailyMessageCount=24*60*(60/messageFreq)
    
    print(  str(dailyMessageCount) +  " messages for a day."   )
    while True:
        print(maFollowCoin)
        text, chat = get_last_chat_id_and_text(get_updates())
        if (text, chat) != last_textchat:            
            last_textchat = (text, chat)
        sendUpdates(chat)
        time.sleep(messageFreq)


if __name__ == '__main__':
    main()
