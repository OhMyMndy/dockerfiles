ARG UBUNTU19_10
FROM mandy91/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

USER root

RUN install-package gpg-agent curl

RUN curl -sL https://deb.nodesource.com/setup_12.x | APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn bash -
RUN install-package \
	tree sed ack \
	python3-pip \
	php-cli php-xml php-mbstring php-curl php-zip php-pdo-sqlite php-pdo-mysql php-intl php-zmq \
	nodejs


RUN curl -sS https://getcomposer.org/installer | php \
	&& mv composer.phar /usr/local/bin/composer
RUN chown -R "$USER":"$USER" "$HOME"


USER $USER

RUN pip3 install jupyterlab

RUN curl -sS https://litipk.github.io/Jupyter-PHP-Installer/dist/jupyter-php-installer.phar > /tmp/jupyter.php \
	&& php /tmp/jupyter.php install \
	&& rm /tmp/jupyter.php

RUN pip3 install virtualenv

RUN npm config set prefix "$HOME/.local"
RUN npm install -g ijavascript && ijsinstall

RUN pip3 install bash_kernel && python3 -m bash_kernel.install
RUN pip3 install gnuplot_kernel && python3 -m gnuplot_kernel install --user

RUN jupyter lab --generate-config
RUN pip3 install jupytext && jupyter labextension install jupyterlab-jupytext && jupyter serverextension enable jupytext
RUN jupyter labextension install @jupyterlab/toc
RUN jupyter labextension install @jupyterlab/shortcutui
RUN mkdir -p "$HOME/.jupyter/" \
	&& echo 'c.NotebookApp.contents_manager_class = "jupytext.TextFileContentsManager"' >> "$HOME/.jupyter/jupyter_notebook_config.py"

USER root
RUN install-package libmariadbclient-dev

USER $USER

RUN pip3 install ipython-sql && pip3 install mysqlclient


USER root
RUN chown -R "$USER":"$USER" "$HOME"

CMD s6-setuidgid $USER jupyter lab --ip 0.0.0.0