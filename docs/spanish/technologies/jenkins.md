# Guía de Integración CI/CD - Jenkins & Automatización de Pruebas

## 📚 Tabla de Contenidos
1. [¿Qué es CI/CD?](#qué-es-cicd)
2. [¿Qué es Jenkins?](#qué-es-jenkins)
3. [Conceptos Fundamentales de Jenkins](#conceptos-fundamentales-de-jenkins)
4. [Fundamentos del Lenguaje Groovy](#fundamentos-del-lenguaje-groovy)
5. [Requisitos e Instalación](#requisitos-e-instalación)
6. [Ejemplos de Pipeline](#ejemplos-de-pipeline)
7. [Gestión de Credenciales](#gestión-de-credenciales)
8. [Consumo de Recursos](#consumo-de-recursos-e-implicaciones)
9. [Herramientas Alternativas de CI/CD](#herramientas-alternativas-de-cicd)
10. [Recursos Oficiales](#recursos-oficiales)

---

## ¿Qué es CI/CD?

**CI/CD** = **Integración Continua** + **Entrega/Despliegue Continuo**

### Integración Continua (CI)
- Integra automáticamente cambios de código de múltiples desarrolladores
- Cada commit dispara construcciones y pruebas automáticas
- **Beneficios**: Detección temprana de errores, retroalimentación rápida, reducción de problemas de integración

### Entrega/Despliegue Continuo (CD)
- **Entrega**: Cambios de código preparados automáticamente para liberación
- **Despliegue**: Cambios desplegados automáticamente a producción
- **Beneficios**: Liberaciones más rápidas, despliegues consistentes, riesgo reducido

### ¿Por qué CI/CD para Automatización de Pruebas?
- Las pruebas se ejecutan automáticamente en cada cambio de código
- Detección temprana de errores
- Entornos de prueba consistentes
- Reportes de pruebas centralizados
- Las puertas de calidad previenen código defectuoso

---

## ¿Qué es Jenkins?

**Jenkins** es un servidor de automatización de código abierto para construir, probar y desplegar aplicaciones.


## Herramientas Alternativas de CI/CD

| Herramienta | Costo | Configuración | Mejor Para |
|-------------|-------|---------------|------------|
| **GitHub Actions** | Gratis/Pago | Fácil | Proyectos en GitHub |
| **GitLab CI** | Gratis/Pago | Fácil | Proyectos en GitLab |
| **CircleCI** | Gratis/Pago | Fácil | Flujos de Docker |
| **Travis CI** | Gratis/Pago | Fácil | Código abierto |
| **Azure DevOps** | Gratis/Pago | Media | Stack de Microsoft |
| **TeamCity** | Pago | Difícil | Java empresarial |

**GitHub Actions**: https://github.com/features/actions  
**GitLab CI**: https://docs.gitlab.com/ee/ci/  
**CircleCI**: https://circleci.com/  

---

## Conceptos Fundamentales de Jenkins

### 1. Pipeline
Conjunto de plugins para implementar flujos de trabajo CI/CD.

**Tipos:**
- **Declarativo**: Sintaxis más simple (recomendado)
- **Scripted**: Más flexible, Groovy puro

```groovy
pipeline {
    agent any
    stages {
        stage('Build') { steps { /* ... */ } }
        stage('Test') { steps { /* ... */ } }
    }
}
```

### 2. Stages (Etapas)
Fases principales en el pipeline (Build, Test, Deploy).

```groovy
stages {
    stage('Setup') {
        steps { echo 'Configurando...' }
    }
    stage('Test') {
        steps { sh 'pytest tests/ -v' }
    }
}
```

### 3. Steps (Pasos)
Las tareas significan las acciones que el pipeline ejecutará, en pocas palabras son las acciones que el pipeline ejecutará usando los comandos definidos en el pipeline.
Tareas individuales: `sh`, `bat`, `echo`, `script`, `git`

### 4. Agents (Agentes)
Donde se ejecuta el pipeline:
- `agent any`: Cualquier agente disponible
- `agent { label 'linux' }`: Etiqueta específica
- `agent { docker 'python:3.10' }`: Contenedor Docker

### 5. Variables de Entorno
```groovy
environment {
    PYTHON_VERSION = '3.10'
    API_KEY = credentials('api-key-id')  // Seguro
}
```

### 6. Acciones Post
Ejecutar después del pipeline:
```groovy
post {
    always { publishHTML(/* reportes */) }
    failure { mail to: 'equipo@example.com' }
}
```

### 7. Ejecución Paralela
```groovy
parallel {
    stage('Pruebas API') { steps { /* ... */ } }
    stage('Pruebas UI') { steps { /* ... */ } }
}
```

### 8. Triggers (Disparadores)
```groovy
triggers {
    cron('H 2 * * *')  // Diariamente a las 2 AM
    pollSCM('H/15 * * * *')  // Revisar repo cada 15 min
}
```

## Creación de Jobs en Jenkins

Esta sección explica **paso a paso** cómo crear un job de Jenkins para ejecutar tu pipeline de automatización de pruebas.

El job es el algoritmo que será ejecutado por el servidor de Jenkins, este algoritmo está definido en el Jenkinsfile.


La estrategia recomendada es usar el tipo de job "Pipeline", esto es porque es el más flexible y es el recomendado por el equipo de Jenkins.

Esta es la estructura de los jobs usados en este framework:

```
ci-cd/
├── jenkins_smoke/          ← Pruebas Smoke (¡NUEVO!)
│   └── jenkinsfile
├── jenkins_api/            ← Solo pruebas API
│   └── jenkinsfile
├── jenkins_ui/             ← Solo pruebas UI
│   └── jenkinsfile
├── jenkins_stagin/         ← Pruebas staging combinadas
│   └── jenkinsfile
├── jenkins_regression/     ← Regresión completa
│   └── jenkinsfile
└── jenkins_production/     ← Despliegue a producción
    └── jenkinsfile
```

### Tipos de Jobs en Jenkins

Antes de crear un job, comprende los diferentes tipos:

| Tipo de Job | Descripción | Caso de Uso |
|-------------|-------------|-------------|
| **Freestyle Project** | Simple, configuración basada en UI | Tareas básicas, no pipelines complejos |
| **Pipeline** | Pipeline basado en código (Jenkinsfile) | **Recomendado para automatización** |
| **Multibranch Pipeline** | Crea automáticamente pipelines para cada rama | Múltiples ramas (dev, staging, main) |
| **Folder** | Organizar jobs | Agrupar jobs relacionados |

**Para este framework, usa "Pipeline" o "Multibranch Pipeline".**

---

### Método 1: Pipeline Job (Rama Única)

#### Paso 1: Crear Nuevo Pipeline Job

1. **Acceder al Dashboard de Jenkins**
   - Abrir navegador: `http://localhost:8080`
   - Iniciar sesión con tus credenciales de administrador

2. **Click en "New Item"**
   - En la barra lateral izquierda, click en **"New Item"**

3. **Configurar Nombre del Job**
   - Ingresar un nombre descriptivo: `QA-Automation-API-Tests`
   - Seleccionar **"Pipeline"**
   - Click en **"OK"**

#### Paso 2: Configurar Ajustes Generales

1. **Descripción** (Opcional pero recomendado)
   ```
   Pipeline de Automatización de Pruebas API
   Ejecuta pruebas API usando pytest contra la API de JSONPlaceholder
   ```

2. **Descartar Construcciones Antiguas** (Recomendado)
   - Marcar "Discard old builds"
   - Días para mantener construcciones: `30`
   - Máx # de construcciones a mantener: `20`

3. **Proyecto GitHub** (Si usas GitHub)
   - Marcar "GitHub project"
   - URL del proyecto: `https://github.com/tu-usuario/C-QA-Automation-Framework`

#### Paso 3: Disparadores de Construcción (Opcional)

Elige cómo debe iniciar el pipeline:

**Opción A: Poll SCM** (Revisar cambios periódicamente)
```
H/15 * * * *  # Cada 15 minutos
```

**Opción B: GitHub Webhook** (Disparar en push)
- Requiere configuración de webhook en GitHub
- Marcar "GitHub hook trigger for GITScm polling"

**Opción C: Construcción Periódica** (Programada)
```
H 2 * * *     # Diariamente a las 2 AM
H 2 * * 1-5   # Días de semana a las 2 AM
```

**Opción D: Solo Manual**
- No marcar ningún disparador (ejecutar manualmente)

#### Paso 4: Configuración del Pipeline

**Hay dos formas de definir el pipeline:**

##### Opción A: Pipeline Script from SCM (Recomendado)

Esto lee el Jenkinsfile directamente desde tu repositorio Git.

1. **Definition**: Seleccionar **"Pipeline script from SCM"**

2. **SCM**: Seleccionar **"Git"**

3. **Repository URL**: Ingresar la URL de tu repositorio
   ```
   https://github.com/tu-usuario/C-QA-Automation-Framework.git
   ```
   
4. **Credentials**: 
   - Si es repo público: Seleccionar "none"
   - Si es repo privado: Click en "Add" → Agregar credenciales de GitHub

5. **Branch Specifier**: 
   ```
   */main
   ```
   O usa `*/develop` para la rama de desarrollo

6. **Script Path**: Ruta al Jenkinsfile en tu repositorio
   ```
   ci-cd/jenkins_stagin/jenkinsfile
   ```
   
7. **Click en "Save"**

---

## Fundamentos del Lenguaje Groovy

Los Pipelines de Jenkins usan **Groovy** (lenguaje dinámico basado en JVM), esto no es el núcleo principal de este contenido educativo, pero es importante conocerlo, para entender mejor cómo se estructura una lógica de pipeline siguiendo una lógica declarativa.

### Sintaxis Básica:
```groovy
// Variables
def myVar = "Hola"
String typed = "Mundo"

// Interpolación de strings
println "Hola, ${nombre}!"

// Condicionales
if (env.BRANCH_NAME == 'main') {
    echo 'Rama principal'
}

// Bucles
for (item in ['a', 'b', 'c']) {
    echo item
}

// Funciones
def deploy(env) {
    sh "deploy.sh ${env}"
}
```

### En Jenkinsfile:
```groovy
stage('Pruebas Dinámicas') {
    steps {
        script {
            def suites = ['smoke', 'api', 'regression']
            for (suite in suites) {
                sh "pytest -m ${suite}"
            }
        }
    }
}
```

**Documentación de Groovy**: https://groovy-lang.org/documentation.html

---

## Requisitos e Instalación

### Requisitos del Sistema
- **RAM**: 4 GB+ recomendado
- **Disco**: 50 GB+ (construcciones, artefactos)
- **Java**: JDK 11 o 17 (requerido)
- **CPU**: 2+ núcleos

### Instalación

**Ubuntu/Debian:**
```bash
# Instalar Java
sudo apt update
sudo apt install openjdk-11-jdk

# Agregar repositorio de Jenkins
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

# Instalar e iniciar Jenkins
sudo apt update
sudo apt install jenkins
sudo systemctl start jenkins
sudo systemctl enable jenkins
```

**Docker (Más Fácil):**
```bash
docker run -d -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  --name jenkins jenkins/jenkins:lts
```

**Acceder a Jenkins**: http://localhost:8080

### Plugins Requeridos
1. Pipeline
2. Git
3. HTML Publisher
4. Allure
5. Credentials Binding
6. Email Extension

Instalar: `Manage Jenkins` → `Manage Plugins`

**Plugins de Jenkins**: https://plugins.jenkins.io/

### Mejores Prácticas

1. **Usar Pipeline from SCM**: Mantener Jenkinsfile en el repositorio
2. **Nombres Descriptivos**: Usar nombres claros de jobs como `API-Tests-Staging`
3. **Organizar con Carpetas**: Agrupar jobs relacionados
4. **Configurar Retención de Construcciones**: No mantener construcciones para siempre
5. **Usar Gestor de Credenciales**: Nunca codificar secretos en duro
6. **Etiquetar Construcciones**: Usar descripciones de construcción para construcciones importantes
7. **Monitorear Espacio en Disco**: Las construcciones antiguas consumen espacio

---

### Siguientes Pasos

Después de crear tu primer job:

1. **Agregar Credenciales**: Para claves API, contraseñas
2. **Configurar Notificaciones**: Email o Slack en fallas
3. **Configurar Webhooks**: Disparadores automáticos desde Git
4. **Crear Más Pipelines**: Pruebas UI, staging, producción
5. **Explorar Blue Ocean**: UI moderna para pipelines (`http://localhost:8080/blue`)

---

## Ejemplos de Pipeline

### Ejemplo 1: Pipeline Completo de Pruebas API
Ver ejemplo completo: `ci/cd/jenkins_api/jenkinsfile`

### Ejemplo 2: Pipeline Completo de Pruebas UI
Ver ejemplo completo: `ci/cd/jenkins_ui/jenkinsfile`

### Ejemplo 3: Pipeline Completo de Staging
Ver ejemplo completo: `ci/cd/jenkins_staging/jenkinsfile`

---

## 🔐 Gestión de Credenciales

### Agregar Credenciales:
1. `Manage Jenkins` → `Manage Credentials`
2. Seleccionar dominio → "Add Credentials"
3. Elegir tipo (Secret text, Username/Password, etc.)
4. Asignar ID

### Usar en Pipeline:
```groovy
environment {
    API_KEY = credentials('api-key-id')  // Texto secreto
    DB_CREDS = credentials('db-creds')   // Usuario:contraseña
}

steps {
    // Automáticamente enmascarado en logs
    sh 'curl -H "Authorization: Bearer ${API_KEY}" https://api.example.com'
    
    // Acceder por separado
    sh 'echo "Usuario: ${DB_CREDS_USR}"'
    sh 'echo "Contraseña: ${DB_CREDS_PSW}"'  // Oculto
}
```

**Mejores Prácticas:**
- Nunca codificar secretos en duro
- Usar IDs descriptivos
- Rotar credenciales regularmente
- Limitar alcance cuando sea posible

---

## ⚠️ Consumo de Recursos e Implicaciones

### Memoria (RAM):
- **Jenkins Master**: 2-4 GB mínimo
- **Por Construcción**: 500 MB - 2 GB
- **Agentes**: 2-8 GB cada uno

**Incrementar heap:**
```bash
JAVA_OPTS="-Xmx4096m -Xms1024m"
```

### CPU:
- **Master**: 2+ núcleos
- **Pruebas Selenium**: Intensivo en CPU
- **Construcciones Paralelas**: Multiplica el uso

### Espacio en Disco:
- **Jenkins Home**: 10-50 GB
- **Workspaces**: 1-10 GB por job
- **Artefactos**: Reportes, logs se acumulan

**Gestionar construcciones:**
```groovy
options {
    buildDiscarder(logRotator(
        numToKeepStr: '30',
        artifactNumToKeepStr: '10'
    ))
}
```

### Tiempo:
- **Pruebas API**: 2-10 minutos
- **Pruebas UI**: 10-60 minutos
- **Regresión**: 1-4 horas

**Optimización**: Ejecución paralela, caché, pruebas smoke primero

### Costos:
- **Auto-hospedado**: Hardware + mantenimiento
- **Nube** (AWS/Azure): ~$30+/mes por instancia

---

## 📚 Recursos Oficiales

### Jenkins:
- **Sitio Web**: https://www.jenkins.io/
- **Documentación**: https://www.jenkins.io/doc/
- **Sintaxis de Pipeline**: https://www.jenkins.io/doc/book/pipeline/syntax/
- **Plugins**: https://plugins.jenkins.io/
- **Tutoriales**: https://www.jenkins.io/doc/tutorials/

### Groovy:
- **Sitio Web**: https://groovy-lang.org/
- **Documentación**: https://groovy-lang.org/documentation.html

### Comunidad:
- **Stack Overflow**: https://stackoverflow.com/questions/tagged/jenkins
- **GitHub**: https://github.com/jenkinsci/jenkins

---

**Version**: 0.1.2  
**Framework**: C-QA Automation Framework  