

import begin

@begin.subcommand
def status(compact: 'Short or long format' = True):
    """ Report the current status. """
    if compact:
        print('ok.')
    else:
        print('Very well, thank-you.')

@begin.subcommand
def fetch(url: 'Data source' = 'http://google.com'):
    """ Fetch data from the URL. """
    print('Work goes here')

@begin.start(auto_convert=True)
def main(a: 'First value' = 0.0, b: 'Second value' = 0.0):
    """ Add two numbers """
    print(a + b)


