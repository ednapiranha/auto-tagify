import unittest
from auto_tagify2 import AutoTagify

class AutoTagifyTestCase(unittest.TestCase):

    def testTextNotEmptyStrict(self):
        """Verify strict text returns content, if text is provided and
        not null.
        """
        a = AutoTagify()
        a.text = 'This is a test'
        a.css = 'taggable'
        self.assertEqual(a.tag_list(), ['test'])
        self.assertEqual(a.generate(), 'This is a <a href="/test" class="taggable">test</a> ')

    def testTextNotEmptyNotStrict(self):
        """Verify non-strict text returns content, if text is provided and
        not null.
        """
        a = AutoTagify()
        a.text = 'These are my tests'
        a.css = 'taggable'
        self.assertEqual(a.tag_list(), ['are', 'test'])
        self.assertEqual(a.generate(strict=False),
                         'These <a href="/are" class="taggable">are</a> my <a href="/tests" class="taggable">tests</a> ')

    def testTextEmpty(self):
        """Verify sending no text returns nothing."""
        a = AutoTagify()
        self.assertEqual(a.generate(), '')

    def testTagsNotEmpty(self):
        """Verify that tags are returned."""
        a = AutoTagify()
        a.text = 'This is a test with other valid tags'
        test_array = ['test', 'other', 'valid', 'tag']
        self.assertEqual(a.tag_list(), test_array)

if __name__ == "__main__":
        unittest.main()
