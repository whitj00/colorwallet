# Sat Feb  7 13:44:07 CST 2015 - Sat Feb  7 14:45:54 CST 2015 (1 hour)

The plan is to use the Bitcoin color coin web wallet, colorcore.py, and bitcoind to find out what exactly happens with colored coins, i.e. what the metadata should look like, etc. Before getting into that, though, I want to make some progress getting the actual wallet app set up. So first task is to create the registration / login / logout / session / authentication app.

- Working on user registration and related views / models / templates.

DONE:

Created registration app in Django project. Created view and template for user registration, added static files from mockup to registration app, used Django Form from django.contrib.auth.forms for form input validation, sanitation, and error messages. The registration view serves a registration form to GET requests, and on validated POST requests adds a new user to the database using the User model from django.contrib.auth.models.

Passwords are stored as secure hashes, existing usernames cannot be overwritten by new registrations, all user model data is accessible in the Django Admin app, etc.

Created login template for use with the django.contrib.auth.views login view. Made login view work, e.g. registered URL, added necessary parameters, etc.

# Sat Feb  7 20:27:33 CST 2015 - Sat Feb  7 23:12:27 CST 2015 (2.5 hours)

Continuing with the registration app, making the User object and session accessible from wallet app.

---

Creating an interface between the web app and the opalcoind / colorcore backend.

Realizing more and more that the mockup interface is just thrown together with zero spec. I'm just going to copy Coinprism for as much as I need.

Coinprism main nav: Home, Send coins, Addresses & Colors, Transactions, Settings.

I'll do all of the normal Opalcoin functionality first, and then the colored coins functionality.

Coinprism wallet is divided into wallet addresses and coin issuance addresses. It is also divided into labels with "Receive Bitcoins" and "Receive assets" addresses. I don't understand exactly why BTC and assets are sent to different addresses, but it kind of makes sense and I'll figure out the concrete reason for it when I examine some colored bitcoins.

SPEC:

Coinprism homepage shows a wallet balance and an address to receive BTC/assets.

DONE:

Completed registration app. Added logout view, logout button to base template. User session is available in wallet app. Made wallet app require login and redirect to login page is user is not currenty logged in.

Began work on connecting to opalcoind from Django app. Tried to find a JSON-RPC library that is compatible with Python 3 (necessary for running colorcore.py), but I'm going to pick up next time with just using `subprocess` from the standard library.

What I'll do is not put any RPC/subprocess stuff directly in the app, I'll just connect to my own API for all of my wallet operations, so later on the implementation can be changed to use JSON-RPC.

# Sun Feb  8 14:31:43 CST 2015 - Sun Feb  8 16:43:09 CST 2015 (2 hours)

DONE:

Created a context processor to get an updated balance from opalcoind on every request and add balance variable to every template in the project.

Get list of Opal accounts (using "" as "Main account") and insert into template as list of options for "From" in the send Opal form. Users can now create send transactions for Opal through the web wallet.

Working on methods for seperating Opalcoin environments for different users, creating fresh wallets encrypted during registration, etc.

# Sun Feb  8 21:10:13 CST 2015 - Sun Feb  8 21:46:45 CST 2015 - Sun Feb  8 22:29:14 CST 2015 - Sun Feb  8 23:27:34 CST 2015 (1.5 hours)

Finishing up sending Opal from wallet app.

DONE:

Created a custom Django Form for POST data validation and sanitation for sending Opal. Created backend to send Opal using opalcoind and form submitted data. Form errors and Opal errors create alerts on 'send' template. Successful 'send' transactions redirect to the transaction overview page.

Creating custom form fields for Opal addresses would be a good idea.

# Wed Feb 11 05:43:47 CST 2015 - Wed Feb 11 07:15:14 CST 2015 (1.5 hours)

DONE:

Created function to get transcations from opalcoind and return to the 'transactions' view of the wallet app. Converted raw transaction data to show readable timestamp and 8 decimal float values for transaction amounts. Added transaction data to the 'transactions' template.

List accounts and balances on 'Accounts' page using `listaccounts` command, 90% done getting full account history using `listunspent`

# Wed Feb 11 15:58:58 CST 2015 - Wed Feb 11 17:04:27 CST 2015 

List uses `listunspent` and gets the account for each address.

Each page load is pretty slow because it has to run all of the opalcoind subprocesses, so I'm going to make a 'load wallet' that will run all of the opalcoind calls at one time and keep the data in memory, then I'll add a context processor, so all of the other views can load very quickly.

Using Redis to store wallet data (unspent outputs, transactions, etc).

Making a quick installation video.