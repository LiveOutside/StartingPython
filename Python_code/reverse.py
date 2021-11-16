def reverse():
    inp = open('input.dat', 'rb').read()
    out = open('output.dat', 'wb')
    out.write(bytes(inp)[::-1])
