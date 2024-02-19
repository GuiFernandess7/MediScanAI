FROM ubuntu:20.04

ENV TF_ENABLE_ONEDNN_OPTS=0

LABEL maintainer="guilhermesampaio"

# Copia os arquivos necessários para o container
COPY ../requirements.txt /requirements.txt
COPY . /app
COPY ../scripts /scripts
COPY ../package /package

WORKDIR /app
EXPOSE 8000

# Instalação de dependências adicionais
RUN apt-get update && apt-get install -y \
    libsm6 libxext6 libxrender-dev \
    postgresql-client libpq-dev gcc\
    python3-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalação do Python 3.8 (versão mais recente disponível)
RUN apt-get update && apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && apt-get update && \
    apt-get install -y python3.8

# Instalação de dependências do sistema para psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Criação do ambiente virtual e instalação das dependências do Python
RUN python3.8 -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt

RUN /py/bin/pip install /package/tensorflow-2.7.0-cp38-cp38-linux_x86_64.whl

# Configuração de permissões e criação de diretórios
RUN adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

# Usa o ambiente virtual a cada execução do contêiner
ENV PATH="/scripts:/py/bin:$PATH"

USER app

CMD ["run.sh"]