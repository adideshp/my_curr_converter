# Currency Converter Application
The application should use the public api (https://api.exchangeratesapi.io/latest) to convert the current conversion rate between any two currencies that you select.

## Application screenshot
![alt text](appshot.png)
## Application structure
The application should have following components:

### Input Form (CurrencyForm): 
This from takes input from the user and send this input to the convert view. The user should take special care to perform validations for all the fields in the form. Also, initialization of the select component should be done. Use Django forms to implement this functionality.

### Currency conversion view (convert)
Currency conversion view is responsible to process the form fields and return a result. In this case the form fields will specify the amount and name of the currencies (TO and FROM) for the conversion. All the exceptions and edge cases related to missing data and HTTPError should be handled in the view. 

## Passing criteria
The application should convert the amount from source currency to target currency.

### The application can be evaluated based on the milestones mentioned below,
          1. Write a function get_currency that takes no argument and returns a list of all the available currencies
          2. Base currency is "EUR". Add the base currency to the list of available currencies
          3. Fill all the currency values in the select boxes
          4. Write a function to convert a currency from one type to other
          5. Show the results on the frontend
          
## Test Cases
|No.  | Name | TargetComponent  | Description |
|--|--|--|--|
|1|test_init|CurrencyFormTest|Test form initialization|
|2|	test_init_without_choices|	CurrencyFormTest|	Test form initialization with missing args|
|3|	test_blank_data|	CurrencyFormTest|	Test form initialization on blank data|
|4|	test_valid_data|	CurrencyFormTest|	Test form initialization with valid data|
|5|	test_special_char_in_amount|	CurrencyFormTest|	Test form initialization with special chars in amount field|
|6|	test_alphabets_in_amount|	CurrencyFormTest|	Test form initialization with alphabets in amount field|
|7|	test_float_in_amount|	CurrencyFormTest|	Test form initialization with floating point number in amount field|
|8|	test_zero_in_amount|	CurrencyFormTest|	Test form initialization with 0 in the amount field|
|9|	test_negetive_in_amount|	CurrencyFormTest|	Test form initialization with negative amount field|
|10|	test_same_to_from_currency|	CurrencyFormTest|	Test form initialization for same source and target currency fields|
|11|	test_get_currencies_valid|	HelperFunctionsTest|	Test get_currencies for valid case|
|12|	test_get_currencies_output_type|	HelperFunctionsTest	|Test get_currencies output type|
|13|	test_update_curr_list|	HelperFunctionsTest	|Test update_curr for valid output|
|14|	test_update_curr_no_args|	HelperFunctionsTest	|Test update_curr for no args|
|15|	test_update_curr_type|	HelperFunctionsTest	|Test update_curr output type|
|16|	test_create_choices_valid|	HelperFunctionsTest	|Test create_choice for valid cases|
|17|	test_create_choices_no_args|	HelperFunctionsTest	|Test create_choice with no args|
|18|	test_create_choices_type|	HelperFunctionsTest	|Test create_choice for the output type|
|19|	test_index_status	|AppViewsTest|	Test Index view response status|
|20|	test_index_context_keys|	AppViewsTest|	Test keys in context in index response|
|21|	test_index_context_values|	AppViewsTest|	Test values in context in index response|
|22|	test_convert_valid|	AppViewsTest|	Test convert view for valid case|
|23|	test_convert_invalid|	AppViewsTest	|Test convert view for invalid case|
|24|	test_convert_result	|AppViewsTest|	Test convert view for result|
|25|	test_convert_form_reinitialize|	AppViewsTest|	Test how the form is reinitialized after the convert view returns|
|26|	test_convert_same_curr|	AppViewsTest	|Test convert view for same currency conversions|
|27|	test_convert_status_wo_params|	AppViewsTest	|Test convert view when no get params are passed|


## Solution:
The below mentioned steps are for Ubuntu. The user will have to perform minor modifications to install the app on other platforms
### Installation

The application requires Python 3 to run.
Install python 3 from https://realpython.com/installing-python/


virtual environment is a part of standard library for python3. 

Clone the application 
```sh
$ git clone  https://github.com/adideshp/my_curr_converter.git
```


Follow the installation steps as mentioned below,
```sh
$ python3.6 -m venv <NAME_OF_THE_ENVIRONMENT> 
$ source <NAME_OF_THE_ENVIRONMENT>/bin/activate
```
Above mentioned commands create a virtual-env named <NAME_OF_THE_ENVIRONMENT> (This is a custom name). Second command activates the virtual env. Virtual environment creates a isolated environment for all the package installation.

Install all the packages listed in requirements.txt. Follow the steps below,
```sh
$ cd my_curr_converter
$ pip install -r requirements.txt
```

Although the app does not interact with the database you can run all the migrations as follows,
```sh
$ python manage.py migrate
```

The app needs a active internet connection to work as it interacts with the online APIs.

### Starting the application
The application can be started by executing the command below. The app starts at http://localhost:8000

```sh
$ python manage.py runserver
```
### Running test cases
Use the following command to run all the tests in the project

```sh
$ python manage.py test app
```

### Test Coverage
![alt text](coverage.png)
