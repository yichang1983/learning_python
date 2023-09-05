"""

Char	Description	Meaning
.	Period or dot	Matches any single character
+	Plus sign	Match one or more of the previous
*	Asterisk or star	Match zero, one or more of the previous
\	Backslash	Used to escape a special character
^	Caret	Beginning of a string
$	Dollar sign	End of a string
\s  Whitespace character class
\d  Digit character class
\S  Non-whitespace character class
[ ]	Opening and closing square bracket	Matches a range of characters
( )	Opening and closing parenthesis	Group characters
|	Vertical bar or pipe symbol	Matches previous OR next character/group
?	Question mark	Match zero or one of the previous
{ }	Opening and closing curly brace	Matches a specified number of occurrences of the previous
"""
import re
ip_1 = '172.16.20.20'
ip_2 = '      192.168.1.10    '

# print(re.search(r".",ip_1).group(0))
# print(re.search(r"\d\d",ip_1).group(0))     #數字

# print(re.search(r"^\s+\S\S",ip_2).group(0))     # ^開始, \s 空白,+就是前一個空白一直持續  \S 非空白的文字
# print(re.search(r"^\s+[\d\.]+",ip_2).group(0))     #\s+: 這是一個匹配一個或多個空格字符（空格、制表符、換行等）的模式。 [\d\.]+: 這部分匹配一個或多個數字（0-9）或小數點（.）字符。方括號[]用於表示一個字符集合，\d表示匹配數字，而點.本身也被包含在集合中，所以這可以匹配數字和小數點的序列。

match = re.search(r"^\s+([\d\.]+)", ip_2)        #\s+: 這是一個匹配一個或多個空格字符（空格、制表符、換行等）的模式。 [\d\.]+: 這部分匹配一個或多個數字（0-9）或小數點（.）字符。方括號[]用於表示一個字符集合，\d表示匹配數字，而點.本身也被包含在集合中，所以這可以匹配數字和小數點的序列。


if match:
    result = match.group(1)
    print(result)