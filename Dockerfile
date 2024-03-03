# Usa uma imagem base do Python
FROM python:3.10.12

# Copia os arquivos do projeto para o diretório de trabalho no contêiner
WORKDIR /app
COPY . /app

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Defina a variável de ambiente FLASK_APP
ENV FLASK_APP=app.py

# Expõe a porta 5000 para acessar o aplicativo Flask
EXPOSE 5000

# Comando para iniciar o aplicativo Flask quando o contêiner for iniciado
CMD ["flask", "run", "--host=0.0.0.0"]
