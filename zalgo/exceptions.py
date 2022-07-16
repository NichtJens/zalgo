import sys
from types import SimpleNamespace

try:
    import IPython
except ImportError:
    IPython = None

from .zalgo import zalgo


def invoke():
    invoke_sys()

    if IPython is not None:
        invoke_ipy()


def invoke_sys():
    old_excepthook = sys.excepthook

    def new_excepthook(etype, evalue, tb):
        update_exc_value(evalue, zalgo)
        old_excepthook(etype, evalue, tb)

    sys.excepthook = new_excepthook


def invoke_ipy():
    ipysh = IPython.core.interactiveshell.InteractiveShell

    old_showtraceback = ipysh.showtraceback

    def new_showtraceback(self, exc_tuple=None, **kwargs):
        exc_tuple = exc_tuple or sys.exc_info()
        exc_tuple = update_exc_tuple(exc_tuple, zalgo)
        old_showtraceback(self, exc_tuple=exc_tuple, **kwargs)

    ipysh.showtraceback = new_showtraceback


def update_exc_tuple(etuple, func):
    etype, evalue, tb = etuple
    update_exc_value(evalue, func)
    etuple = (etype, evalue, tb)
    return etuple

def update_exc_value(evalue, func):
    evalue.args = tuple(func(a) for a in evalue.args)


# use a namespace to show only invoke* in tab completion
exceptions = SimpleNamespace(
    invoke=invoke,
    invoke_sys=invoke_sys,
    invoke_ipy=invoke_ipy
)



if __name__ == "__main__":
    invoke()



