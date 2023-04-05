USD_TO_KSH= 112.50

EUR_TO_KSH = 132.45

EUR_TO_USD = 1.20

KSH_TO_USD= 0.00888

KSH_TO_EUR= 0.00755

USD_TO_EUR= 0.8333

def usd_to_ksh(usd):
    return usd * USD_TO_KSH

def eur_to_ksh(eur):
    return eur * EUR_TO_KSH

def eur_to_usd(eur):
    return eur * EUR_TO_USD

def ksh_to_usd(ksh):
    return ksh * KSH_TO_USD

def ksh_to_eur(ksh):
    return ksh * KSH_TO_EUR

def usd_to_eur(usd):
    return usd * USD_TO_EUR

def main():
    from_currency = input("Enter currency to convert from (USD, EUR, KSH): ")
    to_currency = input("Enter currency to convert to (USD, EUR, KSH): ")
    amount = float(input( "Enter amount): "))

    if from_currency == "USD":
       usd = amount

    elif from_currency == "EUR":
       usd = eur_to_usd(amount)

    elif from_currency == "KSH":
       usd = ksh_to_usd(amount)

    else :
       print("Invalid input currency")
       return

    if to_currency == "USD":
       result = usd

    elif to_currency == "EUR":
       result = usd_to_eur(usd)

    elif to_currency == "KSH":
       result = usd_to_ksh(usd)

    else:
       print("Invalid output currency")
       return

    print(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")

if __name__== "__main__":
    main()