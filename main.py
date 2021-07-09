from bdd import BDD
from time import sleep
twitter = BDD('Welling83488832', 'Wellington24', 'tonmedeiros', 'firefox', test= True)
try:
    twitter.login()
    twitter.fall_process(5)
    print(twitter.number_of_process)
except(KeyboardInterrupt):
    twitter.abort_bot(emergency=True)
except:
    quit()