def lines(file):
    #建立行生成器
    for line in file:yield  line
    yield '\n'

def blocks(file):
    block = []
    #建立块（段）生成器
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield  ''.join(block).strip()
            block = []
