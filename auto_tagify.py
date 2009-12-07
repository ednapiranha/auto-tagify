import re
import urllib

class AutoTagify():
  stop_word = re.compile('(^(th|wh|hi|sh|an|ha|wa|it)[adeisouy]$)|(^(th|wh|do|is|he)[aeionur][nstey]$)|(^(wh|th|h|w)(ere))|(^(w|sh|c)(ould))|(but)|(how)|(very)|(really)|(with)|(not)|(their)|(theyre)|(are)|(for)|(because)')
  eol = re.compile('[\r\n\t]')
  clean_word = re.compile('[\[\],().:"\'?!*<>/\+={}`~]')
  clean_link = re.compile('(?<=^\/)\/+|\/+$')
  min_word_length = 3
  
  def __init__(self):
    self.css = ''
    self.link = ''
    self.text = ''
    
  def generate(self,strict=True):
    tag_words = ''

    for word in self.eol.sub(' ',self.text).split(' '):
      if strict:
        tag_word = self.clean_word.sub('',word.lower())
      else:
        tag_word = urllib.quote(word.lower())
      if len(tag_word) >= self.min_word_length and not self.stop_word.match(tag_word):
        tag_words += '<a href="'+self.clean_link.sub('', self.link)+'/'+urllib.quote(tag_word)+'" class="'+self.clean_word.sub('',self.css)+'">'+word+'</a> '
      else:
        tag_words += word+' '

    return tag_words
  
  def tag_list(self,strict=True):
    tag_words = []
    
    for word in self.eol.sub(' ',self.text).split(' '):
      if strict:
        tag_word = self.clean_word.sub('',word.lower())
      else:
        tag_word = urllib.quote(word.lower())
      if len(tag_word) >= self.min_word_length and not self.stop_word.match(tag_word):
        tag_words.append(tag_word)
 
    return tag_words