

def use_dis():
    import dis
    with open("demo.py") as f:
        s = f.read()
    co = compile(s, "demo.py", 'exec')
    print(dis.dis(co))


def use_dis_can_debug():
    from python37_dis import dis
    with open("demo.py") as f:
        s = f.read()
    co = compile(s, "demo.py", 'exec')
    print(dis(co))


# use_dis()
use_dis_can_debug()
