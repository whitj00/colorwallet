import subprocess
import settings

def get_balance():
    balance = subprocess.check_output(['opalcoind', 'getbalance'])
    return balance.decode()

