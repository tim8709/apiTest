from hamcrest import *


def test_hamcrest():
    the_string = 'Hello Hamcrest'
    my_string = 'Hello Hamcrest'
    assert_that(the_string, equal_to(my_string))
