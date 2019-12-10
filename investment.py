vim investment.py #创建investment文件，在vim里面编辑

#!/usr/bin/env python3
  2 amount = float(input("Enter amount: ")) # \输入数额
  3 inrate = float(input("Enter Interest rata: ")) #输入利率
  4 period = int(input("Enter period: ")) #输入期限
  5 value = 0
  6 year = 1
  7 while year <= period:
  8     value = amount + (inrate * amount)
  9     print("Year {} Rs. {:.2f}".format(year,value))
 10     amount = value
 11     year = year + 1
 
'Esc'   ':'+'wq'    'enter'   #退出vim

$ cd /home/shiyanlou
$ chmod +x investment.py
$ ./investment.py
Enter amount: 10000
Enter Interest rate: 0.14
Enter period: 5
Year 1 Rs. 11400.00
Year 2 Rs. 12996.00
Year 3 Rs. 14815.44
Year 4 Rs. 16889.60
Year 5 Rs. 19254.15

#while year <= period: 的意思是，当 year 的值小于等于 period 的值时，下面的语句将会一直循环执行下去，直到 year 大于 period 时停止循环。

Year {} Rs. {:.2f}".format(year, value) 称为字符串格式化，大括号和其中的字符会被替换成传入 str.format() 的参数，也即 year 和 value。其中 {:.2f} 的意思是替换为 2 位精度的浮点数。
