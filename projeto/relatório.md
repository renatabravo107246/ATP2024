<p align="center">
  <img src="imagens/DEM_thumbnail.jpg" alt="logo" width="200"/>
</p>



<h1 align="center"><strong>Relatório do Projeto Final</strong></h1>
<h2 align="center"><strong>Algoritmos e Técnicas de Programação</strong></h2>
<h2 align="center"><strong>Sistema de gestão de publicações médicas</strong></h2>
<h3 align="center"><strong>Licenciatura em Engenharia Biomédica, 2ºano</strong></h3>

Docentes: 
- José Carlos Ramalho
- Luís Filipe Cunha

Grupo: 
- A107185 Joana Rodrigues da Silva
- A107282 Lara Machado Rodrigues
- A107246 Renata Madalena Ferreira Bravo 

---
# **Índice**
## 1 ÍNDICE [X](#índice)
## 2 INTRODUÇÃO [X](#introdução)
## 3 INTERFACE GRÁFICA [X](#interface-gráfica)
<blockquote>
  <h3><em>3.1 FILE</em></h3>
</blockquote> 

      I. UPLOAD
      II. IMPORT
      III. SAVE/SAVE AS

<blockquote>
  <h3><em>3.2 ACTIONS</em></h3>
</blockquote>

      I. CREATE
      II. DELETE 
      III. EDIT 
      
<blockquote>
  <h3><em>3.3 SEARCH</em></h3>
</blockquote>

      I. PUBLICATIONS
      II. AUTHORS
      III. KEYWORDS
      
<blockquote>
  <h3><em>3.4 STATS</em></h3>
</blockquote>
    
      I. DISTRIBUTION OF PUBLICATIONS BY YEAR
      II. DISTRIBUTION OF PUBLICATIONS BY MONTH
      III. NUMBER OF PUBLICATIONS PER AUTHOR (TOP 20 AUTHORS)
      IV. DISTRIBUTION OF AN AUTHOR'S PUBLICATIONS BY YEARS
      V. NUMBER OF PUBLICATIONS PER KEYWORS (TOP 20 KEYWORDS)
      VI. DISTRIBUTION OF MOST FREQUENT KEYWORD PER YEAR
      
<blockquote>
  <h3><em>3.5 HELP</em></h3>
</blockquote>

## 4 INTERFACE DE LINHA DE COMANDO (CLI) [X](#interface-de-linha-de-comando-cli)
<blockquote>
  <h3><em>4.1 CARREGAR FICHEIRO</em></h3>
</blockquote>

<blockquote>
  <h3><em>4.2 MENU</em></h3>
</blockquote>

      I. CRIAR PUBLICAÇÃO
      II. EDITAR PUBLICAÇÃO
      III. CONSULTAR PUBLICAÇÃO
      IV. CONSULTAR PUBLICAÇÕES
      V. ELIMINAR PUBLICAÇÃO
      VI. RELATÓRIOS DE ESTATÍSTICA
      VII. LISTAR AUTORES
      VIII. IMPORTAR PUBLICAÇÕES
      IX. GUARDAR PUBLICAÇÕES
      X. HELP
      XI. SAIR
      
## 5. CONSIDERAÇÕES FINAIS [X](#considerações-finais)
<blockquote>
  <h3><em>5.1 DIFICULDADES ENCONTRADAS</em></h3>
</blockquote>

<blockquote>
  <h3><em>5.2 CONCLUSÃO</em></h3>
</blockquote>

