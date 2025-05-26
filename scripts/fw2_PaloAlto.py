import paramiko
import time

# Datos de conexión al Palo Alto PA-VM
hostname = "5.0.10.7"
port = 22
username = "admin"
password = "Admin@123"

commands = """
configure

# Asignación de IPs y zonas
set network interface ethernet ethernet1/1 layer3 ip 192.168.200.1/24
set network virtual-router default interface ethernet1/1
set zone dmz network layer3 ethernet1/1

set network interface ethernet ethernet1/2 layer3 ip 192.168.20.1/24
set network virtual-router default interface ethernet1/2
set zone intranet network layer3 ethernet1/2

set network interface ethernet ethernet1/3 layer3 ip 192.168.10.1/24
set network virtual-router default interface ethernet1/3
set zone intranet network layer3 ethernet1/3

# Perfil de gestión (útil para acceso admin)
set network profiles interface-management-profile mgmt-profile ssh yes https yes
set network interface ethernet ethernet1/1 layer3 interface-management-profile mgmt-profile
set network interface ethernet ethernet1/2 layer3 interface-management-profile mgmt-profile
set network interface ethernet ethernet1/3 layer3 interface-management-profile mgmt-profile

# Objetos de dirección
set address web_server_dmz ip-netmask 192.168.200.10/32
set address base_datos ip-netmask 192.168.20.10/32
set address dns_server ip-netmask 192.168.20.2/32
set address gestion_host ip-netmask 192.168.10.100/32

# Regla de seguridad: acceso interno al firewall
set rulebase security rules allow_mgmt_pa from intranet to intranet
set rulebase security rules allow_mgmt_pa source gestion_host
set rulebase security rules allow_mgmt_pa destination 192.168.10.1
set rulebase security rules allow_mgmt_pa application ssh
set rulebase security rules allow_mgmt_pa application web-browsing
set rulebase security rules allow_mgmt_pa service application-default
set rulebase security rules allow_mgmt_pa action allow

commit
exit
"""

def configure_palo_alto():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print("[+] Conectando al Palo Alto PA-VM...")
    client.connect(hostname, port=port, username=username, password=password)

    shell = client.invoke_shell()
    time.sleep(1)
    print("[+] Enviando configuración...")

    for line in commands.strip().split('\n'):
        if not line.strip().startswith("#") and line.strip():
            shell.send(line + '\n')
            time.sleep(0.5)
            output = shell.recv(5000).decode('utf-8')
            print(output)

    shell.close()
    client.close()
    print("[+] Configuración finalizada.")

if __name__ == "__main__":
    configure_palo_alto()
