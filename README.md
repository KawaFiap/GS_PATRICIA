# GS_PATRICIA

 GS da prof patricia
 
Esse código tem como objetivo monitorar o consumo de energia ao longo de vários dias, comparando com uma meta definida de 150 kWh por dia. Ele calcula a média de consumo, o maior e o menor consumo registrado, e informa quantos dias ficaram acima ou abaixo da meta. Aqui está um passo a passo de como usá-lo e o que ele faz:

### **Explicação do código**
1. **Entradas:**
   - O programa começa pedindo para o usuário informar o número de dias que ele vai monitorar o consumo de energia.
   - Para cada dia, o programa pede o consumo de energia em kWh.

2. **Processamento:**
   - **Soma do consumo:** O programa soma o consumo de todos os dias para calcular a média no final.
   - **Contagem de dias acima e abaixo da meta:** Ele verifica, para cada dia, se o consumo foi maior ou igual a 150 kWh (meta). Se sim, conta como "acima da meta", caso contrário, conta como "abaixo da meta".
   - **Maior e menor consumo:** Durante o monitoramento, ele também armazena o maior e o menor consumo registrados.

3. **Saídas:**
   - **Relatório final:** Ao final, o programa informa:
     - Quantos dias cumpriram a meta (ficaram acima de 150 kWh).
     - Quantos dias ficaram abaixo da meta.
     - A média do consumo de energia.
     - O maior e o menor consumo registrado durante o período.

### **Passo a Passo para Usar o Código**

1. **Execute o código:** Rode a função `monitorar_consumo()` em um ambiente Python, seja no seu computador ou em uma IDE online.
   
2. **Informe o número de dias:** O programa vai pedir para você digitar a quantidade de dias para monitorar. Por exemplo:
   ```
   Digite a quantidade de dias: 5
   ```
   Aqui você informou que vai monitorar o consumo durante 5 dias.

3. **Informe o consumo de energia para cada dia:** O programa vai pedir o consumo de energia para cada um dos dias. Para cada dia, você deverá informar um valor em kWh. Por exemplo:
   ```
   Insira seu consumo de energia no dia 1: 120
   Insira seu consumo de energia no dia 2: 180
   Insira seu consumo de energia no dia 3: 150
   Insira seu consumo de energia no dia 4: 130
   Insira seu consumo de energia no dia 5: 160
   ```

4. **Resultado final:** Após você fornecer os consumos de todos os dias, o programa vai exibir um resumo, informando:
   - **Se a meta foi atingida em todos, nenhum ou apenas alguns dias.**
   - **A média de consumo de energia.**
   - **O maior e o menor consumo registrado.**
   
   Por exemplo, com os valores acima, a saída seria algo assim:
   ```
   3 dias cumpriram a meta e 2 dias não cumpriram a meta.
   A média de consumo foi de 148.00 kWh. O maior consumo foi de 180 kWh e o menor consumo foi de 120 kWh.
   ```

### **Resumo do que o código faz:**
- Conta quantos dias cumpriram ou não a meta de consumo de 150 kWh.
- Calcula a média de consumo de energia.
- Mostra o maior e o menor consumo de energia.
- Exibe um resumo final com esses dados.

Esse código é útil para analisar o padrão de consumo de energia ao longo de vários dias e verificar como ele se compara a uma meta estabelecida.