---
# **Introdução**
Este projeto, realizado no âmbito da Unidade Curricular de Algoritmos e Técnicas de Programação, teve como objetivo o desenvolvimento de uma aplicação em Python, cuja finalidade passa pela gestão de uma base de dados de publicações médicas. Desta forma, foi também necessário o desenvolvimento de uma interface gráfica, por intermédio do PySimpleGUI, para que as funções pudessem ser aplicadas com clareza.
O programa disponibiliza ao utilizador algumas ferramentas para gestão das publicações, tais como:  criação de uma nova publicação;  edição de uma publicação; consulta de publicações através de filtros; eliminação de uma publicação; apresentação de relatórios de estatística; listagem de autores; importação de publicações e o armazenamento de publicações, juntamente com as alterações possivelmente efetuadas. 
Tendo isto em conta,  definimos a realização das funções pedidas juntamente com uma interface de utilização fácil e clara o nosso principal objetivo, tentando minimizar ao máximo as situações de erro, colocando-nos no lugar do utilizador. 

---
# **Interface Gráfica**

Ao iniciar o sistema, é possível o carregamento de uma base de dados, em extensão JSON, à escolha do usuário. A interface permite a filtração de arquivos para que apareçam apenas aqueles em JSON, facilitando a escolha do ficheiro correto.

<img src="imagens/Captura%20de%20ecrã%202024-12-30%20212009.png" alt="Janela inicial" width="500"/> 

Durante o processo de carregamento, o sistema verifica a integridade do ficheiro selecionado, assegurando que ele seja compatível com o formato JSON esperado. Caso o ficheiro não seja válido, uma mensagem de aviso é exibida para o utilizador.

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20232928.png" alt="Ficheiro carregado!" width="130"/> <img src="imagens/Captura%20de%20ecrã%202024-12-30%20221308.png" alt="Ficheiro inválido" width="100"/> 

## ***File***

Selecionando a opção *File* no programa, o usuário poderá efetuar as seguintes operações:

<img src="imagens/Captura%20de%20ecrã%202024-12-31%20172028.png" alt="File opções" width="300"/> 

<blockquote>
  <h3><em><strong>Upload</strong></em></h3>
</blockquote>

Além do carregamento inicial, durante a utilização do programa será possível dar upload a um novo ficheiro.
Quando o usuário opta por esta opção, uma mensagem de confirmação será exibida, solicitando ao usuário que confirme se deseja prosseguir com a substituição do arquivo atual, de modo a evitar a perda acidental de dados, caso o arquivo atual contenha alterações não salvas. 

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20233312.png" alt="Upload" width="300"/> 

Confirmando a substituição, o sistema abrirá uma janela para selecionar o novo ficheiro a ser carregado e procederá de maneira semelhante à do carregamento inicial. 

<blockquote>
  <h3><em><strong>Import</strong></em></h3>
</blockquote>

Caso o usuário selecione "Import", poderá importar novas publicações existentes num ficheiro novo (com estrutura
semelhante à do dataset fornecido) e adicioná-las ao modelo em memória, atualizando-o. O sistema abrirá uma janela para que o utilizador selecione o ficheiro a importar.

<img src="imagens/Captura%20de%20ecrã%202024-12-30%20220620.png" alt="Ficheiro importado" width="150"/> 

Se o ficheiro importado contiver artigos iguais ao ficheiro já adicionado, estes não serão importados.

<img src="imagens/Captura%20de%20ecrã%202025-01-01%20180727.png" alt="Artigos iguais" width="300"/> 

<blockquote>
  <h3><em><strong>Save/Save as</strong></em></h3>
</blockquote>

Ambos as opções permitem salvar o ficheiro, a qualquer momento da utilização do programa. 

A opção *Save* não solicita ao usuário que escolha um nome ou localização desde que o ficheiro já possua um local e nome definidos.

A opção *Save as*:
- Abre uma janela onde o usuário pode definir um novo nome para o arquivo ou escolher uma pasta diferente para salvá-lo.
- Cria uma nova cópia do arquivo, sem substituir o original (exceto se forem escolhidos o mesmo nome e local).

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20125426.png" alt="Save as" width="300"/> 

Ao fechar o programa, também será possível guardar as alterações feitas:

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20120713.png" alt="Salvar alterações" width="300"/> 


## ***Actions***
Selecionando a opção *Actions* na interface, o usuário poderá efetuar as seguintes operações:

