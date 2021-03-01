FROM php:8.0-cli-buster


RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN docker-php-ext-install pcntl && docker-php-ext-enable pcntl
RUN docker-php-ext-install opcache && docker-php-ext-enable opcache
RUN docker-php-ext-install pdo && docker-php-ext-enable pdo
RUN docker-php-ext-install pdo_mysql && docker-php-ext-enable pdo_mysql