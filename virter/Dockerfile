FROM fedora:41

RUN dnf install virt-install virt-backup virt-lightning virt-top libvirt libvirt-nss -y
RUN systemctl enable libvirtd

RUN mkdir -p /var/lib/virt-lightning/pool/upstream \
  && chown -R qemu:qemu /var/lib/virt-lightning/pool \
  && chown -R root /var/lib/virt-lightning/pool/upstream \
  && chmod 775 /var/lib/virt-lightning \
  && chmod 775 /var/lib/virt-lightning/pool /var/lib/virt-lightning/pool/upstream


COPY ./libvirt-pool-setup.service /etc/systemd/system/libvirt-pool-setup.service
RUN systemctl enable libvirt-pool-setup.service

RUN authselect enable-feature with-libvirt

RUN dnf install curl -y
RUN curl -SsL https://github.com/LINBIT/virter/releases/download/v0.28.1/virter-linux-amd64 -o /usr/bin/virter
RUN chmod +x /usr/bin/virter


RUN dnf install openssh -y

RUN ssh-keygen -t rsa -b 4096 -N "" -f ~/.ssh/id_rsa <<< y >/dev/null 2>&1

RUN useradd --create-home --groups kvm,libvirt,qemu,wheel virter
RUN mkdir -p ~/.ssh/ \
  && touch ~/.ssh/config 
COPY ./ssh-config /home/virter/.ssh/config
RUN chown virter:virter -R /home/virter

USER virter
RUN ssh-keygen -t rsa -b 4096 -N "" -f ~/.ssh/id_rsa <<< y >/dev/null 2>&1

USER root
ENTRYPOINT /sbin/init

