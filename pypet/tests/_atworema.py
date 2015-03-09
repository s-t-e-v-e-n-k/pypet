__author__ = 'Robert Meyer'

from pypet.tests.testutils.ioutils import run_tests, discover_tests, TEST_IMPORT_ERROR

if __name__ == '__main__':
    suite = discover_tests(predicate= lambda class_name, test_name, tags:
                                                class_name != TEST_IMPORT_ERROR)
    run_tests(remove=False, folder=None, suite=suite)