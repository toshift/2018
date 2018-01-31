import mock
from os.path import join

with mock.patch('os.path.join', return_value='test') as m:
    join('param1','param2')
    print(m is join)

with mock.patch('__main__.join', return_value='test') as m:
    join('param1','param2')
    print(m is join)    

import os.path

with mock.patch('os.path.join', return_value='test') as m:
    os.path.join('param1','param2')
    print(m is os.path.join)    
