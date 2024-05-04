'''
    A enhance pdb, inherent from https://github.com/pdbpp/pdbpp
    author: fengshuyang
    email: fsy_daily@163.com
'''
import sys
import traceback
import pdb
from fancycompleter import ConfigurableClass, my_execfile
import os

class ConClass(ConfigurableClass):

    def get_config(self, Config, config_filename = 'config.py'):
        if Config is not None:
            return Config()
        filename = os.path.join(os.path.dirname(__file__), config_filename)
        rcfile = os.path.normpath(os.path.expanduser(filename))
        if not os.path.exists(rcfile):
            return self.DefaultConfig()

        mydict = {}
        try:
            my_execfile(rcfile, mydict)
        except Exception as exc:
            import traceback

            sys.stderr.write("** error when importing %s: %r **\n" % (filename, exc))
            traceback.print_tb(sys.exc_info()[2])
            return self.DefaultConfig()

        try:
            Config = mydict["Config"]
        except KeyError:
            return self.DefaultConfig()

        try:
            return Config()
        except Exception as exc:
            err = "error when setting up Config from %s: %s" % (filename, exc)
            tb = sys.exc_info()[2]
            if tb and tb.tb_next:
                tb = tb.tb_next
                err_fname = tb.tb_frame.f_code.co_filename
                err_lnum = tb.tb_lineno
                err += " (%s:%d)" % (err_fname, err_lnum,)
            sys.stderr.write("** %s **\n" % err)
        return self.DefaultConfig()


class EasyPDB(pdb.Pdb, ConClass):
    """A pdbpp subclass that may be used
    from a forked multiprocessing child

    """


    def interaction(self, frame, traceback):
        if frame is None:
            # Skip clearing screen if called with no frame (e.g. via pdb.main).
            self._sticky_skip_cls = True

        self._in_interaction = True
        _stdin = sys.stdin
        try:
            sys.stdin = open('/dev/stdin')
            super().interaction(frame, traceback)
        finally:
            sys.stdin = _stdin
            self._in_interaction = False


def set_trace(frame=None):
    """Wrapper function to keep the same import x; x.set_trace() interface.

    We catch all the possible exceptions from pdb and cleanup.

    """
    
    debugger = EasyPDB()
    try:
        debugger.set_trace(frame or sys._getframe().f_back)
    except Exception:
        traceback.print_exc()