<img src="imagens/Captura%20de%20ecrã%202024-12-31%20184452.png" alt="Actions opções" width="300"/> 

<blockquote>
  <h3><em><strong>Create</strong></em></h3>
</blockquote>

A opção "Create" permite criar uma nova publicação, adicionando-a ao ficheiro caso ele exista ou, se o utilizador desejar, criando um novo ficheiro, adicionando a este a publicação.

<img src="imagens/Captura%20de%20ecrã%202024-12-30%20223540.png" alt="Janela create" width="500"/>

Para criar uma publicação, é necessário preencher os campos assinalados como obrigatórios:
- Title: O título da publicação.
- Abstract: Um resumo descritivo do conteúdo.
- DOI: O identificador digital único da publicação.
- Author (Name): Nome(s) do(s) autor(es).
- PDF: O caminho ou link para o documento em formato PDF.
- URL: O endereço na web onde a publicação pode ser encontrada.

Se o usuário não tiver adicionado algum dos campos, será exibido um pop-up a solicitar para que esse campo seja selecionado, por exemplo:

<img src="imagens/Captura%20de%20ecrã%202025-01-03%20003837.png" alt="Create pop-up" width="200"/>

Os campos não obrigatórios são:
- Keyword: Palavra(s)-chave da publicação.
- Author Affiliation: Filiação institucional dos autores.
- Publish Date: Data de publicação.

Para escolher a data de publicação, um calendário será exibido:

<img src="imagens/Captura%20de%20ecrã%202024-12-30%20223643.png" alt="Calendário" width="200"/>

O utilizador pode adicionar múltiplas *keywords* e autores, desde que, relativamente aos autores, o campo *Author Name* seja preenchido. Se o usuário tentar adicionar apenas *Author Affiliation*, aparecerá:

<img src="imagens/Captura%20de%20ecrã%202025-01-03%20011927.png" alt="Adicionar autor" width="200"/>

Também é possível remover os autores e *keywords* adicionadas, clicando em *Remove*.
Depois de adicionados todos os campos pretendidos (para além dos obrigatórios), a seguinte mensagem será apresentada:

<img src="imagens/Captura%20de%20ecrã%202025-01-03%20004332.png" alt="Publicação Criada" width="200"/>


<blockquote>
  <h3><em><strong>Delete</strong></em></h3>
</blockquote>

De modo a viabilizar a eliminação de uma publicação específica, o usuário precisa de pesquisar e selecionar primeiro essa publicação. Assim, perante a escolha de *Delete*, é aberta uma janela "**Consultar Publicação**" que permite a adição de múltiplos filtros (nomeadamente Title, Author (Name), Author (Affiliation), Keyword e Publish Date) de modo a facilitar a procura da publicação desejada. Se o utilizador pretender remover um filtro, basta selecioná-lo e, de seguida, clicar em "*Remove Filter*".

<img src="imagens/Imagem%20WhatsApp%202025-01-02%20às%2013.17.07_bd7b0a70.jpg" alt="Janela Consultar Publicação" width="400"/> <img src="imagens/Captura%20de%20ecrã%202025-01-02%20144347.png" alt="Filtro aplicado" width="400"/>


<img src="imagens/Captura%20de%20ecrã%202025-01-02%20132022.png" alt="Filtros" width="150"/>


Mediante a escolha da publicação desejada na janela de consultar publicações, é aberta uma nova janela com todas as informações da publicação (janela "**Detalhes da Publicação**"). Nesta janela, para além do utilizador poder eliminar a publicação, também a pode exportar ou editar.

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20134450.png" alt="Detalhes da Publicação" width="500"/>

<blockquote>
  <h3><em><strong>Edit</strong></em></h3>
</blockquote>

À semelhança do *Delete*, também a seleção de *Edit* abre a janela "**Consultar Publicação**" para encontrar a publicação que o utilizador deseja editar e, posteriormente, a janela "**Detalhes da Publicação**". Selecionando *Edit*, é apresentada a seguinte janela:

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20150233.png" alt="Edit" width="500"/>

