# Management Historical Medicals Backend

Api de la aplicación web para la prestación de servicios terapéuticos, de salud y bienestar, además de la visualización de un listado de profesionales de la salud que estén acordes al servicio que sea solicitado, agendamiento de citas, relización de pagos y demás requerimientos que se contemplaron para el desarrollo de software de este proyecto. También se entregará la documentación necesaria incluyendo un plan de pruebas ejecutado.

### Dependencias 📋

---

Como prerequisito debe tener instalado Docker en el sistema operatvo: [Obtener Docker](https://www.docker.com/products/overview)

### Parámetros de configuración ⚙️

---

- django

| **KEY**                      | **VALUE**                                             |
| ---------------------------- | ----------------------------------------------------- |
| DJANGO_SETTINGS_MODULE       | management_medical_history_backend.settings.local |
| DJANGO_SECRET_KEY            | 'plj!mk+bg=2!0qq37o)p6@j500(+o6+$1yq1\*^dbxrlf6439zc' |
| DJANGO_ADMIN_URL             | admin/                                                |
| DJANGO_ALLOWED_HOSTS         | localhost,0d895c4d2e45.ngrok.io                       |
| DJANGO_CORS_ORIGIN_WHITELIST | http://localhost:3000                                 |
| SERVER_HOST                  | http://localhost:9010                                 |

- postgres

| **KEY**           | **VALUE**                        |
| ----------------- | -------------------------------- |
| POSTGRES_HOST     | postgres                         |
| POSTGRES_PORT     | 5432                             |
| POSTGRES_DB       | siellano_db                      |
| POSTGRES_USER     | siellano_user                    |
| POSTGRES_PASSWORD | ZAvrFHvY9kDo7ZFrhvj5Z391Ifin6Wcp |

### Instrucciones de construcción o despliegue 📦

---

| **DESCRIPCIÓN**                   | **COMANDO**                                            |
| --------------------------------- | ------------------------------------------------------ |
| Compilación entorno de pruebas    | `docker-compose -f docker-compose.dev.yml up --build`  |
| Compilación entorno de producción | `docker-compose -f docker-compose.prod.yml -d --build` |

### Autores ✒️

---

Edwin Castaño - ecastano@pcaingenieria.com

#### Observaciones 📄

---
