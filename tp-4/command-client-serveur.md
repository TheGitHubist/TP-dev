# Commandes côté serveur

```powershell
[yasei@localhost ~]$ sudo nano /etc/sysconfig/network-scripts/ifcfg-enp0s3
[yasei@localhost ~]$ sudo systemctl restart NetworkManager
[yasei@localhost ~]$ git clone [lien de ce git]
[yasei@localhost ~]$ sudo firewall-cmd --add-port=13337/tcp --permanent
[yasei@localhost ~]$ sudo firewall-cmd --reload
[yasei@localhost ~]$ python -u ~/TP-dev/tp-4/b2_server_I1.py
```

# Commandes côté client

```powershell
[yasei@localhost ~]$ sudo nano /etc/sysconfig/network-scripts/ifcfg-enp0s3
[yasei@localhost ~]$ sudo systemctl restart NetworkManager
[yasei@localhost ~]$ git clone [lien de ce git]
[yasei@localhost ~]$ sudo firewall-cmd --add-port=13337/tcp --permanent
[yasei@localhost ~]$ sudo firewall-cmd --reload
[yasei@localhost ~]$ python -u ~/TP-dev/tp-4/b2_client_I1.py
```

# resultat

```powershell
[yasei@localhost ~]$ ss -lnpt | grep 13337
LISTEN 0      1            0.0.0.0:13337      0.0.0.0:*    users:(("python",pid=16073,fd=3))
```