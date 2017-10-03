# pytef - Python Test Code Create Framework

easy to create Python test code.

## Install

```bash
git clone https://github.com/miyagaw61/pytef /path/to/pytef
cd /path/to/pytef
python setup.py install
```
※/path/to/は任意のディレクトリです

## Usage

1. create config file
2. pytef [config file]

* How to create config file

先頭が"from"または"import":宣言を記述
一文字めが"\*":普通に記述
一文字めが"!":テストする関数名
それ以外:カンマ区切りで引数を書き、セミコロンで区切った後に望みの答え(返却値)を記述

## Usage Example

```bash
vim add.py
```

> import sys
> 
> def add_func(x, y):
>     if type(y) == int:
>         return x + y
>     else:
>         return TypeError
> 
> if __name__ == '__main__':
>     print(add_func(int(sys.argv[1]), int(sys.argv[2])))

```bash
vim pytef.conf
```

> from .add import *
> import sys
> \*strings = "AAA"
> !add_func
> 1,2;3
> 2,3;6
> 4,0;4
> -1,2;1
> -2,0;-2
> -3,-3;-6
> -3,strings;TypeError

```bash
pytef pytef.conf
```

> ===== test session starts =====
> platform linux -- Python 3.6.2, pytest-3.2.2, py-1.4.34, pluggy-0.4.0
> rootdir: /home/miyagaw61/git/pytef, inifile:
> 
> collected 1 item  
> 
> pytef_out.py F
> 
> ===== FAILURES =====
> ----- test_add_func -----
> 
>     def test_add_func():
>         assert add_func(1,2) == 3
> \>       assert add_func(2,3) == 6
> E       assert 5 == 6
> E        +  where 5 = add_func(2, 3)
> 
> pytef_out.py:4: AssertionError
> ===== 1 failed in 0.06 seconds =====
