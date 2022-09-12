#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ Divide elements in a list
    Args:
        my_list_1: the first list
        my_list_2: the second list
        list_length: number of items to divide
    Returns:
        a new list of length list_length
    """
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError):
            result = 0
            print("division by 0")
        except (TypeError):
            result = 0
            print("wrong type")
        except (IndexError):
            result = 0
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
