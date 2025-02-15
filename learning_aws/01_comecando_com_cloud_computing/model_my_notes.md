# <span style="color: #87BBA2">===   Começando em Cloud: usando a AWS e explorando os recursos da nuvem como serviço   ===</span> <!-- omit in toc -->

# <span style="color: #87BBA2">INDICE</span> <!-- omit in toc -->
- [Aula XX: TituloAula](#aula-xx-tituloaula)
  - [Capitulo](#capitulo)

# <span style="color: #87BBA2">NAVEGANDO NA NUVEM</span>

## INDENTIFICANDO A COMPUTAÇÃO COMO SERVIÇO
Segue-se o conceito de Cliente / Servidor, onde, lembrando, um servidor é um computador que armazena a aplicação e recebe as requisições do cliente para atender suas solicitações.

Os clientes podem ser telefones, notebooks, a televisão de casa.

### Onde fica o servidor?
O servidor poderia ser um computador que fica em nossa casa ligada 24h sempre respondendo as solicitações das pessoas, **ou**, podemos utilizar a Computação em Núvem, que seu conceito é a oferta de serviços computacionais como armazenamento e hospedagem de website como um serviço.

### Facilidades
Não precisamos, por exemplo, de nos preocuparmos com o estado deste computador, se ele está ligado, e afins, pois isso fica a cargo de um provedor de serviços.

### Outras ocorrencias
Além de armazenamento, podemos observar o Cloud Computing atuando em armazenar Softwares onde os clientes acessem via navegador, e o Software está executando na Clound. Isso se chama Software as a Service (SaaS).

![alt text](assets/diagrama_cloud_computing.png)

## FUNCIONALIDADES COMUNS NA NUVEM

Armazenamento de dados

Um dos recursos mais populares da nuvem é o armazenamento de dados. Serviços de armazenamento em nuvem são oferecidos por provedores como Google, Microsoft, Amazon e Dropbox, permitindo acessar dados de qualquer dispositivo conectado à Internet. Isso elimina a necessidade de transferências manuais de arquivos e é uma opção confiável para backups e recuperação de dados, garantindo a disponibilidade das informações em caso de falhas.

Muitas aplicações em celulares e notebooks fazem uso desse recurso em suas operações. Anteriormente, os dados eram armazenados localmente em discos rígidos, SSDs e outros dispositivos físicos. Com os avanços tecnológicos, o armazenamento em nuvem se tornou mais popular, permitindo que os usuários armazenem seus dados de forma segura e acessível em servidores remotos.

Compartilhamento de arquivos

Outro recurso bem comum é o compartilhamento de arquivos, a nuvem facilita a colaboração e o compartilhamento de arquivos entre equipes. Ferramentas como Google Docs, Google Drive, Microsoft OneDrive, iCloud e Trello permitem criar, acessar, editar e colaborar em documentos, fotos, planilhas e apresentações, sincronizando e salvando tudo em tempo real na nuvem. Para isso, você só precisa de um dispositivo com conexão à Internet.

Hospedagem de aplicativos

A nuvem também permite a hospedagem de aplicativos, facilitando para pessoas desenvolvedoras e empresas gerenciarem seus aplicativos de maneira escalável e confiável, sem precisar configurar e manter servidores físicos. Amazon Web Services (AWS), Microsoft Azure e Google Cloud Platform possuem vários serviços que podem ser utilizados com essa finalidade.

Processamento de dados

Além de tudo o que já comentamos, a nuvem pode ser usada para processamento de dados, executando tarefas de processamento, análise e armazenamento de grandes volumes de dados.

A flexibilidade e acessibilidade oferecidas pela nuvem são essenciais para indivíduos e empresas modernas, promovendo uma maior colaboração e inovação. À medida que a tecnologia evolui, é provável que vejamos ainda mais recursos e capacidades sendo integrados às soluções em nuvem, solidificando ainda mais sua posição como uma ferramenta indispensável no cotidiano.

## ENTENDENDO ONDE ESTÁ A NUVEM
Indo em um site, na aba de inspecionar > rede, podemos observar as nossas solicitações.

Quando clicamos em algum botão, ou realizamos alguma ação, visualizamos que uma série de Solicitações de Recursos são feitas, e essas solicitações são feitas ao Servidor que está armazenando este site e, ao mesmo tempo, o Servidor está retornando o conteudo da escola de programação.

E o que faz a ligação entre o dispositivo do cliente e o servidor (que pode estar como serviço de computação em nuvem) é a internet. Ou melhor, são as redes de computadores.
> A internet é um sistema global de redes de computadores interligadas.