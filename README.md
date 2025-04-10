
# 有道请求合法性验证算法：

1.  **计算 time：**
    
    ```js
    time = ("" + e.text + v).length % 10
    
    ```
    
    这里把查询文本（e.text）和一个外部变量 v 拼接后计算字符串长度，然后对 10 取余，得到 time。
    
2.  **第一次哈希：**
    
    ```js
    r = "" + e.text + v
    o = h(r)
    
    ```
    
    将 e.text 与 v 拼接后，用函数 h 进行一次哈希，结果存入 o。通常 h 可能是 MD5 函数。
    
3.  **构造待签名字符串：**
    
    ```js
    n = "web" + e.text + time + "Mk6hqtUp33DGGtoS63tTJbMUYjRrG1Lu" + o
    
    ```
    
    拼接固定字符串 `"web"`、查询文本、刚刚计算的 time、一个固定密钥 `"Mk6hqtUp33DGGtoS63tTJbMUYjRrG1Lu"` 以及第一次哈希 o。
    
4.  **第二次哈希得到 sign：**
    
    ```js
    f = h(n)
    
    ```
    
    对构造好的字符串 n 进行再次哈希，得到最终的 sign。
    
5.  **构造请求数据：**  
    最后将 q、le、t、client、sign、keyfrom 等参数打包发送 POST 请求。
    
-   **输入：** 查询文本 `e.text` 与外部变量 `v`（一般就是 keyfrom 的值）
    
-   **步骤：**
    
    1.  计算 `time = (e.text + v).length % 10`
        
    2.  计算 `o = h(e.text + v)`
        
    3.  构造字符串：`"web" + e.text + time + "Mk6hqtUp33DGGtoS63tTJbMUYjRrG1Lu" + o`
        
    4.  计算 `sign = h(上面拼接后的字符串)`
        
-   **输出：** 最终的 sign 值
    

这意味着最终的签名是通过两次哈希（通常是 MD5）的方式生成的，其中第一次哈希处理 (e.text + v)，第二次哈希处理拼接了固定前缀 `"web"`、固定密钥和第一次哈希结果。

