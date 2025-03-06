# <span style="color: #87BBA2">===   Modelagem de dados: desenvolvendo o modelo lógico   ===</span> <!-- omit in toc -->

# <span style="color: #87BBA2">INDICE</span> <!-- omit in toc -->
- [Aula XX: TituloAula](#aula-xx-tituloaula)
  - [Capitulo](#capitulo)


# <span style="color: #87BBA2"> Transformação de modelo conceitural em lógico </span>

## INICIANDO A PASSAGEM DE CONCEITUAL PARA LÓGICO
Inicialmente, focaremos nas entidades e utilizaremos os elementos gráficos chamados de **tables**.

Caso pensarmos em uma planilha ou modelo de banco de dados, a representação do conceitual pode não fazer muito sentido (a caixa de Entidade com as bolinhas de atributos). Para isso, colocaremos como titulo da tabela a a Entidade e suas linhas como seus atributos, ou seja, os atributos estarão contidos nas suas respectivas Entidades.

Notamos que essa representação começa a ficar mais proxima na resolução do problema com uma ferramenta de dados, já conseguimos imaginar onde irão suas colunas, as tabelas e afins.

### Padronização
Neste projeto, o instrutor utilizou o radical "Tabela" como radical do nome da tabela, o qual facilitará na sua identificação. Ou seja, o nome ficou da tabela ficou "TabelaColaboradores".

## MODELO LÓGICO, ENTIDADES E ATRIBUTOS
### O que é um Modelo Lógico?
Um modelo lógico é uma representação estruturada de como os dados serão organizados em um banco de dados. Ele descreve as entidades, que são objetos ou conceitos sobre os quais queremos armazenar informações, e os atributos, que são as propriedades dessas entidades. O modelo lógico serve como um intermediário entre o modelo conceitual, que é mais abstrato e focado nas necessidades de negócios, e o modelo físico, que é implementado diretamente no sistema de gerenciamento de banco de dados (SGBD).

#### Entidades
Entidades são elementos fundamentais no modelo lógico. Elas representam objetos ou conceitos do mundo real que possuem existência independente e que queremos armazenar no banco de dados. Cada entidade é definida por um conjunto de atributos que a caracterizam.

Por exemplo, em um sistema de gerenciamento de biblioteca, algumas possíveis entidades são:
- Livro
- Autor
- Usuário

Cada entidade deve ser identificável de forma única dentro do sistema.

#### Atributos
Atributos são as propriedades ou características que descrevem uma entidade. Cada atributo tem um nome. Eles fornecem mais detalhes sobre a entidade e permitem armazenar informações relevantes.

Considerando as entidades mencionadas, alguns exemplos de atributos são:
- Livro
    - ID do Livro
    - Título
    - ISBN
    - Ano de Publicação

- Autor
    - ID do Autor
    - Nome
    - Nacionalidade

- Usuário
    - ID do Usuário
    - Nome
    - Email
    - Data de Cadastro

Os atributos ajudam a capturar todas as informações necessárias sobre cada entidade de maneira estruturada e organizada.

#### Passando do Modelo Conceitual para o Modelo Lógico
A transição do modelo conceitual para o modelo lógico envolve várias etapas importantes:

1. Identificação das Entidades: No modelo conceitual, começamos identificando todas as entidades principais baseadas nos requisitos do negócio. Essas entidades são então mapeadas diretamente para o modelo lógico.
2. Definição dos Atributos: Para cada entidade identificada, determinamos os atributos necessários. Esses atributos são propriedades que descrevem a entidade e são derivadas das necessidades de informação do negócio.

O modelo lógico é um passo crucial no desenvolvimento de um banco de dados bem-estruturado. Ele traduz as necessidades de negócio, capturadas no modelo conceitual, em uma estrutura organizada de entidades e atributos. Essa estrutura serve como base para a implementação física do banco de dados, garantindo que os dados sejam armazenados de maneira eficiente, consistente e fácil de acessar.

### TRANSFORMANDO O MODELO CONCEITUAL E LÓGICO
Agora, transferindo a entidade Cliente para o modelo lógico, pontos interessantes a elencar:
- O endereço foi indicado como atributo "EndereçoCompleto", abstraindo so demais itens do atributo composto
- Aplicou-se padronização e recomendou-se fortemente seguir a os padrões escolhidos. No caso deste projeto, escolheu-se PascalCase para atributos.
    - Essa não é uma preocupação no momendo de realizar uma modelagem conceitual, mas começa a ser na modelagem lógica

### Padronizações adotadas
Quando um nome de atributo se repete
- Unir atributo com o nome da entidade sem radical
  - NomeColaborador
  - CPFColaborador
- Neste projeto, o instrutor aplica a regra acima a todos, com exceção da entidade mais forte (Cliente), o qual ele deixa apenas Nome, CPF e afins. Tenho sensação que isso não é muito recomendado.
- Usar PascalCase nos atributos, com exceção de siglas (como CPF) e com o prefixo de ID, como em IDCliente, IDColaborador

# <span style="color: #87BBA2"> Definindo tabelas e relacionamentos </span>

## DEFININDO ENTIDADE E ATRIBUTOS NO MODELO LÓGICO
Instrutor constrói tabela de Departamento. Ponto interessante:
- O padrão para nomear o atributo "gerente" foi "NomeColaboradorGerente", ou seja, fez-se alusão a outra entidade na nomenclatura.

## PARA SABER MAIS: A IMPORTÃNCIA DO DICIONÁRIO DE DADOS NA MODELAGEM DE DADOS
No nosso projeto até agora estabelecemos a base do nosso modelo lógico, definindo entidades e atributos seguindo um padrão de nomenclatura consistente. Agora, à medida que avançamos na construção e organização das nossas tabelas, é fundamental garantir que todos os envolvidos no projeto tenham uma compreensão clara e unificada de cada elemento do modelo. É aqui que entra a importância da documentação, especificamente a criação de um dicionário de dados.

### O que é um Dicionário de Dados?
Um dicionário de dados é um documento detalhado que descreve cada campo, atributo e entidade no banco de dados. Ele serve como uma referência centralizada que documenta as definições e outras características relevantes de cada elemento no modelo de dados.

#### Importância do Dicionário de Dados
1. Claridade e Consistência: Ao documentar cada campo e entidade, garantimos que todos os membros da equipe, desde desenvolvedores a analistas de dados, tenham uma compreensão clara e consistente do que cada termo significa. Isso elimina ambiguidades e interpretações diferentes que podem levar a erros na implementação e uso do banco de dados.
2. Facilidade de Manutenção: Um dicionário de dados bem elaborado facilita a manutenção e atualização do banco de dados. Quando novos desenvolvedores ou analistas ingressam na equipe, eles podem rapidamente se familiarizar com a estrutura e os detalhes do banco de dados consultando o dicionário.
3. Conformidade com Padrões: Documentar os dados assegura que todos os campos e entidades estão de acordo com os padrões de nomenclatura e representação estabelecidos. Isso é crucial para manter a uniformidade e profissionalismo no projeto.
4. Referência Centralizada: Com um dicionário de dados, todas as informações relevantes sobre o banco de dados estão centralizadas em um único documento. Isso facilita a consulta e evita a dispersão de informações em diferentes fontes, que pode causar confusão e inconsistências.
5. Suporte na Tomada de Decisões: Ter um dicionário de dados completo permite uma melhor tomada de decisões. Quando se planeja a expansão do banco de dados ou se avaliam mudanças, ter acesso a um documento detalhado ajuda a entender as implicações e a tomar decisões informadas.

A criação de um dicionário de dados é um passo fundamental na modelagem de dados. Ele proporciona clareza, consistência e uma referência centralizada que facilita a comunicação e o entendimento entre todos os membros da equipe. Com um dicionário de dados bem elaborado, podemos mitigar problemas de interpretação e garantir que o nosso modelo de dados seja robusto e bem documentado, facilitando tanto a implementação quanto a manutenção do banco de dados.

## CRIANDO UMA ENTIDADE DE RELACIONAMENTO
Vimos como representar uma entidade de relacionamento, o qual segue a mesma regra das demais entidades.
- Nome: TabelaClienteConta
- Preenche os atributos que encontra-se no modelo conceitual, acrescentando alguma especificação quando necessário
  - Tipo = TipoConta
  - Nome = NomeCliente

# <span style="color: #87BBA2"> Avançando na modelagem lógica </span>

## IMPLEMENTANDO OS RELACIONAMENTOS
Ainda não conseguimos representar algumas regras de negócio dos requisitos. Por exemplo, um empréstimo precisa de um cliente para existir; não é possível ter um empréstimo sem um cliente associado.

No modelo conceitual, representamos essa relação com um relacionamento entre as entidades de cliente e empréstimo, onde o cliente é uma entidade forte e o empréstimo é uma entidade fraca que depende do cliente. Esse relacionamento era indicado por um losango com um verbo explicativo

Agora, devemos conectar essas entidades de acordo com o relacionamento. A inclusão do verbo é opção (porém, interessante).

### Praticas interessantes
- Posicionou-se as tabelas similar ao posicionamento das entidades no modelo conceitual
- Conectou tabelas com setas comuns colocando os verbos de ida em cima e volta embaixo

## MONTANDO AS CARDINALIDADES

### Pontos interessantes
- Relação entre TabelaDepartamento e TabelaColaboradores, onde existem dois relacionamentos
  - Colaboradores gerenciando Departamento
  - Departamento contendo Colaboradores
- Aplicando cardinalidade
  - Atentar-se a mesma ordem de leitura: Entidade > verbo > cardinalidade
  - Ou seja, a cardinalidade de uma entidade é aquela que está proxima da outra cardinalidade ao qual ela se relaciona. Ou seja: Departamento possui (1,N) Colaboradores.

## PARA SABER MAIS: CRIAÇÃO DE RELACIONAMENTOS E CARDINALIDADE NA MODELAGEM DE DADOS
Na construção de um banco de dados robusto e funcional, a definição precisa de relacionamentos entre entidades é tão crucial quanto a definição das próprias entidades e seus atributos. Já estabelecemos nossas entidades e atributos, mas agora precisamos garantir que as regras de negócio que regem essas entidades sejam fielmente representadas no modelo lógico. Isso é feito através da definição de relacionamentos e da especificação de cardinalidades.

### Relacionamentos no Modelo Lógico
Relacionamentos descrevem como as entidades estão conectadas entre si e quais são as regras que governam essas conexões. Em um modelo lógico, os relacionamentos são representados de maneira detalhada para garantir que as regras de negócio sejam respeitadas e que o banco de dados funcione conforme o esperado.

### Passos para Definir Relacionamentos:
- Identificação das Regras de Negócio: Antes de criar os relacionamentos, é essencial entender as regras de negócio. Por exemplo, uma conta deve ter um cliente responsável, e um cliente deve ter um colaborador responsável. Essas regras ajudam a definir como as entidades se relacionam.
- Definição das Entidades Fortes e Fracas: No modelo lógico, distinguimos entre entidades fortes (independentes) e entidades fracas (dependentes). As entidades fortes podem existir por si mesmas, enquanto as fracas dependem de outras entidades para sua existência. Por exemplo, uma "Conta" pode ser considerada uma entidade fraca que depende de um "Cliente".
- Conectando Entidades: Utilizamos setas para conectar as entidades no diagrama, partindo da entidade dependente para a entidade independente. Isso ajuda a visualizar claramente a direção do relacionamento. Podemos também incluir verbos para descrever a natureza do relacionamento, como "uma conta pertence a um cliente" e "um cliente possui uma conta".
- Padronização dos Nomes: É importante seguir uma padronização de nomes para atributos e entidades, garantindo consistência e clareza na leitura e interpretação do modelo.

### Direção da Seta no Relacionamento
A direção da seta no modelo lógico indica a dependência entre as entidades. Geralmente, as setas partem da entidade dependente (ou entidade fraca) para a entidade independente (ou entidade forte). Essa convenção ajuda a entender quais entidades dependem de outras para existir e clarifica a estrutura do relacionamento.

### Exemplo de Direção da Seta:
- Conta e Cliente:
    - Entidades: Conta (entidade dependente), Cliente (entidade independente).
    - Relacionamento: Uma conta pertence a um cliente, e um cliente pode ter várias contas.
    - Representação: A seta vai da entidade Conta para a entidade Cliente.

### Cardinalidade
A cardinalidade define quantas instâncias de uma entidade podem ou devem estar associadas a instâncias de outra entidade. Ela é crucial para representar as restrições de negócios no modelo lógico.

### Tipos de Cardinalidade:
- Um para Um (1:1): Cada instância de uma entidade está associada a exatamente uma instância de outra entidade.
- Um para Muitos (1:N): Cada instância de uma entidade está associada a várias instâncias de outra entidade.
- Muitos para Muitos (N:N): Várias instâncias de uma entidade estão associadas a várias instâncias de outra entidade.

### Representação da Cardinalidade:
Para representar a cardinalidade no diagrama lógico, utilizamos números entre parênteses no início e no fim de cada seta que representa o relacionamento. Esses números indicam o mínimo e o máximo de instâncias permitidas ou exigidas.

### Exemplos de Cardinalidade:
- Uma conta deve ter no mínimo um cliente e no máximo vários: (1,N)
- Um departamento deve ter um gerente e apenas um gerente: (1,1)

A criação de relacionamentos e a definição de cardinalidades são etapas críticas na modelagem de dados. Elas garantem que as regras de negócio sejam corretamente implementadas no modelo lógico, o que, por sua vez, assegura a integridade e funcionalidade do banco de dados final. Documentar e padronizar esses relacionamentos facilita a construção e a manutenção do banco de dados, promovendo uma compreensão clara e compartilhada entre todos os envolvidos no projeto. Com todas as entidades e relacionamentos definidos, podemos avançar para a próxima etapa, que é a implementação física dessas regras no banco de dados.

## CRIANDO CHAVE PRIMARIA
A chave primária é um campo que representa de maneira única uma entidade. Por exemplo, uma das regras de negócio é que os clientes sejam únicos. Embora o CPF possa servir para isso, o recomendado é usar um ID, como o IDCliente, para garantir a unicidade e otimizar o banco de dados, mesmo em casos onde o cliente possa não ter um CPF. Assim, o IDCliente é um atributo que representa o cliente, e precisamos adicionar a característica de chave primária a esse atributo.

### Padronizando
Para representar uma PK (Primary Key, ou Chave Primaria), há um campo separado na tabela apenas para ela, com negrito e sublinhado.
- PK sempre serão unicas (não podem ter valores iguais em outas linhas da tabela) e nunca podem ser nulas.

A padronização do nome que utilizaremos para as PKs são:
- `id_<nome_do_campo>`: Para a tabela Cliente, id_cliente. Para a tabela Departamento: id_departamento.

### Chave composta
Nas situações de chave composta, como ocorre na tabela `TabelaClienteConta`, que é uma tabela de relacionamento, temos, etnão, duas Primary Keys, que será o `id_cliente` e `id_conta`, mas, ela não tem um id próprio. Ou seja, o id dessa tabela é composta por dois ids, sendo de Cliente e Conta.

Sua representação é igual quando temos um PK único, mas duplicado, um espaço reservado para cada um PK.
- `id_cliente` e `id_conta` = id da tabela da composta

## CHAVE ESTRANGEIRA
O problema que temos agora é que garantimos que, por exemplo, um cliente seja único em nosso banco de dados, porém, ainda não conseguimos garantir os relacionamentos. Como sabemos que um empréstimo está associado a um cliente?

Aí que entra a chave estrangeira (Foreign Key).

### Aplicando FK
Para aplicar Foreign Keys no modelo lógico, acrescentamos o id da tabela a qual a tabela que estamos escrevendo se relaciona e indicamos o tempo "FK" no espaço a esquerda do nome do atributo.

Por padrão, é interessante deixar o campo da tabela que esta recebendo a FK ser igual a PK da tabela a qual ela faz referencia. A cardinalidade indica a nulidade (ou não nulidade) e também indica a dependencia.
- TabelaEmprestimo tem relação de (1,1) com TabelaCliente, ou seja, um Emprestimo DEVE estar associado a um, e somente um, Cliente. Então, isso indica que Emprestimo terá uma FK de Cliente para fazer relação com ele.
  - No modelo lógico: `TabelaCliente (1,1) <--- Fazer/Feito ---- (0,n) TabelaEmprestimo`
  - Essa lógica corresponde a regra de negócio onde um Empréstimo sempre estará associado a um Cliente, mas, um Cliente pode ser cadastrado sem Empréstimo e pode ter varios Empréstimos
  - A relação que indica que TabelaEmprestimo terá a FK é, primeiro, por ela ser dependente de Cliente (só existe Emprestimo se existir Cliente) e por Cliente poder ter nenhum ou varios Emprestimos, e Emprestimos TER DE TER UM CLIENTE, logo, é mais lógico Emprestimos ter a FK para relacionar com Cliente pois, se não, Cliente deveria (de alguma forma) ter diversas colunas para relacionar com os diversos emprestimos que ele tem a possibilidade de ter.

### Nas Tabelas Relacionais
No caso, as tabelas relacionais receberão as FK das tabelas que ela fará o relacionamento. Caso ela tenha, como identificador, uma chave composta, **as PK que compõe seu identificador também serão FK**.
- Na TabelaClienteConta
  - PK, FK: id_conta
  - PK, FK: id_cliente

## PARA SABER MAIS: CHAVE PRIMÁRIA E CHAVE ESTRANGEIRA NO MODELO LÓGICO
À medida que avançamos na modelagem lógica de dados, é essencial garantir que nossos relacionamentos entre entidades sejam concretizados de maneira clara e funcional. Para isso, utilizamos conceitos fundamentais como chave primária (PK) e chave estrangeira (FK). Esses elementos são cruciais para garantir a integridade referencial e a unicidade das informações no banco de dados.

### Chave Primária (PK)
A chave primária é um atributo ou um conjunto de atributos que identifica de maneira única cada registro em uma tabela. Ela desempenha um papel crucial na integridade e na eficiência do banco de dados, garantindo que cada registro possa ser referenciado de forma única e sem ambiguidade.

#### Características da Chave Primária:

- Unicidade: A chave primária deve conter valores únicos. Não pode haver dois registros com o mesmo valor de chave primária.
- Não Nulo: A chave primária não pode ter valores nulos. Cada registro deve ter um valor definido para a chave primária.
- Imutabilidade: Uma vez definido, o valor da chave primária não deve ser alterado.

#### Exemplo:
Vamos considerar a entidade Cliente. Embora o CPF possa ser usado como identificador único, pode ser mais prático e flexível criar um identificador próprio, como id_cliente. Este atributo será a chave primária da tabela Cliente.
```
TabelaCliente
-------------
id_cliente (PK)
nome_cliente
cpf_cliente
email_cliente
```
Neste exemplo, id_cliente é a chave primária, garantindo que cada cliente possa ser identificado de maneira única no banco de dados.

### Chave Estrangeira (FK)
A chave estrangeira é um atributo ou um conjunto de atributos em uma tabela que referencia a chave primária de outra tabela. Ela estabelece e reforça o relacionamento entre as tabelas, garantindo a integridade referencial dos dados.

#### Características da Chave Estrangeira:
- Referência: A chave estrangeira deve corresponder a um valor existente na tabela referenciada (aquela que possui a chave primária).
- Integridade Referencial: As chaves estrangeiras garantem que os relacionamentos entre tabelas sejam válidos, prevenindo a inserção de valores órfãos que não têm correspondência na tabela referenciada.

#### Exemplo:
Vamos considerar o relacionamento entre as entidades Conta e Cliente. Uma conta deve estar associada a um cliente. Portanto, a chave primária da tabela Cliente (id_cliente) será utilizada como chave estrangeira na tabela Conta.
```
TabelaConta
-------------
id_conta (PK)
numero_conta
id_cliente (FK)
saldo_conta
```
Neste exemplo, id_cliente na tabela Conta é uma chave estrangeira que referencia id_cliente na tabela Cliente. Isso garante que cada conta esteja associada a um cliente válido e existente.

### Implementação no Modelo Lógico
#### Definindo Chaves Primárias:
Para cada entidade, identificamos um ou mais atributos que possam servir como identificador único. Esses atributos são então designados como chaves primárias.

##### Definindo Chaves Estrangeiras:
Para concretizar os relacionamentos, identificamos os atributos dependentes que precisam referenciar outra tabela. Esses atributos são designados como chaves estrangeiras e configurados para garantir a integridade referencial.

A chave primária e a chave estrangeira são componentes essenciais na modelagem lógica de dados. A chave primária garante a unicidade e a identificação clara de registros dentro de uma tabela, enquanto a chave estrangeira estabelece e reforça os relacionamentos entre tabelas. Juntas, elas asseguram que o banco de dados mantenha a integridade dos dados e que as regras de negócio sejam respeitadas, proporcionando uma estrutura sólida e eficiente para o gerenciamento de informações.

# <span style="color: #87BBA2"> Aplicando o modelo lógico na planilha </span>

## PARA SABER MAIS: USANDO O MODELO LÓGICO PARA MELHORAR PLANILHAS EMPRESARIAIS
Transformar dados empresariais armazenados em planilhas para um formato mais estruturado e eficiente pode parecer desafiador, mas aplicar um modelo lógico bem definido pode trazer inúmeros benefícios.

Este texto explora como utilizar o modelo lógico para melhorar a planilha de uma empresa, destacando boas práticas e os benefícios dessa abordagem.

### Benefícios do Modelo Lógico para Planilhas
- Organização Estruturada: Um modelo lógico organiza dados de maneira clara e estruturada, facilitando a navegação e o entendimento das informações. Isso ajuda a evitar a duplicação de dados e a manter a consistência.
- Integridade dos Dados: Utilizando chaves primárias (PK) e chaves estrangeiras (FK), o modelo lógico garante a integridade referencial. Mesmo que as planilhas não suportem diretamente essas características, podemos criar colunas que imitam essas relações, ajudando a manter dados precisos e relacionados.
- Facilidade de Atualização: Um modelo lógico bem estruturado facilita a atualização e manutenção dos dados. As mudanças podem ser aplicadas de maneira consistente em toda a planilha, evitando erros e inconsistências.
- Escalabilidade: Uma planilha estruturada com base em um modelo lógico pode facilmente ser escalada para um banco de dados relacional, caso a empresa precise migrar para uma solução mais robusta no futuro.

### Boas Práticas ao Aplicar o Modelo Lógico a Planilhas
- Definir Entidades Claramente: Identifique as principais entidades do negócio (por exemplo, clientes, contas, empréstimos) e crie abas ou seções separadas para cada uma delas na planilha.
- Estabelecer Atributos Precisos: Para cada entidade, defina claramente os atributos necessários e padronize os nomes. Isso inclui usar identificadores únicos (como id_cliente para clientes) para imitar chaves primárias.
- Simular Relacionamentos: Embora planilhas não suportem chaves estrangeiras diretamente, podemos criar colunas de referência. Por exemplo, a aba de contas pode incluir uma coluna id_cliente que referencia a aba de clientes.
- Manter a Consistência: Use formatos e tipos de dados consistentes para evitar ambiguidades. Por exemplo, todas as datas devem estar no mesmo formato, e todos os identificadores devem ser únicos e consistentes.
- Documentação e Notas: Inclua uma aba ou seção de documentação dentro da planilha, explicando a estrutura, os relacionamentos, e as regras de negócio implementadas. Isso ajuda os usuários a entenderem e seguirem o modelo.

### Exemplo prático
Vamos considerar um exemplo simplificado da FlexEmpresta:

1 - Entidades e Atributos:
- Clientes: id_cliente, nome_cliente, cpf_cliente, email_cliente
- Contas: id_conta, numero_conta, id_cliente, saldo_conta
- Empréstimos: id_emprestimo, id_conta, valor_emprestimo, data_emprestimo

2 - Planilha Estruturada:
- Aba "Clientes":
```
id_cliente | nome_cliente | cpf_cliente | email_cliente
-------------------------------------------------------
1          | João Silva   | 12345678900 | joao@email.com
2          | Maria Souza  | 09876543211 | maria@email.com
```

- Aba "Contas":
```
id_conta | numero_conta | id_cliente | saldo_conta
-------------------------------------------------
1       | 12345        | 1          | 1000.00
2       | 67890        | 2          | 2500.00
```

- Aba "Empréstimos":
```
id_emprestimo | id_conta | valor_emprestimo | data_emprestimo
-------------------------------------------------------------
1             | 1        | 5000.00          | 2023-01-15
2             | 2        | 3000.00          | 2023-02-20
```

### Benefícios Observados
- Melhoria na Organização: Cada entidade é claramente separada, e os dados são mais fáceis de localizar e gerenciar.
- Integridade e Relacionamentos: Mesmo sem suporte nativo para chaves estrangeiras, os relacionamentos são imitados, garantindo a integridade referencial.
- Preparação para Escalabilidade: A estrutura atual da planilha facilita uma futura migração para um sistema de banco de dados, se necessário.

Aplicar um modelo lógico a planilhas empresariais pode transformar a maneira como os dados são gerenciados, trazendo maior organização, consistência, e integridade. Seguindo boas práticas e entendendo os benefícios dessa abordagem, empresas como a FlexEmpresta podem melhorar significativamente a eficiência e a qualidade dos seus dados.

# <span style="color: #87BBA2"> Aplicando em outros contextos </span>

## PARA SABER MAIS: A UTILIZAÇÃO DO MODELO LÓGICO NO POWERBI E EM DIVERSOS SISTEMAS DE ARMAZENAMENTO DE DADOS
Ao longo deste curso, aprendemos a importância de um modelo lógico bem definido para a organização e gestão de dados. A aplicação desse modelo não se limita a planilhas, ele também pode ser integrado a diversas ferramentas de Business Intelligence (BI) e sistemas de armazenamento de dados, ampliando a eficiência e a escalabilidade das operações. Vamos explorar como os pontos criados no modelo lógico podem ser utilizados eficazmente no PowerBI e em diversos sistemas de armazenamento de dados, como bancos de dados relacionais, Data Warehouses, bancos NoSQL e Google BigQuery.

### Aplicação do Modelo Lógico em Bancos de Dados Relacionais
Os bancos de dados relacionais são fundamentais para armazenar e gerenciar grandes volumes de dados de maneira eficiente. A estrutura definida no modelo lógico pode ser diretamente aplicada para criar tabelas, definir chaves primárias e estrangeiras, e estabelecer relacionamentos que garantem a integridade dos dados.

> No banco de dados relacional, os relacionamentos, chaves primárias, chaves estrangeiras e IDs desempenharam um papel crucial. Por exemplo, a regra de negócio que impede a criação de uma conta de usuário sem que ele exista no cadastro foi aplicada com sucesso. Isso garantiu a integridade e a consistência dos dados, assegurando que cada ação respeitasse as restrições e normas definidas no modelo lógico.

### Benefícios:
- Integridade dos Dados: A utilização de chaves primárias e estrangeiras garante que os relacionamentos entre tabelas sejam mantidos, prevenindo dados inconsistentes ou órfãos.
- Consulta Eficiente: A organização dos dados em tabelas relacionadas permite a execução de consultas SQL complexas de forma eficiente, otimizando a recuperação de informações.
- Escalabilidade: Com o crescimento dos dados, os bancos de dados relacionais oferecem ferramentas e técnicas para escalabilidade horizontal e vertical, garantindo desempenho consistente.

### Aplicação do Modelo Lógico no PowerBI
Ferramentas de Business Intelligence como o PowerBI permitem a visualização e análise de dados de forma dinâmica. A integração do modelo lógico no PowerBI ajuda a criar relatórios e dashboards que refletem com precisão as regras de negócio e os relacionamentos entre os dados.

> No Power BI, o impacto do modelo lógico foi igualmente significativo. As tabelas ou entidades foram automaticamente relacionadas graças ao uso consistente de nomenclatura e IDs, que foram transformados em atributos das entidades. Esse alinhamento facilitou a criação de relatórios e visualizações precisas e integradas, economizando tempo e reduzindo o risco de erros.
>
> Esses exemplos ilustram os benefícios tangíveis de ter um modelo lógico robusto para apoiar a criação e gestão da sua base de dados. Com ele, você pode garantir a coerência, precisão e eficiência no armazenamento e uso dos dados.

#### Benefícios:
- Clareza Visual: A estrutura lógica dos dados facilita a criação de visualizações claras e informativas, permitindo uma melhor tomada de decisões.
- Relatórios Dinâmicos: Utilizando a lógica de relacionamento entre tabelas, é possível criar relatórios interativos que permitem explorar os dados de diferentes perspectivas.
- Automatização de Processos: O PowerBI permite a atualização automática dos dados, garantindo que as visualizações estejam sempre atualizadas com as informações mais recentes.

### Aplicação do Modelo Lógico em Data Warehouses
Data Warehouses são usados para armazenar grandes volumes de dados históricos de uma maneira que facilita a análise e a tomada de decisões. A estrutura de um Data Warehouse pode ser baseada no modelo lógico, mas adaptada para suportar a agregação e análise de dados.

#### Benefícios:
- Análise Histórica: Armazena dados históricos que permitem análises de tendências ao longo do tempo.
- Otimização para Consultas: Estrutura os dados de maneira otimizada para consultas analíticas complexas.
- Centralização dos Dados: Centraliza dados de diferentes fontes, proporcionando uma visão unificada.

### Aplicação do Modelo Lógico em Bancos NoSQL
Bancos de dados NoSQL, como MongoDB, oferecem flexibilidade no armazenamento de dados sem a necessidade de um esquema rígido. No entanto, o modelo lógico pode servir como uma base para organizar a estrutura dos documentos.

#### Benefícios:
- Flexibilidade: Permite alterações na estrutura dos dados sem necessidade de grandes mudanças no esquema.
- Desempenho Escalável: Otimizado para grandes volumes de dados e alta disponibilidade.
- Modelagem Flexível: Adapta-se facilmente a dados sem estrutura definida.

Ao dominar a integração do modelo lógico com essas ferramentas, você estará preparado para enfrentar desafios de gestão de dados em diferentes contextos, garantindo que as informações essenciais estejam sempre acessíveis e bem-organizadas.

