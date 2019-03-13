from django import forms

class CurrencyForm(forms.Form):

    def __init__(self, currency_choices, *args, **kargs):
        super(CurrencyForm, self).__init__(*args, **kargs)
        self.fields['from_curr'].choices = currency_choices
        self.fields['to_curr'].choices = currency_choices

    amount = forms.FloatField(label='Amount', required=True, min_value=1)
    from_curr = forms.ChoiceField(label='Convert from', choices=(), required=True)
    to_curr = forms.ChoiceField(label='Convert to', choices=(), required=True)