Aqui, é possível editar qualquer campo e salvar as alterações. 

## ***Search***

<blockquote>
  <h3><em><strong>Publications</strong></em></h3>
</blockquote>

Conforme descrita acima, a escolha de *Publications* também abre a janela "**Consultar Publicação**" e, aquando selecionada, é aberta a janela "**Detalhes da Publicação**", na qual se encontram todas as informações acerca da publicação selecionada.


<blockquote>
  <h3><em><strong>Authors</strong></em></h3>
</blockquote>

Ao selecionar a opção Authors, será aberta a janela "**Pesquisar Autores**" na qual é possível escolher a forma de ordenação dos autores, alfabética ou por frequência, que será impressa no espaço "**AUTORES**". 

<img src="imagens/Captura de ecrã 2025-01-03 130515.png" alt="autores" width="500"/>

Caso não seja selecionada uma forma de ordenação dos autores, será a mostrado o aviso abaixo.

<img src="imagens/Captura%20de%20ecrã%202025-01-03%20014730.png" alt="forma de ordenação" width="150"/>

Selecionando um dos autores, os seus artigos serão listados no espaço "**ARTIGOS**". Poderá ainda ser selecionado um dos artigos, abrindo a janela **Consulta de Publicação** anteriormente descrita.

<blockquote>
  <h3><em><strong>Keywords</strong></em></h3>
</blockquote>

Semelhante à opção Authors, selecionando a opção Keywords será aberta a janela "**Pesquisar Keywords**" que realiza exatamente as mesmas funções, porém tendo em conta todas as keywords do dataset e não os autores.

<img src="imagens/Captura de ecrã 2025-01-03 130544.png" alt="keywords" width="500"/>

Do mesmo modo, se não for selecionada uma forma de ordenação, é exibida a mensagem:

<img src="imagens/Captura%20de%20ecrã%202025-01-03%20020147.png" alt="forma de ordenação" width="150"/>

## ***Stats***
A opção *Stats* permite selecionar as seguintes operações:

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20153317.png" alt= "Stats opções" width="300"/>

Face à seleção de uma estatística, será gerado um gráfico de barras correspondente, pois acreditamos que este tipo de gráfico é o adequado para uma melhor análise dos dados.

<blockquote>
  <h3><em><strong>Distribution of publications by year</strong></em></h3>
</blockquote>

Nesta estatística, no eixo das abcissas encontram-se todos os anos presentes no ficheiro e no eixo das ordenadas encontra-se o número de publicações lançadas correspondente a cada ano. De seguida, encontra-se um exemplo:

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20154514.png" alt= "Gráfico 1" width="380"/>

<blockquote>
  <h3><em><strong>Distribution of publications by month</strong></em></h3>
</blockquote>

Selecionando esta estatística, será necessária a escolha de um ano para analisar a distribuição de publicações por mês.
No exemplo abaixo, foi selecionado o ano de 2021. 

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20155001.png" alt= "Janela de seleção de ano" width="150"/> <img src="imagens/Captura%20de%20ecrã%202025-01-02%20155024.png" alt= "Gráfico 2" width="380"/>

<blockquote>
  <h3><em><strong>Number of publications per author (top 20 authors)</strong></em></h3>
</blockquote>

O gráfico *Number of publications per author (top 20 authors)* mostra os 20 autores com mais publicações e o respetivo número de publicações. 

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20155050.png" alt= "Gráfico 3" width="480"/>

<blockquote>
  <h3><em><strong>Distribution of an author's publications by years</strong></em></h3>
</blockquote>

Com *Distribution of an author's publications by years*, o utilizador pode analisar as publicações de um autor à sua escolha distribuídas pelos anos em que foram publicadas. Para escolher o autor, uma janela com todos os autores (cujas publicações têm *Publish Date*) ordenados alfabeticamente. No seguinte exemplo, foi selecionado o autor "João Costa":

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20155135.png" alt= "Seleção de autor" width="200"/> <img src="imagens/Captura%20de%20ecrã%202025-01-02%20155222.png" alt= "Gráfico 4" width="520"/>

