import sys

def echo():
    """
    获取用户输入并打印出来，支持-s标志以大写形式输出
    
    使用方法:
    - python echo.py (普通模式)
    - python echo.py -s (大写模式)
    """
    shout = "-s" in sys.argv
    message = input("Please enter something: ")
    print(message.upper() if shout else message)

if __name__ == "__main__":
    echo()