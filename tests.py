import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from retirement import calculate_retirement_age


#test negative numbers raises the value error
def test_calculate_retirement_age_when_birth_year_is_negative():
    with pytest.raises(ValueError):
        calculate_retirement_age(-1900) 




@given('user types in -1900 (or any negative number)')
def negative_number():
    calculate_retirement_age(-1900) 


@when('When the number is entered')
def number_entered():
    pass

@then('Then the user will recieve a Value Error')
def recieve_a_value_error():
    return ValueError


#test postive numbers
def test_calculate_retirement_age_when_birth_year_is_postive():
    assert calculate_retirement_age(1900)




@given('user types in -1900 (or any negative number)')
def positive_number():
    calculate_retirement_age(1900) 


@when('When the number is entered')
def number_entered2():
    pass

@then('Then the user will recieve a no Error')
def recieve_no_error():
    return None





# test to make sure the age range works
def test_calculate_retirement_age_range():
    with pytest.raises(ValueError):
        calculate_retirement_age(1899)
        calculate_retirement_age(3001)





@given('user types in a 3001')
def number():
    calculate_retirement_age(3001) 


@when('When the number is entered')
def number_entered3():
    pass

@then('Then the user will recieve a Index Error')
def recieve_a_index_error():
    return IndexError

