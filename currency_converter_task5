from forex_python.converter import CurrencyRates,CurrencyCodes
list=['EUR','IDR','BGN','ILS','GBP','DKK','CAD','JPY','HUF','RON','MYR','SEK','SGD','HKD','AUD','CHF','KRW','CNY','TRY','HRK','NZD','THB','USD','NOK','RUB','INR','MXN','CZK','BRL','PLN','PHP','ZAR']
print("CURRENCY CONVERTER")
print("\nCURRENCY CODES\n")
try:
    o=CurrencyCodes()
    for i in range(len(list)):
        print((i+1),". ",list[i],":",o.get_currency_name(list[i]),"(",o.get_symbol(list[i]),")")
except:
    print("\nNOT CONNECTED")
while(True):
    while(True):
        i=input("\nenter currency code for starting currency: ")
        j=input("\nenter currency code for ending currency: ")
        if(i in list and j in list):
            break
        print("\nINVALID CURRENCY")
    k=float(input("\nenter amount: "))
    print("\nCONVERSION RESULT\n")
    try:
        o=CurrencyCodes()
        O=CurrencyRates()
        print(k,o.get_symbol(i),"(",o.get_currency_name(i),")","=",O.convert(i,j,k),o.get_symbol(j),"(",o.get_currency_name(j),")")
    except:
        print("\nNOT CONNECTED")
    print("-"*50)
