from time import sleep
import random as rd

ends = [
' ',
' - ',
'',
' / ',
' \ ',
'   ',
' . ',
' _ ',
'_',
'$',
'#',
'@',
'*',
' * ',
'%',
'!',
'!!!',
'~',
' ` ',
]

words = [
'fuck',
'motherfucker',
'shit',
'shitface',
'ass',
'asshole',
'cunt',
'pussy',
'slut',
'bitch',
'twat',
]

if __name__ == '__main__':
    while True:
        sleep(rd.random() / 420)
        print(rd.choice(words), end=rd.choice(ends))
