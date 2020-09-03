<h1> Atividade 3 - Particionamento por classes de equivalência </h1>
<p>Defina classes de equivalência e um conjunto de casos de teste adequado para o critério particionamento por classes de equivalência para o programa com a seguinte descrição:</p>
<p>O programa deve determinar se um identificador é válido ou não em Silly Pascal (uma variante do Pascal). Um identificador válido deve começar com uma letra e conter apenas letras ou dígitos. Além disso, deve ter no mínimo um caractere e no máximo seis caracteres de comprimento.</p>

<p>Implemente a função isValid(string): boolean que recebe uma string e retorna verdadeiro se a string pode ser um identificador de Silly Pascal e falso caso contrário. Crie os testes para essa função.</p>
<h2>Descrição Solução:</h2>
<p>A linguagem escolhida foi python com a biblioteca pytest utilizando o método de TDD.</p>
<h2>Testes realizados:</h2>
<ul>
    <li>test_not_a_integer: testa se o número não for um integer</li>
    <li>test_negative_integer: testa se o número for negativo</li>
    <li>test_multiple_three: testa se o número é múltiplo de 3</li>
    <li>test_multiple_five: testa se o número é múltiplo de 5</li>
    <li>test_multiple_five_and_three: testa se o número é múltiplo de 3 e 5</li>
    <li>test_not_multiples_five_or_three: testa se o número não for múltiplo de 3 ou 5</li>
</ul>
