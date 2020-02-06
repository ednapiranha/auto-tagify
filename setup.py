from distutils.core import setup

setup(name='auto_tagify2',
      version='1.4.3',
      author='operatorjen',
      author_email='python@0112358.io',
      url='https://github.com/operatorjen/auto-tagify',
      description='Auto-tags a selection of text and generates links to the tagified versions of the words',
      license='BSD',
      long_description="""

Auto Tagify2 is a simple auto tagging module that uses NLTK to generate tags out of a selection of text. Any
text that is less than 3 characters long or matches a particular POS (part-of-speech) will be ignored.

There are two operations Auto Tagify performs - one returns the selection of text with links embedded in the
string and the other returns a list of all the taggable words as the stem word (using lemmatization).

For the first operation, everything is optional, but it is most effective to enter some text. Optional
parameters you can set are the paths for tag links and the css classes for link. For instance, if you set
your tag routing to a relative path such as /tags/<tagged_word> and want to use the css class named "tagged":

from auto_tagify2 import AutoTagify

t = AutoTagify()

t.text = "This is the text to display!"

t.link = "/tags"

t.css = "tagged"

t.generate()

The result will be: This is the <a href="/tags/text" class="tagged">text</a> to <a href="/tags/display" class="tagged">display!</a>

If no link is set, the default path is "/<tagged word>", such as "/text".

For the second operation, you will only receive a list of all your taggable words from the text. You can call it like so:

t.text = "This text is tagged kittens"

t.tag_list()

The result will be a list: ['text', 'tag', 'kitten']

By default, generate() and tag_list() will be in strict mode, which means all special characters will be stripped and
lemmatization will be enforced. If generate(strict=False) or tag_list(strict=False) is set, then special characters will be url encoded
and lemmatization will be ignored.

These two operations are sufficient for you to maintain tag counts and tag references to text in your application.
        """,
        packages=['auto_tagify2'],
        keywords='tagging tags html nltk english',
        classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        ],
        )
