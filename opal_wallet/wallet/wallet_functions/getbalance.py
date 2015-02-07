import os
import subprocess

balance = subprocess.check_output(['opalcoind', 'getbalance'])

return balance.decode()
