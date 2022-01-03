from selenium import webdriver

#Inicio
def before_all(context):    #Antes de tudo
    #Declarar o Selenium, instanciar como o navegador e apontar o driver
    context.driver = webdriver.Chrome('C:/Users/User/PycharmProjects/fts132_blazedemo/drivers/chromedriver.exe')

    #Maximizar a janela do navegador
    context.driver.maximize_window()

    # Define uma espera para todos os elementos do script
    context.driver.implicitly_wait(30)

    print('Passo a - Antes de tudo')

#fim
def after_all(context): #Depois de tudo

    #Desigar / Destruir o objeto do Selenium
    context.driver.quit()

    print('passo z - Depois de tudo')
'''
#Bloco executado ao final de cada site
def after_step(context, step):
    print()
'''