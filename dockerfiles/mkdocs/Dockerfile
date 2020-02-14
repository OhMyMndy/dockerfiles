ARG UBUNTU19_10
FROM mandy91/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

ENV MKDOCS_VERSION=1.0.4 \
    GIT_REPO='false' \
    LIVE_RELOAD_SUPPORT='false' \
    ADD_MODULES='false'


RUN install-package python3-pip git
# ==${MKDOCS_VERSION}
RUN pip3 install mkdocs 
RUN pip3 install git+https://github.com/jldiaz/mkdocs-plugin-tags.git
RUN pip3 install mkdocs-awesome-pages-plugin 
RUN pip3 install mkdocs-bootstrap
RUN pip3 install mkdocs-gitbook
RUN pip3 install mkdocs-bootstrap4
RUN pip3 install mkdocs-nav-enhancements
RUN pip3 install mkdocs-material
RUN pip3 install mkdocs-toc-sidebar-plugin
RUN pip3 install markdown-table
RUN pip3 install markdown-toc
RUN pip3 install mkdocs-markdownextradata-plugin
RUN pip3 install mkdocs-macros-plugin
RUN pip3 install pygments
RUN pip3 install jupyter
RUN pip3 install mkdocs-jupyter






RUN mkdir -p "$HOME/mkdocs/mkdocs" && chown "$USER:$USER" -R "$HOME/mkdocs"

WORKDIR $HOME/mkdocs/mkdocs
EXPOSE 8000
CMD s6-setuidgid $USER mkdocs serve -a 0.0.0.0:8000 --livereload