from tabulate import tabulate
import asyncio
import sys
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(funcName)5s - %(message)s")

# current = input("Enter current: ")
result = {'date': '19.02.2024', 'bank': 'PB', 'baseCurrency': 980, 'baseCurrencyLit': 'UAH', 'exchangeRate': [{'baseCurrency': 'UAH', 'currency': 'AUD', 'saleRateNB': 24.7615, 'purchaseRateNB': 24.7615}, {'baseCurrency': 'UAH', 'currency': 'AZN', 'saleRateNB': 22.3496, 'purchaseRateNB': 22.3496}, {'baseCurrency': 'UAH', 'currency': 'BYN', 'saleRateNB': 13.8019, 'purchaseRateNB': 13.8019}, {'baseCurrency': 'UAH', 'currency': 'CAD', 'saleRateNB': 28.1659, 'purchaseRateNB': 28.1659}, {'baseCurrency': 'UAH', 'currency': 'CHF', 'saleRateNB': 43.0911, 'purchaseRateNB': 43.0911, 'saleRate': 43.73, 'purchaseRate': 43.03}, {'baseCurrency': 'UAH', 'currency': 'CNY', 'saleRateNB': 5.2786, 'purchaseRateNB': 5.2786}, {'baseCurrency': 'UAH', 'currency': 'CZK', 'saleRateNB': 1.6063, 'purchaseRateNB': 1.6063, 'saleRate': 1.63, 'purchaseRate': 1.6}, {'baseCurrency': 'UAH', 'currency': 'DKK', 'saleRateNB': 5.4853, 'purchaseRateNB': 5.4853}, {'baseCurrency': 'UAH', 'currency': 'EUR', 'saleRateNB': 40.8919, 'purchaseRateNB': 40.8919, 'saleRate': 41.65, 'purchaseRate': 40.65}, {'baseCurrency': 'UAH', 'currency': 'GBP', 'saleRateNB': 47.7838, 'purchaseRateNB': 47.7838, 'saleRate': 48.58, 'purchaseRate': 47.8}, {'baseCurrency': 'UAH', 'currency': 'GEL', 'saleRateNB': 14.0238, 
'purchaseRateNB': 14.0238}, {'baseCurrency': 'UAH', 'currency': 'HUF', 'saleRateNB': 0.105019, 'purchaseRateNB': 0.105019}, {'baseCurrency': 'UAH', 'currency': 'ILS', 'saleRateNB': 10.5264, 'purchaseRateNB': 10.5264}, {'baseCurrency': 'UAH', 'currency': 'JPY', 'saleRateNB': 0.25266, 'purchaseRateNB': 0.25266}, {'baseCurrency': 'UAH', 'currency': 'KZT', 'saleRateNB': 0.084435, 'purchaseRateNB': 0.084435}, {'baseCurrency': 'UAH', 'currency': 'MDL', 'saleRateNB': 2.1234, 'purchaseRateNB': 2.1234}, {'baseCurrency': 'UAH', 'currency': 'NOK', 'saleRateNB': 3.6016, 'purchaseRateNB': 3.6016}, {'baseCurrency': 'UAH', 'currency': 'PLN', 'saleRateNB': 9.4223, 'purchaseRateNB': 9.4223, 'saleRate': 9.78, 'purchaseRate': 9.38}, {'baseCurrency': 'UAH', 'currency': 'SEK', 'saleRateNB': 3.6286, 'purchaseRateNB': 3.6286}, {'baseCurrency': 'UAH', 'currency': 'SGD', 'saleRateNB': 28.2025, 'purchaseRateNB': 28.2025}, {'baseCurrency': 'UAH', 'currency': 'TMT', 'saleRateNB': 10.7322, 'purchaseRateNB': 10.7322}, {'baseCurrency': 'UAH', 'currency': 'TRY', 'saleRateNB': 1.2318, 'purchaseRateNB': 1.2318}, {'baseCurrency': 'UAH', 'currency': 'UAH', 'saleRateNB': 1.0, 'purchaseRateNB': 1.0}, {'baseCurrency': 'UAH', 'currency': 'USD', 'saleRateNB': 37.9719, 'purchaseRateNB': 37.9719, 'saleRate': 38.5, 'purchaseRate': 37.9}, {'baseCurrency': 'UAH', 'currency': 'UZS', 'saleRateNB': 0.0030243, 'purchaseRateNB': 0.0030243}, {'baseCurrency': 'UAH', 'currency': 'XAU', 'saleRateNB': 76207.32, 'purchaseRateNB': 76207.32}]}
# for key, valume in result.items():
    
#     # print(f"Key = {key}")
#     # print(f"Valume = {valume}")
#     if isinstance(valume, list):
#         # print(tabulate(valume))
#         for val in valume:
# #             # print(val)
#             if isinstance(val, dict):
#                 for valum in val.values():
#                     # print(valum)
#                     if current==valum:
#                         valu = val # dict
#                         for kk, vv in valu.items():
#                             valu[kk]=str(vv).split()
                          
# # print(tabulate(valu))
#                             # print(tabulate(valu))
# head = ["baseCurrency", "currency", "sale", "purchase"]
# data = tabulate(valu, headers=head, tablefmt="grid")
# print(data)
# fdf = {'baseCurrency': 'UAH', 'currency': 'USD', 'saleRateNB': 0.0030243, 'purchaseRateNB': 0.0030243}
# # print(tabulate(fdf))
# for key, val in fdf.items():
    
#     fdf[key]=str(val).split()
#         # print(val)
# print(tabulate(fdf, headers="keys"))
# f = {"one": ["1"], "2": "two", "3": ["three"], "4": "2", "5": "five"}
# print(tabulate(f, headers="keys"))
# for currens in asyncio.run(main(sys.argv[1])):
async def main():
    logging.debug(f"result: ")
    for valume in result.values():
        if isinstance(valume, list):
            for val in valume:
                if isinstance(val, dict):
                    for valum in val.values():
                        if currensy==valum:
                            valu = val # dict
                            for kk, vv in valu.items():
                                valu[kk]= str(vv).split()
            # print("---------------------")
            # print(valu)
            # print("+++++++++++++++++++++++++++++++")
                        

                            
                            head = ["baseCurrency", "currency", "sale", "purchase"]
                            data = tabulate(valu, headers=head, tablefmt="grid")
                            
                            return data
        # if currens == currensy:
        #     return currens
        # else:
        #     return asyncio.run(main(sys.argv[1]))
    

if __name__ =="__main__":
    currensy = input("Enter currensy: ")
    r = asyncio.run(main())
    print(r)