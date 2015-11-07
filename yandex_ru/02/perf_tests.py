import check_with_if
import check_with_regexp
import time
from datetime import datetime

test_data = {'': False, ' '*20: False, 'Z'*20: True,
             '0'*20: False, 'a'*21:False, 'a': True, '!': False,
             'aaaaaaaaaaa!': False, ' sfsafsfsfsafsf!': False, 
             'aaaaaaaaa!aa!': False, ' s!fsafsfsfsafsf!': False, 
             'aaaaaaqaaaaa!': False, ' sfsaqwfsfsfsafsf!': False, 
             'aaaaaaqweaaa!aa!': False, ' s!fsafqewqwsfsfsafsf!': False, 
             'aaaaaaaasfsdaaa!': False, ' sfsasdfsfsfsfsafsf!': False, 
             'aaaasfsdfaaaaa!aa!': False, ' s!fsafsfsfssfsdafsf!': False, 
             'a1': True, 'a2': True, 'a3': True, 'a4': True, 'a5': True, 
             'a6': True, 'a7': True, 'a8': True, 'a9': True, 
             'ab1': True, 'ab2': True, 'ab3': True, 'ab4': True, 'ab5': True, 
             'ab6': True, 'ab7': True, 'ab8': True, 'ab9': True, 
             }

if __name__ == '__main__':

    # Test IF:
    result = ''
    start = time.time()
    for s in test_data.keys():
        result += str(check_with_if.check_login(s))
    print('IF time: ' + str(time.time() - start))
    
    # Test RegExp:
    result = ''
    start = time.time()
    for s in test_data.keys():
        result += str(check_with_regexp.check_login(s))
    print('RegExp time: ' + str(time.time() - start))

    #print('Timeit: ' + str(timeit.timeit(check_with_if.check_login(' '))))