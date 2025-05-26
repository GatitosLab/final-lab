
import paramiko
import time

# Datos de conexión al Fortigate
hostname = "5.0.10.9"
port = 22
username = "admin"
password = "admin"

# Comandos de configuración actualizada
commands = """
config system interface
    edit "port1"
        set mode dhcp
        set allowaccess ping https ssh http fgfm
        set alias "MGMT"
    next
    edit "port2"
        set ip 10.0.200.1 255.255.255.0
        set allowaccess ping
        set alias "DMZ"
    next
    edit "port3"
        set ip 203.0.113.1 255.255.255.0
        set allowaccess ping
        set alias "INTERNET"
    next
end

config firewall address
    edit "web_server_dmz"
        set subnet 10.0.200.10 255.255.255.255
    next
    edit "host_gestion_remoto"
        set subnet 5.0.10.12 255.255.255.255
    next
    edit "all_internal"
        set subnet 10.0.0.0 255.255.0.0
    next
end

config firewall policy
    edit 1
        set name "WEB desde Internet a DMZ"
        set srcintf "port3"
        set dstintf "port2"
        set srcaddr "all"
        set dstaddr "web_server_dmz"
        set action accept
        set schedule "always"
        set service "HTTP" "HTTPS"
        set logtraffic all
        set nat enable
    next
    edit 2
        set name "Gestión Remota FortiGate"
        set srcintf "port3"
        set dstintf "port1"
        set srcaddr "10.0.200.10"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "HTTPS" "SSH"
        set logtraffic all
    next
    edit 3
        set name "Respuestas desde DMZ"
        set srcintf "port2"
        set dstintf "port3"
        set srcaddr "web_server_dmz"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "ALL"
        set logtraffic all
        set nat enable
    next
    edit 4
        set name "Denegar DMZ hacia Intranet"
        set srcintf "port2"
        set dstintf "port1"
        set srcaddr "web_server_dmz"
        set dstaddr "all_internal"
        set action deny
        set schedule "always"
        set service "ALL"
        set logtraffic all
    next
end
"""

def configure_firewall():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print("[+] Conectando al Fortigate...")
    client.connect(hostname, port=port, username=username, password=password)

    remote_shell = client.invoke_shell()
    time.sleep(1)

    print("[+] Enviando configuración...")
    for line in commands.strip().split('\n'):
        remote_shell.send(line + '\n')
        time.sleep(0.5)
        output = remote_shell.recv(5000).decode('utf-8')
        print(output)

    print("[+] Configuración finalizada. Cerrando conexión...")
    remote_shell.close()
    client.close()

if __name__ == "__main__":
    configure_firewall()
