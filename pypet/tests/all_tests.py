__author__ = 'Robert Meyer'

import getopt
import sys


from pypet.tests.testutils.ioutils import make_run, do_tag_discover, TEST_IMPORT_ERRORS


if __name__ == '__main__':
    opt_list, _ = getopt.getopt(sys.argv[1:],'k',['folder='])
    remove = None
    folder = None
    for opt, arg in opt_list:
        if opt == '-k':
            remove = False
            print('I will keep all files.')

        if opt == '--folder':
            folder = arg
            print('I will put all data into folder `%s`.' % folder)

    sys.argv=[sys.argv[0]]
    suite = do_tag_discover(tests_exclude=TEST_IMPORT_ERRORS)
    make_run(remove, folder, suite=suite)