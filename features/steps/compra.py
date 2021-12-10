import time

from behave import given, when, then
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#precisa sempre importar a classe em environment (onde estão o  antes e o depois do teste)
from features import environment

# método executado antes da feature e serve para chamar os passos seguintes
def before_feature(context, feature):
    if 'compra_passagem' in feature.tag:
        context.execute_steps(
            # Pode ser incluido outras açoes
        )

@given(u'que acesso o site Blazedemo')
def step_impl(context):
    context.driver.get('https://blazedemo.com')
    print('Passo 1 - Acessou o site Blazedemo')
    time.sleep(30)   #espera bruta - sempre remover

@when(u'Quando seleciono a cidade de origem como "{origem}"')
def step_impl(context, origem):
    # Mapeia o combo com as cidades de origem
    combo_origem = context.driver.find_element(By.NAME, 'fromPort')

    #Cria um objeto para permitir selecionar as opções do combo
    objeto_origem = Select(combo_origem)

    # Seleciona o elemento no combo
    objeto_origem.select_by_visible_text(origem)

    print('Passo 2 - Selecionou a cidade de origem')

@when(u'seleciono a cidade destino como "{destino}"')
def step_impl(context,destino):
    # Mapeia o combo com as cidades de origem
    combo_origem = context.driver.find_element(By.NAME, 'toPort')

    #Cria um objeto para permitir selecionar as opções do combo
    objeto_origem = Select(combo_origem)

    # Seleciona o elemento no combo
    objeto_origem.select_by_visible_text(destino)
    time.sleep(30)  # espera bruta - sempre remover

    print('Passo 3 - Selecionou a cidade de destino')

@when(u'clico em "Find Flights"')
def step_impl(context):

    print('Passo 4 - Clicou no botão Find Fligths')

@then(u'sou direcionado para  a pagina selecao de voos')
def step_impl(context):
    print('Passo 5 - Direcionou para a pagina de voos')

@when(u'seleciono o primeiro voo')
def step_impl(context):
    print('Passo 6 - Selecionou primeiro voo')

@then(u'sou direcionado para a pagina de pagamento')
def step_impl(context):
    print('Passo 7 - Direcionou para a pagina de pagamento ')

@when(u'preencho os dados para pagamento')
def step_impl(context):
    print('Passo 8 - Preencheu os dados')

@when(u'clico no botao Purchase Fligth')
def step_impl(context):
    print('Passo 9 - Clicou no boyão Purchase Fligth')

@then(u'sou direcionado para a pagina de confirmacao')
def step_impl(context):
    print('Passo 10 - Direcionou para a pagina de confirmação')


@when(u'Quando seleciono de "São Paolo" para "Rome"')
def step_impl(context):
        print('Passo 2c - Selecinou a cidade origem e destino')
