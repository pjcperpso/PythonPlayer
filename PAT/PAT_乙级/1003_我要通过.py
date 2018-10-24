"""
只包含PAT
任何形容*PAT*都正确
若aPbTc正确  则aPbATca正确  针对最开始:b是A,c=a才满足*PAT*   每次遍历中间多个A   末尾多个a
AAPATAA---AAPAATAAAA---AA((nA))PAAA(3A)TAAAAAA(3(nA))---AAPAAAATAAAAAAAA    所以左A*中间个数=右A数
"""
import re

def passMe():
    message = input('please input message:')
    if message.
    for x in range(1,len(message)):
        if message[x] == 'P':
            p_index = x
        elif message[x] =='T':
            t_index = x
    between = t_index-p_index-1
    last = len(message)-t_index-1
    if p_index*between == last:
        print('通过')
    else:
        print('错误')
passMe()
