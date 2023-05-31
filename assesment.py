

def Add(string: str) -> int:

    if string == "":
        return 0 
    
    elif "," in string:
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



