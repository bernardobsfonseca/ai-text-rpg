# Modo de Instalação
### Requisitos do Sistema:
* Python 3 ou superior
* IDE com suporte a Python

### Instalação e Preparação do ambiente
* Clone o repositório
* Abra utilizando sua IDE
* Abra o prompt da IDE na pasta do projeto e crie a pasta do Ambiente Virtual¹ com o comando:
</br>`python -m venv venv`
* Ative o ambiente virtual com o comando:
	* No Windows:
<br>`venv\Scripts\activate`
	* No Linux:
<br>`source venv/bin/activate`
* Já no ambiente virtual digite o comando para instalar as bibliotecas requeridas:
<br>`pip install -r requirements.txt`

### Download do Modelo de IA
* Acesse: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q4_K_M.gguf
* Click em "download"
* Preferencialmente, coloque o modelo num repositório próximo à pasta do jogo

### Utilizando o Modelo
* Abra o jogo na sua IDE
* Abra a pasta "Misc"
* Substitua o valor da variável "model_path" pelo caminho até o modelo que você baixou²

### Iniciando o Jogo
* Abra a pasta do jogo utilizando um terminal, como da própria IDE, Windows Powershell ou o de sua preferência.
* Acesse o ambiente virtual (se ainda não estiver nele)
* Inicie o jogo digitando com o comando:
<br>`python main.py`
* Aguarde o modelo ser carregado nos geradores de cenas³

---

1- Ambientes Virtuais isolam as dependências de cada projeto, permitindo usar diferentes versões de pacotes sem conflitos. Isso facilita a organização, manutenção e compartilhamento de projetos Python.
<br>2- Coloque o ".gguf" junto. Ex: C:/modelo/llama-2-7b-chat.Q4_K_M.gguf
<br>3- Pode demorar mais ou menos a depender da capacidade de processamento do computador.

