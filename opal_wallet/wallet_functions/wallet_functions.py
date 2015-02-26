import os
import json
import subprocess
from datetime import datetime

from wallet_functions import opal_cache

# Change this to the Opal path
opal_path = "/Users/whit/opalCoin/src"

os.environ['PATH'] += opal_path

def get_balance():
    balance = subprocess.check_output(['opalcoind', 'getbalance'])
    return balance.decode()

def account_balance(account):
    balance = subprocess.check_output(['opalcoind', 'getbalance', account])
    return balance.decode()


def list_accounts():
    accounts = subprocess.check_output(['opalcoind', 'listaccounts']).decode()
    accounts = json.loads(accounts)
    account_names = []
    these_accounts = []
    for account in accounts.keys():
        if account == "":
            account_name = "Main account"
        else:
            account_name = account.replace("_", " ")
        account_names.append(account_name)
        these_accounts.append({'account':account_name, 'balance':accounts[account]})
    return (account_names, these_accounts)

def send_opal(transaction):
    if transaction['from_address'] == 'Main account': from_address = ""
    else:
        from_address = transaction['from_address'].replace(" ", "_")
    return subprocess.call(['opalcoind', 'sendfrom', from_address, transaction['to_address'], transaction['amount']])

def get_time(unix_timestamp):
    timestamp = datetime.fromtimestamp(unix_timestamp)
    timestamp = timestamp.strftime('%d-%m-%Y')
    return timestamp

def format_float(tx_amount):
    amount = format(float(tx_amount), '.8f')
    return amount
    
def list_transactions():
    txs = subprocess.check_output(['opalcoind', 'listtransactions'])
    txs = json.loads(txs.decode())
    for tx in txs:
        tx['time'] = get_time(tx['time'])
        tx['amount'] = format_float(tx['amount'])
    return txs

def list_unspent():
    amounts = subprocess.check_output(['opalcoind', 'listunspent'])
    amounts = json.loads(amounts.decode())
    unspent = []
    for amt in amounts:
        address = amt['address']
        account = subprocess.check_output(['opalcoind', 'getaccount', address])
        balance = None
        if account == b'':
            account = "Main account"
            balance = account_balance("")
        else:
            balance = account_balance(account)
            account = account.replace("_", " ")
        unspent.append({'account':account, 'address': address,
                        'confirmations':amt['confirmations'], 'balance':balance})
    return unspent

def update_stats(user):
    balance = get_balance()
    opal_cache.set_stats(user, {'balance': balance})
    
# context = {'test':test}
# return render(request, 'wallet/test.html', context)

