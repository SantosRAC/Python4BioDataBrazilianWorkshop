- [Inicio](../index.md)
- [Cronograma](cronograma.md)
- [Guia de Instalação](guia_de_instalacao.md)
- [Material Python](python.md)
- [Problema 1](problema1.md)
- [Problema 2](problema2.md)


# Guia de Instalação


Algumas **bibliotecas** e **ferramentas** serão utilizadas nesse workshop para podermos mostrar a você o incrível poder da linguagem **Python**.

Devido a isso, aqui se encontra um **Guia de Instalação** para que você possa obter todas essas **bibliotecas**, **pacotes** e **ferramentas** de maneira rápida e simples.

Entretanto, caso tenha **dúvidas** ou esteja enfrentando **problemas** nessa tarefa, envie um e-mail para o nosso **contato** (python4biodatabrazil@gmail.com) com o **assunto** **"GUIA DE INSTALAÇÃO"** e ajudaremos você! 


### Pré-requisitos
* Nenhum

### Pós-instalação
Ao final desse guia, você deverá ter instalado no seu computador:

* [Python 3.6](https://www.python.org/)
* [Anaconda](https://docs.continuum.io/)
* Bibliotecas [NumPy](http://www.numpy.org/), [SciPy](https://www.scipy.org/), [pandas](http://pandas.pydata.org/), [Jupyter](http://jupyter.org/) entre outras.

### Ir para
* [Guia de Instalação para Windows](#guia-de-instala%C3%A7%C3%A3o-para-windows)
* [Guia de Instalação para Linux](#guia-de-instalação-para-linux)
* [Instalando Python e o IDLE](#instalando-python-e-o-idle)
* [Testando o Jupyter Notebook](#testando-o-jupyter-notebook)


## Guia de Instalação para Windows

### 1. Baixando o **Anaconda**

Entre no [site do Anaconda](https://www.anaconda.com/download/#windows) e faça o **download** do instalador para a **versão Python 3.6**. 

Caso seu sistema operacional seja de **64 bits**, baixe o instalador para **64 bits** (__64-bit (535 MB)__).

<img src="https://a-hayasi.github.io/Python4BioDataBrazilianWorkshop/imagens/py_64_windows.jpg"/> 

Caso seu sistema operacional seja de **32 bits**, baixe o instalador para **32 bits** (__32-bit (436 MB)__).

<img src="https://a-hayasi.github.io/Python4BioDataBrazilianWorkshop/imagens/py_32_windows.jpg"/> 

* **OBS:**  Caso não saiba a arquitetura do seu sistema operacional, abra o **Meu Computador**, clique com o botão direito do mouse dentro da janela aberta e em seguida selecione **Propriedades**. Uma nova janela será aberta e em **Tipo de Sistema** se encontrará a informação desejada.



### 2. Instalando o **Anaconda**

Após a conclusão do download, execute o instalador e selecione a opção **Next** para continuar a instalção e em seguida **I Agree** para aceitar os termos de licença. 

Selecione novamente **Next** e **Next**. Nesse momento, aparecerá no instalador duas opções avançadas: **Add Anaconda to my PATH environment variable** e **Register Anaconda as my default Python 3.6**. Selecione ambas e em seguida clique em **Install**.

Com isso, a instalação será iniciada. Após finalizada, selecione **Next** para prosseguir e **Finish** para encerrar e concluir a instalação.



### 3. Atualizando e instalando pacotes

Ao finalizar a instalação, é necessário atualizar os pacotes instalados. 

Para isso, abra o **Menu Iniciar**, digite **Anaconda Prompt** e pressione **Enter**. Com isso, você estará abrindo o terminal do Anaconda.

O Anaconda conta com mais de 100 pacotes pré-instalados, portanto, para atualizar todos simultaneamente execute no terminal do Anaconda aberto o comando:

    conda update --all

Uma lista de pacotes a serem atualizados será exibida no terminal e será requisitada a confirmação da atualização. 

**Confirme** digitando `y` e pressionando **Enter**.

Ao final, você terá atualizado todos os pacotes pré-instalados do Anaconda, o que inclui pacotes como **NumPy**, **SciPy**, **pandas** e **Jupyter**.

## Guia de Instalação para Linux

### 1. Baixando o **Anaconda**

Entre no [site do Anaconda](https://www.anaconda.com/download/#linux) e faça o **download** do instalador para a **versão Python 3.6**. 

Caso seu sistema operacional seja de **64 bits**, baixe o instalador para **64 bits** (__64-Bit (x86) Installer (524 MB)__) .

<img src="https://a-hayasi.github.io/Python4BioDataBrazilianWorkshop/imagens/py_64_linux.jpg"/> 

Caso seu sistema operacional seja de **32 bits**, baixe o instalador para **32 bits** (__32-Bit Installer (430 MB)__).

<img src="https://a-hayasi.github.io/Python4BioDataBrazilianWorkshop/imagens/py_32_linux.jpg"/> 

* **OBS:**  Caso não saiba arquitetura do seu sistema operacional, abra o **Terminal** (em algumas distribuições, a tecla de atalho para isso é __Ctrl+Alt+T__) e execute o comando: `uname -m`.

Se a saída for `x86_64`, seu sistema operacional é de **64 bits**. Caso o contrário, seu sistema operacional é de **32 bits**.



### 2. Instalando o **Anaconda**

Após a conclusão do download, abra o **Terminal** e vá para a pasta **Downloads** executando o comando:

    cd Downloads/

Em seguida, se o seu sistema operacional for de **64 bits**, inicie a instalação executando:

    bash Anaconda3-5.0.1-Linux-x86_64.sh

Do contrário, se seu sistema operacional for de **32 bits**, inicie a instalação executando:

    bash Anaconda3-5.0.1-Linux-x86.sh

A instalação será iniciada no terminal exibindo o **termo de licença** do Anaconda, continue pressionando **Enter** para ler o **termo**. 

Ao final do termo, o instalador irá perguntar se concorda com os termos e deseja prosseguir com a instalação. Digite `yes` e pressione **Enter** para confirmar. Em seguida, pressione **Enter** novamente para confirmar o local de instalação (recomendado) ou especifique outro local (não recomendado).
 
Depois de concluída a instalação de todos os pacotes e requisitos, confirme a adição do Anaconda no seu **PATH**. Para isso, Digite `yes` e pressione **Enter**. Feche o **Terminal**



### 3. Atualizando e instalando pacotes

Após instalar o Anaconda, é necessário atualizar os pacotes instalados. O Anaconda conta com mais de 100 pacotes pré-instalados, portanto, para atualizar todos simultaneamente abra o **Terminal** e execute o comando:

    conda update --all

Uma lista de pacotes a serem atualizados será exibida no terminal e será requisitada a confirmação da atualização. 

**Confirme** digitando `y` e pressionando **Enter**.

Ao final, você terá atualizado todos os pacotes pré-instalados do Anaconda, o que inclui pacotes como **NumPy**, **SciPy**, **pandas** e **Jupyter**.



## Instalando Python e o IDLE

Um modo bem comum de se utilizar a linguagem Python é através do editor IDLE, acrônimo para *Integrated Development and Learning Environment*. Seu objetivo é basicamente fornecer uma maneira rápida e fácil para o desenvolvimento de scripts, uso de funções e bibliotecas da linguagem. Além disso, o editor foi construído utilizando Python e conta com algumas funcionalidades básicas como capacidade de multi-janelas, autocomplemento, etc.

O IDLE possui dos tipos principais de janela, a janela Shell e a Editor. Quando você abre o IDLE, ele automaticamente inicia no Shell.
Utilizando esse modo, é possível programar de modo interativo, isto é, cada instrução escrita é executada em seguida.

<img src="https://a-hayasi.github.io/Python4BioDataBrazilianWorkshop/imagens/shell_python.jpg"/>

Para abrir o modo Editor, você deve acessar no menu superior **File > Arquivo**, ou então usar o atalho **Ctrl+N**. Com o modo Editor, é possível escrever uma série de linhas de código e em seguida usar a opção **Run Module** para que o código escrito seja executado no Shell.

Código escrito no Editor.

<img src="https://a-hayasi.github.io/Python4BioDataBrazilianWorkshop/imagens/editor_python.jpg"/>


Saída no Shell.

<img src="https://a-hayasi.github.io/Python4BioDataBrazilianWorkshop/imagens/saida_editor_python.jpg"/>



### No Windows

Como a linguagem Python não é nativa no Windows, isto é, já vem instalada no sistema operacional, é necessário fazer o download da mesma e em seguida instalar. Por padrão, o IDLE  é instalado em conjunto com a linguagem. 

Portanto, caso deseje instalar a linguagem Python no seu computador, entre no [site do Python](https://www.python.org/downloads/) e faça o **download da versão 3.6.x**

Após a conclusão do download, abra o executável e já na primeira tela você deverá marcar a opção **Add Python 3.6 to PATH** e em seguida clicar em **Install Now** para realizar a instação. Após terminada, basta clicar em **Close** para fechar o instalador.

<img src="https://a-hayasi.github.io/Python4BioDataBrazilianWorkshop/imagens/install_py3_windows.jpg"/>


### No Linux

Em geral, os sistemas operacionais baseados em Unix como Linux e macOS possuem o Python nativo, logo, para acessar o modo interativo basta abrir o **Terminal** do sistema operacional e executar `python`. Com isso, estará abrindo o modo interativo da linguagem. Contudo, também é possível fazer a instalação do IDLE.
Para isso, com o **Terminal** aberto, execute:

Ubuntu, Debian, Mint e derivados:

     sudo apt-get install idle3
     
Fedora, OpenSUSE e derivados:

    sudo yum install python3-tools

Em seguida, confirme a instalação digitando `yes` ou `y` e pressionando **Enter**

## Testando o Jupyter Notebook

Um dos pacotes mais utilizados do Anaconda é o IPython, mais conhecido por Jupyter Notebook. É um ambiente computacional interativo que permite criar, editar, executar e compartilhar códigos-fonte, equações, gráficos, textos, documentos, entre outros. E tudo isso, através de um navegador web, podendo ser executado de modo local e não necessitando assim de acesso a internet, ou então por meio de um servidor remoto.

Além de criar, editar, executar e compartilhar arquivos, o Jupyter Notebook conta com um painel de controle que permite navegar por diretórios, exibir arquivos, etc.

Caso já tenha instalado o Anaconda, para testar o Jupyter Notebook abra o **Menu Iniciar**, digite **Anaconda Prompt** e pressione **Enter**, em seguida, execute no terminal aberto do Anaconda o comando:

    jupyter notebook
    
Uma aba será aberta no seu navegador padrão e nessa aba se encontra o Jupyter. Agora, vamos testar algumas funcionalidades.
 
### Criando um script no Jupyter e executando pelo IPython
 
Na aba do Jupyter aberta, procure o diretório **Desktop** (ou **Área de Trabalho**) e acesse-o. Em seguida, no canto superior direito clique em **New > Text File**. Com isso, você estará abrindo um arquivo no editor de texto do Jupyter.

<img src="https://a-hayasi.github.io/Python4BioDataBrazilianWorkshop/imagens/jupyter1.jpg"/>
 
Onde estiver escrito **"untitled.txt"**, renomeie para **"my_script.py"**. No editor, escreva o seguinte script e pressione **Ctrl+S** para gravar.

```python
for i in range(0, 10):
    print('Eu amo Python')
```

<img src="https://a-hayasi.github.io/Python4BioDataBrazilianWorkshop/imagens/jupyter2.jpg"/>

Por fim, para se executar o script, é necessário utilizar o **IPython**. Para isso, abra o **Menu Iniciar**, digite **IPython** e pressione **Enter**.

Navegue até a **Área de Trabalho**, executando no **IPython**.

    cd ../Desktop

Execute o script com o comando `%run my_script.py` e a saída deverá ser:

<img src="https://a-hayasi.github.io/Python4BioDataBrazilianWorkshop/imagens/jupyter3.jpg"/>
    
## Problemas

Caso você tenha enfrentado algum problema e não conseguiu concluir a instalação, mande um e-mail com o assunto **"GUIA DE INSTALAÇÃO"** para o nosso contato!
