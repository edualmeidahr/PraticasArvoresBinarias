# Impacto do Desbalanceamento em Árvores Binárias

## Comparação de Árvores Balanceadas e Desbalanceadas

### 1. Árvore Desbalanceada
#### **Características:**
- Os nós são inseridos sequencialmente, criando uma estrutura similar a uma **lista ligada**.
- Cada nó tem apenas um único filho (esquerdo ou direito).
- O **caminho mais longo** é igual ao número total de nós na árvore.

#### **Impactos:**
- O **nível máximo (profundidade)** é proporcional ao número de nós, resultando em alto custo computacional para operações como busca, inserção e remoção.
- Operações têm custo **O(n)** (linear), no pior caso.
- Exemplo:
  - Inserindo `[1, 2, 3, 4, 5, 6, 7]` na árvore, o nível máximo será **7** e o caminho mais longo será `[1, 2, 3, 4, 5, 6, 7]`.

#### **Analogia:**
- É como subir uma escada onde todos os degraus estão alinhados verticalmente. Você precisa subir todos os degraus sem atalhos.

---

### 2. Árvore Balanceada
#### **Características:**
- Os nós são distribuídos de forma a manter a profundidade dos ramos equilibrada.
- A profundidade máxima cresce logaritmicamente em relação ao número de nós.

#### **Impactos:**
- O **nível máximo** é significativamente menor, garantindo melhor eficiência nas operações.
- Operações têm custo **O(log n)** no pior caso.
- Exemplo:
  - Inserindo `[4, 2, 5, 1, 7, 6, 3]` na árvore, o nível máximo será **4** e o caminho mais longo será `[4, 5, 7,6]`.

#### **Analogia:**
- É como subir uma escada organizada em formato de pirâmide, permitindo alcançar o topo com menos passos.

---

### 3. Comparação: Impacto do Desbalanceamento

| **Critério**          | **Árvore Desbalanceada**     | **Árvore Balanceada**         |
|-----------------------|-----------------------------|--------------------------------|
| **Nível máximo**      | Igual ao número de nós (n)  | Cresce logaritmicamente (log n) |
| **Caminho mais longo**| Inclui todos os nós         | Muito menor e mais eficiente  |
| **Custo de busca**    | O(n)                        | O(log n)                      |
| **Custo de inserção** | O(n)                        | O(log n)                      |
| **Custo de remoção**  | O(n)                        | O(log n)                      |

#### **Impacto no Desempenho:**
- Árvores desbalanceadas podem desperdiçar até **39% de desempenho computacional** devido ao aumento linear do custo de operações como busca e remoção.
- Em uma árvore com 100 nós:
  - **Árvore Balanceada**: A busca exige cerca de **7 comparações**.
  - **Árvore Desbalanceada**: A busca pode exigir até **100 comparações**.

---

### 4 . Cálculo da Depreciação

Para analisar o impacto do desbalanceamento na profundidade média da árvore, realizamos os cálculos baseados nas profundidades dos nós:

#### **Árvore Desbalanceada**
- **Profundidades dos nós:**
  - Nível 1: Nó 1
  - Nível 2: Nó 2
  - Nível 3: Nó 3
  - Nível 4: Nó 4
  - Nível 5: Nó 5
  - Nível 6: Nó 6
  - Nível 7: Nó 7
- **Soma das profundidades:**  
  \( 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28 \)
- **Profundidade média:**  
  \( \frac{28}{7} = 4 \)

#### **Árvore Balanceada**
- **Profundidades dos nós:**
  - Nível 1: Nó 4
  - Nível 2: Nós 2 e 5
  - Nível 3: Nós 1, 3 e 7
  - Nível 4: Nós 6
- **Soma das profundidades:**  
  \( 1 + 2 + 2 + 3 + 3 + 3 + 4 = 18 \)
- **Profundidade média:**  
  \( \frac{18}{7} \approx 2,57 \)

#### **Cálculo do Percentual de Depreciação**
- Diferença entre as profundidades médias:  
  \( 4 - 2,57 = 1,43 \)
- Percentual de redução devido ao balanceamento:  
  \( \left( \frac{1,43}{4} \right) \times 100 \approx 35,75\% \)

#### **Interpretação**
- A árvore balanceada apresenta uma redução de aproximadamente **35,75%** na profundidade média em comparação à árvore desbalanceada. Esse resultado evidencia a eficiência estrutural do balanceamento, reduzindo o impacto do desbalanceamento natural e otimizando as operações.


### 5. Caminho Mais Longo
#### **Definição:**
O caminho mais longo é a sequência de nós que conecta a raiz à folha mais profunda da árvore. Ele é um indicador direto do grau de desbalanceamento da árvore.

- **Árvore Desbalanceada**: O caminho mais longo inclui todos os nós da árvore.
- **Árvore Balanceada**: O caminho mais longo é muito menor, representando uma estrutura mais eficiente.

#### **Exemplo Visual:**

- **Desbalanceada**: `[1, 2, 3, 4, 5, 6, 7]`
- **Balanceada**: `[4, 5, 7,6]`

---

### 6. Conclusão
- Árvores desbalanceadas apresentam crescimento **linear** na profundidade e nos custos de operações, tornando-as ineficientes para grandes conjuntos de dados.
- Árvores balanceadas mantêm o desempenho **logarítmico**, garantindo eficiência mesmo com muitas inserções ou buscas.
