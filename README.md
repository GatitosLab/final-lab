## 🏥 Proyecto de Topología de Red: Centro de Salud "San Vergeles"

### 🔧 Arquitectura Spine-Leaf con segmentación funcional y seguridad perimetral

Este proyecto consiste en el diseño, despliegue y documentación de una **infraestructura de red simulada para un centro de salud**, utilizando la herramienta [Containerlab](https://containerlab.dev/). Se ha optado por una arquitectura **Spine-Leaf**, altamente escalable, modular y coherente con entornos de producción modernos.

### 🎓 Contexto y propósito

Este proyecto ha sido desarrollado con carácter educativo como parte de la fase final de nuestras prácticas de Administración de Sistemas Informáticos y Redes en Kyndryl, dentro del equipo de Redes y Comunicaciones. 
Objetivos: 
* Consolidar conocimientos de redes, virtualización y seguridad.
* Simular una infraestructura realista y documentarla profesionalmente.
* Poner en práctica el diseño de redes escalables y segmentadas, seguras por diseño.


### 📌 Características principales

* 📡   **Topología Spine-Leaf** con 2 nodos *spine* y 4 nodos *leaf*, más *border-leafs* conectados a firewalls.
* 🌐 **Segmentación por VLANs** para zonas funcionales críticas:

  * VLAN 10 – Administración y soporte técnico incluye DNN, DHCP, BBDD
  * VLAN 20 – Videovigilancia (cámaras IP)
  * VLAN 30 – Equipos médicos especializados
  * VLAN 200 – Zona DMZ para servicios expuestos
* 🧱🔐 **Doble firewall en serie**:

  * `fw_fortinet` como filtro perimetral hacia Internet
  * `fw_paloalto` como inspección profunda entre DMZ y red interna

* 📡 **Servicios funcionales desplegados en contenedores** (DNS, DHCP, Web Server, BBDD, clientes de prueba).
* 📦 Imágenes utilizadas:

  * `vrnetlab/cisco_iol`
  * `vrnetlab/vr-fortios:fortios`
  * `vrnetlab/paloalto_pa-vm:10.0.11`
  * `alpine:latest` para servicios internos y clientes



### 📁 Estructura del proyecto

```
├── configs/                           # Configuración inicial por nodo
│   
├── scripts/                           # Scripts auxiliares (firewalls, dependencias)
│   ├── fw1_Fortinet.py
│   ├── fw2_PaloAlto.py
│   └── requirements.txt
├── documentation/                     # Documentación técnica del proyecto
├── final-lab.clab.yaml                # Archivo de topología Containerlab
├── README.md                          # Este archivo
├── .gitignore

```


### ⚙️  Créditos y herramientas

* 🛠️ [Containerlab](https://containerlab.dev/)
* 🧱 [vrnetlab](https://github.com/plajjan/vrnetlab) para imágenes de firewalls y routers
* 📚 Referencias bibliográficas y más información incluidas en el informe del proyecto


👥 Autoría
LaoLink Consulting
Proyecto desarrollado por:

Laura Ramos Granados
Estudiante de ASIR en el IES Zaidín Vergeles | GitHub: [github.com/ramossinflores](https://github.com/ramossinflores) | LinkedIn: [linkedin.com/in/emele-ramos-granados]

Oleg Fernández-Llebrez Rodríguez
Estudiante de ASIR en el centro Fomento Ocupacional - FOC | GitHub: [github.com/oleg04](https://github.com/oleg04) | LinkedIn: [linkedin.com/in/olegfdezll](https://www.linkedin.com/in/olegfdezll/)


### 📄 Licencia

Proyecto de carácter educativo, no destinado a producción.
Uso libre con fines formativos y académicos.
**© 2025 Laura Ramos Granados y Oleg Fernández-Llebrez Rodríguez – Laolink Consulting**
