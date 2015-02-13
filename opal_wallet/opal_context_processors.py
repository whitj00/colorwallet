from wallet_functions import wallet_functions, opal_cache

def opal_balance(request):
    # balance = wallet_functions.get_balance()
    balance = opal_cache.get_stats(request.user)[0]
    return {'balance':balance}

