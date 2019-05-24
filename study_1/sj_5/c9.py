def curve_pre():
    def curve():
        print('This is a function')
        pass
    return curve
# curve()是错误的

f = curve_pre()
f()