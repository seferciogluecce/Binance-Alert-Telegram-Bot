# Binance-Alert-Telegram-Bot

By running BiTeBot.py you can set your commands to get information on coins you want to follow from binance through Telegram.



Commands through Telegram chat:

To add a coin: <br />
`A/a COINPAIR targetPrice trend` <br />
A/a: for add command <br />
COINPAIR: as YOYOBNB or NEOBTC <br />
targetPrice: price that you want to examine in pair's value <br />
trend: H/h or L/l to be alerted if current price is higher or lower than your target price. <br /><br />

Example : 
<br />
`A BTCUSDT 1000 H` 
<br /> OR <br />
`a BTCUSDT 1000 H`
<br /> OR <br />
`a BTCUSDT 1000 h`
<br /> OR <br />
`A BTCUSDT 1000 h` 
<br />

will add **BTCUSDT** pair to your orderlist and send you a notification if price is higher than 1000 USDT per BTC
<br />
<br />

Similarly
<br />
`A BTCUSDT 1000 L`
<br /> OR <br />
`a BTCUSDT 1000 L`
<br /> OR <br />
`a BTCUSDT 1000 l`
<br /> OR <br />
`A BTCUSDT 1000 l`
<br />

will add **BTCUSDT** pair to your orderlist and send you a notification if price is lower than 1000 USDT per BTC
<br /><br />

To delete a coin: <br />
`D/d COINPAIR` <br />
D/d: for delete command <br />
COINPAIR: as YOYOBNB or NEOBTC <br />
<br /><br />
Examples :
<br />
`D BTCUSDT`
<br /> OR <br />
`d BTCUSDT`
<br />
will delete coinpair **BTCUSDT** from your orderlist

To see your orderlist: <br />
`O` <br />
O: as orders <br /> 

you also need to strings with your Bot token, Binance API key and API secret key in the script
