# <span style="color: #87BBA2">===   DevOps: explorando conceitos, comandos e scripts no Linux CLI   ===</span> <!-- omit in toc -->

# <span style="color: #87BBA2">INDICE</span> <!-- omit in toc -->
- [Aula XX: TituloAula](#aula-xx-tituloaula)
  - [Capitulo](#capitulo)

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

### Acesso remoto
Utilizaremos o protocolo SSH, que permite a conexão com uma máquina de forma remota.

### Passo a passo
Precisaremos:
1. IP da VM

Mas antes, precisamos fazer:
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
- **-czf:** c (cria um arquivo compactado) | z (gera um arquivo zip) | f (vou especificar o nome do arquivo)
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