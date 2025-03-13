# <span style="color: #87BBA2">===   Modelagem de dados: aplicando a normalização   ===</span> <!-- omit in toc -->

# <span style="color: #87BBA2">INDICE</span> <!-- omit in toc -->
- [Aula XX: TituloAula](#aula-xx-tituloaula)
  - [Capitulo](#capitulo)


# <span style="color: #87BBA2">Normalização</span>

## PROJETO A SER NORMALIZADO
![etapas de um projeto](assets/etapas_projeto.png)

### O que é noramlização de dados
A normalização de dados é um processo fundamental na modelagem de bancos de dados que envolve organizar os campos e relações entre as tabelas de um banco de dados para reduzir a redundância e dependência de dados. Esse processo estrutura os dados de maneira a garantir que eles sejam armazenados de forma lógica, eficiente e sem duplicidades.

### Importância da Normalização de Dados
1. Redução de Redundância de Dados: A normalização elimina a duplicação de dados, reduzindo assim o espaço de armazenamento necessário e melhorando a eficiência do banco de dados. Menos redundância também significa que há menos dados para gerenciar e manter, o que simplifica as operações de atualização e manutenção.
2. Evitar Anomalias de Dados: A normalização ajuda a evitar anomalias que podem surgir durante operações de inserção, atualização ou exclusão. Por exemplo, se os dados não estão normalizados, atualizar um endereço de cliente em várias entradas pode levar a inconsistências se a atualização não for aplicada a todos os registros relevantes.
3. Melhoria da Integridade dos Dados: Ao separar os dados em tabelas apropriadas e estabelecer relações corretas entre elas, a normalização ajuda a manter a integridade dos dados. Ela impõe regras lógicas que os dados devem seguir, o que ajuda a prevenir a entrada de dados incorretos ou inválidos.
4. Otimização de Consultas: Um banco de dados bem normalizado é geralmente mais rápido e eficiente em responder a consultas, pois as tabelas são menores e mais focadas, o que reduz o tempo de busca e processamento de dados.
5. Facilitação da Escalabilidade: Bancos de dados normalizados são mais fáceis de expandir e modificar, o que é crucial para sistemas que necessitam evoluir constantemente para atender às mudanças nas necessidades dos negócios ou dos usuários.
6. Melhor Conformidade com Requisitos de Modelagem e Regulamentações: Em muitos casos, especialmente em setores regulados como saúde e finanças, manter a precisão e a confidencialidade dos dados é essencial e obrigatório por lei. A normalização ajuda a garantir que os dados sejam gerenciados de forma segura e conforme os padrões regulatórios.

Em resumo, a normalização é uma prática essencial para qualquer sistema de banco de dados que tenha por objetivo ser eficiente, confiável e escalável. Ela não só melhora o desempenho do banco de dados como também contribui para a precisão e a segurança dos dados armazenados.


### Quando devemos aplicar a normalização
Normalização é um conjunto de regras que visa :
- Evitar redundâncias
- Garantir a integridade dos dados

![tabela de analise](assets/tabela_de_analise.png)
Pontos que podemos observar na tabela:
- O id de estudante está sendo repetido nessa tabela, fazendo-o não ser elegivel para ser uma PK, uma vez que necessita-se de dados distinguiveis.
- Nomes de estudante e professor redundantes
  - Pois, o nome do professor sempre se repetirá quando um curso especifico for repetido também. Ou seja, se tiver duas entradas de Matemática, teremos duas entradas repetidas do nome do professor (no caso, "João Santos")

Com os casos acima mencionado, isso mostra que nossos dados não estão integros, pois, em um momento onde precisariamos atualizar o nome do professor ou do aluno, precisariamos garantir que todos os campos fossem atualizados. Com isso, não conseguimos garantir que todos os campos de fato estão condizentes, afetando a integridade.

## CONHECENDO A NORMALIZAÇÃO
Noramlização trata-se de um conjunto de regras que utilizamos e aplicamos em tabelas para saber se o projeto está ou não normalizado.

### Diretrizes
As **diretrizes informais**, como são conhecidas, são um conjunto de critérios que utilizamos para avaliar se um projeto está ou não normalizado. Nos baseamos nelas para definir a qualidade das tabelas do projeto.
- Chamamos as diretrizes de informais porque são critérios não obrigatórios, já que nem sempre conseguiremos aplicar todas as etapas da normalização. Essa aplicação depende das necessidades e do objetivo do projeto, de como os dados serão armazenados e processados, e assim por diante.

É importante entender que a normalização deve ser aplicada de acordo com o que o projeto precisa.

**As diretrizes informais são:**
1. Semantica clara e esquemas faceis
   1. Dados e visualizações fáceis de entender, permitindo saber as informações armazenadas dentro de cada tabela do projeto.
2. Evitar as redundâncias
   1. Evitar informações que se repetem
3. Prevenir a presença de tuplas nulas
   1. Evitar campos onde as informações podem não ser informadas durante a inserção de dados e buscar manter as tuplas sempre preenchidas
4. Evitar a aparição de tuplas falsas
   1. No momento de buscar essas informações, se o banco não estiver bem organizado, poderemos acabar gerando tuplas falsas no resultado das consultas.

### Dependencias (relacionamento entre atributos)
Além das diretrizes, temos os conceitos de dependencias e o relacionamento entre atributos, sendo um nível mais interno da modelagem. Antes, estavamos analisando algo do nivel de tabelas com tabelas, agora, estamos analizando interno a tabela, uma relação entre um atributo e outro. Chamamos isso de dependencia funcional, ou seja, como esses atributos se relacionam (dependem um do outro).

### Formas normais
Por fim, as formas normais são padrões que aplicaremos para entender se as tabelas e o projeto estão ou não normalizados.

## MAIS SOBRE FORMAS NORMAIS, DIRETRIZES E DEPENDENCIAS
A normalização de dados é um processo crucial em design de banco de dados para garantir que as tabelas sejam eficientemente organizadas e livres de redundâncias desnecessárias.

Este processo envolve a aplicação de um conjunto de regras, conhecidas como formas normais, que ajudam a estruturar os dados de maneira que reduzam problemas de integridade e otimizem o desempenho do banco de dados.

### Formas normais
As formas normais são um conjunto de critérios usados na normalização de banco de dados que ajudam a reduzir a redundância de dados e a evitar anomalias nas operações de inserção, atualização e exclusão. Elas são aplicadas para estruturar tabelas de maneira que as dependências entre os dados sejam lógicas e minimizem a duplicação de informações.

As formas normais são progressivas; cada forma normal constrói sobre a anterior e adiciona novos requisitos, começando pela Primeira Forma Normal e avançando até a Quinta Forma Normal, com algumas variantes como a Forma Normal de Boyce-Codd. Cada nível de forma normal aborda e resolve diferentes tipos de problemas estruturais em um banco de dados para melhorar a integridade e a eficiência dos dados armazenados.

### Diretrizes Informais
Além das formas normais formais, existem diretrizes informais que são critérios úteis para avaliar a qualidade das tabelas em um projeto. Essas diretrizes, embora não obrigatórias, são práticas recomendadas que podem melhorar significativamente o design do banco de dados:

Semântica clara com esquemas fáceis de explicar: As tabelas devem ser projetadas de forma que sejam intuitivas e fáceis de entender, com esquemas que refletem claramente o domínio do problema.

Evitar informações redundantes: As tabelas devem ser projetadas para minimizar a repetição de informações, o que reduz o espaço de armazenamento necessário e simplifica a manutenção dos dados.

Evitar possibilidade de valores NULL nas tuplas: Projetar tabelas de maneira que minimize campos vazios pode ajudar a garantir a completude dos dados e simplificar consultas e análises.

Evitar o surgimento de tuplas falsas: Assegurar que todas as combinações de dados inseridos em tabelas sejam válidas e significativas dentro do contexto do domínio de aplicação.

### Dependências Funcionais
As dependências funcionais são um conceito chave na normalização de dados, descrevendo como os atributos em uma tabela estão relacionados uns aos outros.

Uma dependência funcional ocorre quando um atributo (ou conjunto de atributos) é capaz de determinar unicamente outro atributo. Por exemplo: em um banco de dados de clientes, o CPF pode determinar unicamente o Nome do cliente. Este conceito é fundamental para entender como separar dados em tabelas distintas de forma a manter a integridade dos dados e reduzir redundâncias.

Entender e aplicar essas diretrizes e conceitos é essencial para criar bancos de dados robustos, eficientes e de fácil manutenção. A normalização não apenas melhora o desempenho das operações de banco de dados, mas também facilita a expansão e adaptação do sistema a novos requisitos ao longo do tempo.

## APLICANDO A NORMALIZAÇÃO

Aplicando a normalização, separamos os dados da primeira tabela apresentada em várias tabelas

### Tabela de Estudante
| id_estudante | nome_estudante |
| :----------- | :------------- |
| 1            | Ana Silva      |
| 2            | Carlos Andrade |

O primeiro passo seria tirar os dados das pessoas estudantes e centralizá-los em uma única tabela. Nesta, temos as duas pessoas estudantes cadastradas, Ana Silva e Carlos Andrade.

Esse formato evita a redundância, afinal, não teremos a repetição do nome das pessoas estudantes. Além disso, podemos inserir mais dados de estudantes, além do nome, pois essa tabela é dedicada apenas às pessoas estudantes.

### Tabela de Cursos
| id_curso | nome_curso | nome_professor |
| :------- | :--------- | :------------- |
| 101      | Matemática | João Santos    |
| 102      | História   | Maria Pereira  |

Nela, também poderíamos adicionar a informação das pessoas docentes, como o nome, por exemplo. Isso seria possível, pois outro ponto importante do projeto é seguir as regras de negócio.

A regra de negócio diz que, para cada curso, só podemos ter uma pessoa docente específica. Sabemos que não teremos a repetição de informações da pessoa docente, porque ela só pode lecionar em um único curso.

Saber as regras de negócio, como os dados se relacionarão e como serão armazenados ajuda a normalizar e modelar o projeto. Nesse caso, sabendo da regra de negócio que relaciona docentes a cursos, podemos adicionar todas as informações dentro da mesma tabela ao invés de criar duas tabelas separadas para essas duas entidades.

Poderíamos separar essas informações, colocando a pessoa docente em outra tabela, mas nesse caso, teríamos que entender como esses dados seriam buscados e usados no dia a dia. Para o exemplo que trouxemos, a pessoa docente precisa estar dentro de curso, porque ao buscar o curso, precisamos saber o nome da pessoa docente.
> Apesar de ter sido seguido essa estrutura, acredito que é **totalmente recomendado** separar as tabelas mesmo que a relação fosse (1:1), pois, isso tornaria o banco mais sematinco, mais organizado e passivel a ser escalado, caso queiramos acrescentar mais informações em professores (como sua inscrição, formação e etc)

### Tabela Registro de Notas
| id_estudante | id_curso | nota |
| :----------- | :------- | :--- |
| 1            | 101      | 85   |
| 1            | 102      | 90   |
| 2            | 101      | 88   |

Nela, teríamos uma chave primária composta. Como mencionando antes, só o ID da pessoa estudante não pode ser considerado uma chave primária, porque ele se repete. Mas quando fazemos a união entre dois campos, podemos ter essa chave primária.

Criamos essa chave composta considerando a regra de negócio na qual cada estudante só pode se matricular em um único curso por vez. Não podemos, por exemplo, ter a mesma pessoa estudante matriculada no mesmo curso, mais de uma vez.

Isso garante que a combinação desses dois campos sempre será única.

# <span style="color: #87BBA2">1º e 2º forma normal</span>

## ATRIBUTO MULTIVALORADO E COMPOSTO
Utilizando como exemplo o modelo lógico da FlexEmpresta, avaliaremos seu atributos e suas dependencias
> Precisamos entender se os atributos também estão corretos internamente nas tabelas, se eles fazem sentido, e se há ou não uma dependência entre esses atributos.

### Dependencia Funcional
Como os atributos se relacionam entre si.

Para verificar a dependencia funcional, utilizamos o conceito de **Determinante x Determinado**
- Representação: **Determinante ---> Determinado**

Por exemplo: na tabela de clientes (TabelaClientes), temos diversas informações, sendo uma delas o ID (id_cliente). O ID é único e servirá para identificar de forma exclusiva cada cliente.
- Cada cliente que for inserido na tabela de clientes receberá um ID único. Logo, essa informação não pode se repetir na tabela.

Nessa tabela, temos a informação de que o id_cliente é um **atributo determinante**.
- Ou seja, **através dele, conseguimos identificar o restante das informações de clientes.**
- No exemplo acima, o Nome, o CPF e o EndereçoCompleto, por exemplo, **são determinados pelo id_cliente**. Chamamos essa relação de determinante e determinado, pois através do determinante, conseguimos saber o restante dos valores

Porém, não são apenas as chaves primárias que podem ser consideradas determinantes.
- Por exemplo: o `CPF` não é uma chave primária, mas poderia ser, pois o `CPF` é único, ou seja, cada pessoa só pode ter um `CPF`. Sendo assim, **através do `CPF`, conseguimos identificar o `Nome` do cliente.**

### Atributos chaves e não chaves
Agora que já conhecemos o conceito de dependência, que é muito importante quando trabalhamos com a normalização de dados, vamos avaliar as tabelas com mais calma.

Todas elas possuem chave primária (primary key — PK), e entendemos anteriormente que esse é um campo útil e obrigatório em todas as tabelas. As formas normais, pelo menos a primeira, a segunda e a terceira, serão baseadas no campo de chave primária. Portanto, é um campo muito importante e utilizaremos ele como base neste primeiro momento.

Além de todas as tabelas possuírem o campo de ID, todas elas possuem o que chamamos de FK (foreign key), ou de chave estrangeira, que é justamente o campo que identifica com qual outra tabela determinada tabela se relaciona. Por exemplo: sabemos que a TabelaClientes tem um relacionamento com a TabelaColaboradores através da FK id_colaborador.