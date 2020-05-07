ARG UBUNTU19_10
FROM registry.mandy-home.duckdns.org/mandy91/ubuntu:$UBUNTU19_10
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

ENV MKDOCS_VERSION=1.0.4 \
    GIT_REPO='false' \
    LIVE_RELOAD_SUPPORT='false' \
    ADD_MODULES='false'


RUN install-package python3-pip git
# ==${MKDOCS_VERSION}
RUN pip3 install mkdocs==1.1
RUN pip3 install git+https://github.com/jldiaz/mkdocs-plugin-tags.git
RUN pip3 install mkdocs-awesome-pages-plugin==2.2.1
RUN pip3 install mkdocs-bootstrap==1.1
RUN pip3 install mkdocs-gitbook==0.0.1
RUN pip3 install mkdocs-bootstrap4==0.1.3
RUN pip3 install mkdocs-nav-enhancements==0.9.1
RUN pip3 install mkdocs-material==4.6.3
RUN pip3 install git+https://github.com/Mandy91/mkdocs-toc-sidebar-plugin.git@drop_python_2.7_support
RUN pip3 install markdown-table==2019.4.13
RUN pip3 install markdown-toc==1.2.6
RUN pip3 install mkdocs-markdownextradata-plugin==0.1.2
RUN pip3 install mkdocs-macros-plugin==0.4.4
RUN pip3 install pygments==2.6.1
RUN pip3 install jupyter==1.0.0
# RUN pip3 install mkdocs-jupyter






RUN mkdir -p "$HOME/mkdocs/mkdocs" && chown "$USER:$USER" -R "$HOME/mkdocs"

WORKDIR $HOME/mkdocs/mkdocs
EXPOSE 8000
CMD s6-setuidgid $USER mkdocs serve -a 0.0.0.0:8000 --livereload