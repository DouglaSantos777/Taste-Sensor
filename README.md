# 🎬 TasteSensor: Sistema de Recomendação de Filmes

Este repositório contém o código e o modelo treinado para um Sistema de Recomendação de Filmes baseado em Conteúdo (`main.py` e `Taste_Sensor.ipynb`), desenvolvido como trabalho final da disciplina de Inteligência Artificial.

## ⚙️ Metodologia Principal (IA)

O sistema utiliza a técnica de **Filtragem Baseada em Conteúdo (Content-Based Filtering)** para sugerir obras.

1.  **Vetorização NLP:** As características de conteúdo (`sinopse` e `gênero`) dos filmes são transformadas em vetores numéricos usando o algoritmo **TF-IDF (Term Frequency-Inverse Document Frequency)**. Esta técnica prioriza palavras que são estatisticamente mais importantes para diferenciar um filme dos demais.
2.  **Modelo de Similaridade:** A proximidade temática entre todos os filmes é calculada através da métrica **Similaridade de Cosseno (Cosine Similarity)**.
3.  **Resultado:** O modelo recomenda os filmes que possuem o maior score de similaridade de conteúdo (ângulo mais próximo) com o filme de entrada.

---

## 🚀 Como Executar o Código

Para executar o sistema localmente e obter as recomendações, siga os passos abaixo:

### Pré-requisitos

Certifique-se de ter o **Python 3** e o **pip** instalados.

### Passo 1: Criar e Ativar o Ambiente Virtual

É recomendando utilizar um ambiente virtual para instalar as dependências de forma isolada.

#### Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Passo 2: Instalação das Bibliotecas

Com o ambiente virtual ativado, instale todas as dependências do projeto listadas no arquivo **requirements.txt**:

```bash
pip install -r requirements.txt
```

### Passo 3: Execução do Sistema

```bash
python main.py
```