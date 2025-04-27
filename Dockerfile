# Escolhe uma imagem base oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de requisitos primeiro (boa prática para cache)
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação para dentro do container
COPY . .

# Expõe a porta que o Flask vai rodar
EXPOSE 8080

# Define o comando para rodar o app
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