<blockquote>
  <h3><em><strong>Number of publications per keyword (top 20 keywords)</strong></em></h3>
</blockquote>

Esta estatística mostra as 20 palavras-chave mais frequentes e o número de publicações nas quais são mencionadas.

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20155247.png" alt= "Gráfico 5" width="520"/>

<blockquote>
  <h3><em><strong>Distribution of most frequent keyword per year</strong></em></h3>
</blockquote>

Por fim, nesta estatística é mostrado o top 5 de palavras-chave mais frequentes em cada ano, sendo necessária a seleção de um ano na janela "**Selecionar o ano**" são apresentados os anos presentes no ficheiro, desde que as publicações associadas tenham *keywords*.

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20155306.png" alt= "Seleção de ano" width="220"/> <img src="imagens/Captura%20de%20ecrã%202025-01-02%20160227.png" alt= "Gráfico 6" width="510"/>

## ***Help***

A opção *Help* é uma funcionalidade relevante para guiar o utilizador no uso da interface. O seu objetivo é fornecer uma explicação clara e organizada dos botões e operações possíveis, facilitando a navegação no programa.

<img src="imagens/Captura%20de%20ecrã%202025-01-04%20190558.png" alt= "Help" width="400"/>

---

# **Interface de linha de comando (CLI)**

## Carregar ficheiro

Ao iniciar o programa, o utilizador deverá inserir no terminal o caminho do ficheiro (formato JSON) que pretende carregar. 

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20181523.png" alt= "inserir caminho" width="510"/>

Se o dataset não estiver no formato JSON, será apresentada a mensagem de erro "O ficheiro não é do tipo JSON.". Se o ficheiro não existir, será exibida a mensagem "Ficheiro não encontrado".

<img src="imagens/Captura%20de%20ecrã%202025-01-03%20024540.png" alt= "ficheiro inválido" width="500"/>

## Menu:

Após ocorrer um carregamento correto do ficheiro pretendido pelo utilizador, surge no terminal um menu principal que apresenta todas as opções disponíveis. O menu apresenta opções de manipulação do ficheiro numeradas de 0 a 10, exigindo que o utilizador introduza o número correspondente à ferramenta desejada.

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20181623.png" alt= "menu" width="510"/>

<blockquote>
  <h3><em><strong>Criar Publicação</strong></em></h3>
</blockquote>

Para criar uma nova publicação, o utilizador deve selecionar a opção 1 e devendo preencher os campos que vão surgindo no terminal. Não sendo obrigatório o preenchimento dos campos "keywords", "afilliation" e "publish_date".

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20184802.png" alt= "1" width="510"/>

<blockquote>
  <h3><em><strong>Editar Publicação</strong></em></h3>
</blockquote>

Para editar uma publicação, após selecionar a opção 2, o utilizador deverá indicar se pretende pesquisar a publicação por título ou doi. Após apresentar uma resposta válida o utilizador terá de preencher o campo disponibilizado no terminal de acordo com a escolha anterior.

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20185012.png" alt= "2" width="510"/>

Se a publicação não existir essa mesma informação será apresentada no terminal, voltando a aparecer o menu.

Se existir uma publicação cujo título/doi corresponda ao indicado pelo utilizador será apresentada a publicação completa no terminal, bem como a opção do utilizador indicar ao programa qual o campo da publicação pretende editar. Sendo depois possível ao utilizador introduzir o novo conteúdo para o respetivo campo. Depois de submeter a primeira alteração o utilizador poderá decidir se pretende ou não editar mais informações da publicação. Quando não pretender efetuar mais alterações a publicação será guardada com as novas informações.
 
<blockquote>
  <h3><em><strong>Consultar Publicação</strong></em></h3>
</blockquote>

