from exchange import get_exchange
from make_query import get_top_7, search_crypto, get_curr_list  


print("###  Welcome to crypto dashboard. Here, you'll get info about your favourite crypto currency.  ###\n")

search = True


currency = input("Enter your preferred currency_exchange 'btc by default ' : ").strip().lower()
print()

if not currency:
    currency = 'btc'
print(f"chosen currency: {currency}")

while search:
    while True:
        try:
            choice = int(input("Press 1 to get list of trending coins\nPress 2 to search a particular coin\nPress 3 to get currency list\nPress 4 to exchange rates\n ").strip())
            
            if choice not in [1, 2, 3, 4]:
                raise ValueError

            else:
                break

        except ValueError:
            print("Enter integer between 1, 2, 3 or 4")
            
    if choice ==  1:
        get_top_7()
    elif choice == 2:
        search_crypto()
    elif choice == 3:
        get_curr_list()
    elif choice == 4:
        get_exchange()
        

    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    
    choice = input("Would you like to search more. Press (Y/N): ").strip().lower()
    search = (choice == "y" or choice =="yes")


print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
print("-.-.-.-.-.-.-.|\----/|.-|.-.-.-.-|.-.-.-|.-.-.-.-.-.-.-.-.-.-")
print("-.-.-.-.-.-.-.|-\--/-|.-|.-.-.-.-|.-.-.-|.-.-.-.-.-.-.-.-.-.-")
print("-.-.-.-.-.-.-.|--\/--|.-|.-.-.-.-|------|.-.-.-.-.-.-.-.-.-.-")
print("-.-.-.-.-.-.-.|-.--.-|.-|.-.-.-.-|.-.-.-|.-.-.-.-.-.-.-.-.-.-")
print("-.-.-.-.-.-.-.|-.--.-|.-|______.-|.-.-.-|.-.-.-.-.-.-.-.-.-.-")
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
print('\n###........Thanks for using crypto dashboard..........###\n')