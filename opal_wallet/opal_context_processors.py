from wallet_functions import wallet_functions

def opal_balance(request):
    balance = wallet_functions.get_balance()
    return {'balance':balance}
