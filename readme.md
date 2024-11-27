# Color Recognition API

Este é uma API utilizando FastAPI para reconhecimento de cores baseado em um modelo treinado com TensorFlow. A API permite classificar imagens e obter a previsão de classes e suas respectivas probabilidades.

## Requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

## Instalação das Dependências

Primeiro, clone este repositório para o seu diretório local:

```bash
git clone https://github.com/felipethamay/color-recognition-fastapi.git
cd color-recognition-fastapi
```

Em seguida, instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

## Executando a API

Executar diretamente com uvicorn:
```bash
uvicorn app.main:app --reload
```

Se preferir, você pode garantir que as dependências sejam instaladas automaticamente ao iniciar o servidor com o seguinte comando, executando no diretório do projeto:
```bash
python app.py
```

Em seguida, instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

## Documentação
Com o servidor em execução, acesse a documentação da API através do Swagger UI:

http://127.0.0.1:8000/docs


### Endpoints
- POST /color-classification/predict

Este endpoint recebe uma imagem e retorna a classificação do modelo.

Parâmetros de entrada:

- file: A imagem a ser classificada (deve ser enviada como um arquivo de imagem).

Resposta esperada:

```json
{
  "Classe Prevista": "0",
  "Probabilidades": [35, 22, 14, 10, 5, 3, 2]
}
```