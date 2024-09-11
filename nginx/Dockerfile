# Используем базовый образ Ubuntu
FROM ubuntu:latest

# Обновляем систему и устанавливаем необходимые пакеты
RUN apt-get update && \
    apt-get install -y \
    nginx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Копируем конфигурационный файл Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Открываем порт 80
EXPOSE 80

# Запускаем Nginx при старте контейнера
CMD ["nginx", "-g", "daemon off;"]