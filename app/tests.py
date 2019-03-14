from django.test import TestCase

from .forms import CurrencyForm
from .views import get_currencies, update_curr_list, create_choices


# Create your tests here.
class CurrencyFormTest(TestCase):
    #Setup ensures that we have a list of all the currency choices 
    def setUp(self):
        self.currency_choices =  create_choices(update_curr_list(get_currencies()))       

    #Test to verify whether the form accepts currency choices as an argument
    def test_init(self):
        CurrencyForm(self.currency_choices)

    def test_init_without_choices(self): 
        with self.assertRaises(TypeError):
            CurrencyForm()

    def test_blank_data(self):
        form = CurrencyForm(self.currency_choices, {})
        self.assertFalse(form.is_valid())
    
    def test_valid_data(self):
        form = CurrencyForm(self.currency_choices, {
            'amount': 100,
            'to_curr': "INR",
            'from_curr': "EUR",
        })
        self.assertTrue(form.is_valid())
        

    def test_special_char_in_amount(self):
        form = CurrencyForm(self.currency_choices, {
            'amount': "$$",
            'to_curr': "INR",
            'from_curr': "EUR",
        })
        self.assertFalse(form.is_valid())

    def test_alphabets_in_amount(self):
        form = CurrencyForm(self.currency_choices, {
            'amount': "asd",
            'to_curr': "INR",
            'from_curr': "EUR",
        })
        self.assertFalse(form.is_valid())

    def test_float_in_amount(self):
        form = CurrencyForm(self.currency_choices, {
            'amount': 100.2,
            'to_curr': "INR",
            'from_curr': "EUR",
        })
        self.assertTrue(form.is_valid())

    def test_zero_in_amount(self):
        form = CurrencyForm(self.currency_choices, {
            'amount': 0,
            'to': "INR",
            'from': "EUR",
        })
        self.assertFalse(form.is_valid())

    def test_negetive_in_amount(self):
        form = CurrencyForm(self.currency_choices, {
            'amount': "100",
            'to': "INR",
            'from': "EUR",
        })
        self.assertFalse(form.is_valid())

    def test_same_to_from_currency(self):
        form = CurrencyForm(self.currency_choices, {
            'amount': -19,
            'to_curr': "INR",
            'from_curr': "EUR",
        })
        self.assertFalse(form.is_valid())



class HelperFunctionsTest(TestCase):

    def setUp(self):
        self.curr_list = ['MXN', 'AUD', 'HKD', 'RON', 'HRK', 'CHF', 'IDR', 'CAD', 'USD', 'ZAR','JPY', 'BRL', 'HUF', 'CZK', 'NOK', 'INR', 'PLN', 'ISK', 'PHP', 'SEK', 'ILS', 'GBP','SGD', 'CNY', 'TRY', 'MYR', 'RUB', 'NZD', 'KRW', 'THB', 'BGN', 'DKK']
        self.base_curr = "EUR"
        self.choices = (('MXN', 'MXN'), ('AUD', 'AUD'), ('HKD', 'HKD'), ('RON', 'RON'), ('HRK', 'HRK'), ('CHF', 'CHF'), ('IDR', 'IDR'), ('CAD', 'CAD'), ('USD', 'USD'), ('ZAR', 'ZAR'), ('JPY', 'JPY'), ('BRL', 'BRL'), ('HUF', 'HUF'), ('CZK', 'CZK'), ('NOK', 'NOK'), ('INR', 'INR'), ('PLN', 'PLN'), ('ISK', 'ISK'), ('PHP', 'PHP'), ('SEK', 'SEK'), ('ILS', 'ILS'), ('GBP', 'GBP'), ('SGD', 'SGD'), ('CNY', 'CNY'), ('TRY', 'TRY'), ('MYR', 'MYR'), ('RUB', 'RUB'), ('NZD', 'NZD'), ('KRW', 'KRW'), ('THB', 'THB'), ('BGN', 'BGN'), ('DKK', 'DKK'))
        pass

    def test_get_currencies_valid(self):
        op_list = get_currencies()
        self.assertEquals(op_list, self.curr_list)

    def test_get_currencies_output_type(self):
        op_list = get_currencies()
        self.assertIsInstance(op_list, type(list()))

    def test_update_curr_list(self):
        #Adds base currency to the list of currencies
        self.assertFalse(self.base_curr in self.curr_list)
        lst = update_curr_list(self.curr_list)
        self.assertTrue(self.base_curr in lst)

    
    def test_update_curr_no_args(self):
        with self.assertRaises(TypeError):
            update_curr_list()

    def test_update_curr_type(self):
        op_list = update_curr_list(self.curr_list)
        self.assertIsInstance(op_list, type(list()))
    

    def test_create_choices_valid(self):
        choices = create_choices(self.curr_list)
        self.assertEquals(choices, self.choices)


    def test_create_choices_no_args(self):
        with self.assertRaises(TypeError):
            create_choices()

    def test_create_choices_type(self):
        choices = create_choices(self.curr_list)
        self.assertIsInstance(choices, type(tuple()))


class AppViewsTest(TestCase):
    #Setup ensures that we have a list of all the currency choices 
    def setUp(self):
        self.currency_choices =  create_choices(update_curr_list(get_currencies()))
        from django.test import Client
        self.form = CurrencyForm(self.currency_choices,{'amount': 1, 'to_curr': "INR", 'from_curr': "EUR"})
        self.form_invalid = CurrencyForm(self.currency_choices,{'amount': -1, 'to_curr': "INR", 'from_curr': "EUR"})
        self.client = Client()

    def test_index_status(self):
        response = self.client.get('/app/')
        self.assertEquals(response.status_code, 200)

    def test_index_context_keys(self):
        response = self.client.get('/app/')
        self.assertTrue('form' in response.context)

    def test_index_context_values(self):
        response = self.client.get('/app/')
        self.assertIsInstance(response.context['form'], type(self.form))

    def test_convert_valid(self):
        response = self.client.get('/app/convert/', data= {'amount': 1, 'to_curr': "INR", 'from_curr': "EUR"}, content_type="application/x-www-form-urlencoded")
        self.assertEquals(response.status_code, 200)

    def test_convert_invalid(self):
        response = self.client.get('/app/convert/', data= {'amount': -1, 'to_curr': "INR", 'from_curr': "EUR"}, content_type="application/x-www-form-urlencoded")
        self.assertEquals(len(response.context['errors']),1)
        self.assertEquals(response.status_code, 200)

    def test_convert_result(self):
        response = self.client.get('/app/convert/', data= {'amount': 1, 'to_curr': "INR", 'from_curr': "EUR"}, content_type="application/x-www-form-urlencoded")
        # 10% Margin for changes
        self.assertTrue(response.context['result'] > 72 and response.context['result'] < 88)

    def test_convert_form_reinitialize(self):
        response = self.client.get('/app/convert/', data= {'amount': 1, 'to_curr': "INR", 'from_curr': "EUR"}, content_type="application/x-www-form-urlencoded")
        self.assertEquals(response.context['form'], self.form)

    def test_convert_same_curr(self):
        response = self.client.get('/app/convert/', data= {'amount': 1, 'to_curr': "INR", 'from_curr': "INR"}, content_type="application/x-www-form-urlencoded")
        self.assertEquals(response.context['result'], 1)

    def test_convert_status_wo_params(self):
        response = self.client.get('/convert/')
        self.assertEquals(response.status_code, 404)