# Testes de Hipóteses para Média e para Proporção e Testes de Hipóteses para Diferença entre Médias

Na tomada de decisões em engenharia, é comum aceitar ou rejeitar afirmações baseadas em parâmetros. Essas afirmações são chamadas de hipóteses, e a tomada de decisão é chamada de teste de hipótese.

Existem duas formas de hipóteses: a primeira é a hipótese nula, onde as observações e as ações são devidas ao acaso; a segunda é a hipótese alternativa, que sugere que as ações não podem ser explicadas pelo acaso ou que há uma diferença significativa entre as observações.

Por exemplo, um médico que quer testar um novo tratamento pode criar a hipótese nula (H0) de que o tratamento é ineficaz e as melhorias observadas são devidas ao acaso. A hipótese alternativa (H1) sugere que as melhorias observadas não podem ser explicadas pelo acaso. Na estatística, a hipótese nula é representada por H0 e é simbolizada por um sinal de igualdade, `≤` ou `>`. A hipótese alternativa é representada por H1, e só será aceita se a H0 for rejeitada.

Os testes de hipóteses podem ser bilaterais, monocaudais ou unilaterais, dependendo da afirmação levantada. Um teste bilateral é usado quando a afirmação inclui termos como `maior que`, `menor que`, `superior a`, `excede` ou `no mínimo`. Nesse caso, o valor esperado pode estar tanto acima quanto abaixo do valor observado.

Por outro lado, um teste monocaudal é usado quando a afirmação se refere apenas a uma direção, como "maior" ou "menor". Já um teste unilateral é usado quando a hipótese alternativa sugere uma mudança significativa, independentemente da direção. Por exemplo, um teste unilateral poderia ser usado para verificar quanto tempo uma pessoa leva para percorrer uma determinada distância, independentemente de ser mais rápido ou mais lento.


<center>
$Z = \frac{\bar{X} - \mu}{\sqrt{\sigma^2/n}}$
</center>


O "z" é obtido a partir da fórmula e comparado com o valor crítico obtido a partir da tabela de distribuição normal. Se o valor de "Z" for maior que o valor tabelado, logo, a hipótese nula é descartada. Basicamente, esse valor crítico é um valor mínimo que precisa ser superado para que a hipótese nula seja rejeitada.

```
O valor crítico pode ser comparado ao tempo de cozimento de um bolo. A hipótese nula diz que para fazer um bolo leva 30 minutos (valor crítico) e a hipótese alternativa sugere que o tempo pode ser superior a 30 minutos ou inferior a 30 minutos. Se realizarmos os testes e descobrirmos que o tempo é superior a 30 minutos (valor crítico), logo, a hipótese nula é rejeitada.
```