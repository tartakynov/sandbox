#!/usr/bin/env python


def base_convert(value, base):
    if 2 <= base <= 32:
        result = ""
        while value > 0:
            r = value % base
            c = chr(ord('a') + (r - 10)) if r >= 10 else str(r)
            result = c + result
            value /= base
        return result
    raise ValueError("Base %d is not supported" % base)


def main():
    print 2, base_convert(567623, 2)
    print 4, base_convert(567623, 4)
    print 8, base_convert(567623, 8)
    print 10, base_convert(567623, 10)
    print 16, base_convert(567623, 16)
    print 32, base_convert(567623, 32)


if __name__ == "__main__":
    main()
