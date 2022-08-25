firstNum = int(input( '첫째 수를 입력하세요 : ' ))
secondNum = int(input( '둘 째 수를 입력하세요 : ' ))

sum = 0
for number in range( firstNum, secondNum + 1 ):
    sum += number

print( f'{ firstNum }에서 { secondNum }까지의 합은 { sum }입니다.' )