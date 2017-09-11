def gen_pattern(s):
    d = ''
    mid = '*'.join(s[len(s):0:-1] + s)
    s = s[::-1]
    for i in range(0, len(s) - 1):
        tmp = (2 * (len(s) - (i + 1))) * '*'  # add front * #
        tmp = tmp + '*'.join(s[:i + 1])  # add * between front pattern #
        d = d + tmp + tmp[-2::-1] + '\n'
    str = d + mid + d[::-1]
    return str


print(gen_pattern('SDNOMAID'))
