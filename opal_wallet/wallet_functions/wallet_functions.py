import subprocess
import os
import json

# Change this to the Opal path

opal_path = ":/Users/tom/tmp/tmp/OpalCoin/src"

os.environ['PATH'] += opal_path

def get_balance():
    balance = subprocess.check_output(['opalcoind', 'getbalance'])
    return balance.decode()

def list_accounts():
    accounts = subprocess.check_output(['opalcoind', 'listaccounts']).decode()
    accounts = list(json.loads(accounts).keys())
    account_names = []
    for account in accounts:
        if account == "":
            account_name = "Main account"
        else:
            account_name = account.replace("_", " ")
        account_names.append(account_name)
    return account_names

def send_opal(transaction):
    if transaction['from_address'] == 'Main account': from_address = ""
    else:
        transaction = transation.replace(" ", "_")
    return subprocess.call(['opalcoind', 'sendfrom', from_address, transaction['to_address'], transaction['amount']])

def list_transactions():
    tx = subprocess.check_output(['opalcoind', 'listtransactions'])
    return json.loads(tx.decode())
    
