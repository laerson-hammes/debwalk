# DebWalk

Uma simples classe para acompanhar o debug de um projeto, basta instanciar a classe Log() e chamar o método check(), passsando como argumento da função a mensagem que deseja printar juntamente com o **debug** desejado, esses podendo ser:

+ Errors.SUCCESS.name
+ Errors.FAIL.name
+ Errors.INFO.name

Repare que os elementos estão dentro de uma classe chamada Errors que transforma os elementos da mesma em um Enum...

Segue imagem da chamada completa:

<img src="https://github.com/laerson-hammes/debwalk/blob/main/img/use.png" alt="Modelo chamada" title="Modelo chamada">

Você pode obter o mesmo resultado com o seguinte comando no root do projeto:

> python -m main

Output:

<img src="https://github.com/laerson-hammes/debwalk/blob/main/img/run.png" alt="Resultado da chamada" title="Resultado da chamada">

Caso deseja rodar os testes você pode usar o coverage:

> python -m coverage run -m unittest discover

Após, reportar o resultado e ver o index:

<img src="https://github.com/laerson-hammes/debwalk/blob/main/img/report.png" alt="Coverage report" title="Coverage report">
