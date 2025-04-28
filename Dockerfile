# Escolhe uma imagem base oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de requisitos primeiro (boa prática para cache)
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

# Copia o restante da aplicação para dentro do container, excluindo arquivos desnecessários
COPY . .

# Variáveis de ambiente para Flask
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Expõe a porta que o Flask vai rodar
EXPOSE 8080

# Define o comando para rodar o app com Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "--workers", "2", "app:app"]
