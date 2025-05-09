FROM fedora:41

USER root

RUN dnf install virt-install virt-backup virt-lightning virt-top libvirt libvirt-nss openssh openssh-clients -y && dnf clean all


COPY ./libvirt-pool-setup.service /etc/systemd/system/libvirt-pool-setup.service
RUN systemctl enable libvirt-pool-setup.service \
    && systemctl enable libvirtd \
    && authselect enable-feature with-libvirt

RUN printf 'user = "root"\ngroup = "qemu"\ndynamic_ownership = 0\nremember_owner = 0\nnamespaces=[]' > /etc/libvirt/qemu.conf

RUN mkdir -p /var/lib/virt-lightning/pool/upstream \
  && chown -R qemu:qemu /var/lib/virt-lightning/pool \
  && chown -R root /var/lib/virt-lightning/pool/upstream \
  && chmod 775 /var/lib/virt-lightning \
  && chmod 775 /var/lib/virt-lightning/pool /var/lib/virt-lightning/pool/upstream

RUN dnf install curl -y && dnf clean all \
    && curl -SsL https://github.com/LINBIT/virter/releases/download/v0.28.1/virter-linux-amd64 -o /usr/bin/virter \
    && chmod +x /usr/bin/virter

RUN yes | ssh-keygen -t rsa -b 4096 -N "" -f ~/.ssh/id_rsa >/dev/null 2>&1

RUN useradd --create-home --groups kvm,libvirt,qemu,wheel virter \
    && mkdir -p ~/.ssh/ \
    && touch ~/.ssh/config
COPY ./ssh-config /home/virter/.ssh/config
RUN chown virter:virter -R /home/virter

USER virter
RUN yes | ssh-keygen -t rsa -b 4096 -N "" -f ~/.ssh/id_rsa >/dev/null 2>&1

# hadolint ignore=DL3002
USER root
ENTRYPOINT [ "/sbin/init" ]
