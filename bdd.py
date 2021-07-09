from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as wait
import selenium.common.exceptions as error
import platform
from time import sleep
from random import randint


class BDD:
    def __init__(self, username, password, target_user, browser='chrome', test=False, mtime = 'normal'):
        self.__target = target_user
        self.__password = password
        self.__username = username
        self.__test = test
        self.__mtime = mtime
        browser = browser.lower()
        

        if platform.system() == 'Linux':
            if browser == 'firefox':
                self.__driver = webdriver.Firefox(executable_path=r'drivers/geckodriver/geckodriver')
            elif browser == 'chrome':
                self.__driver = webdriver.Chrome(executable_path=r'drivers/chromedriver/chromedriver')
            elif browser == 'opera':
                self.__driver = webdriver.Opera(executable_path=r'drivers/operadriver/operadriver')
            elif browser == 'edge':
                self.__driver = webdriver.Edge(executable_path=r'drivers/edgedriver/msedgedriver')
            else:
                raise ImportWarning('Navegador não suportado, por favor utilize algum dos seguintes navegadores: firefox, chrome, opera ou edge.')

        elif platform.system() == 'Windows':
            if browser == 'firefox':
                self.__driver = webdriver.Firefox(executable_path=r'drivers/geckodriver/geckodriver.exe')
            elif browser == 'chrome':
                self.__driver = webdriver.Chrome(executable_path=r'drivers/chromedriver/chromedriver.exe')
            elif browser == 'opera':
                self.__driver = webdriver.Opera(executable_path=r'drivers/operadriver/operadriver.exe')
            elif browser == 'edge':
                self.__driver = webdriver.Edge(executable_path=r'drivers/edgedriver/msedgedriver.exe')
            else:
                raise ImportWarning('Navegador não suportado, por favor utilize algum dos seguintes navegadores: firefox, chrome, opera ou edge.')
        else:
            raise ImportWarning('Sistema Operacional não suportado, não será possível rodar o programa')



    def sort_time(self):
        minutes = randint(5,10)
        return minutes


    def login(self, verify=False):
        print('Inicializando BDD')
        driver = self.__driver
        self.show('abrindo janela')
        try:
            if self.__test:
                self.show('movendo janela para a esquerda')
                driver.set_window_size(width=960, height=1080), driver.set_window_position(0, 0)
            else:
                self.show('aviso: processo sendo executado em segundo plano')
                driver.minimize_window()
            self.show(f'abrindo twitter')
            driver.get('https://www.twitter.com/login/')
            wait(driver, 10).until(lambda driver: driver.find_element_by_name('session[username_or_email]'))

            username_box = driver.find_element_by_name('session[username_or_email]')
            password_box = driver.find_element_by_name('session[password]')
            username_box.clear()
            password_box.clear()
            self.show('inserindo as credenciais')
            username_box.send_keys(self.__username)
            password_box.send_keys(self.__password)
            self.show('autenticando as credenciais')
            password_box.send_keys(Keys.ENTER)
            wait(driver, 5).until(lambda driver: driver.find_element_by_xpath(
                    '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div'))
            self.show('login feito com sucesso')


        except(ConnectionAbortedError, ConnectionError, ConnectionRefusedError, ConnectionResetError):
            print(f'\033[1;31mPerda de Conexão, verifique seus cabos ou o wifi e tente novamente.')
            driver.quit()
            return 404

        except(error.TimeoutException):
            print(f'\033[1;31mTempo de Carregamento maior do que o esperado, verfique sua conexão e tente novamente.')
            driver.quit()
            return 408

    def fall_process(self, rounds=None, duration = None):
        self.show('iniciando processo de derrubada')
        if self.__test and self.__mtime == 'faster':
            duration = 0.18
        else:
            duration = self.sort_time()
        duration = duration * 60#SE HOUVER ERRO NO TEMPO MUDE PARA duration = durantion* 60
        target = self.__target
        driver = self.__driver
        self.number_of_process = 0
        if self.__test:
            if rounds == None:
                self.abort_bot()
                raise ValueError('[TESTER-MODE] Atríbuto "rounds" não definido na função "fall_process')
        try:
            while True: ### Criar um jeito de verificar quando o twitter mandar yma tela de login no meio do processo, crie outra função para isso, só pegar o código do login
                self.show(f'entrando no perfil: {target}')
                link_target = f'https://www.twitter.com/{target}'
                driver.get(link_target)
                self.verify()
                self.show(f'perfil encontrado')
                self.show('iniciando report')
                wait(driver, 5).until(lambda driver: driver.find_element_by_xpath(
                    '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/div'))
                if self.__test:
                    self.show('[teste-mode] clicando no botão de três pontos')
                driver.find_element_by_xpath(
                    '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/div').click()  # Botão três pontos
                if self.__test:
                    self.show('[teste-mode] clicando na opção de denunciar')
                driver.find_element_by_css_selector('div.r-1loqt21:nth-child(8)').click()  # Botão de denunciar
                sleep(1)
                if self.__test:
                    self.show('[teste-mode] entrando no iframe')
                driver.switch_to.frame(0)  # Entrando no iFrame
                wait(driver, 5).until(
                    lambda driver: driver.find_element_by_css_selector('#compromised-btn#compromised-btn'))
                if self.__test:
                    self.show('[teste-mode] clicando para denuciar')
                driver.find_element_by_css_selector(
                    '#compromised-btn#compromised-btn').click()  # Botão de Denúncia por hack
                wait(driver, 5).until(lambda driver: driver.find_element_by_xpath('/html/body/div/div/div/div[1]'))
                self.number_of_process += 1
                driver.switch_to.default_content()
                self.show(f'Report {self.number_of_process} feito com sucesso')

                if self.__test:
                    if rounds == self.number_of_process:
                        print(f'Fim do teste')
                        self.abort_bot(True)
                driver.refresh()
                self.show(f'Aguardando próximo report, que acontecerá em {duration/60} minuto(s).')
                sleep(duration)
        except(error.NoSuchElementException):
            self.verify()

    def abort_bot(self, cod=None, emergency=False):
        self.show('Encerrando processo')
        sleep(3)
        self.__driver.quit()
        if emergency:
            quit()

    def verify(self):
        if self.__test:
            self.show('[teste-mode] Verificando Barreira')
        driver = self.__driver
        target = self.__target
        try:
            if driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div'):
                if self.__test:
                    self.show('[teste-mode] Barreira Encontrada')
                driver.find_element_by_xpath(
                '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/a[1]').click()
                if self.__test:
                    self.show('[teste-mode] Barreira eliminada')
                wait(driver,5).until(lambda driver: driver.find_element_by_xpath('/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[1]/h1/a/div/svg'))
                if self.__test:
                    self.show('[teste-mode] Voltando ao perfil alvo')
                driver.get(f'https://www.twitter.com/{target}')
        except(error.NoSuchElementException):
            if self.__test:
                self.show('[teste-mode] barreira não detectada')
            pass

    def show(self, text='*'):
        text = text.title()
        print(text)

