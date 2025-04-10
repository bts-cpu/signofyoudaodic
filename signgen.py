import hashlib

def h(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

def get_sign(text, v="webdict"):
    # 计算 time
    time_val = len(text + v) % 10
    # 第一次哈希
    o = h(text + v)
    # 拼接待签名字符串
    n = "web" + text + str(time_val) + "Mk6hqtUp33DGGtoS63tTJbMUYjRrG1Lu" + o
    # 第二次哈希得到 sign
    sign = h(n)
    return sign, time_val

if __name__ == '__main__':
    text = "lj:genius"
    sign, time_val = get_sign(text)
    print("sign:", sign)
    print("t:", time_val)

