# 🧠 Task Notes API con IA y GraphQL

Este proyecto es una API para gestionar notas con funcionalidades de CRUD y una función extra para **resumir texto usando inteligencia artificial (IA)**. Está construido con **Django**, **Strawberry GraphQL**, **Docker**, y utiliza el modelo de **transformers** `distilbart-cnn-12-6` para realizar resúmenes automáticos.

---

## 🚀 Tecnologías Usadas

- Python 3.11
- Django 5.x
- Strawberry GraphQL
- Docker + Docker Compose
- PostgreSQL
- Hugging Face Transformers (IA)
- Django REST Framework (solo para pruebas / extensibilidad)

---

## 📦 Instalación y ejecución

### 1. Clona el repositorio

```bash
git clone https://github.com/Aljodor21/MV3-CES3.git
cd tu_proyecto
```

### 2. Crea el archivo `.env`

Crea el archivo .env en la raiz del proyecto y pega esto:

```
DATABASE_URL=postgresql://postgres:0000@servelejo.lat:5432/mv3
```

### 3. Construye y levanta el proyecto con Docker

```bash
docker-compose up --build
```

Esto:

- Crea los contenedores de Django y PostgreSQL
- Instala las dependencias automáticamente (incluyendo `transformers`)
- Ejecuta migraciones

### 4. Aplica migraciones manualmente (si es necesario)

```bash
docker-compose exec web python manage.py migrate
```

---

## 🎯 Endpoints y uso de GraphQL

Una vez levantado el proyecto, accede a la interfaz de GraphQL en:

📍 `http://localhost:8000/graphql`

### ✅ Queries disponibles

#### Obtener todas las notas

```graphql
query {
  allNotes {
    id
    title
    content
    createdAt
    updatedAt
  }
}
```

#### Resumir texto (IA)

```graphql
query {
  summarizeText(content: "La inteligencia artificial es una disciplina de la informática que estudia cómo crear programas capaces de realizar tareas que requieren inteligencia humana, como el aprendizaje, el razonamiento y la comprensión del lenguaje natural...")
}
```

📌 *El modelo utilizado es `sshleifer/distilbart-cnn-12-6` de Hugging Face.*

---

### 🔄 Mutaciones disponibles

#### Crear una nota

```graphql
mutation {
  createNote(title: "Título", content: "Contenido largo de la nota") {
    id
    title
    content
  }
}
```

#### Actualizar una nota

```graphql
mutation {
  updateNote(id: 1, title: "Nuevo Título") {
    id
    title
    content
  }
}
```

#### Eliminar una nota

```graphql
mutation {
  deleteNote(id: 1)
}
```

---

## 🧪 Probar desde DRF (opcional)

También puedes probar el modelo `Note` con Django REST Framework en:

📍 `http://localhost:8000/api/notes/` 

---

## 🧠 ¿Cómo funciona la IA?

- Se usa `transformers.pipeline("summarization")`
- Se carga el modelo `sshleifer/distilbart-cnn-12-6` al inicio
- El método `summarizeText(content)` retorna un resumen con `max_length=60` y `min_length=20`

---

## 🛠 Estructura del Proyecto

```
MV3/
├── notes/                  # App principal
│   ├── models.py           # Modelo Note
│   ├── schema.py           # GraphQL Schema con Strawberry
│   ├── serializers.py      # (Opcional) DRF Serializer para Note
│   └── ...
├── core/                   # Proyecto principal
│   ├── settings.py         # Configuracion general
├── .env                    # Debes crearlo
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── favicon.ico
├── manage.py
└── requirements.txt
```

---

## 📚 Requisitos extra

Para correr fuera de Docker (Recomendado crear un entorno virtual):

```bash
pip install -r requirements.txt
```

Si usas `transformers`, asegúrate de tener instalado `torch` o `tensorflow`, por ejemplo:

```bash
pip install transformers torch
```

---

## 📌 Autor

Desarrollado por **Alejandro Toro Guarin** como MV3 para CES3 🌱

---