De forma a consultar uma publicação, após selecionar a opção 3, o utilizador deverá indicar se pretende pesquisar a publicação por título ou doi. Após apresentar uma resposta válida o utilizador terá de preencher o campo disponibilizado no terminal de acordo com a escolha passada.

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20185120.png" alt= "3" width="510"/>

Se a publicação não existir a mesma informação irá ser apresentada no terminal, voltando a aparecer o menu.

Se existir uma publicação cujo título/doi corresponda ao indicado pelo utilizador será apresentada a publicação completa no terminal.


<blockquote>
  <h3><em><strong>Consultar Publicações</strong></em></h3>
</blockquote>

Caso pretenda consultar publicações, após selecionar a opção 4, o utilizador deverá indicar o filtro que pretende usar na sua pesquisa (title/author/affiliation/publish_date/keywords) inserindo depois a informação que corresponde ao filtro selecionado.

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20185342.png" alt= "4" width="510"/>

Se não existir publicações que obedeçam à pesquisa a mesma informação irá ser apresentada no terminal, voltando a aparecer o menu.

Se existirem publicações que obdeçam à pesquisa as mesmas serão apresentadas na íntegra no terminal.
  
<blockquote>
  <h3><em><strong>Eliminar Publicação</strong></em></h3>
</blockquote>

Para eliminar uma publicação, após selecionar a opção 5, o utilizador deverá indicar se pretende pesquisar a publicação por título ou doi. Após apresentar uma resposta válida o utilizador terá de preencher o campo disponibilizado no terminal de acordo com a escolha passada.

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20185951.png" alt= "5" width="500"/>
<img src="imagens/Captura%20de%20ecrã%202025-01-02%20190018.png" alt= "5" width="500"/>

Se a publicação existir será eliminada.

<blockquote>
  <h3><em><strong>Relatórios de Estatística</strong></em></h3>
</blockquote>

A nível de estatística, após selecionar a opção 6, será apresentado no terminal o menu relativo aos relatórios estatísticos da base de dados, informando o utilizador das opções (numeradas de 1 a 6) de gráficos que estão disponíveis para consulta.

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20190100.png" alt= "6" width="500"/>

Por exemplo, selecionando a opção 2 e o ano de 2022, será mostrado o seguinte gráfico:

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20190411.png" alt= "6" width="500"/>

Após a visualização de um gráfico o utilizador terá a oportunidade de selecionar outro relatório ou voltar ao menu.

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20190441.png" alt= "6" width="500"/>

<blockquote>
  <h3><em><strong>Listar Autores</strong></em></h3>
</blockquote>

Caso o utilizador pretenda listar os autores, após a seleção da opção 7, terá de escolher entre a ordenação dos mesmos por ordem alfabética ou por frequência de publicações. Aquando de uma resposta válida por parte do utilizador serão listados então os autores pela ordem optada.

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20190737.png" alt= "7" width="500"/>

De seguida, é dada ao utilizador a oportunidade de, na eventualidade do mesmo pretender consultar os artigos de um autor dos listados, o fazer, respondendo "s" à pergunta "Deseja consultar os artigos de um autor? [s/n]" que aparece no terminal. 

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20190759.png" alt= "7" width="500"/>

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20190856.png" alt= "7" width="500"/>

Neste caso será solicitado ao utilizador que indique o nome do autor, sendo de seguida apresentadas todas as suas publicações.

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20190829.png" alt= "7" width="500"/>
<img src="imagens/Captura%20de%20ecrã%202025-01-02%20190917.png" alt= "7" width="500"/>

<blockquote>
  <h3><em><strong>Importar Publicações</strong></em></h3>
</blockquote>

No que diz respeito a importar publicações, após selecionar a opção 8, o utilizador deverá indicar o caminho do ficheiro (formato JSON) que pretende importar para a base de dados atual.

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20191129.png" alt= "8" width="500"/>

Caso o ficheiro de importação contenha alguma publicação já existente na base de dados a mesma não será importada, o que será informado no terminal na forma: "A publicação já existe no dataset, por isso não foi importada."

