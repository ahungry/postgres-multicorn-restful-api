from multicorn import ForeignDataWrapper
from multicorn.utils import log_to_postgres as log
from requests import get
import logging

class Ahu(ForeignDataWrapper):
  def __init__(self, options, columns):
    super(Ahu, self).__init__(options, columns)

    self.validate(options, columns)
    self.columns = columns
    self.domain = options['domain']

  def validate(self, options, columns):
    if 'domain' not in options:
      log(message = 'No domain provided', level = logging.ERROR)

  def handle_error(self, response):
    if response['error_description']:
      error = response['error_description']
    else:
      error = response['error']

    log(message = error, level = logging.ERROR)

  def execute(self, quals, columns):
    headers = {}
    url = '%s/api/eq/get-item-listings/wts.json' % (self.domain)
    res = get(url, headers=headers)
    data = res.json()

    if 'error' in data:
      self.handle_error(data)
    else:
      for entry in data:
        yield entry
