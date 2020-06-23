FROM docker:19.03-dind
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/ash", "-o", "pipefail", "-c" ]

USER root

RUN apk add --no-cache build-base libffi-dev openssl-dev python3-dev curl krb5-dev linux-headers zeromq-dev
RUN apk add --no-cache py-pip
RUN pip3 install jupyterlab
RUN pip3 install bash_kernel && python3 -m bash_kernel.install
RUN pip3 install gnuplot_kernel && python3 -m gnuplot_kernel install --user

RUN jupyter lab --generate-config

RUN apk add --no-cache nodejs npm
RUN pip3 install jupytext
RUN jupyter labextension install jupyterlab-jupytext
RUN jupyter serverextension enable jupytext

RUN jupyter labextension install @jupyterlab/toc
RUN jupyter labextension install @jupyterlab/shortcutui
RUN mkdir -p "$HOME/.jupyter/" \
	&& echo 'c.NotebookApp.contents_manager_class = "jupytext.TextFileContentsManager"' >> "$HOME/.jupyter/jupyter_notebook_config.py"

RUN apk add --no-cache libmariadbclient-dev

RUN pip3 install ipython-sql && pip3 install mysqlclient


#CMD s6-setuidgid $USER jupyter lab --ip 0.0.0.0#

ENTRYPOINT [ "jupyter", "lab", "--ip", "0.0.0.0" ]