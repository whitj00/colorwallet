https://en.bitcoin.it/wiki/Original_Bitcoin_client/API_calls_list

## Get wallet balance

./opalcoind getbalance

## Show all addresses (even brand new ones):

`./opalcoind listreceivedbyaddress 0 true`

## Get new address

`./opalcoind getnewaddress`

## When a password is necessary

I can still see the balance and transactions and stuff without a password, so getting the wallet balance in a template context processor is not a problem.

```
./opalcoind sendtoaddress oUBLRj8sJjtdBNaKc119xcEscCTdpRGntV 5.0
error: {"code":-13,"message":"Error: Please enter the wallet passphrase with walletpassphrase first."}
```
