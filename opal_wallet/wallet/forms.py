from django import forms

from wallet_functions import wallet_functions

class OpalSendForm(forms.Form):
    accounts = wallet_functions.list_accounts()
    account_choices = []
    for account in accounts:
        new_choice = (account, account)
        account_choices.append(new_choice)
    from_address = forms.ChoiceField(choices=account_choices,
                                     widget=forms.Select(attrs={'class':'form-control'}))
    to_address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'Opal Address',
                                                               'id':'toField'}))
    amount = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'Opal Amount',
                                                               'id':'amountField'}))
    fee = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control',
                                                                'placeholder':'Opal Amount',
                                                                'id':'feeField'}))
    initial = {'from_address':account_choices[0]}
