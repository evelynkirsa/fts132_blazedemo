Feature: Compra de passagem Aerea
  # Descreve a compra pelo site  Blazedemo.com
  # E2E = End To End = Inicio ao fim, etc
  Scenario: De Sao paulo a Roma
    Given que acesso o site Blazemo
    When Quando seleciono a cidade de origem como "São Paolo"
    And seleciono a cidade destino como "Rome"
    And clico em "Find Flights"
    Then sou direcionado para  a pagina selecao de voos
    When seleciono o primeiro voo
    Then sou direcionado para a pagina de pagamento
    When preencho os dados para pagamento
    And clico no botao Purchase Fligth
    Then sou direcionado para a pagina de confirmacao


  Scenario: De Sao paulo a Roma Compacto
    Given que acesso o site Blazemo
    When Quando seleciono de "São Paolo" para "Rome"
    Then sou direcionado para  a pagina selecao de voos
