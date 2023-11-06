import threading

def msg(msg='None'): 
    print(msg)

thread = [
        threading.Thread(target=msg, args=['thread 1']),
        threading.Thread(target=msg, args=['thread 2']),
        threading.Thread(target=msg, args=['thread 3']),
        threading.Thread(target=msg, args=['thread 4']),
        ]


if __name__ == '__main__':
    for i in thread:
        i.start()









