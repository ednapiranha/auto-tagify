# -*- coding: utf-8 -*-
import re
try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote

import nltk

from nltk.stem.wordnet import WordNetLemmatizer

CLEAN_LINK = re.compile('(?<=^\/)\/+|\/+$')
CLEAN_WORD = re.compile('[\[\],().:;"\/\'?*%!*+=@$;#%{}`~\r\n\t]')
LONG_DASH = re.compile('(\&#8212;)')
MIN_TAG_LENGTH = 2
SMART_QUOTES_D = re.compile('(\xe2\x80\x9c)|(\xe2\x80\x9d)|(\&#8220;)|(\&#8221;)')
SMART_QUOTES_S = re.compile('(\xe2\x80\x98)|(\xe2\x80\x99)|(\&#8216;)|(\&#8217;)')
STOP_WORDS = ['DT', 'IN', 'TO', 'VBD', 'VBD', 'VBG', 'VBN', 'VBZ', 'MD', 'RB',
              'CC', 'WDT', 'PRO', 'PRP', 'PRP$']


class AutoTagify():
    lemma = WordNetLemmatizer()

    def __init__(self):
        self.css = ''
        self.link = ''
        self.text = ''

    def _tokenize(self):
        """Tag words from the string."""
        return nltk.pos_tag(nltk.word_tokenize(self._clean_text()))

    def _cleaned(self, word, strict):
        lemmatized = self.lemma.lemmatize(self._clean_text(word))
        if strict:
            return lemmatized
        else:
            return quote(self._clean_text(word))

    def _clean_text(self, word=''):
        if len(word) > MIN_TAG_LENGTH:
            return CLEAN_WORD.sub('', self._replace_special_chars(word.lower()))
        else:
            return CLEAN_WORD.sub('', self._replace_special_chars(self.text))

    def _replace_special_chars(self, text):
        return SMART_QUOTES_S.sub('\'', SMART_QUOTES_D.sub('"', LONG_DASH.sub('-',text)))

    def generate(self, strict=True):
        """Return the HTML version of tags for the string."""
        tag_words = []
        for (word, word_type) in self._tokenize():
            tag_word = self._cleaned(word, strict)
            if len(tag_word) > MIN_TAG_LENGTH and word_type not in STOP_WORDS:
                tag_words.append('<a href="%s/%s" class="%s">%s</a> ' % (CLEAN_LINK.sub('', self.link),
                                                                         quote(tag_word),
                                                                         CLEAN_WORD.sub('', self.css),
                                                                         self._replace_special_chars(word)))
            else:
                tag_words.append(word + ' ')
        return ''.join(tag_words)

    def tag_list(self, strict=True):
        """Return the tags from string as a list. If strict is set
        to True, then only return the stemmed version. Otherwise, return the
        full string - therefore, `cat` will be considered different from `cats`.
        """
        tag_words = []
        for (word, word_type) in self._tokenize():
            tag_word = self._cleaned(word, strict)
            if len(tag_word) > MIN_TAG_LENGTH and word_type not in STOP_WORDS:
                tag_words.append(tag_word)
        return tag_words
