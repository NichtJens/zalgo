from __future__ import print_function

try:
    mkchr = unichr # py2
except NameError:
    mkchr = chr # py3

try:
    strtype = basestring # py2
except NameError:
    strtype = str # py3


from functools import wraps
from random import choice, randint

MARKS = [mkchr(i) for i in range(768, 879)]
N_MAX = 10 # beyond 10 it becomes visually indistinguishable; on the order of several thousand it becomes slow

flatten = "".join


def handle_seq_args(f):
    @wraps(f)
    def wrapper(x, *args, **kwargs):
        if isinstance(x, strtype):
            return f(x, *args, **kwargs)
        else:
            return [wrapper(i, *args, **kwargs) for i in x]
    return wrapper



@handle_seq_args
def zalgo(s, n=None):
    if n is None:
        n = get_rand_n()
    return flatten(fup_char(c, n) for c in s)

@handle_seq_args
def escalate(s):
    return flatten(fup_char(c, n//N_MAX+1) for n, c in enumerate(s))

@handle_seq_args
def random(s):
    return flatten(fup_char(c, get_rand_n()) for c in s)



def fup_char(c, n):
    if not c.isalnum():
        return c
    return c + get_fup(n)

def get_rand_n():
    return randint(1, N_MAX)

def get_fup(n):
    n = min(n, N_MAX)
    return flatten(get_n_marks(n))

def get_n_marks(n):
    return (choice(MARKS) for _ in range(n))



def main():
    import argparse

    parser = argparse.ArgumentParser(description=zalgo("ZALGO!"))
    parser.add_argument("text", nargs="+")
    parser.add_argument("-s", "--strength", default=None, type=int)
    clargs = parser.parse_args()

    print(*zalgo(clargs.text, clargs.strength))



if __name__ == "__main__":
    main()



