# 打印99乘法表

def multiplication_table():
    s = ""
    for i in range(1,10):
        for j in range(1,i+1):
            s += f"{j} * {i} = {j*i}\t"
        s += '\n'
    return s

if __name__ == '__main__':
    s = multiplication_table()
    print(s)