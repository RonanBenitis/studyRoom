# <span style="color: #87BBA2">===   Modelagem de dados: identificando entidades, atributos, relacionamentos   ===</span> <!-- omit in toc -->

# <span style="color: #87BBA2">INDICE</span> <!-- omit in toc -->
- [Aula XX: TituloAula](#aula-xx-tituloaula)
  - [Capitulo](#capitulo)

# <span style="color: #87BBA2">Conhecendo o projeto</span>

## PROJETO A SER DESENVOLVIDO
Utilizaremos a modelagem de dados
- A modelagem de dados se constitue de diversas etapas que serão utilizadas para identificar os dados que queremos armazenar e padronizar através do desenho de fluxogramas.

## ALINHAMENTO DO TIME
Um dos pontos é o uso do mesmo material referencial. É essencial utilizar os mesmos conceitos para poder utilizá-los na criação de modelos conceituais e lógicos nesse fluxo de modelagem de dados.

### Problemas identificados no material de consumo
- Repetição de informação
  - Os dados de um mesmo cliente é replicado em varias linhas, ou seja, se precisar atualizar o cadastro deste cliente, precisará atualizar em todas a linhas ao qual ele aparece
- Informações estão todas juntas
  - Informações de clientes entra em score de crédito, que entra em tipo de conta de por aí vai, tudo em uma mesma linha
- Campos de mesmo nome
  - Temos dois campos chamado "Status". Vendo os valores dos dados, observamos que um é referente ao pagamento e outro é referente ao empréstimo, mas, indo apenas pelo titulo, gera-se confusão.

### O que podemos fazer
- Criar padronização de dados
- Separação e organização de dados
  - O que é cliente
  - O que é score
  - Informações bancárias e etc

## IMPOTANCIA DO ALINHAMENTO ENTRE TIMES

Desenvolver um projeto de banco de dados utilizando modelagem de dados é uma tarefa complexa que requer uma compreensão clara dos requisitos do sistema, dos processos de negócio e das necessidades dos usuários finais. O alinhamento de toda a equipe durante este processo é crucial, pois cada membro pode ter perspectivas únicas e contribuições essenciais para o sucesso do projeto. Aqui estão os principais motivos pelos quais é importante manter todos os membros do time alinhados ao desenvolver um projeto de banco de dados:

1 - Compreensão compartilhada dos requisitos

Um projeto de banco de dados bem-sucedido começa com um entendimento claro dos requisitos do negócio. O alinhamento entre os membros da equipe garante que todos entendam os objetivos do projeto, os dados que precisam ser capturados e como esses dados serão usados. Isso ajuda a evitar mal-entendidos e a garantir que o banco de dados atenda às necessidades do negócio de forma eficaz.

2 - Consistência no design

Quando todos na equipe estão alinhados, o design do banco de dados tende a ser mais consistente. Isso inclui a nomenclatura padronizada de tabelas e campos, a aplicação consistente de normas de normalização e a implementação uniforme de regras de negócio. A consistência facilita a manutenção, o desenvolvimento e a escalabilidade futura do banco de dados.

3 - Eficiência na implementação

O alinhamento da equipe reduz a duplicação de esforços e aumenta a eficiência. Com todos os membros da equipe trabalhando com o mesmo conjunto de expectativas e diretrizes, menos tempo é desperdiçado corrigindo erros ou redefinindo aspectos do projeto. Isso não apenas acelera o desenvolvimento, mas também ajuda a manter o projeto dentro do cronograma e do orçamento.

4 - Decisões mais informadas

Em um ambiente colaborativo, as decisões sobre o design e a implementação do banco de dados são geralmente mais informadas e bem pensadas. A diversidade de conhecimentos e experiências na equipe pode levar a soluções mais inovadoras e eficazes, reduzindo a probabilidade de problemas futuros.

5 - Facilidade de manutenção

Um banco de dados que é desenvolvido com a contribuição de toda a equipe tende a ser mais fácil de manter. Isso ocorre porque as decisões tomadas durante a fase de design são mais prováveis de considerar todos os aspectos do uso do banco de dados, incluindo a manutenção rotineira, a atualização de dados e a escalabilidade.

6 - Melhor adoção pelo usuário final

Quando o desenvolvimento do banco de dados é alinhado com as necessidades dos usuários finais (que podem ser representadas pela equipe), a adoção pelo usuário tende a ser mais alta. Um sistema que atende bem às necessidades dos usuários finais é mais provável de ser aceito e utilizado efetivamente.

7 - Redução de erros e riscos

Alinhamento e comunicação eficazes ajudam a identificar e resolver problemas potenciais mais cedo no processo de desenvolvimento. Isso minimiza o risco de erros significativos que poderiam ser caros e demorados para corrigir após o banco de dados estar em produção.

Manter todos os membros da equipe alinhados durante o desenvolvimento de um projeto de banco de dados é essencial para garantir que o resultado final seja robusto, eficiente e eficaz. A colaboração e o compromisso com objetivos comuns permitem não apenas um desenvolvimento mais suave, mas também um produto final que realmente suporta as operações e estratégias de negócio da organização.

## MODELO CONCEITUAL

### Conceito do Minimundo
> O minimundo é uma porção do mundo real, ou seja, uma parte do nosso todo.

Suponha que vamos construir um projeto para uma empresa bancária, como um banco. Normalmente, em um banco físico, existem clientes, gerência e parte de atendimento. Mas, muitas vezes, também podemos ter uma lanchonete dentro de um banco. A lanchonete não é relevante para a modelagem.

Por isso, devemos construir um minimundo apenas com o que é importante para o nosso projeto.

Os dados para construção do minimundo vêm do levantamento de requisitos.

### Levantamento de requisitos
No levantamento de requisitos, iremos reunir pontos importantes que precisam estar presentes no projeto.

É um dos momentos mais importantes quando vamos desenvolver um projeto, porque é quando teremos o contato com a clientela para entender suas necessidades. Por exemplo, uma entrevista com gerência, stakeholders (pessoas interessadas no projeto), pessoas colaboradoras e pessoas que vão usar o sistema para entender exatamente quais as necessidades do dia a dia.

Por meio do levantamento de requisitos, vamos conhecer o todo do nosso projeto para continuar o desenvolvimento do minimundo.

### Modelo conceitual (Diagrama de Chen ou DER - Modelo de Entidade e Relacionamento)
Depois que fazemos o levantamento de requisitos, vamos para o primeiro modelo, que é justamente o modelo conceitual.

No modelo conceitual, vamos desenvolver o nosso primeiro diagrama. Também é a etapa onde conheceremos o projeto e as regras de negócio, ou seja, começaremos a descrever quais são os dados que queremos armazenar.

## MINIMUNDO, LEVANTAMENTO DE REQUISITOS E MODELO CONCEITUAL NO CONTEXTO DE UMA BIBLIOTECA

### Minimundo
O conceito de Minimundo refere-se a uma parte específica do mundo real que é relevante para o sistema que está sendo desenvolvido. Imagine que você está construindo um sistema para uma biblioteca; o minimundo incluiria coisas como livros, empréstimos, leitores e funcionários, mas não incluiria elementos irrelevantes como o café vendido na cafeteria ao lado. O minimundo ajuda a definir claramente o escopo do que será incluído no sistema de banco de dados.

### Levantamento de Requisitos
O Levantamento de Requisitos é o processo de coletar informações sobre o que os usuários precisam e esperam do sistema. No contexto da biblioteca, isso poderia envolver entender como os leitores gostariam de pesquisar livros, quais informações sobre os livros são importantes (como título, autor, gênero), e como os funcionários gerenciam os empréstimos. Esse processo é crucial porque define as funcionalidades que o sistema precisa suportar e influencia diretamente como o banco de dados será projetado.

### Modelo Conceitual (Diagrama de Chen ou DER - Modelo de Entidade e Relacionamento)
Após definir o minimundo e coletar os requisitos, o próximo passo é criar um Modelo Conceitual. Este modelo é uma representação visual de alta abstração de como os dados no sistema são organizados. Ele usa elementos como entidades (objetos do mundo real como 'Livro' ou 'Leitor'), atributos (propriedades das entidades como 'Título do Livro' ou 'Nome do Leitor') e relacionamentos (como 'empresta' entre 'Leitor' e 'Livro'). O modelo conceitual é geralmente criado usando um Diagrama Entidade-Relacionamento (DER), que ajuda a visualizar como os diferentes elementos estão interconectados.

### Conclusão
Esses três componentes — Minimundo, Levantamento de Requisitos e Modelo Conceitual — são fundamentais na modelagem de dados porque juntos eles garantem que o sistema de banco de dados será bem projetado, funcional e capaz de atender às necessidades dos usuários. Ao começar com uma compreensão clara do minimundo, passando por uma coleta meticulosa de requisitos, até a criação de um modelo conceitual eficaz, os desenvolvedores podem construir bases de dados robustas e eficientes que apoiam os processos e operações críticas de negócios.

# <span style="color: #87BBA2">Criando entidades</span>

## LEVANTAMENTO DE REQUISITOS

### Abstração
Após o levantamento de requisitos, é fundamental aplicar o conceito de abstração. Esse princípio consiste em identificar e isolar os elementos essenciais para o nosso projeto, ignorando detalhes irrelevantes.

Por exemplo, ao modelar os dados dos clientes, sabemos que podem ser pessoa física ou pessoa jurídica. No caso de uma pessoa física, diversas informações poderiam ser armazenadas, como nome, CPF e endereço. No entanto, características como cor do cabelo, hobbies ou cor dos olhos não são relevantes para a empresa FlexEmpresta.

Portanto, a abstração nos ajuda a focar apenas nos dados necessários para o projeto, garantindo um modelo mais eficiente e alinhado aos objetivos do sistema.

A **abstração** envolve tanto **isolar os elementos essenciais quanto identificar pontos em comum dentro de um contexto**.

Por exemplo, ao modelar um sistema para clientes, percebemos que tanto uma pessoa física quanto uma pessoa jurídica compartilham atributos comuns, como nome, telefone e endereço. Já os atributos específicos, como CPF (para pessoa física) e CNPJ (para pessoa jurídica), podem ser tratados separadamente.

Dessa forma, a abstração permite generalizar conceitos para facilitar a organização dos dados e evitar redundâncias, ajudando na criação de estruturas mais reutilizáveis e eficientes

## SOBRE MER E DER

Na modelagem de dados, dois conceitos fundamentais que frequentemente aparecem são o Modelo Entidade-Relacionamento (MER) e o Diagrama Entidade-Relacionamento (DER). Esses conceitos são vitais para planejar e visualizar como os dados serão organizados e interagirão em um sistema de banco de dados. Vamos explorá-los de forma simplificada.

**Modelo Entidade-Relacionamento (MER)**

O Modelo Entidade-Relacionamento (MER) é uma abordagem teórica usada para descrever e especificar a estrutura de dados de um sistema de banco de dados. O MER ajuda a identificar os dados que devem ser armazenados no banco de dados e a definir as relações entre esses grupos de dados. No MER, os dados são organizados em entidades, atributos e relacionamentos:

Entidades: São objetos ou conceitos do mundo real que possuem dados que precisam ser armazenados. Exemplos de entidades podem ser 'Cliente', 'Pedido', ou 'Produto'.
Atributos: São as propriedades ou características de uma entidade. Por exemplo, a entidade 'Cliente' pode ter atributos como 'Nome do Cliente', 'Endereço' e 'Telefone'.
Relacionamentos: Descrevem como as entidades estão conectadas entre si e interagem. Por exemplo, um relacionamento entre 'Cliente' e 'Pedido' pode ser descrito como um cliente que 'realiza' um pedido.

**Diagrama Entidade-Relacionamento (DER)**

O Diagrama Entidade-Relacionamento (DER) é a representação gráfica do MER. O DER utiliza um conjunto de símbolos gráficos como retângulos, losangos e linhas para representar entidades, relacionamentos e atributos, respectivamente. O objetivo do DER é fornecer uma visualização clara e compreensível da estrutura do banco de dados, facilitando a compreensão das relações entre os dados, mesmo para aqueles sem conhecimento técnico profundo.

Por exemplo, num DER:

- Retângulos representam as entidades.
- Losangos representam os relacionamentos.
- Oval representa os atributos.
- Linhas conectam entidades com seus atributos e relacionamentos.

**Importância do MER e do DER**

- Comunicação e Planejamento: MER e DER são ferramentas essenciais para comunicar a estrutura de dados proposta entre os desenvolvedores e stakeholders do projeto, incluindo analistas de sistemas, gerentes de projeto e clientes. Eles facilitam a discussão e o planejamento antes da implementação do banco de dados.
- Organização e Design: Ajudam na organização dos dados de forma lógica, garantindo que todas as informações necessárias sejam capturadas e corretamente interligadas.
- Prevenção de Erros: Usar MER e DER na fase de design pode ajudar a identificar e corrigir potenciais erros de modelagem, como redundâncias de dados ou relações mal definidas, antes que o banco de dados seja fisicamente implementado.

Em resumo, o Modelo Entidade-Relacionamento e o Diagrama Entidade-Relacionamento são fundamentais na modelagem de dados, ajudando a estruturar, planejar e visualizar a organização de dados em sistemas de banco de dados de maneira eficiente e eficaz.

## ENTIDADES
Agora identificaremos as entidades, onde elas poderão ser abstratas ou concretas.
- Abstrato: Aquilo que não existe fisicamente no mundo real.
- Concreto: O que existe fisicamente no mundo real.

Foi identificado, por exemplo, as Entidades Cliente e Dados Bancários, sendo Cliente uma Entidade Concreta e Dados Bancários uma Entidade Abstrata.

Foi identificado, também, o Score de Crédito como uma Entidade para o Banco de dados.

### Como identificar Entidade
Pelo que identifiquei, este exemplo utilizou como forma para identificar quais seriam as Entidades do banco de dados a interpretação do Levantamento de Requisitos, tendo a pergunta 3 (Quais informações devem ser Armazenadas) uma pergunta extremamente importante.
- Vemos no texto varias menções de caracteristicas de algo, isso é uma dica de Entidade e Atributos, já que Atributos são as características que definem uma Entidade.

Ou seja, quando se diz: Armazenamos os CPF, Nome e Email dos Clientes, podemos entender como: Para uma Entidade Cliente, teremos atributos CPF, Nome e Email

### Entidades identificadas (Esboço do MER)
- Cliente: Nome, CPF, Telefones, endereço, data de nascimento e email
- Dados Bancários: Tipo de conta, saldo, número da conta e data de abertura
- Score de Crédito: Justificativa, pontuação, data da consulta e fonte
- Empréstimos: Valor do empréstimo, status, tipo de empréstimo, data de inicio, nome do cliente e prazo
- Pagamentos: Data pagamento da parcela, valor pago, status da parcerla
- Colaboradores: CPF, telefone, salário, cargo e e-mail
- Deparatamentos: Numero do departamento, nome do departamento e gerente

### Construindo o DER
Inicia-se a construção do DER com a separação das Entidades
![Inicio da Diagramação](assets/rascunho_der_01.png)

## ENTIDADE FORTES
- Entidade forte: existe por si só, sem dependência de outra entidade. Ou seja, ela não precisa de outra entidade ligada a ela para existir.
- Entidade fraca: É o inverso, ela só existe porque outra entidade também existe.

No nossocaso, Clientes, Colaboradores e Departamentos são Fortes, pois, elas não dependem de outras tabelas para existirem.

Já Score de Créditos, Conta, Empréstimo e Pagamento são entendidades fracas, pois, as 3 primeiras inerentemente dependem da tabela de Clientes (pois, não existirá Crédito, Conta ou Empréstimo sem Clientes) e só existe Pagamento com a existencia de Empréstimo.
- Ou seja, uma entidade fraca pode depender de outra entidade fraca.

## ENTIDADE FRACAS
Entidades fracas são representadas por retangulos duplos. 

# <span style="color: #87BBA2">RELACIONAMENTO</span>

## REPRESENTANDO RELACIONAMENTOS
Um ponto muito interessante é na representação da relação de Colaboradores com Departamentos.
- Como existe cargo de Colaborador que gerencia um Departamento, temos essa relação de gerenciamento.
- Porém, temos uma segunda relação, pois, um Departamento, no minimo, possui dois colaboradores.
![Departamento com dois relacionamentos com Colaboradores](assets/relacionamento_01.png)

Imagem do sistema geral
![Diagrama Entidade Relacionamento V2](assets/rascunho_der_02.png)

### Refletindo sobre entidades Fortes e Fracas no momento
1. **Entidade Forte**  
   - É uma entidade que **pode existir por conta própria**, ou seja, **não depende de outra entidade** para existir.  
   - No banco de dados, isso significa que ela **possui uma chave primária própria** e **não depende de uma chave estrangeira obrigatória**.  
   - Exemplo:  
     - No seu caso, **Departamento, Colaborador e Cliente** podem ser entidades fortes, pois fazem sentido existir independentemente.  

2. **Entidade Fraca**  
   - É uma entidade que **não pode existir sem estar associada a uma entidade forte**.  
   - Isso significa que **a sua chave primária depende da chave primária de outra entidade** (chave primária composta).  
   - No banco, isso geralmente se traduz em uma **chave estrangeira obrigatória**.  
   - Exemplo:  
     - Se tivéssemos uma entidade **Dependente** (filho de um colaborador), ela **só faria sentido existir se estiver associada a um Colaborador**.  
     - Assim, a tabela **Dependente** teria como chave primária uma composição entre um **ID próprio** e o **ID do Colaborador** ao qual pertence.  

### **Interpretação**  
O ponto principal não é aceitar ou não **null**, mas sim **se a entidade pode ou não existir sem outra**.  

- Se a entidade for **forte**, a FK pode ser **opcional** (pode aceitar `NULL`), pois ela pode existir sozinha.  
- Se a entidade for **fraca**, a FK **não pode ser nula**, pois ela precisa obrigatoriamente de uma entidade forte para existir.  

## SOBRE GRAU DE RELACIONAMENTO

1. Relacionamento Unário (Auto-relacionamento)
Um relacionamento unário, também conhecido como auto-relacionamento, ocorre quando uma entidade está relacionada a si mesma. Esse tipo de relacionamento é usado para expressar uma relação onde instâncias da mesma entidade estão conectadas de alguma forma.

Exemplo:
- Supervisão em uma Empresa: Um colaborador(a) pode ser supervisor de outro colaborador(a). Aqui, a entidade colaborador tem um relacionamento consigo mesma, onde cada instância (colaborador) pode ser 'supervisor de' outra instância (outro colaborador).

2. Relacionamento Binário
Um relacionamento binário envolve duas entidades diferentes. É o tipo de relacionamento mais comum na modelagem de dados e pode expressar uma variedade de interações entre as entidades.

Exemplos:
- Cliente e Pedido: Um relacionamento binário típico pode ser entre Cliente e Pedido, onde um cliente realiza um pedido.

3. Relacionamento Ternário
Um relacionamento ternário envolve três entidades diferentes. Esses relacionamentos são usados quando uma interação não pode ser adequadamente representada por vários relacionamentos binários.

Exemplo:
- Professores, Estudantes e Cursos: Um relacionamento ternário pode existir entre Professor, Estudante, e Curso, onde um professor pode ensinar a um estudante em um curso específico. Esse tipo de relacionamento indica que a interação envolve todas as três entidades simultaneamente e não pode ser simplificada em relacionamentos menores sem perder informações críticas.

Importância dos Graus de Relacionamento
- Clareza no Design: Compreender o grau de relacionamento ajuda a definir claramente como as entidades interagem dentro do sistema, permitindo um design mais claro e lógico do banco de dados.
- Precisão na Modelagem: Usar o grau correto de relacionamento assegura que o modelo conceitual capture todas as nuances das relações entre as entidades, o que é crucial para a integridade dos dados e a funcionalidade do sistema.
- Eficiência na Implementação: Identificar o grau correto de relacionamento pode simplificar a implementação do banco de dados e otimizar o desempenho, pois o sistema pode ser mais diretamente alinhado com as necessidades reais de interação de dados.

## ENTENDENDO SOBRE CARDINALIDADE
A cardinalidade será utilizada para definir quantas vezes as entidades vão se relacionar.

### Cardinalidade mínima
A cardinalidade mínima define a participação da entidade no relacionamento, indicando se é obrigatório que um colaborador esteja associado a um cliente, por exemplo.

### Cardinalidade máxima
Já a cardinalidade máxima determina a quantidade de ocorrências que podem realmente acontecer.

Por exemplo, um colaborador pode estar associado a 5 clientes, o que representa a cardinalidade máxima, ou seja, o número máximo de ocorrências.

### Sentido de leitura
O sentido de leitura da cardinalidade é sempre oposto à entidade, ou seja, a cardinalidade de uma entidade está ligada proxima à entidade a qual ela se liga. Algo como 
- [ ENTIDADE A ] (cardinalidade da Entidade B) ---- < RELACIONAMENTO > ---- (Cardinalidade da Entidade A) [ ENTIDADE B ]

Ou seja, se for:
- [ A ] 1:n --- Relacionamento --- 1:1 [ B ]
- Interpreta-se: Entidade B possui 1, e somente 1, relaçaão com Entidade A e Entidade A possui no minimo 1 e no maximo N (varias) relações com entidade B.
- [ FUNCIONARIO ] 1:N --- Trabalha/Contem --- 1:1 [ DEPARTAMENTO ]
- Interpreta-se: Um DEPARTAMENTO pode conter no minimo 1 e no maximo N FUNCIONARIOS
- No outro sentido: Um FUNCIONARIO pode trabalhar em no minimo 1 e somente 1 DEPARTAMENTO

### Ordem de leitura do relacionamento
A ordem de leitura de um relacionamento **sempre será**: ENTIDADE + RELACIONAMENTO + CARDINALIDADE + ENTIDADE.
- DEPARTAMENTO + pode CONTER + 1:N + FUNCIONARIOS

## MAIS SOBRE CARDINALIDADE
A cardinalidade nos relacionamentos em um modelo conceitual é um aspecto fundamental que descreve como as entidades estão quantitativamente relacionadas em um banco de dados. Em outras palavras, a cardinalidade define o número de instâncias de uma entidade que podem ou devem estar associadas a um número de instâncias de outra entidade. Este conceito é crucial para desenhar um sistema de banco de dados que reflita com precisão as regras e necessidades de negócio.

### Tipos de Cardinalidade
A cardinalidade é tipicamente expressa em termos das possíveis quantidades de conexões entre entidades e é categorizada principalmente em três tipos:

Obs.: Nesta representação, apenas a cardinalidade máxima é informada

#### Um-para-Um (1:1):
Descrição: Cada instância de uma entidade está associada a no máximo uma instância da outra entidade.

Exemplo: Suponha um sistema onde cada Gerente é responsável por um único Departamento e cada Departamento é gerenciado por um único Gerente. Aqui, a relação entre Gerente e Departamento é um-para-um.

#### Um-para-Muitos (1:N):
Descrição: Uma instância de uma entidade pode estar associada a várias instâncias de outra entidade, mas uma instância da segunda entidade pode estar associada a no máximo uma instância da primeira entidade.

Exemplo: Em um sistema escolar, um Professor pode lecionar várias Turmas, mas cada Turma é lecionada por apenas um Professor. Assim, a relação entre Professor e Turma é um-para-muitos.

#### Muitos-para-Muitos (N:M):
Descrição: Instâncias de uma entidade podem estar associadas a várias instâncias da outra entidade e vice-versa.

Exemplo: Em uma universidade, um Estudante pode se inscrever em várias Disciplinas e cada Disciplina pode ter vários Estudantes inscritos. Esta é uma relação muitos-para-muitos.

### Representação da Cardinalidade
Em um Diagrama Entidade-Relacionamento (DER), a cardinalidade é representada por meio de símbolos ou etiquetas nas linhas que conectam as entidades. Esses símbolos indicam as regras de cardinalidade, como "1", "N" ou "M", mostrando como as entidades estão relacionadas.

### Importância da Cardinalidade
Integridade dos Dados: As regras de cardinalidade ajudam a manter a integridade dos dados ao garantir que os relacionamentos entre as entidades respeitem as regras de negócio definidas. Isso previne erros como ter uma Turma sem Professor em um sistema que exige que todas as turmas tenham professores.

Eficiência na Consulta: Entender as cardinalidades ajuda a otimizar as consultas ao banco de dados. Por exemplo, saber que a relação entre Professor e Turma é 1 permite otimizações ao buscar todas as turmas de um professor específico.

Design do Banco de Dados: A cardinalidade informa decisões sobre como as tabelas devem ser estruturadas, como os índices devem ser criados e como as chaves estrangeiras são definidas, influenciando diretamente a performance e a escalabilidade do banco de dados.

Portanto, definir corretamente as cardinalidades dos relacionamentos no modelo conceitual é crucial para o sucesso do design e da funcionalidade de um sistema de banco de dados, garantindo que ele seja capaz de atender eficientemente às necessidades do usuário e às exigências do negócio.

## CARDINALIDADE
Realizar a definição correta de cardinalidade estamos garantindo que nossos dados sejam integro e estamos atendendo às regras de negócio, como visto no exemplo da conta conjunta. Onde, quando a conta é de uma pessoa, tinhamos a relação de N:1 entre Cliente e Conta e quando passou a ser conjunta se tornou N:N.

Para representar nossas cardinalidades, é **importantissimo** sempre seguirmos as **regras de negócios**;

### Regras de negócio da FlexEmpresta
- Um cliente pode ter nenhum ou varios emprestimos
- Um emprestimo DEVE estar associado a UMA e exclusivamente UMA pessoa
- Ao criar um emprestimo, não precisa-se pagar a primeira parcela de imediato, mas o pagamento poderá ser parcelado
- Um pagamento sempre deve estar associado a um emprestimo, quitando apenas um emprestimo
- Nem todo colaborador gerencia um cliente, mas pode gerenciar mais de um
  - Pois, temos colaboradores que não são gerentes
  - Mas um gerente pode gerenciar mais de um cliente
- Um cliente sempre será gerenciado por um colaborador
- Um departamento precisa ser gerenciado no minimo e no maximo 1 colaborador (gerente)
- Nem todo colaborador é gerente, então, nem todos estarão gerenciando um Departamento
  - Mas quando o colaborador gerencia, ele só pode gerenciar um departamento
- Um departamento pode conter no minimo 2 colaboradores atuando e no maximo é N
- Um colaborador deve e só pode pertencer a um departamento
- Um cliente, no momento da criação, PRECISA ter uma conta, no minimo, e varias contas no maximo
- Pra conta existir, precisa estar associada a um cliente, mas, no maximo, precisará de varios clientes pois a FlexEmpresta aceita conta conjunta

## SOBRE REGRAS DE NEGÓCIO

Quando estamos criando um sistema, uma das etapas mais importantes é entender como esse sistema vai funcionar, certo? É aí que entram as Regras de Negócio. Imagine que você está montando um quebra-cabeça. As peças são os dados que você tem, e as regras de negócio são as instruções de como essas peças devem se encaixar. Sem essas instruções, você pode até montar algo, mas provavelmente não será o que você queria no início.

### O que são Regras de Negócio?
As regras de negócio são, basicamente, as leis que definem como uma empresa ou sistema deve operar. Elas são as diretrizes que dizem como os dados devem ser tratados, quais operações são permitidas, e como diferentes partes do sistema interagem entre si. Por exemplo, uma regra de negócio pode dizer que "um cliente deve ter mais de 18 anos para abrir uma conta".

### Por que são importantes?
Sem regras de negócio bem definidas e implementadas, um sistema pode se comportar de maneira imprevisível, causar erros, ou até mesmo falhar em realizar suas funções básicas. Além disso, elas ajudam a garantir que o sistema esteja alinhado com os objetivos da empresa, cumprindo com regulamentações e oferecendo um serviço de qualidade para os usuários.

### Influência no Modelo Conceitual
O Modelo Conceitual é como o esboço de um edifício antes de começar a construção. Ele mostra a estrutura dos dados, como eles se relacionam, e quais são as principais operações que podem ser realizadas. As regras de negócio influenciam diretamente esse modelo porque definem:

Quais dados são necessários: Se a regra diz que todo cliente deve ter mais de 18 anos, o modelo precisa de um campo para a data de nascimento ou idade do cliente.
Como os dados se relacionam: Se uma regra determina que cada pedido deve estar associado a um único cliente, isso define uma relação específica entre os dados de pedidos e clientes.
Restrições e validações: Por exemplo, se uma regra estabelece que o estoque de um produto não pode ser negativo, isso precisa ser considerado no modelo para garantir que a regra seja respeitada.

### Implementação no Modelo Conceitual
A implementação dessas regras no modelo conceitual é crucial para o sucesso do sistema. Isso geralmente envolve:

Definir entidades e atributos: Identificar quais são os elementos de dados necessários e suas características.
Estabelecer relações: Determinar como as entidades se relacionam entre si.
Aplicar restrições: Incluir regras que limitam os valores que os dados podem ter ou como eles podem ser alterados.

### Exemplo Prático
Vamos considerar um sistema de biblioteca. Uma regra de negócio pode ser que "um usuário pode pegar no máximo 5 livros por vez". No modelo conceitual, isso influencia:

A criação de uma entidade Usuário e uma entidade Livro.
Uma relação entre Usuário e Livro que permite associar múltiplos livros a um único usuário.
Uma restrição na relação que limita o número de livros associados a um usuário a no máximo 5.

### Conclusão
As regras de negócio são fundamentais para o desenvolvimento de sistemas eficientes e eficazes. Elas orientam a modelagem de dados, garantindo que o sistema atenda às necessidades da empresa e dos usuários. Implementá-las corretamente no modelo conceitual é essencial para construir uma base sólida para o desenvolvimento do sistema. Portanto, entender e aplicar essas regras é uma habilidade valiosa para qualquer desenvolvedor ou analista de sistemas.

## ENTIDADE ASSOCIATIVA
Para um banco de dados relacional, não é possivel mantermos um relacionamento muitos-para-muitos (N:N), mas, como podemos resolver a questão deste relacionamento, uma vez que se faz necessário a relação de muitos-para-muitos entre essas duas entidades. Resolvemos isso através das **Entidades Associativas**, tornando uma relação N:N em uma relação indireta.

A entidade associativa não é nem uma entidade, nem um relacionamento. Ela vem da mistura desses dois objetos. Trata-se da junção de uma entidade com um relacionamento, porque ela será uma entidade ao final do projeto, mas também é responsável por associar duas entidades.

### Como o banco se comportaria sem entidade associativa

#### Sem associação
![tab sem associacao](./assets/sem_assoc.png)
- Observe que Luiza e Carlos compartilhar a mesma conta 12487

#### Representação do banco sem associação
![representacao do banco](./assets/represent_banco_sem_assoc.png)
![highlight na repeticao](./assets/repeticao_highlited.png)
- Como Luiza e Carlos estavam fazendo referencia a uma mesma linha, e isso não é possivem no banco de dados, uma solução para isso seria replicar a linha, tornando uma delas associada a Luiza e uma delas associada a Carlos.
- Isso não é pratico, pois, se tivesse um caso de 30 instancias de um objeto fazendo referencia a 2 instancia de outro objeto, já seriam 60 linhas. Se fossem para 3 instancias, 90 linhas, sendo 60 linhas replicadas (só mudando a quem está associado), ocupando desnecessariamente espaço no banco e necessitando realizar operações especificas para fazer alguma alteração, caso necessita-se de atualização, e afins.

#### Com associação
![Realizando associação](./assets//com_assoc.png)
Agora, tendo uma tabela intermediaria realizando as associações, sempre teremos relacionamentos unicos.
- A tabela de associação unirá uma entidade com a outra, ou seka, Luiza tem conta X, Luiza tem conta Y, Carlos tem Conta Z, Carlos tem conta Y, e por aí vai.
- Isso facilita a manutenção e economiza espaço, pois associa-se apenas chaves únicas.

## MAIS SOBRE ENTIDADE ASSOCIATIVA
Uma entidade associativa no contexto de modelagem de dados é um conceito crucial quando se lida com relacionamentos muitos-para-muitos (N:M) entre duas entidades. Em modelos conceituais, uma entidade associativa é usada para resolver a complexidade que surge ao tentar implementar diretamente um relacionamento muitos-para-muitos em um sistema de banco de dados relacional.

### Definição de Entidade Associativa
Uma entidade associativa, também conhecida como tabela de junção, tabela de associação, ou tabela intermediária, é uma tabela que serve como uma ponte entre duas outras entidades para gerenciar um relacionamento muitos-para-muitos entre elas. Essa entidade não só armazena as chaves das duas entidades relacionadas como também pode conter atributos adicionais que são específicos para o relacionamento.

### Funcionalidade da Entidade Associativa
Gerenciamento de Relacionamentos (N:M): A principal função de uma entidade associativa é transformar um complicado relacionamento muitos-para-muitos em dois relacionamentos um-para-muitos (1:N), o que é mais simples de implementar em bancos de dados relacionais.

Armazenamento de Dados de Relacionamento: Além de conectar duas entidades, a entidade associativa frequentemente armazena informações relevantes para o relacionamento. Por exemplo, se uma entidade associativa conecta Estudantes e Cursos em um relacionamento de inscrição, ela pode também armazenar informações como Data de Inscrição, Nota Final ou Status da Inscrição.

#### Exemplo de Entidade Associativa
Vamos considerar um sistema de gerenciamento universitário onde estudantes podem se inscrever em múltiplos cursos e cada curso pode ter vários estudantes. Aqui, temos um relacionamento muitos-para-muitos entre as entidades Estudante e Curso.

- Estudantes (EstudanteID, Nome, Email)
- Cursos (CursoID, NomeCurso, Professor)

Para gerenciar esse relacionamento, criamos uma entidade associativa chamada Inscrições:

- Inscrições (EstudanteID, CursoID, DataInscrição, NotaFinal)

Aqui, EstudanteID e CursoID são chaves que referenciam Estudantes e Cursos, respectivamente, e DataInscrição e NotaFinal são atributos específicos do relacionamento.

### Benefícios da Entidade Associativa
Clareza e Organização: Facilita o entendimento e a gestão de relacionamentos muitos-para-muitos, proporcionando uma visão clara de como as entidades estão inter-relacionadas.

Integridade de Dados: Mantém a integridade referencial ao garantir que todas as relações sejam válidas dentro do contexto das regras de negócio definidas.

Flexibilidade para Armazenar Dados Complexos: Permite o armazenamento de dados detalhados sobre o relacionamento, que não seriam possíveis de armazenar diretamente nas tabelas das entidades principais.

Em resumo, a entidade associativa é uma ferramenta valiosa no arsenal de modelagem de dados, essencial para lidar com complexidades específicas de relacionamentos muitos-para-muitos e para enriquecer o banco de dados com informações detalhadas sobre as interações entre entidades.

