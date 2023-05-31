import pytest

def Add(string: str) -> int:

    if string == "":
        return 0 
    
    if string[:2] == "//":

        idx = string.index('\n')

        delimeter = string[2: idx]

        numbers = string[idx: ].split(delimeter)

        return sum(int(num) for num in numbers)
    
    
    elif "," in string or "\n" in string:

        string = string.replace("\n", ",")

        numbers = string.split(",")

        return sum(int(num) for num in numbers)
    
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
    
    with pytest.raises(Exception) as excinfo:
        Add("1,\n")
    assert str(excinfo.value) == "invalid literal for int() with base 10: ''"


'''
Solving 4th requirement. Sipport different delimeter.
'''



def test_different_delimeter():


    assert Add("//;\n1;2") == 3
    # using  ;; as delimeter
    assert Add("//;;\n1;;2") == 3