No final o programa informa também o número de publicações que foram importadas, por exemplo: "Foram importadas 5 publicações."

<blockquote>
  <h3><em><strong>Guardar Publicações</strong></em></h3>
</blockquote>

Para garantir as alterações efetuadas na base de dados o utilizador terá de recorrer à opção 9. A ferramenta de guardar publicações exigirá assim que o utilizador indique o nome do ficheiro onde pretende guardar a base de dados (no formato JSON) e imediatamente terá salvo as publicações com as alterações que possa ter efetuado.

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20191231.png" alt= "9" width="500"/>

Se, por exemplo, uma publicação foi eliminada por engano basta sair do programa sem guardar as publicações e a base de dados manter-se-á inalterada. 

<blockquote>
  <h3><em><strong>Help</strong></em></h3>
</blockquote>

Na eventualidade do utilizador ter dúvidas quanto ao papel de alguma das ferramentas do programa está à sua disposição o comando "Help" que apresentará no terminal, após a seleção da opção 10, uma explicação mais clara das ferramentas disponíveis.

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20191319.png" alt= "10" width="500"/>

<blockquote>
  <h3><em><strong>Sair</strong></em></h3>
</blockquote>

Por forma a sair do programa, o utlizador terá de selecionar a opção 0, sendo de seguida questionado quanto à sua intenção de fechar o programa e informado que caso não tenha guardado as alterações as mesmas serão perdidas.
Caso responda "n" voltará ao menu. 
Se responder "s" o programa terminará.

---
# **Considerações finais**
## **Dificuldades encontradas**

1. Ao integrar funcionalidades do Matplotlib na interface gráfica desenvolvida em PySimpleGUI, deparamo-nos com a dificuldade de manter o tamanho da janela principal depois de qualquer funcionalidade de *Stats* fosse selecionada, visto que a abertura da janela do gráfico provocava a desformatação da janela da interface. A solução para este problema passou por utilizar a seguinte biblioteca:

   ```python
   import threading

   # Exemplo de uso
   
   threading.Thread(target=mp.pub_ano, args=(dataset,), daemon=True).start()

2. Outra dificuldade encontrada durante o desenvolvimento do projeto foi implementar um comportamento em que o popup de confirmação "Deseja guardar as alterações antes de sair?" fosse exibido antes da janela principal fechar.

<img src="imagens/Captura%20de%20ecrã%202025-01-02%20120713.png" alt="Salvar alterações" width="300"/> 

  ```python
  while not stop:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == sg.WIN_CLOSED:
        response = sg.popup_yes_no("Deseja guardar as alterações antes de sair?", no_titlebar=True)
        if response == 'Yes':
            if ficheiro:
                try:
                    mp.armazenamento(ficheiro, dataset)
                except Exception as e:
                    sg.popup_error(f"Erro ao salvar o arquivo: {e}")
            else:
                if dataset:
                    newfile = sg.popup_get_file("Selecione o ficheiro JSON",
                                        file_types=[("JSON Files", "*.json")], save_as=True)
                    if newfile:
                        try:
                            mp.armazenamento(newfile, dataset)
                            sg.popup_timed("Ficheiro salvo!", auto_close=True, auto_close_duration=5)
                        except Exception as e:
                            sg.popup_error(f"Erro ao salvar o arquivo: {e}")
                else:
                    sg.popup("Nenhum ficheiro carregado para salvar.")
        stop = True
  ```

## **Conclusão**

Durante a realização deste projeto, aplicando os conhecimentos retidos durante o semestre, podemos desenvolver uma interface e uma linha de comando que nos permite trabalhar com dados reais. Ao longo da sua concessão foram surgindo alguns obstáculos, o que nos levou à pesquisa e conhecimento de novas ferramentas, aumentando o conhecimento já adquirido. Assim, este projeto não só contribuiu para consolidarmos como aprendermos novas ferramentas Python.


