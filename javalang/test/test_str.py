import unittest

from .. import parse

class ImportStrTest(unittest.TestCase):

    def test_import_str(self):
        source = "import org.junit.Assert;"
        tree = parse.parse(source)
        self.assertEqual(source, tree.imports[0].to_java())

    def test_static_import_str(self):
        source = "import static org.junit.Assert.assertEquals;"
        tree = parse.parse(source)
        self.assertEqual(source, tree.imports[0].to_java())

    def test_import_wildcard_str(self):
        source = "import static org.junit.Assert.*;"
        tree = parse.parse(source)
        self.assertEqual(source, tree.imports[0].to_java())
