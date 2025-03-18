# Galatea Artifact Clue API

## Descripción
Esta API permite analizar manuscritos antiguos para detectar pistas sobre artefactos mágicos. Se implementa en **Python con Flask**, usa **PostgreSQL** como base de datos y está preparada para desplegarse en la nube (AWS/GCP) con **Docker**.

## Características
- Detecta pistas en un manuscrito verificando secuencias de cuatro letras consecutivas en **horizontal, vertical o diagonal**.
- Expone dos endpoints principales:
  - `/clue/` (POST) → Recibe un manuscrito y devuelve si contiene pistas.
  - `/stats/` (GET) → Devuelve estadísticas sobre los manuscritos analizados.
- Base de datos **PostgreSQL** para almacenar manuscritos y sus resultados.
- Preparada para correr en **Docker** y desplegarse en **AWS ECS**.

---

##  Instalación y configuración local

### 1️ Clonar el repositorio
```sh
git clone https://github.com/AndresRes3/artificios.git
cd app
```

### 2️ Crear un entorno virtual e instalar dependencias
```sh
python -m venv venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3️ Configurar la base de datos local (PostgreSQL)
Asegúrate de tener PostgreSQL instalado y ejecuta:
```sql
CREATE DATABASE galatea;
CREATE TABLE manuscripts (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    has_clue BOOLEAN NOT NULL
);
```

### 4️ Configurar variables de entorno
Crea un archivo `.env` con:
```ini
DATABASE_URL=postgresql://postgres:password@localhost:5432/galatea
FLASK_ENV=production
```

### 5️ Ejecutar la API
```sh
python app/api.py
```
La API estará disponible en `http://localhost:8080/`

---

## Uso con Docker

### 1️ Construir la imagen Docker
```sh
docker build -t galatea-api .
```

### 2️ Levantar API y base de datos con Docker Compose
```sh
docker-compose up -d
```

### 3️ Probar la API con `curl`
```sh
curl -X POST "http://localhost:8080/clue/" \
     -H "Content-Type: application/json" \
     -d '{"manuscript": ["RTHGQW","XRLORE","NARURR","REVRAL","EGSILE","BRINDS"]}'
```

---

## Despliegue en la nube (Nivel 2)

### ** AWS ECS + RDS**
1. Crear un repositorio en **Amazon Elastic Container Registry (ECR)**:
   ```sh
   aws ecr create-repository --repository-name galatea-api
   ```
2. Construir y subir la imagen:
   ```sh
   docker build -t galatea-api .
   docker tag galatea-api:latest [AWS_ACCOUNT_ID].dkr.ecr.[REGION].amazonaws.com/galatea-api:latest
   docker push [AWS_ACCOUNT_ID].dkr.ecr.[REGION].amazonaws.com/galatea-api:latest
   ```
3. Crear una **tarea en AWS ECS** conectada a **Amazon RDS (PostgreSQL)**.

---

## Pruebas de rendimiento

Se recomienda usar **JMeter o Postman** para evaluar el rendimiento. Un ejemplo de prueba de carga:
```sh
ab -n 1000 -c 100 http://localhost:8080/clue/
```
**Resultados esperados:**
- **Tasa de transacciones por segundo** > 1000 req/s.
- **Percentil 90 del tiempo de respuesta** < 200ms.

---

## Endpoints de la API

### **POST `/clue/`**
**Descripción:** Analiza un manuscrito y determina si contiene una pista.

**Ejemplo de request:**
```json
{
  "manuscript": ["RTHGQW", "XRLORE", "NARURR", "REVRAL", "EGSILE", "BRINDS"]
}
```

**Ejemplo de response:**
```json
{"message": "Elowen el manuscrito contenia una pista"}
```

---

### **GET `/stats/`**
**Descripción:** Devuelve estadísticas de los manuscritos analizados.

 **Ejemplo de response:**
```json
{
  "count_clue_found": 40,
  "count_no_clue": 100,
  "ratio": 0.4
}
```

 **Creado por:** Andres Restrepo

