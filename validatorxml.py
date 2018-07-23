import sys
from lxml import etree

class ValidatorXML(object):
  def __init__(self):
    self.parser = etree.XMLParser(dtd_validation=True)
    self.validation()
  def validation(self):
    if len(sys.argv) > 1:
      inXML = sys.argv[1]
      try:
        tree = etree.parse(inXML, self.parser)
        print '[VALID]'
        return tree
      except Exception, exp:
        print '[NOT valid]\nError:', exp
        return False
    else:
      print 'Error: enter xml file name'

V = ValidatorXML()
