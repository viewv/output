import execnet

# 创建一个本地网关，或远程网关（可以通过 ssh 等方式）
gateway = execnet.makegateway()

# 发送 Python 代码到网关执行
channel = gateway.remote_exec("""
def safe_add(a, b):
    return a + b

channel.send(4)
""")

# 接收结果
result = channel.receive()
print(f"Result from remote execution: {result}")
