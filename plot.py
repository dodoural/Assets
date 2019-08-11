from time import sleep
import matplotlib.pyplot as plt
import csv
from datetime import date

today = date.today()
formattedDate = today.strftime("%d/%m/%Y")
fileName = "holdings" + formattedDate + ".png"
fileName = fileName.replace("/","_",2)

plt.rcParams['text.color'] = 'black'
plt.rcParams['lines.linewidth'] = 4
# plt.rcParams['font.family'] = 'Helvetica'
# plt.rcParams['font.sans-serif'] = ['Helvetica']
holdings=[]

with open('holdings.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Holdings are {", ".join(row)}')
                line_count += 1
            else:
                holdings = row
                break
print(holdings)
def RealTimeCurrencyExchangeRate(from_currency, to_currency, api_key) :

        import requests, json

        base_url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

        main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key

        response = requests.get(main_url)
        json_data = json.loads(response.text)
        print(json_data)
        if not "Realtime Currency Exchange Rate" in json_data:
                return 0
        parity = float(json_data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
        print(from_currency," - ",to_currency,parity)
        return parity

if __name__ == "__main__" :

        api_key = "40THYJJIDLMM4Y8E"
        usd = 0
        btc = 0
        eur = 0
        au = 0

        while True :
                usd = RealTimeCurrencyExchangeRate("USD", "TRY", "api_key")
                if usd > 0 :
                        usd = usd * float(holdings[0])
                        break
                sleep(1)

        while True :
                btc = RealTimeCurrencyExchangeRate("BTC", "TRY", "api_key")
                if btc > 0 :
                        btc = btc * float(holdings[1])
                        break
                sleep(1)

        while True :
                eur = RealTimeCurrencyExchangeRate("EUR", "TRY", "api_key")
                if eur > 0 :
                        eur = eur * float(holdings[2])
                        break
                sleep(1)

        while True :
                au = RealTimeCurrencyExchangeRate("XAU", "TRY", "api_key")
                if au > 0 :
                        au = au * float(holdings[3]) / 31.103
                        break
                sleep(1)


        assets = [usd,btc,eur,au,float(holdings[4])]
        currencies = ['USD', 'BTC','EURO','AU','TRY']
        currenciesLegend = []
        colors = ['green','yellow','indigo','gold','red']
        explode = (0.05, 0.05, 0.05, 0.05, 0.05)
        total = "{0:.2f}".format(usd+btc+eur+au+float(holdings[4]))

        indice = 0
        for x in currencies :
                i = 0
                currenciesLegend.append(x + str(" {0:.2f}".format(assets[indice])) )
                indice += 1

        patches, texts, _ = plt.pie(assets,labels=currencies,
        colors=colors,
        startangle=90,
        autopct='%.1f%%',
        explode=explode,
        wedgeprops   = {
        'linewidth' : 3,
        'edgecolor' : "black" })
        plt.legend(patches, currenciesLegend, bbox_to_anchor=(0.9,1.0))
        plt.title('YATIRIMLAR',{'fontsize': "20",'fontweight' : "40"},bbox=dict(facecolor='black', alpha=4.5))
        plt.text(0.7,-1, "TOTAL = "+ total + " TRY",fontweight ="bold",bbox=dict(facecolor='black', alpha=1.5))
        plt.savefig(fileName)
        plt.show()

