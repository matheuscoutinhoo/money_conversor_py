
import requests
import json 
from time import sleep

prices = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,GBP-BRL")
prices = prices.json()
price_dolar = prices['USDBRL']["bid"]
price_euro = prices['EURBRL']["bid"]
price_pound = prices['GBPBRL']["bid"]
price_btc = prices['BTCBRL']["bid"]

opt = int(input("Hello. What do you want to do?\n[1] - Convert BRL into other currencies.\n[2] - Convert other currencies into BRL\n[3] - See prices\n"))

while True:
    if opt == 1:
        target = int(input("In which currency would you like to convert the BRL\n[1] - Dollar\n[2] - Euro\n[3] - Pound\n[4] - Bitcoin\n"))
        if target == 1:
            brl = float(input("Enter the amount to be converted: "))
            value = brl/float(price_dolar)
            print(f"R$ {brl:.2f} is equivalent to USD {value:.2f}")
            sleep(3)
            repeater = int(input("Do you want to continue?\n[1] - Yes\n[2] - No\n"))
            if repeater == 1:
                opt = int(input("Hello. What do you want to do?\n[1] - Convert BRL into other currencies.\n[2] - Convert other currencies into BRL\n[3] - See prices\n"))
            else:
                print("Thanks for using our services.")
                break
        elif target == 2:
            brl = float(input("Enter the amount to be converted: "))
            value = brl/float(price_euro)
            print(f"R$ {brl:.2f} is equivalent to EUR {value:.2f}")
            sleep(3)
            repeater = int(input("Do you want to continue?\n[1] - Yes\n[2] - No\n"))
            if repeater == 1:
                opt = int(input("Hello. What do you want to do?\n[1] - Convert BRL into other currencies.\n[2] - Convert other currencies into BRL\n[3] - See prices\n"))
            else:
                print("Thanks for using our services.")
                break
        elif target == 3:
            brl = float(input("Enter the amount to be converted: "))
            value = brl/float(price_pound)
            print(f"R$ {brl:.2f} is equivalent to GBP {value:.2f}")
            sleep(3)
            repeater = int(input("Do you want to continue?\n[1] - Yes\n[2] - No\n"))
            if repeater == 1:
                opt = int(input("Hello. What do you want to do?\n[1] - Convert BRL into other currencies.\n[2] - Convert other currencies into BRL\n[3] - See prices\n"))
            else:
                print("Thanks for using our services.")
                break
        elif target == 4:
            brl = float(input("Enter the amount to be converted: "))
            value = (brl/float(price_btc))/1000
            print(f"R$ {brl:.2f} is equivalent to BTC {value:0.5f}")
            sleep(3)
            repeater = int(input("Do you want to continue?\n[1] - Yes\n[2] - No\n"))
            if repeater == 1:
                opt = int(input("Hello. What do you want to do?\n[1] - Convert BRL into other currencies.\n[2] - Convert other currencies into BRL\n[3] - See prices\n"))
            else:
                print("Thanks for using our services.")
                break
    elif opt == 2:
        target = int(input("Wich currency would you like to convert to BRL\n[1] - Dollar\n[2] - Euro\n[3] - Pound\n[4] - Bitcoin\n"))
        if target == 1:
            dol = float(input("Enter the amount in dollar to be converted: "))
            value = dol*float(price_dolar)
            print(f"USD {dol:.2f} is equivalent to BRL {value:.2f}")
            sleep(3)
            repeater = int(input("Do you want to continue?\n[1] - Yes\n[2] - No\n"))
            if repeater == 1:
                opt = int(input("Hello. What do you want to do?\n[1] - Convert BRL into other currencies.\n[2] - Convert other currencies into BRL\n[3] - See prices\n"))
            else:
                print("Thanks for using our services.")
                break
        elif target == 2:
            euro = float(input("Enter the amount in euro to be converted: "))
            value = euro*float(price_euro)
            print(f"EUR {euro:.2f} is equivalent to BRL {value:.2f}")
            sleep(3)
            repeater = int(input("Do you want to continue?\n[1] - Yes\n[2] - No\n"))
            if repeater == 1:
                opt = int(input("Hello. What do you want to do?\n[1] - Convert BRL into other currencies.\n[2] - Convert other currencies into BRL\n[3] - See prices\n"))
            else:
                print("Thanks for using our services.")
                break
        elif target == 3:
            pound = float(input("Enter the amount in pounds to be converted: "))
            value = pound*float(price_pound)
            print(f"GBP {pound:.2f} is equivalent to BRL {value:.2f}")
            sleep(3)
            repeater = int(input("Do you want to continue?\n[1] - Yes\n[2] - No\n"))
            if repeater == 1:
                opt = int(input("Hello. What do you want to do?\n[1] - Convert BRL into other currencies.\n[2] - Convert other currencies into BRL\n[3] - See prices\n"))
            else:
                print("Thanks for using our services.")
                break
        elif target == 4:
            btc = float(input("Enter the amount in bitcoin to be converted: "))
            value = (float(price_btc)*btc)*1000
            print(f"BTC {btc:.5f} is equivalent to BRL {value:.2f}")
            sleep(3)
            repeater = int(input("Do you want to continue?\n[1] - Yes\n[2] - No\n"))
            if repeater == 1:
                opt = int(input("Hello. What do you want to do?\n[1] - Convert BRL into other currencies.\n[2] - Convert other currencies into BRL\n[3] - See prices\n"))
            else:
                print("Thanks for using our services.")
                break
        else:
            print("Invalid Option.")
            break
    elif opt == 3:
        target = int(input("Of wich currency would you like to see the price\n[1] - Dollar\n[2] - Euro\n[3] - Pound\n[4] - Bitcoin\n[5] - See all\n"))
        if target == 1:
            print(f"The price of the dollar right now is R$ {price_dolar}")
            sleep(3)
            repeater = int(input("Do you want to continue?\n[1] - Yes\n[2] - No\n"))
            if repeater == 1:
                opt = int(input("Hello. What do you want to do?\n[1] - Convert BRL into other currencies.\n[2] - Convert other currencies into BRL\n[3] - See prices\n"))
            else:
                print("Thanks for using our services.")
                break
        elif target == 2:
            print(f"The price of the euro right now is R$ {price_euro}")
            sleep(3)
            repeater = int(input("Do you want to continue?\n[1] - Yes\n[2] - No\n"))
            if repeater == 1:
                opt = int(input("Hello. What do you want to do?\n[1] - Convert BRL into other currencies.\n[2] - Convert other currencies into BRL\n[3] - See prices\n"))
            else:
                print("Thanks for using our services.")
                break
        elif target == 3:
            print(f"The price of the pound right now is R$ {price_pound}")
            sleep(3)
            repeater = int(input("Do you want to continue?\n[1] - Yes\n[2] - No\n"))
            if repeater == 1:
                opt = int(input("Hello. What do you want to do?\n[1] - Convert BRL into other currencies.\n[2] - Convert other currencies into BRL\n[3] - See prices\n"))
            else:
                print("Thanks for using our services.")
                break
        elif target == 4:
            print(f"The price of the bitcoin right now is R$ {float(price_btc)*1000}")
            sleep(3)
            repeater = int(input("Do you want to continue?\n[1] - Yes\n[2] - No\n"))
            if repeater == 1:
                opt = int(input("Hello. What do you want to do?\n[1] - Convert BRL into other currencies.\n[2] - Convert other currencies into BRL\n[3] - See prices\n"))
            else:
                print("Thanks for using our services.")
                break
        elif target == 5:
            print(f"The price of the dollar right now is R$ {price_dolar}")
            print(f"The price of the euro right now is {price_euro}")
            print(f"The price of the pound right now is R$ {price_pound}")
            print(f"The price of the bitcoin right now is {float(price_btc)*1000}")
            sleep(3)
            repeater = int(input("Do you want to continue?\n[1] - Yes\n[2] - No\n"))
            if repeater == 1:
                opt = int(input("Hello. What do you want to do?\n[1] - Convert BRL into other currencies.\n[2] - Convert other currencies into BRL\n[3] - See prices\n"))
            else:
                print("Thanks for using our services.")
                break
    else:
        print("Invalid Option.")
        break