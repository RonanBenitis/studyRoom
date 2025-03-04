# <span style="color: #87BBA2">===   DevOps: explorando conceitos, comandos e scripts no Linux CLI   ===</span> <!-- omit in toc -->

# <span style="color: #87BBA2">INDICE</span> <!-- omit in toc -->
- [LINUX E DEVOPS](#linux-e-devops)
  - [MUNDO DEVOPS](#mundo-devops)
    - [Abordagem DevOps](#abordagem-devops)
    - [Virtual Machine](#virtual-machine)
    - [VirtualBox da Oracle](#virtualbox-da-oracle)
    - [Passo a passo](#passo-a-passo)
    - [Baixando Ubuntu](#baixando-ubuntu)
  - [CONFIGURANDO UM AMBIENTE LINUX](#configurando-um-ambiente-linux)
    - [Passo a passo](#passo-a-passo-1)
      - [Avançando: Opções de Memória](#avançando-opções-de-memória)
      - [Avançando: Disco Rígido Virtual](#avançando-disco-rígido-virtual)
      - [IMPORTANTE: Sobre as Specs](#importante-sobre-as-specs)
      - [Avançando: Sintese](#avançando-sintese)
      - [Avançando: Iniciando VM](#avançando-iniciando-vm)
    - [É comum nós estarmos próximos do servidor quando colocamos um software em produção?](#é-comum-nós-estarmos-próximos-do-servidor-quando-colocamos-um-software-em-produção)
  - [WSL COMO ALTERNATIVA AO USO DO VIRTUALBOX](#wsl-como-alternativa-ao-uso-do-virtualbox)
    - [O que é WSL?](#o-que-é-wsl)
  - [ACESSO VIA SSH](#acesso-via-ssh)
    - [Porque Linux?](#porque-linux)
    - [O que é Sistema Operacional?](#o-que-é-sistema-operacional)
    - [Acesso remoto, CONFORME ALURA](#acesso-remoto-conforme-alura)
    - [Passo a passo](#passo-a-passo-2)
    - [Acessando VM](#acessando-vm)
    - [Acesso Remoto com Port Forwarding e Conexão NAT (não bridge)](#acesso-remoto-com-port-forwarding-e-conexão-nat-não-bridge)
    - [**📌 Melhor não usar modo Bridge?**](#-melhor-não-usar-modo-bridge)
    - [**📌 Como conectar via SSH usando NAT (mais seguro)**](#-como-conectar-via-ssh-usando-nat-mais-seguro)
    - [**1️⃣ Configure o Port Forwarding no VirtualBox**](#1️⃣-configure-o-port-forwarding-no-virtualbox)
    - [**2️⃣ Descubra o IP da VM**](#2️⃣-descubra-o-ip-da-vm)
    - [**3️⃣ Conectar via SSH do Windows (CMD ou PowerShell)**](#3️⃣-conectar-via-ssh-do-windows-cmd-ou-powershell)
    - [**4️⃣ Insira a senha da VM**](#4️⃣-insira-a-senha-da-vm)
    - [**📌 Conclusão: NAT + Port Forwarding é mais seguro!**](#-conclusão-nat--port-forwarding-é-mais-seguro)
  - [MAIS SOBRE NAT E BRIDGE](#mais-sobre-nat-e-bridge)
    - [**📌 O que é NAT e Bridge no VirtualBox?**](#-o-que-é-nat-e-bridge-no-virtualbox)
    - [**1️⃣ NAT (Network Address Translation) - Modo padrão do VirtualBox**](#1️⃣-nat-network-address-translation---modo-padrão-do-virtualbox)
    - [**2️⃣ Bridge (Placa em modo Bridge - Ponte)**](#2️⃣-bridge-placa-em-modo-bridge---ponte)
    - [**📌 Por que a VM consegue acessar a internet no modo NAT?**](#-por-que-a-vm-consegue-acessar-a-internet-no-modo-nat)
    - [**📌 Qual escolher?**](#-qual-escolher)
    - [**📌 Conclusão**](#-conclusão)
    - [**📌 Como o NAT funciona para conexão na internet?**](#-como-o-nat-funciona-para-conexão-na-internet)
    - [**🛠 Como o NAT funciona no VirtualBox?**](#-como-o-nat-funciona-no-virtualbox)
    - [**📌 "Mas o NAT não abre brecha de segurança como o Bridge?"**](#-mas-o-nat-não-abre-brecha-de-segurança-como-o-bridge)
    - [**🔒 NÃO! Ele é seguro porque:**](#-não-ele-é-seguro-porque)
    - [**📌 Como funciona o NAT no meu PC quando estou no Wi-Fi de casa?**](#-como-funciona-o-nat-no-meu-pc-quando-estou-no-wi-fi-de-casa)
    - [**📌 Conclusão**](#-conclusão-1)
  - [COMANDOS PARA PRATICAR](#comandos-para-praticar)
- [EXPLORANDO O LINUX SERVER](#explorando-o-linux-server)
  - [NAVEGANDO NO LINUX SERVER](#navegando-no-linux-server)
    - [**Escalando privilégios com `sudo`**](#escalando-privilégios-com-sudo)
    - [**Verificando pacotes e atualizações**](#verificando-pacotes-e-atualizações)
    - [**📌 Significado de algumas siglas importantes**](#-significado-de-algumas-siglas-importantes)
    - [**📌 O que é Shell CLI?**](#-o-que-é-shell-cli)
    - [**📌 Por que o nome "Shell"?**](#-por-que-o-nome-shell)
    - [**📌 Tipos de Shell**](#-tipos-de-shell)
    - [**📌 Shell no contexto do VirtualBox e Ubuntu**](#-shell-no-contexto-do-virtualbox-e-ubuntu)
    - [**📌 Estrutura Geral de um Comando no Linux**](#-estrutura-geral-de-um-comando-no-linux)
    - [**📌 Exemplo 1: Comando `ls`**](#-exemplo-1-comando-ls)
    - [**📌 Exemplo 2: Comando `sudo apt install`**](#-exemplo-2-comando-sudo-apt-install)
    - [**📌 Tipos de Elementos em um Comando**](#-tipos-de-elementos-em-um-comando)
    - [**📌 Teste na Prática**](#-teste-na-prática)
    - [Criando um diretório (pasta) e indo até ele](#criando-um-diretório-pasta-e-indo-até-ele)
  - [GERENCIANDO ARQUIVOS](#gerenciando-arquivos)
    - [Criando arquivo (touch)](#criando-arquivo-touch)
    - [Inserindo notas e conferindo (cat)](#inserindo-notas-e-conferindo-cat)
    - [Alternativas de inserção de conteúdo com echo](#alternativas-de-inserção-de-conteúdo-com-echo)
    - [Outra alternativa comum para edição de texto (nano)](#outra-alternativa-comum-para-edição-de-texto-nano)
    - [Movendo arquivos (mv)](#movendo-arquivos-mv)
    - [Removendo arquivos (rm)](#removendo-arquivos-rm)
  - [REMOVENDO ARQUIVOS E DIRETÓRIOS](#removendo-arquivos-e-diretórios)
  - [IMPORTANTE DICA](#importante-dica)
  - [PARAMETROS DE LISTAGEM](#parametros-de-listagem)
  - [Praticando](#praticando)
    - [Outra atividade](#outra-atividade)
- [SHELL SCRIPTING](#shell-scripting)
  - [CONSTRUINDO SCRIPTS NO SHELL](#construindo-scripts-no-shell)
    - [Caso prático](#caso-prático)
    - [Criando Shell Script](#criando-shell-script)
  - [PARA SABER MAIS: TESTANDO DIFERENTES CONDIÇÕES](#para-saber-mais-testando-diferentes-condições)
    - [Igualdade entre duas strings](#igualdade-entre-duas-strings)
    - [Desigualdade entre duas strings](#desigualdade-entre-duas-strings)
    - [Igualdade entre dois números](#igualdade-entre-dois-números)
    - [Desigualdade entre dois números](#desigualdade-entre-dois-números)
    - [Testando se um número é maior que outro](#testando-se-um-número-é-maior-que-outro)
    - [Testando se um número é menor que outro](#testando-se-um-número-é-menor-que-outro)
    - [Testando se um número é maior ou igual a outro](#testando-se-um-número-é-maior-ou-igual-a-outro)
    - [Verificando a existência de um arquivo ou diretório](#verificando-a-existência-de-um-arquivo-ou-diretório)
  - [PASSAGEM DE PARAMETROS](#passagem-de-parametros)
    - [Scripts com parametros](#scripts-com-parametros)
      - [Validando se parametros foram passados](#validando-se-parametros-foram-passados)
      - [Pegando os parametros](#pegando-os-parametros)
      - [Compactando](#compactando)
      - [Script completo](#script-completo)
      - [Executando script](#executando-script)
  - [PARA SABER MAIS: PASSANDO PARAMETROS EM SCRIPTS](#para-saber-mais-passando-parametros-em-scripts)
  - [**📌 Diferença entre `$VARIAVEL` e `${VARIAVEL}`**](#-diferença-entre-variavel-e-variavel)
    - [**🎯 Exemplo prático: Quando `${}` é necessário**](#-exemplo-prático-quando--é-necessário)
    - [**📌 Segurança e legibilidade**](#-segurança-e-legibilidade)
    - [**🔥 Resumo final**](#-resumo-final)
  - [EXEMPLOS DE SCRIPT](#exemplos-de-script)
    - [Verificando existencia de arquivos na pasta](#verificando-existencia-de-arquivos-na-pasta)
    - [Verifique a validade do caminho informado](#verifique-a-validade-do-caminho-informado)
    - [Exiba uma mensagem de boas-vindas quando executado](#exiba-uma-mensagem-de-boas-vindas-quando-executado)
    - [Criar uma cópia de segurança de um diretório específico](#criar-uma-cópia-de-segurança-de-um-diretório-específico)
    - [Solicite ao usuário o nome de um diretório e, em seguida, o crie](#solicite-ao-usuário-o-nome-de-um-diretório-e-em-seguida-o-crie)
    - [Aceite um nome de arquivo como argumento e verifique se o arquivo existe](#aceite-um-nome-de-arquivo-como-argumento-e-verifique-se-o-arquivo-existe)
    - [Utilize um loop para contar de 1 a 5](#utilize-um-loop-para-contar-de-1-a-5)
- [AUTOMATIZAÇÃO DE TAREFAS](#automatização-de-tarefas)
  - [EXECUTANDO MULTIPLAS TAREFAS](#executando-multiplas-tarefas)
    - [Notas](#notas)
      - [Sintaxe case](#sintaxe-case)
      - [Descompactando](#descompactando)
  - [SHELL SCRIPTING COM APENAS OS DOCUMENTOS](#shell-scripting-com-apenas-os-documentos)
    - [Compactando apenas arquivos](#compactando-apenas-arquivos)
    - [Compactando caminho, descompactando apenas os arquivos](#compactando-caminho-descompactando-apenas-os-arquivos)
  - [FUNÇÕES DIRETAS NO CLI](#funções-diretas-no-cli)
    - [**🔥 Criando uma função direto no CLI**](#-criando-uma-função-direto-no-cli)
    - [**📌 Passando parâmetros para a função**](#-passando-parâmetros-para-a-função)
    - [**📌 Funções mais complexas**](#-funções-mais-complexas)
    - [**📌 Mas e se eu fechar o terminal?**](#-mas-e-se-eu-fechar-o-terminal)
    - [**🚀 Resumo**](#-resumo)
  - [QUANDO USAR E QUANDO NÃO USAR ASPAS](#quando-usar-e-quando-não-usar-aspas)
    - [**1️⃣ Por que `"$arquivo_saida"` e `"$caminho"` têm aspas?**](#1️⃣-por-que-arquivo_saida-e-caminho-têm-aspas)
    - [**2️⃣ Por que `$arquivos` está sem aspas?**](#2️⃣-por-que-arquivos-está-sem-aspas)
    - [**📌 Regra Geral**](#-regra-geral)
    - [**Resumo**](#resumo)
  - [INSTALANDO UM SERVIDOR WEB](#instalando-um-servidor-web)
    - [O que é um servidor web](#o-que-é-um-servidor-web)
    - [Insalando Nginx em nosso servidor](#insalando-nginx-em-nosso-servidor)
      - [Verificando servidor web](#verificando-servidor-web)
  - [CONVERSÃO DE ARQUIVOS](#conversão-de-arquivos)
    - [Script](#script)
  - [EXEMPLO DE SCRIPTS](#exemplo-de-scripts)
    - [automatiza a atualização de pacotes do sistema operacional.](#automatiza-a-atualização-de-pacotes-do-sistema-operacional)
    - [renomeie todos os arquivos em um diretório, adicionando um prefixo ou sufixo especificado](#renomeie-todos-os-arquivos-em-um-diretório-adicionando-um-prefixo-ou-sufixo-especificado)
    - [automatiza a criação de usuários no sistema, solicitando ao usuário que forneça o nome e outros detalhes necessários](#automatiza-a-criação-de-usuários-no-sistema-solicitando-ao-usuário-que-forneça-o-nome-e-outros-detalhes-necessários)
    - [monitorar o espaço em disco usando o comando df na coleta de informações](#monitorar-o-espaço-em-disco-usando-o-comando-df-na-coleta-de-informações)
    - [**📌 O que acontece em `espaco`?**](#-o-que-acontece-em-espaco)
      - [**1️⃣ `df -h` → Verifica o espaço em disco**](#1️⃣-df--h--verifica-o-espaço-em-disco)
      - [**2️⃣ `awk 'NR==2 {print $5}'` → Filtra a linha e coluna certas**](#2️⃣-awk-nr2-print-5--filtra-a-linha-e-coluna-certas)
      - [**3️⃣ `sed 's/%//'` → Remove o símbolo `%`**](#3️⃣-sed-s--remove-o-símbolo-)
    - [**📌 Recapitulando o que acontece**](#-recapitulando-o-que-acontece)
    - [**📌 Exemplo prático**](#-exemplo-prático)
    - [automatizar o backup de um diretório específico para um local de destino, utilizando a compressão gzip](#automatizar-o-backup-de-um-diretório-específico-para-um-local-de-destino-utilizando-a-compressão-gzip)

# <span style="color: #87BBA2">LINUX E DEVOPS</span>

## MUNDO DEVOPS
Contextualizado em um mundo onde o ambiente de desenvolvimento de software é departamentalizado, separado, e a colaboração e integração torna-se um fator de alta importancia.

Assim que uma aplicação estiver pronta, testada e aprovada, ela precisará ser colocada de forma disponível aos usuários, seu publico alvo. O que irá cuidar do local onde nossa aplicação estará disponivel aos usuário, será a infraestrutura.

O time de pessoas dedicadas a manutenção e monitoramento desta parte do sistema é o time de operações. Ou seja, é o time que lida com as tarefas da implementação e manutenção de um sistema em produção.

- Devs: Responsaveis pela construção da aplicação;
- DevOps: Integra desenvolvimento e operações;
  - Ou seja, disponibilizar e manter de forma eficiente aos seu usuários.

### Abordagem DevOps
Cultura que surge para integrar essas duas equipes e torna-las responsáveis pela criação, manutenção, desempenho, segurança e eficiente à aplicação que está sendo disponibilizada aos usuários.

**Aí que nasce o DevOps, que é a união do termo "Developer" com "Operations".**

### Virtual Machine
Maquina virtual, ou VM, pode ser descrita como:
- uma duplicata eficiente e isolada de uma maquina real;
- cópia isolada de um sistema físico, sendo totalmente protegida
  - segundo Alura: um software que emula o funcionamento de um sistema operacional sobre um outro sistema operaciona no mesmo dispositivo, tendo, sob um único hardware diferentes sistemas operacionais em funcionamento.

### VirtualBox da Oracle
Para utilizar uma Virtual Machine, utilizaremos o Virtual Box da Oracle, onde podemos baixá-lo neste [link.](https://www.virtualbox.org/wiki/Downloads)
> Ideal baixarmos sempre a ultima versão.

Para instruções de como baixá-lo, [veja aqui a partir dos minutos 4:13](https://cursos.alura.com.br/course/devops-conceitos-comandos-scripts-linux-cli/task/146504)

### Passo a passo
1. Abrimos o Virtual Box
2. Clicamos em **Novo**
   1. Uma janela será aberta
3. Damos o nome "Linux" à VM
   1. Note que a segunda opção é **a pasta**, ou seja, é o local onde serão armazenados todos os arquivos relacionados a esta VM
4. Na imagem ISO, precisaremos subir a imagem do sistema operacional que utilizaremos nessa VM
   1. No nosso caso, é o Ubuntu, precisaremos baixar essa imagem

### Baixando Ubuntu
O site para realizar o download da ISO do Ubuntu é [este site](https://ubuntu.com/download);
- Lá, existem varias opções de imagem. Nós queremos a imagem para Servidores, que é o que normalmente colocamos no ambiente de produção.
- **Importante**: Na aba de "Manual server installation", queremos baixar a versão mais recenete **que possua o termo LTS** ao seu lado, ou seja, Long Term Support, pois, como nosso servidor funcionará por um longo período de tempo, queremos que ele seja o mais estável possível.

## CONFIGURANDO UM AMBIENTE LINUX

### Passo a passo
1. Retornamos a aba de "Novo" e na imagem ISO colocamos o arquivo .iso que baixamos
2. Na caixa "Pular Instalação Desassistida" é importantíssimo seleciona-la
   1. Nesta etapa, gostariamos de realizar a configuração manualmente para vermos na prática como funcionará

#### Avançando: Opções de Memória
1. Na proxima tela, teremos as opções de memória
   1. Importante **NÃO** alocarmos toda a memória de nosso PC e nem todos os nossos processadores, recomendando, para este cenário, não passar de 1/3 da memória e 2 processadores.
   2. No nosso caso, não necessitaremos de mais do que 2048MB de memória. Então, deixaremos como 4096MB
   3. Para os processadores, pegaremos dois.

#### Avançando: Disco Rígido Virtual
1. Aqui, no Disco Rígido Virtual, deixaremos como a opção **default**, pois, não precisaremos mais do que 25 GB

#### IMPORTANTE: Sobre as Specs
Na prática, quando nós formos configurar um servidor para hospedaremos a solução que estamos construíndo, precisaremos analisar com maior cuidado esses detalhes e especificações, de acordo com o sistema que deixaremos em execução.

#### Avançando: Sintese
1. Aparecerá uma sintese do que escolhemos e, então, clicamos em finalizar.

#### Avançando: Iniciando VM
1. No menu superior, clique em iniciar
2. Selecionamos a opção "Try or install Ubuntu Server".
3. Escolha a lingua desejada
4. Na variante do teclado, vemos que já está em Português, avançamos
5. No "base for the installation", escolheremos, para esta aula, o **Ubuntu Server (minimized)**, sendo a opção do meio.
   1. Clique espaço para selecionar a opção
   2. A barra de seleção vai apra "Cocluido / Voltar" e clicamos "Enter" em Concluído para avançar a tela
6. Proxima tela é a configuração de ligações de rede
   1. Como iremos querer fazer o acesso remoto desta VM usando SSH, é importante garantir que nós estejamos vinculando esta VM com uma placa de rede física.
   2. Precisamos só garantir que estamos vinculando a uma placa de rede física e observarmos se já está configurado corretamente.
   3. Então, como já foi alocado e tem um DHCPv4, avançaremos.
7. Para configuração de Proxy, no momento, deixaremos default, clicamos em **Concluído**
8. Inicia-se a configuração da imagem baixando pacotes de instalação
   1. Durante a instalação do Ubuntu, o sistema precisa baixar pacotes e atualizações. Para isso, ele utiliza um mirror (espelho), que é basicamente um servidor de réplicas onde ficam armazenados os pacotes do sistema
9. Caso apareça algumas mensagens de FAILED, não tem problema. Damos um enter para avançar
10. Caso recebermos o erro de "FAILED unmounting /cdrom", não precisamos nos preocupar

**EXPLICAÇÂO DO CASO (GPT):**

Essas mensagens indicam que o sistema tentou desmontar (unmount) o /cdrom (o disco de instalação do Ubuntu), mas falhou. Vamos entender melhor:

📌 O que significa "Failed unmounting /cdrom"?
Durante a instalação do Ubuntu em uma VM, a ISO (imagem do sistema) é montada como um CD virtual no diretório /cdrom. Quando a instalação termina, o sistema tenta desmontar (unmount) essa mídia antes de reiniciar.

Porém, essa desmontagem pode falhar por alguns motivos, como:

- A ISO ainda está em uso → O sistema pode estar acessando arquivos da ISO no momento da desmontagem.
- Processo bloqueado → Algum serviço pode estar travado e impedindo a desmontagem.
- Erro normal do VirtualBox → Em VMs, essa falha é comum e geralmente não causa problemas.

📌 O que fazer quando isso acontece?
No seu caso, a instalação já foi concluída, então basta seguir a instrução:

"Please remove the installation medium, then press ENTER."

Isso significa que você deve:

- Ejetar a ISO do VirtualBox
  - Vá até Dispositivos → Unidade de CD/DVD → Remover disco da unidade virtual.
- Pressionar ENTER na VM para continuar.
  
Caso não remova a ISO, a VM pode tentar iniciar a instalação do Ubuntu novamente ao invés de carregar o sistema já instalado.

11. Instrutor apenas deu um ENTER e saiu da tela
12. Aparentemente, inicia-se a instalação do Ubuntu e devemos aguardar sua conclusão.
13. Agora, coloque o login e senha configurados (Particularmente, não sei onde foi configurado)
14. Após isso, a nossa VM foi configurada com sucesso

### É comum nós estarmos próximos do servidor quando colocamos um software em produção?
Não! Não é comum! Na realidade, o mais comum é nem sabermos a posição geografica deste servidor e, para acessá-lo, realizar de forma remota através da tecnologia SSH, o que veremos a seguir.

## WSL COMO ALTERNATIVA AO USO DO VIRTUALBOX
Alguns computadores podem apresentar certa lentidão e até mesmo alguns bugs quando usamos máquinas virtuais (VMs) através de softwares de virtualização como o VirtualBox.

Se este for o seu caso, temos uma alternativa de virtualização de ambiente Linux no Windows que pode facilitar bastante sua trajetória de aprendizado aqui no curso: o uso do Windows Subsystem for Linux (WSL). O WSL é um recurso do Windows 10 e Windows 11 que permite executar um ambiente Linux diretamente no Windows, sem a necessidade de uma VM. Com o WSL, você pode instalar distribuições Linux (como Ubuntu, Debian, e outras) e utilizá-las como se fossem aplicativos nativos do Windows.

Todos os passos e configurações que faremos aqui são compatíveis com o WSL, sendo assim você não terá nenhuma perda de aprendizado ao optar por esse ambiente.

Para começar a usar o WSL, siga os passos abaixo:
1. Abra o PowerShell como administrador e execute o comando wsl --install.
2. Após a instalação inicial, você pode instalar outras distribuições disponíveis na Microsoft Store. Assim, basta escolher a distribuição Ubuntu (a mesma que estamos usando no curso).
3. Para acessar o WSL, basta procurar pela distribuição instalada no menu iniciar (pesquise, por exemplo, "Ubuntu"). Com alguns poucos passos, você terá um terminal Linux pronto para dar sequência aqui no curso!

### O que é WSL?
WSL significa Windows Subsystem for Linux (ou Subsistema Linux para Windows) e permite que desenvolvedores executem um ambiente GNU/Linux diretamente no Windows, sem precisar de uma máquina virtual ou realizar um dual-boot.

Essa ferramenta já está em funcionamento há alguns anos e atualmente conta com sua segunda versão publicada, o WSL2.

O grande benefício de conhecer e utilizar essas ferramentas, incluindo o seu contexto de estudos aqui na Alura, é que fica muito mais fácil de seguir os passos de colegas que já utilizam sistemas Linux como ambiente de desenvolvimento.

Outra vantagem é que, ao compreender mais esses recursos, podemos nos adequar a grandes comunidades que usam o Linux com muito peso, como os usuários da ferramenta Docker.

Temos um [artigo que você pode consultar caso tenha alguma dúvida em relação ao processo de configuração e funcionamento do WSL](https://www.alura.com.br/artigos/wsl-executar-programas-comandos-linux-no-windows).

## ACESSO VIA SSH

### Porque Linux?
O Linux é um projeto open source (código aberto) de sistema operacional registrado sob a licença GPL, uma licença pública geral. Dessa forma, podemos utilizar esse projeto, criar outras versões para dispositivos específicos, seja um dispositivo IoT, servidor ou smartphone, gratuitamente e nos comprometemos em deixar esse projeto que criamos também de forma aberta.

Mas, o Linux não é um sistema operacional, e sim um núcel (Kernel) de sistema operacional, sendo a base principal que utilizamos para criar diferentes distribuições, sendo as distribuições as que chamamos de **distros**, como o Ubuntu, Fedora, Android etc.

Quase toda a infraestrutura da internet é construida sobre o kernel do Linux.

### O que é Sistema Operacional?
Não trata-se de uma caixinha, mas sim, módulos que são integrados para oferecer uma série de funcionalidades ao usuário final. O Kernel é a parte principal, o núcleo, mas de acordo com a aplicação ou o dispositivo onde esse sistema será instalado pode-se adicionar outros módulos, como drivers e etc.

### Acesso remoto, CONFORME ALURA
Utilizaremos o protocolo SSH, que permite a conexão com uma máquina de forma remota.

### Passo a passo
Precisaremos:
1. IP da VM

Mas antes, precisamos fazer:
**ATENÇÃO, VEJA O MÉTODO PORT FORWARDING ABAIXO, É MAIS SEGURO**
1. Na VM aberta (olhando no terminal), vamos no menu Dispositivos
   1. Rede
   2. Configurações de rede
   3. Alterar o "Conectado a" de NAT para Placa em modo Bridge
   4. E o Name precisará mostrar uma placa física, realmente
   5. Clique ok
2. Agora, digite o comando `ip address`
   1. Observamos a interface "loopback" que é a interface que a máquina usa para falar com ela mesma
   2. Observamos a interface, também, outra interface com um nome mais complicada (enp0s3), é nessa interface que receberemos o endereço de IP
   3. As vezes ela não aparece de imediato, caso realizamos alguma alteração recente (como a de passagem de NAT para Bridge), aí precisamos esperar um pouco mesmo
3. Demos um tempo e digitamos o comando `ip_address` novamente, mas, sem sucesso de retorno
   1. Vamos no menu Dispositivo > rede
   2. Clicar em Conectar Placa de Rede
4. `ip_address` de novo, e na interface enp0s3 vimos que estabeleceu o IP: 192.168.40.36, no caso.

### Acessando VM
1. Vamos agora no prompt de comando (cmd windows)
2. digitamos `ssh username_que_definimos@endereco_da_maquina_que_desejamos_conectar`
   1. No exemplo do instrutor: `ssh lucasrm@192.168.40.36`
   2. Dado enter
3. Dando certo, solicitará a senha e inserimos a senha
4. Após isso, teremos em nosso prompt algo como `username@username: $`
   1. Isso indica que estamos dentro de nossa VM e os comandos que inserimos rodará nela.
5. Agora, rodemos o comando `ls`, que é o comando de listar no Linux, e veremos que nada será retornado. Isso é um sucesso, pois, quer dizer que o comando foi reconhecido e nada foi retornado pois de fato há nada no diretorio.

### Acesso Remoto com Port Forwarding e Conexão NAT (não bridge)
### **📌 Melhor não usar modo Bridge?**  
Sim, **para um ambiente de estudos e testes, o modo NAT é mais seguro e suficiente para conexões SSH**. O modo Bridge pode **expor sua VM na rede local**, o que pode trazer riscos caso você esteja em uma rede compartilhada ou sem firewall adequado.  

Mas **não se preocupe!** Você **ainda pode se conectar via SSH no NAT**, apenas precisa configurar o **Port Forwarding** (Redirecionamento de Portas).  

---

### **📌 Como conectar via SSH usando NAT (mais seguro)**  

### **1️⃣ Configure o Port Forwarding no VirtualBox**  
1️⃣ **Com a VM desligada**, vá até o **VirtualBox** e selecione sua VM.  
2️⃣ Clique em **Configurações → Rede**.  
3️⃣ Certifique-se de que o **Adaptador 1 está no modo NAT**.  
4️⃣ Clique em **Avançado → Redirecionamento de Portas**.  
5️⃣ Adicione uma nova regra com os seguintes valores:  
   - **Nome**: SSH  
   - **Protocolo**: TCP  
   - **Porta do host**: `2222` *(pode ser outra, mas lembre-se dela)*  
   - **IP do convidado**: `10.0.2.15` *(IP padrão do NAT no VirtualBox)*  
   - **Porta do convidado**: `22` *(porta padrão do SSH no Linux)*  
6️⃣ **Clique em OK e inicie a VM**.  

---

### **2️⃣ Descubra o IP da VM**  
Dentro da VM, abra o terminal e rode:  

```bash
ip address
```
📌 No modo NAT, o IP padrão geralmente será **`10.0.2.15`**.  

Se quiser confirmar, rode:  

```bash
hostname -I
```

---

### **3️⃣ Conectar via SSH do Windows (CMD ou PowerShell)**  
Agora, no seu **Prompt de Comando (CMD)** do Windows, use:  

```bash
ssh -p 2222 username@localhost
```
📌 **Substitua "username" pelo usuário da sua VM** (exemplo: `ssh -p 2222 ronan@localhost`).  

---

### **4️⃣ Insira a senha da VM**  
Se tudo estiver certo, ele pedirá sua senha. **Digite-a** e pronto! 🚀 Agora você está conectado à VM **sem precisar do modo Bridge**.  

---

### **📌 Conclusão: NAT + Port Forwarding é mais seguro!**  
✅ **Modo NAT protege sua VM de acessos externos.**  
✅ **Port Forwarding permite acessar via SSH sem expor a VM na rede.**  
✅ **Mais seguro para estudo e testes.**  

Se precisar de mais alguma ajuda na configuração, só chamar! 🔥

Ótima pergunta! Vamos esclarecer isso de forma simples e prática.  

---

## MAIS SOBRE NAT E BRIDGE

### **📌 O que é NAT e Bridge no VirtualBox?**  

Essas são **configurações de rede** que definem **como sua VM se conecta à rede e à internet**.  

---

### **1️⃣ NAT (Network Address Translation) - Modo padrão do VirtualBox**  

🔹 **Como funciona?**  
- O VirtualBox **cria uma rede privada interna** para a VM.  
- Sua VM **não está diretamente visível** na rede local, apenas o seu **PC hospedeiro** (Windows).  
- Quando a VM quer acessar a internet, **o VirtualBox faz a tradução de endereço** e envia o tráfego pela conexão do seu PC.  

🔹 **Resumo:**  
✅ A VM **tem acesso à internet** automaticamente.  
✅ É **segura**, pois **não fica visível na rede local**.  
❌ **Outros dispositivos da rede não conseguem acessar a VM facilmente** (precisa de Port Forwarding para isso).  

💡 **Exemplo de uso:**  
✔ Quando você **só precisa acessar a internet a partir da VM**.  
✔ Quando quer **evitar exposição desnecessária da VM na rede**.  

---

### **2️⃣ Bridge (Placa em modo Bridge - Ponte)**  

🔹 **Como funciona?**  
- A VM **se conecta diretamente à rede local**, como se fosse um outro computador físico na mesma rede.  
- Ela recebe um **IP diretamente do roteador**, assim como seu PC hospedeiro.  

🔹 **Resumo:**  
✅ A VM **fica visível na rede local**, podendo ser acessada por outros dispositivos.  
✅ A VM pode **se comunicar facilmente com outros computadores** na rede.  
❌ **Pode ser inseguro**, pois expõe a VM como se fosse um PC normal na rede.  

💡 **Exemplo de uso:**  
✔ Se você quer rodar um **servidor que deve ser acessado por outros dispositivos na rede**.  
✔ Se você precisa **simular um ambiente real de rede**.  

---

### **📌 Por que a VM consegue acessar a internet no modo NAT?**  
Mesmo estando isolada, a VM pode acessar a internet porque o **VirtualBox age como um "roteador virtual"**. Ele recebe as solicitações da VM e as repassa para a internet, como se fosse um intermediário.  

É o mesmo princípio que acontece com seu Wi-Fi em casa:  
1️⃣ Seu computador tem um IP privado, mas acessa a internet porque o **roteador traduz os endereços**.  
2️⃣ No NAT do VirtualBox, a VM tem um IP privado, mas acessa a internet através do seu PC hospedeiro.  

---

### **📌 Qual escolher?**  
✅ **Para estudo e segurança** → Use **NAT** (e adicione Port Forwarding se precisar de acesso externo).  
✅ **Para testes de rede ou simulação de servidores** → Use **Bridge** (mas cuidado com a segurança).  

Se precisar acessar a VM externamente, mas quiser manter NAT, pode usar **Port Forwarding**, como expliquei antes.  

---

### **📌 Conclusão**  
✔ **NAT** → Seguro, fácil, já conecta à internet, mas sem acesso direto da rede.  
✔ **Bridge** → Mais liberdade na rede local, mas expõe a VM.  
✔ **Sua VM acessa a internet no NAT porque o VirtualBox faz a tradução de endereços**.  

Se precisar de mais alguma explicação, só chamar! 🚀🔥

Ótima pergunta, parceiro! Vamos entender isso de forma clara e conectada ao mundo real.  

---

### **📌 Como o NAT funciona para conexão na internet?**  

O **NAT (Network Address Translation - Tradução de Endereços de Rede)** é um método que permite que sua VM **use a conexão de internet do PC Host sem estar diretamente exposta à rede**.  

### **🛠 Como o NAT funciona no VirtualBox?**  
1️⃣ **Sua VM recebe um IP privado (exemplo: `10.0.2.15`)**.  
2️⃣ **Quando a VM quer acessar a internet**, ela envia a solicitação para o VirtualBox.  
3️⃣ **O VirtualBox age como um "roteador" e troca o IP da VM pelo IP do Host**.  
4️⃣ O tráfego vai para a internet como se fosse o Host acessando.  
5️⃣ Quando a resposta chega, o VirtualBox traduz de volta para a VM.  

🔹 **Isso é igual ao que acontece no seu Wi-Fi em casa!** (Explico isso já já 👇).  

🔹 **A VM nunca aparece diretamente na rede local**, apenas o **Host** faz essa mediação.  

---

### **📌 "Mas o NAT não abre brecha de segurança como o Bridge?"**  

### **🔒 NÃO! Ele é seguro porque:**  
✅ **A VM não está visível na rede local** (ela não tem um IP público na rede).  
✅ **Outros dispositivos na rede não podem acessá-la diretamente**.  
✅ **Somente o VirtualBox sabe que a VM existe e controla o tráfego**.  
✅ Mesmo que sua VM tenha um serviço rodando (exemplo: um servidor web), **ninguém da rede local consegue acessá-la diretamente** sem configurações extras (como Port Forwarding).  

📌 **Já no modo Bridge, a VM recebe um IP da rede local e fica exposta, podendo ser acessada por qualquer máquina da rede.**  

---

### **📌 Como funciona o NAT no meu PC quando estou no Wi-Fi de casa?**  

🔹 Seu **roteador Wi-Fi em casa faz NAT o tempo todo** para que seus dispositivos (PC, celular, TV) possam acessar a internet.  

💡 **Exemplo prático:**  
1️⃣ Você conecta seu PC e seu celular ao Wi-Fi de casa.  
2️⃣ O roteador dá a cada dispositivo um **IP privado** (exemplo: `192.168.1.100`, `192.168.1.101`).  
3️⃣ Quando você acessa um site (`google.com`), seu PC manda o pedido para o roteador.  
4️⃣ O roteador **troca o IP privado pelo IP público da sua internet** e envia o pedido.  
5️⃣ O site responde para o IP público, e o roteador traduz de volta para seu PC.  

🔹 **Por isso, todos os seus dispositivos compartilham o mesmo IP público, mas cada um tem um IP privado dentro da rede interna.**  

🔹 **O NAT do VirtualBox funciona igual!** A diferença é que, em vez de um roteador de Wi-Fi, é o próprio VirtualBox que faz esse papel.  

---

### **📌 Conclusão**  
✔ **NAT no VirtualBox** = Mesma ideia do seu roteador Wi-Fi.  
✔ **Seguro**, pois a VM **não fica visível na rede local**.  
✔ **A VM acessa a internet através do Host, mas sem exposição direta**.  
✔ **O Bridge expõe a VM diretamente na rede, podendo ser menos seguro**.  

Se precisar de mais explicações, só chamar, parceiro! 🚀🔥

## COMANDOS PARA PRATICAR
- `ls`: **list** - Lista os arquivos e diretórios existentes dentro de um diretório
- `ls -a`: **list -all** - para exibir nos resultados da listagem os arquivos e pastas ocultas existentes dentro do diretório.
- `pwd`: **print working directory** - retorna o caminho completo do diretório em que você se encontra.
- `cd /caminho/do/diretorio/desejado`: **Change directory** - Para percorrer diferentes diretórios dentro do Linux, podemos usar o seguinte comando
- `ls -l`: **ls -long** - para obter uma listagem mais detalhada, incluindo permissões, proprietário, tamanho e data de modificação dos arquivos.

# <span style="color: #87BBA2">EXPLORANDO O LINUX SERVER</span>

## NAVEGANDO NO LINUX SERVER
O que significa o `$` em um ambiente Linux?
- Significa que não somos um usuário privilegiado, ou seja, que não conseguimos executar tarefas como administradores desse sistema

-----------------------------------------------------------------------------------

### **Escalando privilégios com `sudo`**
Para executar comandos com privilégios de administrador (**root**), utilizamos a ferramenta `sudo` (**Super User DO**).  
- Qualquer ação com `sudo` pode solicitar a senha do usuário para confirmar a execução.  
- O uso de `sudo` pode ser configurado para permitir ou restringir o acesso a usuários específicos. Isso é feito editando o arquivo `/etc/sudoers` ou adicionando usuários ao grupo `sudo`.  

### **Verificando pacotes e atualizações**
Para atualizar a lista de pacotes disponíveis no sistema, utilizamos:  
```bash
sudo apt update
```
- `apt` (**Advanced Package Tool**) → Gerenciador de pacotes do Debian/Ubuntu, usado para instalar, atualizar e remover softwares.  
- `update` → Atualiza a lista de pacotes disponíveis nos repositórios, mas **não instala nada**.  

Depois de atualizar a lista, se quisermos realmente atualizar os pacotes para suas versões mais recentes, usamos:  
```bash
sudo apt upgrade
```
- `upgrade` → Instala as versões mais recentes dos pacotes já instalados.  

---

### **📌 Significado de algumas siglas importantes**
Aqui estão algumas siglas de comandos comuns no Linux:  

- **`sudo`** → **Super User DO** (executa comandos como administrador).  
- **`apt`** → **Advanced Package Tool** (gerenciador de pacotes do Debian/Ubuntu).    
- **`ls`** → **List** (lista arquivos e diretórios).  
- **`cd`** → **Change Directory** (muda de diretório).  
- **`pwd`** → **Print Working Directory** (exibe o diretório atual).  
- **`rm`** → **Remove** (remove arquivos/diretórios).  
- **`mv`** → **Move** (move ou renomeia arquivos).  
- **`cp`** → **Copy** (copia arquivos).  
- **`chmod`** → **Change Mode** (muda permissões de arquivos).
  - Usar o comando chmod com a opção +x concede permissão de execução a um script em Bash. Por exemplo, você pode executar o comando chmod +x meu_script.sh para tornar o script "meu_script.sh" executável no Ubuntu.
- **`chown`** → **Change Owner** (muda o dono de um arquivo).  

Para mais retirar mais duvidas sobre os comandos disponiveis, podemos rodar o comando `help`.

### **📌 O que é Shell CLI?**  
O **Shell** é um interpretador de comandos que permite interagir com o sistema operacional digitando instruções. Ele funciona como uma ponte entre o usuário e o kernel (o núcleo do sistema).  

Ou seja, **Shell** é um programa que atua como uma **camada de comunicação** entre o usuário e o **kernel** (o núcleo do sistema operacional). Ele interpreta os comandos digitados pelo usuário e os repassa para o sistema operacional executar.  

Ele permite:  
✅ Executar programas e comandos  
✅ Gerenciar arquivos e diretórios  
✅ Automatizar tarefas com scripts  
✅ Configurar o sistema  

A **CLI (Command Line Interface)** é a interface baseada em texto onde esses comandos são inseridos. Diferente de uma interface gráfica (GUI), onde usamos cliques e janelas, na CLI **interagimos diretamente com o sistema via comandos**.  

### **📌 Por que o nome "Shell"?**  
O nome **Shell** (que significa "casca" em inglês) foi escolhido porque ele funciona como uma **camada externa** que envolve e protege o kernel do sistema operacional.  

- O **Kernel** é a parte mais interna e essencial do sistema operacional, responsável por gerenciar hardware e processos.  
- O **Shell** atua como uma "casca protetora" que permite ao usuário interagir com o sistema sem acessar diretamente o kernel.  

🔹 **Analogia:** Imagine um computador como uma **noz**:  
- O **kernel** é o miolo interno (o núcleo do sistema).  
- O **shell** é a casca protetora que permite acessar o conteúdo sem danificá-lo.  


### **📌 Tipos de Shell**  
No Linux, existem diferentes tipos de Shell, sendo os mais populares:  
- **Bash (Bourne Again Shell)** → O mais usado no Linux e Ubuntu.  
- **Zsh (Z Shell)** → Uma versão mais avançada do Bash, com mais recursos.  
- **Fish (Friendly Interactive Shell)** → Focado em interatividade e facilidade de uso.  

Como você está usando o Ubuntu no VirtualBox, o padrão é o **Bash**. Você pode verificar qual Shell está usando com:  
```bash
echo $SHELL
```

### **📌 Shell no contexto do VirtualBox e Ubuntu**  
No **VirtualBox**, ao instalar o Ubuntu, você pode interagir com o sistema de duas formas:  
1. **Interface Gráfica (GUI)** → Se estiver usando o Ubuntu Desktop, verá uma tela com botões, menus e janelas.  
2. **Shell CLI** → Se estiver no Ubuntu Server (ou acessando o terminal no Desktop), estará interagindo apenas por linha de comando.  

No seu caso, como você está configurando a VM, é provável que esteja lidando com o **Shell CLI** para instalar pacotes, configurar a rede ou gerenciar arquivos.  

-----------------------------------------------------------------------------------

###  **📌 Estrutura Geral de um Comando no Linux**  
A maioria dos comandos no Linux segue esta estrutura:  

```bash
comando [opções] [argumentos]
```

🔹 **Comando** → A ação a ser executada  
🔹 **Opções (flags ou parâmetros)** → Modificam o comportamento do comando  
🔹 **Argumentos** → O alvo do comando (arquivo, diretório, pacote, etc.)  


### **📌 Exemplo 1: Comando `ls`**
```bash
ls -l /home
```
- `ls` → **Comando** que lista arquivos e diretórios  
- `-l` → **Opção (flag)** para exibir detalhes em formato de lista  
- `/home` → **Argumento**, especifica o diretório a ser listado  


### **📌 Exemplo 2: Comando `sudo apt install`**
```bash
sudo apt install vim -y
```
Agora, vamos entender cada parte:  

| Componente  | Definição |
|-------------|----------|
| `sudo`  | **Comando/ferramenta** para executar ações como administrador (superusuário). |
| `apt`  | **Comando/ferramenta** para gerenciar pacotes no Ubuntu/Debian. |
| `install` | **Subcomando** do `apt` que indica a ação de instalação. |
| `vim`  | **Argumento**, ou seja, o pacote que queremos instalar. |
| `-y` | **Opção (flag)** que responde "sim" automaticamente às perguntas do instalador. |

🔹 **Observação:**  
- `sudo` não é uma "opção", mas sim um **comando separado** que está sendo usado antes do `apt`.  
- `install` é um **subcomando** do `apt`. Muitos comandos possuem subcomandos (ex: `git commit`, `docker run`).  


### **📌 Tipos de Elementos em um Comando**
| Nome         | Definição |
|-------------|----------|
| **Comando**  | A ferramenta ou programa executado (ex: `ls`, `apt`, `cat`, `rm`). |
| **Subcomando** | Algumas ferramentas, como `git` e `apt`, possuem subcomandos (ex: `apt install`, `git commit`). |
| **Opção (flag ou parâmetro)** | Modifica o comportamento do comando (ex: `-l` no `ls -l`). |
| **Argumento** | O alvo do comando (ex: um arquivo, diretório, pacote). |


### **📌 Teste na Prática**
Quer saber mais sobre um comando? Use a opção `--help`:  

```bash
ls --help
apt --help
```

Ou consulte o manual completo com `man`:  
```bash
man ls
man apt
```

-----------------------------------------------------------------------------------

### Criando um diretório (pasta) e indo até ele
- `mkdir <nome_do_arquivo>`: **Make directory** - cria pasta no diretório atual
- `cd caminho`: **change directory** - Muda de diretório. Nesse caso, podemos passar o caminho completo ou o relacional (tipo, passar só o nome do diretório caso este esteja imediatamente acessivel no diretório ao qual atualmente estamos)
- `cd ..` = Este comando nós retornamos uma pasta de nível superior
- `cd` = Change Directory sem nada, nós voltamos para o ponto inicial. Neste caso, é a pasta home do usuário.
- `history` = Lista um histórico de todos os comandos utilizados no ambiente

## GERENCIANDO ARQUIVOS
Apesar de não parecer tão intuitivo utilizar o terminal, frente ao que geralmente estamos acostumados (com a interface gráfica), no entanto, quando colocamos sistemas em produção e utilizamos servidores, é esse tipo de ambiente que encontraremos.

Além disso, ambientes como este carrega certa praticidade, uma vez que os comandos passam a ser intuitivos e estes funcionarão em qualquer outro servidor, as mesmas ferramentas indepente do servidor e onde ele esteja.

### Criando arquivo (touch)
**Criando um arquivo:**
```bash
touch notas.txt
```
Note que criamos os arquivo mas há nada dentro dele.

### Inserindo notas e conferindo (cat)
**Adicionar notas dentro deste arquivo:**
```bash
cat > notas.txt
# Agora, a barra ficará piscante aguardando o texto que desejamos incluir
# CTRL + D para sair
```

**Verificando conteúdo do arquivo:**
```bash
cat notas.txt
# Printado no terminal o conteudo do arquivo
```

### Alternativas de inserção de conteúdo com echo
O comando **echo** também consegue inserir conteúdo em um arquivo
```bash
touch notas_com_echo.txt # criando arquivo
echo Isso é um teste > notas_com_echo.txt # resultado será parecido, mas não sei como funcionaria com multiline
```

Ao utilizar `echo` sem indicar um arquivo, a ação será um print no terminal
- Isso será muito util para escrevermos código no futuro
```bash
echo "Hello World"
```

### Outra alternativa comum para edição de texto (nano)
Nano é um editor de texto comum para ambientes Linux. Caso rodarmos o comando `nano` e termos o retorno `-bash: nano: command not found` é por que não temos instalado essa ferramenta. Necessitando instala-la.

Podemos instalar o nano com o seguinte comando
```bash
sudo apt-get install nano
```

Agora, damos o comando `nano` e a interface do editor será aberta.
- Escrevemos algumas notas
- `CTRL + X` para sair
- Quando ele pede para **save modified buffer?**, nós damos Y e indicamos onde
- Escrevemos o nome de um arquivo que desejamos salvar este conteúdo, pode ser um novo arquivo

### Movendo arquivos (mv)
Agora, queremos mover estes arquivos para a pasta devops, mas, fazer um por um não seria adequado. Para isso, a opção que o professor utilizou é compactar os arquivos.

```bash
tar -czf compactado.tar.gz arquivo_2.txt notas.txt
```
Explicação do comando:
- **tar:** Comando tar é o de compactação
- **-czf:** c (cria um arquivo compactado, c para Compact) | z (será um arquivo zip, z para Zip) | f (trata-se de um arquivo, f para File)
- **compactado.tar.gz:** nome_do_arquivo_compactado.extensao (que é o .tar.gz)
- **arquivo_2.txt notas.txt**: arquivos que quero **compactar**
- **IMPORTANTE:** cria-se um arquivo compactado com os arquivos desejados mas preserva-os, não os deleta

Agora, vamos mover os arquivos desejados
```bash
mv compactado.tar.gz /home/lucasrm/devops
```

### Removendo arquivos (rm)
Para deletar um arquivo, é só rodar `rm` e o nome do arquivo:
```bash
rm notas.txt
```

## REMOVENDO ARQUIVOS E DIRETÓRIOS
No Linux, a remoção de arquivos e diretórios pode ser feita de forma simples utilizando comandos no terminal como rm para arquivos e rmdir ou rm -r para diretórios. No entanto, é importante ter cautela ao utilizar opções como -f e -r, pois a remoção é definitiva e não há uma lixeira para recuperação posterior.

Para remover um arquivo, use o comando rm (remove):
```bash
rm nome_do_arquivo
```

Para remover um diretório vazio, use o comando rmdir:
```bash
rmdir pasta_vazia
```

Remover um diretório com conteúdo Para remover um diretório e todos os seus arquivos e subdiretórios, use o comando rm com a opção -r (recursivo):
```bash
rm -r nome_do_diretorio
```

## IMPORTANTE DICA
Caso queiramos ver as opções de um comando, podemos utilizar a opção `--h` ao lado de qualquer comando:
```bash
mkdir --h
```

## PARAMETROS DE LISTAGEM
```bash
ls arc* # Lista arquivos/diretórios iniciados com "arc"
ls arcf? # Lista arquuivos/diretórios que iniciam com "arcf" e possuem qualquer outro caracter após arcf, limitado a 1. O "?" indica existencia de algum caracter que você não conhece. Exemplos encontrados: arcf1, arcf2 ...
ls arcf?? # Mesma situação acima, mas com 2 caracteres. Como arcf12 ...
ls 2 # Lista todos os arquivos/diretórios que possuem 2 em qualquer posição do nome
ls ????? # Lista todos os arquivos/diretórios que possuem exatamente 5 caracteres
```

## Praticando
1. Criar dois diretórios chamados dir1 e dir2 na mesma posição hierárquica;
2. Entrar no diretório dir1 e criar dois arquivos chamados data1 e data2;
3. Copiar somente o conteúdo de dir1 para dir2;
4. Criar um novo diretório chamado dir3;
5. Mover o conteúdo de dir1 para dir3.
```bash
mkdir dir1 dir2 # etapa 1
cd dir1 # etapa 2.1
touch data1 data2 # etapa 2.2
cd ..
cp dir1/* dir2 # etapa 3
ls dir2
mkdir dir3 # etapa 4
mv dir1/* dir3 # etapa 5
```

### Outra atividade
Passo 1
- mkdir Docs
- Utilizamos o comando mkdir para criar um novo diretório. Aqui, estamos criando o diretório Docs no diretório atual.

Passo 2
- O comando nano abre o editor de texto Nano, permitindo a edição do arquivo "notas.txt". Se o arquivo não existir, o Nano o criará.
- nano notas.txt

Passo 3
- Usamos o comando touchpara criar um novo arquivo vazio.
- touch novo.txt

Passo 4
- O comando echo exibe a string especificada e o operador > redireciona a saída para o arquivo "saudacao.txt", criando-o se ainda não existir.
- echo "Olá, Mundo!" > saudacao.txt

Passo 5
- O comando cat exibe o conteúdo de um arquivo no terminal.
- cat saudacao.txt

Neste caso, será exibido o conteúdo do arquivo "saudacao.txt".

Passo 6
- O operador >> é usado para adicionar (anexar) texto ao final de um arquivo existente.
- echo "Bem-vindo ao Linux!" >> saudacao.txt

Passo 7
- O comando ls é utilizado para listar o conteúdo de um diretório.
- ls Docs

# <span style="color: #87BBA2">SHELL SCRIPTING</span>

## CONSTRUINDO SCRIPTS NO SHELL
Aqui entra um tópico importante, que seria **automatização de tarefas**, util para não termos que ficar executando comando por comando em ações repetidas.
> A nossa principal ideia com automatização é executar de uma forma mais inteligente e ágil uma série de comandos que teríamos que fazer manualmente na interface.

Então, criamos o que chamamos de `script` para fazer isso. E aí já demos até uma pista do que vamos usar. Vamos usar aqui o que chamamos de Shell Scripting (roteiro de comandos).

E o que é o `script`? O próprio nome sugere que é um roteiro, que vai definir como uma atividade será desempenhada de forma automatizada em nosso servidor. Vamos criá-lo usando uma linguagem própria de script. No nosso caso vai ser o Bash.

### Caso prático
Uma empresa que necessita, de forma rotineira, criar backup dos dados.
- Não seria ideal termos que entrar no terminal e todo dia executarmos o mesmo comando. Para isso, faremos o Shell Scripting

### Criando Shell Script
Para criarmos os nossos scripts, utilizaremos o editor de texto **Nano**, já visto anteriormente.

**Escrevendo Shell Script**
- A primeira linha é para informar quem será o interpretador do comando
  - Escrevemos: `#! /bin/bash`, para dizer que será interpretado pelo bash.
- Em seguida, criamos uma variável para armazenar o diretório de backup desejado:
  - `diretorio_backup="/home/lucasrm/devops"
- Na linha de baixo, criamos variável para o nome do arquivo
  - `nome_arquivo="backup_$(date +%Y%m%d_%H%M%S).tar.gz"`
  - Ou seja: variavel="nomeFixo_$(instrucao de coleta de data).extensaoFixa"
- Na linha de baixo, executaremos o comando para compilação
  - `tar -czf "$nome_arquivo" "diretorio_backup"`
  - **-czf:** c (cria um arquivo compactado) | z (gera um arquivo zip) | f (vou especificar o nome do arquivo)
  - "$nome_arquivo": nome do arquivo a ser criado na compactação
  - "diretorio_backup": arquivos que serão compactados
- No fim, informaremos ao usuários que o processo foi realizado com sucesso
  - Utilizaremos o `echo`
  - `echo "Backup concluido em $nome_arquivo"`
- Agora damos um `ctrl X` para sair da interface
- Damos um `Y` para salvar
- Acrescentamos o nome para o shell script
  - Colocamos o nome como "backup.sh" e ele foi salvo no "working directory".

**Executando Shell Script**
- Primeiro, alteramos o shell script para um executável
  - `chmod +x backup.sh`
- Depois, executamos
  - `bash backup.sh`

**Retornos da execução**
tar: Removing leading `/' from member names
Backup concluido em backup_20231122_175022.tar.gz

Sobre o $():
- Instrumento para informar que dentro dos parenteses será executado um comando
- Comando utilizado: `$(date +%Y%m%d_%H%M%S)`
  - Aqui estamos passando o comando date com a adição (+) de:
    - %Y: Year
    - %d: day
    - %m: month
    - _: separador entre a data e a hora
    - %H: Hour
    - %M: Minutes
    - %S: Seconds

## PARA SABER MAIS: TESTANDO DIFERENTES CONDIÇÕES
De maneira bastante similar ao que aprendemos em lógica de programação, quando implementamos um script no shell também podemos testar uma condição para direcionar a execução de diferentes blocos de instruções.

Usamos o comando condicional ifpara avaliar uma condição e direcionar o próximo passo na execução do código. O trecho de código a seguir apresenta a sintaxe adotada no Bash para execução do comando.

```bash
if [ condição ]; then
  # Comandos a serem executados se a condição testada for verdadeira.
elif [ outra condição ]; then
  # Comandos a serem executados se a primeira condição testada for falsa e a segunda condição testada for verdadeira.
else
  # Comandos a serem executados se nenhuma das condições testadas for verdadeira.
fi
```

Repare que a sintaxe do comando possibilita o teste de várias condições, permitindo a execução de diferentes blocos de comandos com base nesses testes.

Na criação dos testes adotamos operadores relacionais e lógicos de diferentes maneiras, como vemos nos exemplos a seguir:

### Igualdade entre duas strings

```bash
if [ "$string1" = "$string2" ]; then
  # Comandos a serem executados se as strings forem iguais.
fi
```

### Desigualdade entre duas strings
```bash
if [ "$string1" != "$string2" ]; then
  # Comandos a serem executados se as strings forem distintas.
fi
```

### Igualdade entre dois números
```bash
if [ "$numero1" -eq "$numero2" ]; then
  # Comandos a serem executados se os números forem iguais.
fi
```

### Desigualdade entre dois números
```bash
if [ "$numero1" -ne "$numero2" ]; then
  # Comandos a serem executados se os números forem distintos.
fi
```

### Testando se um número é maior que outro
```bash
if [ "$numero1" -gt "$numero2" ]; then
  # Comandos a serem executados se o primeiro número for maior que o segundo.
fi
```

### Testando se um número é menor que outro
```bash
if [ "$numero1" -lt "$numero2" ]; then
  # Comandos a serem executados se o primeiro número for menor que o segundo.
fi
```

### Testando se um número é maior ou igual a outro
```bash
if [ "$numero1" -ge "$numero2" ]; then
  # Comandos a serem executados se o primeiro número for maior ou igual ao segundo.
fi
```

### Verificando a existência de um arquivo ou diretório
```bash
if [  -e "/caminho/do/arquivo" ]; then
  # Comandos a serem executados caso seja constatada a existência do diretório ou arquivo.
fi
```

Note que as expressões condicionais devem estar entre [ ] e os espaços em branco são importantes na sintaxe. Os valores de strings devem ser colocados entre aspas para evitar problemas com espaços e caracteres especiais.

## PASSAGEM DE PARAMETROS
Vimos o comando `tar` e sua aplicação (cmpactação), o qual é muito util para:
- Movimentar arquivos entre diretórios e servidores
- Mudar de infraestrutura ou plataforma
- Fazer backups 

E a função primordial do scripting é na realização de automações, não necessitando mais precisar ficar escrevendo comando por comando no terminal.

No script que escrevemos, nós indicamos dentro dele o diretório que desejamos fazer backup. Como poderiamos deixar esse script mais abstraido para ele funcionar com mais diretórios, solicitando para o usuário indicar o diretório desejado para backup e o script realizar a função?

### Scripts com parametros
Primeira coisa, sempre informar o interpretador do script (que no caso, é o `#! /bin/bash`)

O que desejamos que o usuário faça:
- Informe o nome do arquivo final
- Informe os arquivos que serão compactados
- Então, teremos, pelo menos, 2 parametros

#### Validando se parametros foram passados
```bash
if [ "$#" -lt 2 ]; then # Se os parametros passados forem menores do que 2 (-lt: less then), então (then)
        echo "O programa $0 requer nome do arquivo e arquivos a serem compactados".
        exit 1 # Sai do programa
fi # Encerra bloco if. fi = if ao contrário
```

#### Pegando os parametros
```bash
arquivo_saida="$1" # Pegue o primeiro parametro informado
arquivos=("${@:2}") 
# () = Declarando uma array
# "${@:2}" = O @ significa (pegue todos os parametros). O ":" é para iniciar um indicador de posição, ou seja, "@:2" significa "Pegue todos os parametros depois do primeiro", já que o primeiro parametro será usado para o nome do arquivo de saida
# Com isso, "arquivos" serão todos os demais parametros informados após o primeiro.
# A sintaxe é dentro de aspas e chaves, ainda não sei direito o motivo. Das aspas, imagino que é porque sempre precisaremos utilizar quando é algo que não seja reservado ao sistema, pelo que entendi.
```

#### Compactando
```bash
tar -czf "$arquivo_saida" "${arquivos[@]}"
# ${arquivos[@]} representa todos os elementos do array arquivos.
```

🛠 Diferença entre ${arquivos[@]} e ${arquivos[*]}

📌 ${arquivos[@]}
- Expande cada elemento do array separadamente.
- É a utilização do `{}` que realiza a expansão da variável
- Se tivermos arquivos com espaço no nome ("meu arquivo.txt"), ele será tratado corretamente.

📌 ${arquivos[*]}
- Expande todos os elementos como uma única string, separada por espaços.
- Pode causar problemas com arquivos que contêm espaços no nome.
✅ Por isso, a melhor prática é usar ${arquivos[@]} para evitar problemas com nomes de arquivos que contenham espaços.

#### Script completo
```bash
#! /bin/bash

if [ "$#" -lt 2 ]; then
        echo "O programa $0 requer nome do arquivo e arquivos a serem compactados".
        exit 1
fi
arquivo_saida="$1"
arquivos=("${@:2}")
tar -czf "$arquivo_saida" "${arquivos[@]}"
echo "Compactado com sucesso em $arquivo_saida"
```

#### Executando script
```bash
chmod +x compactador # Mudando permissão de execução
./compactador # Executa o código

# Retorno: rquer nome do arquivo e arquivos a serem compactados
```

```bash
./compactador saida.tar.gz /home/lucasrm/texto2.txt /home/lucasrm/texto3.txt
# retorno: mensagens de compactação e mensagem de sucesso

tar -tf saida.tar.gz # Comando para descompactação para conferir se deu tudo certo
```

## PARA SABER MAIS: PASSANDO PARAMETROS EM SCRIPTS
A passagem de parâmetros em scripts em Bash no Ubuntu é uma forma de fornecer informações ou argumentos para o script durante sua execução. Isso torna os scripts mais flexíveis e reutilizáveis, pois seu comportamento é ajustado de acordo com os argumentos fornecidos.

Essa passagem de parâmetros é realizada por meio de variáveis especiais, conhecidas como variáveis de posição. Elas são numeradas de 1 a 9, com $1 representando o primeiro argumento, $2 representando o segundo, e assim por diante. Além disso, todos os argumentos posicionais podem ser acessados através do $@.

A seguir, temos um exemplo de script que verifica se foram fornecidos exatamente dois argumentos na linha de comando. Se não, ele exibe uma mensagem de erro. Caso contrário, ele atribui os valores dos argumentos às variáveis arg1 e arg2 e os imprime.

```bash
#!/bin/bash

if [ $# -ne 2 ]; then
  echo "Erro! Nao foram fornecidos dois argumentos"
  exit 1
fi

arg1=$1
arg2=$2

echo "O primeiro argumento é: $arg1"
echo "O segundo argumento é: $arg2"
```

Ótima pergunta, Ronan! Vamos esclarecer essa diferença de uma vez por todas. 💡🚀  

---

## **📌 Diferença entre `$VARIAVEL` e `${VARIAVEL}`**

Ambas as formas são usadas para referenciar o valor de uma variável no Bash, **mas `${}` é mais seguro e flexível**.

| Forma  | Explicação |
|--------|------------|
| `$VARIAVEL` | Forma simples. Funciona na maioria dos casos. |
| `${VARIAVEL}` | Forma mais segura. Útil quando precisamos concatenar ou evitar ambiguidades. |

---

### **🎯 Exemplo prático: Quando `${}` é necessário**
Vamos supor que temos esta variável:
```bash
nome="Ronan"
```

Agora, tentamos imprimir **"RonanDev"** concatenando `"Dev"` no final:

```bash
echo "$nomeDev"    # ERRO! Bash procura por uma variável chamada "nomeDev"
echo "${nome}Dev"  # CORRETO! Expande "Ronan" e concatena "Dev"
```
📌 **Explicação**:
- `$nomeDev` → O Bash **procura uma variável chamada `nomeDev`**, que não existe.  
- `${nome}Dev` → O Bash **expande `nome` corretamente** e depois adiciona `"Dev"`.

---

### **📌 Segurança e legibilidade**
Outra vantagem de `${}` é evitar ambiguidades. Exemplo:
```bash
ARQUIVO="backup"
echo "O arquivo é $ARQUIVO2024"  # ERRO! Procura variável $ARQUIVO2024 (que não existe)
echo "O arquivo é ${ARQUIVO}2024"  # CORRETO! Retorna "O arquivo é backup2024"
```

📌 **Conclusão**: Sempre que for concatenar algo ou evitar ambiguidades, **use `${}`**.  

---

### **🔥 Resumo final**
| Uso  | Quando usar? |
|------|-------------|
| `$VARIAVEL`  | Para referências simples. |
| `${VARIAVEL}`  | Para evitar ambiguidades, concatenar valores ou melhorar legibilidade. |

Agora você manja como um verdadeiro mestre do Bash! 🚀🔥

## EXEMPLOS DE SCRIPT

### Verificando existencia de arquivos na pasta
```bash
arquivos=("$@") # Pega todos os parametros
for arquivo in "${arquivos[@]}"; do # Loop for
  if [ ! -e "$arquivo" ]; then # Se não tiver arquivo
    echo "Arquivo não encontrado: $arquivo"
    exit 1 # Sai do script
  fi
done # Indicador de finalização do bloco For
```

### Verifique a validade do caminho informado
```bash
#!/bin/bash

# Solicitamos ao usuário o caminho do diretório
read -p "Digite o caminho do diretório: " caminho

# Verificamos se o caminho do diretório é válido
if [ -d "$caminho" ]; then
    echo "O caminho é um diretório válido."
else
    echo "O caminho não é um diretório válido ou ele não existe."
fi
```
-  operador `-d` verifica se o caminho fornecido $caminho é um diretório válido

### Exiba uma mensagem de boas-vindas quando executado
```bash
#!/bin/bash
echo "Bem-vindo ao meu script!"
```

### Criar uma cópia de segurança de um diretório específico
```bash
#!/bin/bash
tar -czf backup.tar.gz /caminho/do/diretorio
```

### Solicite ao usuário o nome de um diretório e, em seguida, o crie
```bash
#!/bin/bash
echo "Digite o nome do diretório:"
read nome_diretorio
mkdir $nome_diretorio
```

### Aceite um nome de arquivo como argumento e verifique se o arquivo existe
```bash
#!/bin/bash
echo "Digite o nome do arquivo:"
read nome_arquivo
if [ -e $nome_arquivo ]; then
  echo "O arquivo existe."
else
  echo "O arquivo não existe."
fi
```

### Utilize um loop para contar de 1 a 5
```bash
#!/bin/bash
for i in {1..5}
do
  echo $i
done
```

# <span style="color: #87BBA2">AUTOMATIZAÇÃO DE TAREFAS</span>

## EXECUTANDO MULTIPLAS TAREFAS
```bash
#! /bin/bash
read -p "Entre com a operacao desejada: 'compactar' ou 'descompactar'" operacao
case "$operacao" in
        "compactar")
                read -p "Nome do arquivo final (.tar.gz)" arquivo_saida
                read -p "Lista de arquivos separados por espaço:" arquivos
                tar -czf "$arquivo_saida" $arquivos
                echo "Compactados com sucesso em $arquivo_saida"
        ;;
        "descompactar")
                read -p "Qual é o nome do arquivo a ser a descompactar (.tar.gz)" arquivo
                read -p "Diretorio de destino" diretorio
                tar -xzf "$arquivo" -C "$diretorio"
                echo "Descompactado com sucesso em $diretorio"
        ;;
        *)
        echo "Operacao invalida!"
        echo "Selecione descompactar ou compactar"
        exit 1
        ;;
esac
```

### Notas
- `read -p`: Armazena a opção digitada pelo usuário em uma variável
  - Sua sintaxe: `read -p <mensagem_que_aparecerá_para_o_usuário> <nome_da_variavel>`
  - Exemplo: `read -p "O que você digitar, irá para a variável ao lado" variavel_ao_lado`

#### Sintaxe case
```bash
# SINTAXE
case "<variavel_a_ser_lida>" in
        "<valor_esperado_1>")
                # bloco de execução
        ;; # indicador de fim do bloco
        "<valor_esperado_2>")
                # bloco de execução
        ;; # Indicador de fim do bloco
        # demais valores + blocos que quiser
        # A opção abaixo é para valores default, ou seja, tudo que não seja as opções acima
        *)
                # Valores Default
                # bloco de execução
        ;; # indicador de fim do bloco
esac # Indicador de fim do bloco case

# EXEMPLO
case "$operacao" in
        "compactar")
                read -p "Nome do arquivo final (.tar.gz)" arquivo_saida
                read -p "Lista de arquivos separados por espaço:" arquivos
                tar -czf "$arquivo_saida" $arquivos
                echo "Compactados com sucesso em $arquivo_saida"
        ;;
        "descompactar")
                read -p "Qual é o nome do arquivo a ser a descompactar (.tar.gz)" arquivo
                read -p "Diretorio de destino" diretorio
                tar -xzf "$arquivo" -C "$diretorio"
                echo "Descompactado com sucesso em $diretorio"
        ;;
        *)
                echo "Operacao invalida!"
                echo "Selecione descompactar ou compactar"
                exit 1
        ;;
esac
```

#### Descompactando
Comando: `tar -xzf "$arquivo" -C "$diretorio"`
- **-xzf:** x (extraia um arquivo compactado, x para Xtract) | z (o arquivo é zip, z para Zip) | f (trata-se de um arquivo, f para File)

## SHELL SCRIPTING COM APENAS OS DOCUMENTOS

### Compactando apenas arquivos
```bash
#! /bin/bash
read -p "Entre com a operacao desejada: 'compactar' ou 'descompactar'" operacao
case "$operacao" in
	"compactar")
		read -p "Nome do arquivo final (.tar.gz): " arquivo_saida
		read -p "Caminho dos arquivos a compactar: " caminho
		read -p "Lista de arquivos separados por espaço: " arquivos

		tar -czf "$arquivo_saida" -C "$caminho" $arquivos

		echo "Compactados com sucesso em $arquivo_saida"
	;;
	"descompactar")
		read -p "Qual é o nome do arquivo a ser a descompactar (.tar.gz)" arquivo
		read -p "Diretorio de destino" diretorio

		tar -xzf "$arquivo" -C "$diretorio"

		echo "Descompactado com sucesso em $diretorio"
	;;
	*)
		echo "Operacao invalida!"
		echo "Selecione descompactar ou compactar"
		exit 1
	;;
esac
```
- Pedimos caminho base ao usuário
- Flag `-c "$caminho"` entra no diretório antes da compactação
- O resultado será um `.tar.gz` sem os caminhos completos, apenas com os arquivos desejados.

### Compactando caminho, descompactando apenas os arquivos
```bash
#! /bin/bash
read -p "Entre com a operacao desejada: 'compactar' ou 'descompactar'" operacao
case "$operacao" in
	"compactar")
		read -p "Nome do arquivo final (.tar.gz)" arquivo_saida
		read -p "Lista de arquivos separados por espaço:" arquivos
    
		tar -czf "$arquivo_saida" $arquivos
    
		echo "Compactados com sucesso em $arquivo_saida"
	;;
	"descompactar")
		read -p "Qual é o nome do arquivo a ser a descompactar (.tar.gz)" arquivo
		read -p "Diretorio de destino" diretorio

		tar --strip-components=1 -xzf "$arquivo" -C "$diretorio"

		echo "Descompactado com sucesso em $diretorio"
	;;
	*)
		echo "Operacao invalida!"
		echo "Selecione descompactar ou compactar"
		exit 1
	;;
esac
```
- Isso faz com que o primeiro nível de diretórios seja ignorado na extração.

## FUNÇÕES DIRETAS NO CLI  
Não é obrigatório escrever um script separado. Você pode declarar e chamar funções diretamente no terminal.  

### **🔥 Criando uma função direto no CLI**
```bash
minha_funcao() {
  echo "Olá, Ronan! Essa função foi criada no terminal. 🚀"
}
```
Agora, basta chamá-la:
```bash
minha_funcao
```
Saída:
```
Olá, Ronan! Essa função foi criada no terminal. 🚀
```

---

### **📌 Passando parâmetros para a função**
```bash
saudacao() {
  echo "Olá, $1! Seja bem-vindo ao mundo do Bash. 🔥"
}
```
Chamando com um argumento:
```bash
saudacao Ronan
```
Saída:
```
Olá, Ronan! Seja bem-vindo ao mundo do Bash. 🔥
```

---

### **📌 Funções mais complexas**
Quer renomear todos os arquivos da pasta `arquivos/`, adicionando `.txt`? Faz assim:  
```bash
renomear_arquivos() {
  for file in arquivos/*; do
    [[ "$file" == *.txt ]] || mv "$file" "${file}.txt"
  done
  echo "Arquivos renomeados com sucesso! ✅"
}
```
Depois, chama direto no CLI:
```bash
renomear_arquivos
```

---

### **📌 Mas e se eu fechar o terminal?**
Se você definir a função no CLI, ela **some ao fechar o terminal**.  

💡 **Solução:** Para salvar a função permanentemente, adicione ao `~/.bashrc` ou `~/.bash_profile`:
```bash
echo 'saudacao() { echo "Olá, $1! Seja bem-vindo ao Bash. 🔥"; }' >> ~/.bashrc
source ~/.bashrc
```

---

### **🚀 Resumo**
✔ **Sim, você pode criar funções direto no terminal.**  
✔ Para persistência, adicione no `~/.bashrc` ou `~/.bash_profile`.  
✔ Pode chamar funções no CLI como qualquer comando normal.  

Agora você tá pronto para automatizar tudo no Bash! 🔥💻

## QUANDO USAR E QUANDO NÃO USAR ASPAS
Ótima pergunta! O uso (ou não) das aspas no shell script pode afetar o comportamento dos comandos. Vamos analisar a diferença no seu snippet:

```bash
tar -czf "$arquivo_saida" -C "$caminho" $arquivos
```

---

### **1️⃣ Por que `"$arquivo_saida"` e `"$caminho"` têm aspas?**
✅ **Protege valores que podem conter espaços**  

Se as variáveis **podem conter espaços ou caracteres especiais**, devemos **usar aspas** para garantir que o valor seja tratado como um único argumento.  

**Exemplo sem aspas:**
```bash
arquivo_saida="meu backup.tar.gz"
tar -czf $arquivo_saida -C /home/user Documents
```
Expande para:
```bash
tar -czf meu backup.tar.gz -C /home/user Documents
```
🚨 **ERRO!** O `tar` agora interpreta **"meu"** como o nome do arquivo e **"backup.tar.gz"** como outro argumento.

**Exemplo com aspas (correto):**
```bash
arquivo_saida="meu backup.tar.gz"
tar -czf "$arquivo_saida" -C /home/user Documents
```
Agora, `tar` vê `"meu backup.tar.gz"` como um único argumento. ✅

**Por isso `"$arquivo_saida"` e `"$caminho"` têm aspas**:  
- `"$arquivo_saida"` → O nome do arquivo pode conter espaços.  
- `"$caminho"` → O caminho pode ter espaços, como `/home/ronan/Meus Documentos/`.

---

### **2️⃣ Por que `$arquivos` está sem aspas?**
🚨 **Porque queremos que o shell expanda corretamente vários argumentos.**  

Se `arquivos="arquivo1.txt arquivo2.txt arquivo3.txt"`, e usarmos **aspas**, o comportamento muda:

```bash
tar -czf "$arquivo_saida" -C "$caminho" "$arquivos"
```
Isso **passaria tudo como um único argumento**:
```bash
tar -czf "meu backup.tar.gz" -C "/home/user" "arquivo1.txt arquivo2.txt arquivo3.txt"
```
❌ **ERRO:** `tar` tentaria compactar um **único arquivo** chamado `"arquivo1.txt arquivo2.txt arquivo3.txt"`.

Sem aspas, cada arquivo é tratado individualmente:
```bash
tar -czf "$arquivo_saida" -C "$caminho" $arquivos
```
Expande para:
```bash
tar -czf "meu backup.tar.gz" -C "/home/user" arquivo1.txt arquivo2.txt arquivo3.txt
```
✅ **CORRETO:** `tar` recebe cada arquivo separadamente.

---

### **📌 Regra Geral**
| Tipo de variável  | Deve usar aspas? | Exemplo correto |
|------------------|----------------|----------------|
| **Variável única (caminho, nome de arquivo, string)** | ✅ Sim  | `"$arquivo_saida"`, `"$caminho"` |
| **Lista de argumentos separados por espaço** (`$@`, `$arquivos`) | 🚫 Não  | `$arquivos`, `$@` |
| **Lista de argumentos separados por espaço dentro de um array** | ✅ Sim (com `"${array[@]}"`)  | `"${arquivos[@]}"` |

---

### **Resumo**
✅ **Aspas** em **caminhos ou nomes de arquivos** previnem erros com espaços.  
🚫 **Sem aspas** em **listas de argumentos** permite que cada item seja tratado corretamente.  

Se o `$arquivos` fosse um **array**, aí sim usaríamos `"${arquivos[@]}"`. 

## INSTALANDO UM SERVIDOR WEB

### O que é um servidor web
Falamos muito sobre **servidores** até o momento, principalmente porque estamos lidando diretamente com um. Mas por que falamos tanto sobre servidor?

Quando acessamos uma página web, como a página da Alura, para realizar este ou outros cursos, esta página não está hospedada no seu celular ou no seu computador, mas em um **servidor**.

Normalmente, desejamos ter um acesso rápido, ágil, não queremos esperar alguns segundos para o vídeo carregar. Isso afeta muito a nossa experiência como pessoas usuárias de um site ou mesmo de um serviço, como, por exemplo, um serviço de streaming.

Para que isso ocorra de forma ágil e com qualidade, precisamos de um software rodando no nosso servidor, especificamente para atender a essas solicitações encaminhadas pelos nossos dispositivos para ele. **Este software é chamado de servidor web**.

A finalidade deste servidor é atender às solicitações que chamamos de **HTTP**, protocolo de comunicação usado para interagir com recursos e acessar páginas web localizadas em servidores.

Mas como preparamos um servidor web? É possível instalarmos um servidor web neste servidor Ubuntu no qual temos trabalhado? Sim, é possível!

Opções open-source de servidores web:
- Apache
  - Funciona bem para atendimento a grandes demandas e utilização de modulos diversos.
- Nginx
  - Costuma sendo muito usados em consideração a performance e conteudos estáticos.
  - O Nginx é conhecido por sua alta eficiência e performance quando lidando com conteúdo estático e alto volume de tráfego.

### Insalando Nginx em nosso servidor
Primeiro, iremos realizar uma atualização dos pacotes de nosso servidor
```bash
sudo apt update # Verifica os pacotes a serem instalados
sudo apt-get update # Instala de fato os pacotes
```
- Será solicitado sua senha, pois é um comando `sudo`, ou seja, estamos escalando privilégios

Agora, iremos instalar o **Nginx**
```bash
sudo apt install nginx
```
1. Responderemos que sim, para confirmar a instalação

#### Verificando servidor web
Para verificar se o servidor web está de fato rodando em nosso servidor, utilizaremos uma ferramenta que auxilia a monitorar o desempenho de unidades e serviços dentro do servidor:
```bash
sudo systemctl status nginx
```

Mas, e se rodassemos o `systemctl status` sem informar `nginx`?
```bash
sudo systemctl status
```
- Será retornado o status de todas as unidades do nosso servidor ubuntu.
- Ferramenta muito util para monitorarmos, diagnosticarmos erros, monitorar como esta o desempenho das diferentes unidades e serviços de instalados em nosso servidor.

## CONVERSÃO DE ARQUIVOS
Imagine que você tenha vários arquivos na extensão .jpg em um diretório do seu repositório local de armazenamento e deseja mudar sua extensão para .png. Seria possível criar um script que operasse essa conversão de forma prática e automatizada, ou seja, sem a necessidade de converter arquivo por arquivo?

Temos uma ferramenta muito útil nesse processo: o comando convert. Esse comando nos permite converter, editar e exibir imagens em diversos formatos.

A sintaxe do comando é bem prática:
```bash
convert [opções] arquivo_entrada arquivo_saída
```
Para converter uma imagem de .jpg para .png, podemos escrever a seguinte instrução:
```bash
convert imagem.jpg imagem.png
```
E se quiséssemos redimensionar um conjunto de imagens .jpg para uma resolução padrão 800x600?
```bash
convert imagem.jpg -resize 800x600 imagem_redimensionada.jpg
```

### Script
```bash
# Indicamos o interpretador
#!/bin/bash

# Solicitamos a indicação do caminho do diretório
read -p "Digite o caminho do diretório com as imagens JPG: " diretorio

# Verificamos se o diretório indicado existe
if [ ! -d "$diretorio" ]; then
    echo "Diretório não encontrado: $diretorio"
    exit 1
fi

# Convertemos todas as imagens JPG para PNG no diretório
for imagem_jpg in "$diretorio"/*.jpg; do
    convert "$imagem_jpg" "${imagem_jpg%.jpg}.png" && echo "Imagem convertida: ${imagem_jpg%.jpg}.png" || echo "Falha na conversão: $imagem_jpg"
done

echo "Conversão concluída!"
```

O trecho `${imagem_jpg%.jpg}` é um exemplo de **substituição de padrões (parameter expansion)** no Bash. Ele **remove a menor correspondência** do sufixo especificado (.jpg) da variável imagem_jpg.

Exemplo:
```bash
arquivo="foto.jpg.backup.jpg"
echo "${arquivo%.jpg}.png"

# retorno: foto.jpg.backup.png
```

Mas se quisermos **remover todas as ocorrências** de .jpg, usamos %% (duplo %):
```bash
arquivo="foto.jpg.backup.jpg"
echo "${arquivo%%.jpg}.png"

# retorno: foto.png
```

## EXEMPLO DE SCRIPTS
### automatiza a atualização de pacotes do sistema operacional.
```bash
#!/bin/bash
sudo apt update -y
sydo apt upgrade -y
```
O script utiliza os comandos apt update e apt upgrade para automatizar a atualização de pacotes no sistema operacional Debian/Ubuntu. O parâmetro -y é usado para confirmar automaticamente todas as perguntas de confirmação.

### renomeie todos os arquivos em um diretório, adicionando um prefixo ou sufixo especificado
```bash
#!/bin/bash
prefixo="Novo_"
for arquivo in *; do
        mv "$arquivo" "$prefixo$arquivo"
done
```

### automatiza a criação de usuários no sistema, solicitando ao usuário que forneça o nome e outros detalhes necessários
```bash
#!/bin/bash
read -p "Digite o nome do novo usuário: " nome_usuario
sudo useradd -m $nome_usuario
sudo passwd $nome_usuario
```
O script solicita ao usuário o nome do novo usuário, cria um diretório pessoal para o usuário (useradd -m), e define uma senha (passwd).
- Existe também o adduser, que já configura bastante coisa automaticamente. useradd é um comando Debian/Ubuntu de baixo nível

### monitorar o espaço em disco usando o comando df na coleta de informações
```bash
#!/bin/bash
limite=90
espaco=$(df -h | awk 'NR==2 {print $5}' | sed 's/%//')

if [ $espaco -gt $limite ]; then
      echo "Alerta: Espaço em disco excedeu $limite%."
else
      echo "Espaço em disco está abaixo do limite"
fi
```
O script coleta a porcentagem de espaço em disco usando o comando df, compara com um limite predefinido (90% neste exemplo) e emite um alerta se exceder.

Fala, Parceirão! Sem problema nenhum, tamo junto! Vou destrinchar o que acontece na variável `espaco` linha por linha.  

### **📌 O que acontece em `espaco`?**
```bash
espaco=$(df -h | awk 'NR==2 {print $5}' | sed 's/%//')
```
👉 **Ela pega a porcentagem de uso do disco e remove o símbolo `%`.**  
Agora, vamos **quebrar** cada parte para entender direitinho:

---

#### **1️⃣ `df -h` → Verifica o espaço em disco**
```bash
df -h
```
🔹 `df` (**Disk Free**) → Exibe o uso do disco.  
🔹 `-h` (**human-readable**) → Mostra os valores de forma legível (`G`, `M`, `%`).  

Exemplo de saída:
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1      100G   85G   15G  85%  /
tmpfs           16G     0   16G   0%  /dev/shm
```
✔️ O número que **importa** para o script é o da **coluna "Use%"**, que indica quanto do disco está ocupado.

---

#### **2️⃣ `awk 'NR==2 {print $5}'` → Filtra a linha e coluna certas**
```bash
awk 'NR==2 {print $5}'
```
🔹 **`awk`** é uma linguagem de manipulação de texto.  
🔹 **`NR==2`** → Seleciona **a segunda linha** da saída do `df -h` (onde estão os dados do disco principal).  
🔹 **`{print $5}`** → Exibe a **quinta coluna**, que é o valor da porcentagem de uso (`85%` no exemplo).  

---

#### **3️⃣ `sed 's/%//'` → Remove o símbolo `%`**
```bash
sed 's/%//'
```
🔹 `sed` (**stream editor**) edita o texto.  
🔹 `s/%//` → Substitui (`s/`) o símbolo `%` **por nada**, removendo-o.  
✔️ Agora, `espaco` contém apenas o número (`85`), facilitando a comparação.

---

### **📌 Recapitulando o que acontece**
```bash
espaco=$(df -h | awk 'NR==2 {print $5}' | sed 's/%//')
```
1️⃣ **`df -h`** → Mostra o espaço em disco.  
2️⃣ **`awk 'NR==2 {print $5}'`** → Pega **a porcentagem de uso** (`85%`).  
3️⃣ **`sed 's/%//'`** → Remove `%`, deixando só o número (`85`).  

---

### **📌 Exemplo prático**
Se rodarmos o comando direto no terminal:
```bash
$ df -h | awk 'NR==2 {print $5}' | sed 's/%//'
85
```
O valor `85` será salvo na variável `espaco`, permitindo a comparação no `if`:
```bash
if [ $espaco -gt $limite ]; then
```

### automatizar o backup de um diretório específico para um local de destino, utilizando a compressão gzip
```bash
#!/bin/bash
origem="/caminho/do/diretorio"
destino="/caminho/do/backup"
data=$(date +"%Y%m%d")
tar -czf $destino/backup_$data.tar.gz $origem
```
O script utiliza o comando `tar` para criar um arquivo compactado e tarball, adicionando a data ao nome do arquivo para distinguir backups diários. O gzip (`-z`) é usado para compressão.