<h1> Atividade 3 - Particionamento por classes de equivalência </h1>
<p>Defina classes de equivalência e um conjunto de casos de teste adequado para o critério particionamento por classes de equivalência para o programa com a seguinte descrição:</p>
<p>O programa deve determinar se um identificador é válido ou não em Silly Pascal (uma variante do Pascal). Um identificador válido deve começar com uma letra e conter apenas letras ou dígitos. Além disso, deve ter no mínimo um caractere e no máximo seis caracteres de comprimento.</p>

<p>Implemente a função isValid(string): boolean que recebe uma string e retorna verdadeiro se a string pode ser um identificador de Silly Pascal e falso caso contrário. Crie os testes para essa função.</p>
<h2>Descrição Solução:</h2>
<p>A linguagem escolhida foi python com a biblioteca pytest utilizando o método de TDD.</p>
<h2>Testes realizados:</h2>
<ul>
    <li>test_starts_with_a_letter: testa se o identificador começa com uma letra</li>
    <li>test_contains_only_letters_or_digits: testa se o identificador contém somente letras ou digitos</li>
    <li>test_string_length: testa se o identificador possui tamanho entre 1 e 6</li>
    <li>test_null_string: testa se a string é None</li>
</ul>
