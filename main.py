from bdd import BDD
from time import sleep
twitter_1 = BDD('Welling83488832', 'Wellington24', 'tonmedeiros', 'firefox',test= True) #Erro na lina 133 obs:test.py funcionando, depois faz uma comparação entre os códigos
try:
    twitter_1.login()
    twitter_1.fall_process(5)
    print(twitter_1.number_of_process)
except(KeyboardInterrupt):
    twitter_1.abort_bot(emergency=True)
except(Exception):
    twitter_1.abort_bot()