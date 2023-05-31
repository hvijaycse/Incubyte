import pytest


def add_list(numbers: list[str]) -> int:

    '''
    Created this function to handle negative number
    for both the cases. 
    The , delimeter and unknown delimeter.
    '''

    neagtive_num = [ int(num) for num in numbers if int(num) < 0]

    if neagtive_num:
        raise Exception("negatives not allowed:" + ', '.join([str(s) for s in neagtive_num]))
    
    return sum(int(num) for num in numbers)


def Add(string: str) -> int:

    if string == "":
        return 0 
    
    if string[:2] == "//":

        idx = string.index('\n')

        delimeter = string[2: idx]

        numbers = string[idx+1: ].split(delimeter)

        print(string, idx, numbers)

        return add_list(numbers)
    
    
    elif "," in string or "\n" in string:

        string = string.replace("\n", ",")

        numbers = string.split(",")

        return add_list(numbers)
    
    else:
        return int(string)


'''
Solving the first Requriements.

'''

def test_add_empty():
    assert Add("") == 0

def test_add_single():

    assert Add("2") == 2
    assert Add("5") == 5

def test_add_doubles():

    assert Add("1,2") == 3
    assert Add("20, 40") == 60


'''
Solving second requriement of unknown amount of numbers.
'''


def test_add_unknown():

    assert Add("1,2,3,4")  == 10
    assert Add("3, 9, 12") == 24


'''
Solving third requirement.
'''


def test_add_next_line():


    assert Add("1\n2,3") == 6
    
    with pytest.raises(Exception) as exc:
        Add("1,\n")
    assert str(exc.value) == "invalid literal for int() with base 10: ''"


'''
Solving 4th requirement. Sipport different delimeter.
'''



def test_different_delimeter():


    assert Add("//;\n1;2") == 3
    # using  ;; as delimeter
    assert Add("//;;\n1;;2") == 3

'''
Solving 5th requirement. Do not support negative numbers. 
'''


def test_negative_numbers():

    with pytest.raises(Exception) as exc:
        Add("1, -2, 4")
    
    assert str(exc.value) == "negatives not allowed:-2"

    with pytest.raises(Exception) as exc:
        Add("//;;\n-31;;2")
    
    assert str(exc.value) == "negatives not allowed:-31"

