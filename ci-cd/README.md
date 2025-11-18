>English Version: At the Top of this file you are going to see the English version indicated by this sy  mbol 🟦, and below you are going to see the Spanish version indicated by this symbol 🟩, you can choose the one you want to use.

>Version en Español: En la parte superior de este archivo se encuentra la versión en Inglés indicada por este símbolo 🟦, y debajo se encuentra la versión en Español indicada por este símbolo 🟩, puedes escoger la que prefieras.  

# 🟦 CI/CD Integration Guide - Jenkins & Test Automation 🟦

## 📚 Table of Contents
1. [What is CI/CD](#what-is-cicd)
2. [What is Jenkins](#what-is-jenkins)
3. [Jenkins Core Concepts](#jenkins-core-concepts)
4. [Groovy Language Basics](#groovy-language-basics)
5. [Requirements & Installation](#requirements--installation)
6. [Creating Jenkins Jobs](#creating-jenkins-jobs)
7. [Pipeline Examples](#pipeline-examples)
8. [Credentials Management](#credentials-management)
9. [Resource Consumption](#resource-consumption--implications)
10. [Alternative CI/CD Tools](#alternative-cicd-tools)
11. [Official Resources](#official-resources)

---

## What is CI/CD

**CI/CD** = **Continuous Integration** + **Continuous Delivery/Deployment**

### Continuous Integration (CI)
- Automatically integrate code changes from multiple developers
- Every commit triggers automated builds and tests
- **Benefits**: Early bug detection, faster feedback, reduced integration issues

### Continuous Delivery/Deployment (CD)
- **Delivery**: Code changes automatically prepared for release
- **Deployment**: Changes automatically deployed to production
- **Benefits**: Faster releases, consistent deployments, reduced risk

### Why CI/CD for Test Automation?
- Tests run automatically on every code change
- Early bug detection
- Consistent test environments
- Centralized test reports
- Quality gates prevent broken code

---

## What is Jenkins

**Jenkins** is an open-source automation server for building, testing, and deploying applications.


## Alternative CI/CD Tools

| Tool | Cost | Setup | Best For |
|------|------|-------|----------|
| **GitHub Actions** | Free/Paid | Easy | GitHub projects |
| **GitLab CI** | Free/Paid | Easy | GitLab projects |
| **CircleCI** | Free/Paid | Easy | Docker workflows |
| **Travis CI** | Free/Paid | Easy | Open source |
| **Azure DevOps** | Free/Paid | Medium | Microsoft stack |
| **TeamCity** | Paid | Hard | Enterprise Java |

**GitHub Actions**: https://github.com/features/actions  
**GitLab CI**: https://docs.gitlab.com/ee/ci/  
**CircleCI**: https://circleci.com/  

### Key Features:
- **Open Source**: Free with 1800+ plugins
- **Platform Independent**: Windows, Linux, macOS
- **Pipeline as Code**: Define CI/CD in code (Jenkinsfile)
- **Distributed Builds**: Multiple machines
- **Extensible**: Extensive plugin ecosystem

### Common Use Cases:
1. Automated Testing (Unit, API, UI)
2. Build Automation
3. Deployment Automation
4. Scheduled Jobs (nightly builds)
5. Code Quality Monitoring

**Official Website**: https://www.jenkins.io/

---

## Jenkins Core Concepts

### 1. Pipeline
Suite of plugins for implementing CI/CD workflows.

**Types:**
- **Declarative**: Simpler syntax (recommended)
- **Scripted**: More flexible, pure Groovy

```groovy
pipeline {
    agent any
    stages {
        stage('Build') { steps { /* ... */ } }
        stage('Test') { steps { /* ... */ } }
    }
}
```

### 2. Stages
Major phases in pipeline (Build, Test, Deploy).

```groovy
stages {
    stage('Setup') {
        steps { echo 'Setting up...' }
    }
    stage('Test') {
        steps { sh 'pytest tests/ -v' }
    }
}
```

### 3. Steps
The tasks means the actions that the pipeline will perform, in short words is the actions that the pipeline will execute using the commands that are been defined in the pipeline.
Individual tasks: `sh`, `bat`, `echo`, `script`, `git`

### 4. Agents
Where pipeline executes:
- `agent any`: Any available agent
- `agent { label 'linux' }`: Specific label
- `agent { docker 'python:3.10' }`: Docker container

### 5. Environment Variables
```groovy
environment {
    PYTHON_VERSION = '3.10'
    API_KEY = credentials('api-key-id')  // Secure
}
```

### 6. Post Actions
Execute after pipeline:
```groovy
post {
    always { publishHTML(/* reports */) }
    failure { mail to: 'team@example.com' }
}
```

### 7. Parallel Execution
```groovy
parallel {
    stage('API Tests') { steps { /* ... */ } }
    stage('UI Tests') { steps { /* ... */ } }
}
```

### 8. Triggers
```groovy
triggers {
    cron('H 2 * * *')  // Daily at 2 AM
    pollSCM('H/15 * * * *')  // Check repo every 15 min
}
```

---

## Groovy Language Basics

Jenkins Pipelines use **Groovy** (JVM-based dynamic language), this is not the main core of this educational content, but it is important to know it, as better understand on how is structere a pipilene logic attending to a declarative logic.

### Basic Syntax:
```groovy
// Variables
def myVar = "Hello"
String typed = "World"

// String interpolation
println "Hello, ${name}!"

// Conditionals
if (env.BRANCH_NAME == 'main') {
    echo 'Main branch'
}

// Loops
for (item in ['a', 'b', 'c']) {
    echo item
}

// Functions
def deploy(env) {
    sh "deploy.sh ${env}"
}
```

### In Jenkinsfile:
```groovy
stage('Dynamic Tests') {
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

**Groovy Docs**: https://groovy-lang.org/documentation.html

---

## Requirements & Installation

### System Requirements
- **RAM**: 4 GB+ recommended
- **Disk**: 50 GB+ (builds, artifacts)
- **Java**: JDK 11 or 17 (required)
- **CPU**: 2+ cores

### Installation

**Ubuntu/Debian:**
```bash
# Install Java
sudo apt update
sudo apt install openjdk-11-jdk

# Add Jenkins repository
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

# Install & start Jenkins
sudo apt update
sudo apt install jenkins
sudo systemctl start jenkins
sudo systemctl enable jenkins
```

**Docker (Easiest):**
```bash
docker run -d -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  --name jenkins jenkins/jenkins:lts
```

**Access Jenkins**: http://localhost:8080

### Required Plugins
1. Pipeline
2. Git
3. HTML Publisher
4. Allure
5. Credentials Binding
6. Email Extension

Install: `Manage Jenkins` → `Manage Plugins`

**Jenkins Plugins**: https://plugins.jenkins.io/

---

## Creating Jenkins Jobs

### Creating a New Job
1. **New Item**: Click on the "New Item" link on the Jenkins dashboard.
2. **Enter Job Name**: Enter a name for your job.
3. **Select Job Type**: Select "Pipeline" as the job type.
4. **Configure Pipeline**: Configure the pipeline by specifying the pipeline script or Jenkinsfile.

### Configuring the Pipeline
1. **Pipeline Script**: You can either specify the pipeline script directly or point to a Jenkinsfile in your source code repository.
2. **Jenkinsfile**: A Jenkinsfile is a Groovy script that defines the pipeline.

### Example Jenkinsfile
```groovy
pipeline {
    agent any
    stages {
        stage('Build') { steps { /* ... */ } }
        stage('Test') { steps { /* ... */ } }
    }
}
```

---

## Creating Jenkins Jobs

This section explains **step-by-step**, the precise core concepts of how to create a Jenkins job to execute your test automation pipeline.

The jobs is the algorithm that will be executed by the Jenkins server, this algorithm is defined in the Jenkinsfile.


The recomended strategy is to use the "Pipeline" job type, this is because it is the most flexible and it is the one that is recommended by the Jenkins team.

This is the structure of the jobs used in this framework:

```
ci-cd/
├── jenkins_smoke/          ← Smoke tests 
│   └── jenkinsfile
├── jenkins_api/            ← API tests only
│   └── jenkinsfile
├── jenkins_ui/             ← UI tests only
│   └── jenkinsfile
├── jenkins_stagin/         ← Combined staging tests
│   └── jenkinsfile
├── jenkins_regression/     ← Full regression
│   └── jenkinsfile
└── jenkins_production/     ← Production deployment
    └── jenkinsfile

```  

### Job Types in Jenkins

Before creating a job, understand the different types:

| Job Type | Description | Use Case |
|----------|-------------|----------|
| **Freestyle Project** | Simple, UI-based configuration | Basic tasks, not complex pipelines |
| **Pipeline** | Code-based pipeline (Jenkinsfile) | **Recommended for automation** |
| **Multibranch Pipeline** | Automatically creates pipelines for each branch | Multiple branches (dev, staging, main) |
| **Folder** | Organize jobs | Group related jobs |

**For this framework, use "Pipeline" or "Multibranch Pipeline".**

---

### Method 1: Pipeline Job (Single Branch)

#### Step 1: Create New Pipeline Job

1. **Access Jenkins Dashboard**
   - Open browser: `http://localhost:8080`
   - Login with your admin credentials

2. **Click "New Item"**
   - On the left sidebar, click **"New Item"**

3. **Configure Job Name**
   - Enter a descriptive name: `QA-Automation-API-Tests`
   - Select **"Pipeline"**
   - Click **"OK"**

#### Step 2: Configure General Settings

1. **Description** (Optional but recommended)
   ```
   API Test Automation Pipeline
   Runs API tests using pytest against JSONPlaceholder API
   ```

2. **Discard Old Builds** (Recommended)
   - Check "Discard old builds"
   - Days to keep builds: `30`
   - Max # of builds to keep: `20`

3. **GitHub Project** (If using GitHub)
   - Check "GitHub project"
   - Project url: `https://github.com/your-username/C-QA-Automation-Framework`

#### Step 3: Build Triggers (Optional)

Choose how the pipeline should start:

**Option A: Poll SCM** (Check for changes periodically)
```
H/15 * * * *  # Every 15 minutes
```

**Option B: GitHub Webhook** (Trigger on push)
- Requires GitHub webhook configuration
- Check "GitHub hook trigger for GITScm polling"

**Option C: Build Periodically** (Scheduled)
```
H 2 * * *     # Daily at 2 AM
H 2 * * 1-5   # Weekdays at 2 AM
```

**Option D: Manual Only**
- Don't check any triggers (run manually)

#### Step 4: Pipeline Configuration

**There are two ways to define the pipeline:**

##### Option A: Pipeline Script from SCM (Recommended)

This reads the Jenkinsfile directly from your Git repository.

1. **Definition**: Select **"Pipeline script from SCM"**

2. **SCM**: Select **"Git"**

3. **Repository URL**: Enter your repository URL
   ```
   https://github.com/your-username/C-QA-Automation-Framework.git
   ```
   
4. **Credentials**: 
   - If public repo: Select "none"
   - If private repo: Click "Add" → Add GitHub credentials

5. **Branch Specifier**: 
   ```
   */main
   ```
   Or use `*/develop` for development branch

6. **Script Path**: Path to Jenkinsfile in your repository
   ```
   ci-cd/jenkins_stagin/jenkinsfile
   ```
   
7. **Click "Save"**

##### Option B: Pipeline Script (Direct)

Write or paste the Jenkinsfile content directly in Jenkins.

1. **Definition**: Select **"Pipeline script"**

2. **Script**: Paste your pipeline code
   ```groovy
   pipeline {
       agent any
       
       environment {
           PY_VER = "3.10"
       }
       
       stages {
           stage('Setup') {
               steps {
                   echo 'Setting up environment...'
                   sh "python${PY_VER} -m venv venv"
                   sh ". venv/bin/activate && pip install -r requiriments.txt"
               }
           }
           
           stage('Run API Tests') {
               steps {
                   echo 'Running API tests...'
                   sh ". venv/bin/activate && pytest tests/api_test/ -v"
               }
           }
       }
   }
   ```

3. **Click "Save"**

#### Step 5: Run the Pipeline

1. **Click "Build Now"** on the job page
2. **View Build Progress**: Click on the build number (e.g., #1)
3. **View Console Output**: Click "Console Output" to see logs
4. **View Stage View**: See each stage's status visually

#### Step 6: View Results

After build completes:
- 🔵**Blue ball**: Success
- 🔴**Red ball**: Failure
- ⚪**Gray ball**: Aborted
- 🟡**Yellow ball**: Unstable (tests failed)

**Access Reports:**
- Click on build number → **"Test Report"** or **"HTML Reports"**

---

### Method 2: Multibranch Pipeline (Multiple Branches)

Use this when you have multiple branches (main, develop, feature branches).

#### Step 1: Create Multibranch Pipeline

1. **New Item** → Enter name: `QA-Automation-Framework`
2. Select **"Multibranch Pipeline"**
3. Click **"OK"**

#### Step 2: Configure Branch Sources

1. **Add Source** → Select **"Git"**

2. **Project Repository**: Enter your repo URL
   ```
   https://github.com/your-username/C-QA-Automation-Framework.git
   ```

3. **Credentials**: Add if needed (for private repos)

4. **Behaviors**: 
   - Discover branches
   - Discover tags (optional)

#### Step 3: Build Configuration

1. **Mode**: Select **"by Jenkinsfile"**

2. **Script Path**: Path to Jenkinsfile
   ```
   ci-cd/jenkins_stagin/jenkinsfile
   ```

#### Step 4: Scan Multibranch Pipeline Triggers

1. **Periodically if not otherwise run**
   ```
   1 hour
   ```
   Jenkins will scan for new branches every hour

2. **Click "Save"**

Jenkins will automatically:
- Scan repository for branches
- Create a pipeline for each branch with a Jenkinsfile
- Run pipelines when branches are updated

---

### Quick Setup Example (API Tests)

Here's a complete example for your API tests:

**Job Name**: `API-Tests-Pipeline`

**Pipeline Script from SCM**:
- **SCM**: Git
- **Repository URL**: Your GitHub/GitLab URL
- **Branch**: `*/main`
- **Script Path**: `ci-cd/jenkins_stagin/jenkinsfile`

**Build Triggers**:
- Poll SCM: `H/15 * * * *`

**Click "Save"** → **"Build Now"**

That's it! Jenkins will:
1. Clone the repository
2. Read the Jenkinsfile at `ci-cd/jenkins_stagin/jenkinsfile`
3. Execute the pipeline stages
4. Publish test reports

---

### Troubleshooting

#### Issue: "Permission denied" when running shell commands
**Solution**: 
- Make sure Jenkins user has proper permissions
- Check Python is installed: `which python3`

#### Issue: "pip: command not found"
**Solution**:
```bash
sudo apt install python3-pip
```

#### Issue: "Repository not found"
**Solution**:
- Verify repository URL is correct
- Add credentials for private repositories

#### Issue: Jenkinsfile not found
**Solution**:
- Verify the Script Path matches the actual file location
- Use correct case: `jenkinsfile` vs `Jenkinsfile`
- Path is relative to repository root: `ci-cd/jenkins_stagin/jenkinsfile`

#### Issue: Tests fail but pipeline succeeds
**Solution**:
- Remove `|| true` from pytest commands in Jenkinsfile
- This allows the pipeline to fail when tests fail


---


---

## Pipeline Examples

### Example 1: Complete API Tests Pipeline
See complete example: `ci/cd/jenkins_api/jenkinsfile`

### Example 2: Complete UI Tests Pipeline
See complete example: `ci/cd/jenkins_ui/jenkinsfile`

### Example 3: Complete Staging Pipeline
See complete example: `ci/cd/jenkins_staging/jenkinsfile`

---

## 🔐 Credentials Management

### Add Credentials:
1. `Manage Jenkins` → `Manage Credentials`
2. Select domain → "Add Credentials"
3. Choose type (Secret text, Username/Password, etc.)
4. Assign ID

### Use in Pipeline:
```groovy
environment {
    API_KEY = credentials('api-key-id')  // Secret text
    DB_CREDS = credentials('db-creds')   // Username:password
}

steps {
    // Automatically masked in logs
    sh 'curl -H "Authorization: Bearer ${API_KEY}" https://api.example.com'
    
    // Access separately
    sh 'echo "User: ${DB_CREDS_USR}"'
    sh 'echo "Pass: ${DB_CREDS_PSW}"'  // Hidden
}
```

**Best Practices:**
- Never hardcode secrets  
- Use descriptive IDs  
- Rotate credentials regularly  
- Limit scope when possible  

---

## ⚠️ Resource Consumption & Implications

### Memory (RAM):
- **Jenkins Master**: 2-4 GB minimum
- **Per Build**: 500 MB - 2 GB
- **Agents**: 2-8 GB each

**Increase heap:**
```bash
JAVA_OPTS="-Xmx4096m -Xms1024m"
```

### CPU:
- **Master**: 2+ cores
- **Selenium Tests**: CPU-intensive
- **Parallel Builds**: Multiply usage

### Disk Space:
- **Jenkins Home**: 10-50 GB
- **Workspaces**: 1-10 GB per job
- **Artifacts**: Reports, logs accumulate

**Manage builds:**
```groovy
options {
    buildDiscarder(logRotator(
        numToKeepStr: '30',
        artifactNumToKeepStr: '10'
    ))
}
```

### Time:
- **API Tests**: 2-10 minutes
- **UI Tests**: 10-60 minutes
- **Regression**: 1-4 hours

**Optimization**: Parallel execution, caching, smoke tests first

### Costs:
- **Self-hosted**: Hardware + maintenance
- **Cloud** (AWS/Azure): ~$30+/month per instance

---
---

## 📚 Official Resources

### Jenkins:
- **Website**: https://www.jenkins.io/
- **Documentation**: https://www.jenkins.io/doc/
- **Pipeline Syntax**: https://www.jenkins.io/doc/book/pipeline/syntax/
- **Plugins**: https://plugins.jenkins.io/
- **Tutorials**: https://www.jenkins.io/doc/tutorials/

### Groovy:
- **Website**: https://groovy-lang.org/
- **Documentation**: https://groovy-lang.org/documentation.html

### Community:
- **Stack Overflow**: https://stackoverflow.com/questions/tagged/jenkins
- **GitHub**: https://github.com/jenkinsci/jenkins

---

**Version**: 0.1.2  
**Author**: C-QA Automation Framework Team




# 🟩 CI/CD Integration Guide - Jenkins & Test Automation 🟩

## 📚 Tabla de Contenido
1. [¿Qué es CI/CD](#what-is-cicd)
2. [¿Qué es Jenkins](#what-is-jenkins)
3. [Conceptos Core de Jenkins](#jenkins-core-concepts)
4. [Conceptos Básicos de Groovy](#groovy-language-basics)
5. [Requisitos & Instalación](#requirements--installation)
6. [Creación de Jobs en Jenkins](#creating-jenkins-jobs)
7. [Ejemplos de Pipeline](#pipeline-examples)
8. [Gestión de Credenciales](#credentials-management)
9. [Consumo de Recursos](#resource-consumption--implications)
10. [Herramientas Alternativas de CI/CD](#alternative-cicd-tools)
11. [Recursos Oficiales](#official-resources)

---

## ¿Qué es CI/CD?

**CI/CD** = **Integración Continua** + **Entrega/Despliegue Continuo**

### Integración Continua (CI)
- Integración automática de cambios de código de múltiples desarrolladores
- Every commit triggers automated builds and tests
- **Beneficios**: Early bug detection, faster feedback, reduced integration issues

### Entrega/Despliegue Continuo (CD)
- **Entrega**: Cambios de código preparados automáticamente para la liberación
- **Despliegue**: Cambios de código desplegados automáticamente a producción
- **Beneficios**: Rapida liberación de cambios(Release), despliegue consistente, reducido riesgo

### ¿Por qué CI/CD para la Automatización de Pruebas?
- Los Tests se ejecutan automáticamente en cada cambio de código
- Detección temprana de errores
- Entorno de pruebas consistentes
- Reportes centralizados
- Cierres de calidad previenen código roto

---

## ¿Qué es Jenkins?

**Jenkins** es un servidor(software) de automatización de código abierto para construir, probar y desplegar aplicaciones.


## Herramientas Alternativas de CI/CD

| Herramienta | Costo | Configuración | Mejor Para |
|------|------|-------|----------|
| **GitHub Actions** | Gratuita/Paga | Fácil | Proyectos de GitHub |
| **GitLab CI** | Gratuita/Paga | Fácil | Proyectos de GitLab |
| **CircleCI** | Gratuita/Paga | Fácil | Flujos de Docker |
| **Travis CI** | Gratuita/Paga | Fácil | Código abierto |
| **Azure DevOps** | Gratuita/Paga | Medio | Pila Microsoft |
| **TeamCity** | Paga | Dificil | Java empresarial |

**GitHub Actions**: https://github.com/features/actions  
**GitLab CI**: https://docs.gitlab.com/ee/ci/  
**CircleCI**: https://circleci.com/  

### Características Clave:
- **Código Abierto**: Gratuita con 1800+ plugins
- **Plataforma Independiente**: Windows, Linux, macOS
- **Pipeline como Código**: Define CI/CD en código (Jenkinsfile)
- **Builds Distribuidos**: Multiple máquinas
- **Extensible**: Extensive plugin ecosystem

### Casos de Uso Comunes:
1. Testing Automatizado (Unit, API, UI)
2. Automatización de Builds
3. Automatización de Despliegues
4. Trabajos Programados (nightly builds)
5. Monitoreo de Calidad del Código

**Website Oficial**: https://www.jenkins.io/

---

## Conceptos Core de Jenkins

### 1. Pipeline
Suite of plugins for implementing CI/CD workflows.

**Tipos:**
- **Declarativo**: Sintaxis más simple (recomendado)
- **Scriptado**: Más flexible, Groovy puro

```groovy
pipeline {
    agent any
    stages {
        stage('Build') { steps { /* ... */ } }
        stage('Test') { steps { /* ... */ } }
    }
}
```

### 2. Stages= Fases principales en el pipeline (Build, Test, Deploy).

```groovy
stages {
    stage('Setup') {
        steps { echo 'Setting up...' }
    }
    stage('Test') {
        steps { sh 'pytest tests/ -v' }
    }
}
```

### 3. Steps= Pasos o acciones (contienen tareas que se ejecutan por comandos)
Las `tasks` significa acciones que se ejecutan dentro de los pasos del pipeline, por comandos, dichos comandos se ejecutan en el **agente** que es una **instancia virtual** de una computadora virtualizada, por ende los comandos se ejecutan dentro de la terminal o consola de este agente, por ejemplo: `sh`, `bat`, `echo`, `script`, `git`

### 4. Agents= Agentes (donde se ejecuta el pipeline)
- `agent any`: Ejecuta el pipeline en cualquier agente disponible
- `agent { label 'linux' }`: Ejecuta el pipeline en un agente con el label 'linux'
- `agent { docker 'python:3.10' }`: Ejecuta el pipeline en un contenedor de docker con la imagen 'python:3.10'

### 5. Environment Variables= Variables de entorno

```groovy
environment {
    PYTHON_VERSION = '3.10'
    API_KEY = credentials('api-key-id')  // Secure
}
```

### 6. Post Actions= Acciones después de la ejecución del pipeline

```groovy
post {
    always { publishHTML(/* reports */) }
    failure { mail to: 'team@example.com' }
}
```

### 7. Parallel Execution= Ejecución paralela
```groovy
parallel {
    stage('API Tests') { steps { /* ... */ } }
    stage('UI Tests') { steps { /* ... */ } }
}
```

### 8. Triggers= Disparadores, puede ser programados por periodos o por eventos como un push de código

```groovy
triggers {
    cron('H 2 * * *')  // Daily at 2 AM
    pollSCM('H/15 * * * *')  // Check repo every 15 min
}
```

---

## `Groovy` Sintaxis Básica del Lenguaje

Jenkins Pipelines utiliza **Groovy** (JVM-based dynamic language), esto no es el núcleo principal de este contenido educativo, pero es importante comprender cómo está estructurado un pipeline desde la secuencia logica devclarativa que utiliza.

### Sintaxis Básica:
```groovy
// Variables
def myVar = "Hello"
String typed = "World"

// Interpolación de cadenas (string)
println "Hello, ${name}!"

// Condiciones
if (env.BRANCH_NAME == 'main') {
    echo 'Main branch'
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

### En el Jenkinsfile:
```groovy
stage('Dynamic Tests') {
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

**Groovy Docs**: https://groovy-lang.org/documentation.html

---

## Requisitos & Instalación

### Requisitos del Sistema
- **RAM**: 4 GB+ recomendado
- **Disco**: 50 GB+ (builds, artifacts)
- **Java**: JDK 11 or 17 (requerido)
- **CPU**: 2+ cores

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

# Install & start Jenkins
sudo apt update
sudo apt install jenkins
sudo systemctl start jenkins
sudo systemctl enable jenkins
```

**Docker (Mas facil):**
```bash
docker run -d -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  --name jenkins jenkins/jenkins:lts
```

**Acceso a Jenkins**: http://localhost:8080

### Plugins Requeridos
1. Pipeline
2. Git
3. HTML Publisher
4. Allure
5. Credentials Binding
6. Email Extension

Install: `Manage Jenkins` → `Manage Plugins`

**Jenkins Plugins**: https://plugins.jenkins.io/

---

## Creación de Jobs en Jenkins

### Creación de un Job Nuevo
1. **Nuevo Item**: Click en "New Item" en el dashboard de Jenkins.
2. **Nombre del Job**: Ingresa un nombre para tu job.
3. **Tipo de Job**: Selecciona "Pipeline" como el tipo de job.
4. **Configurar Pipeline**: Configura el pipeline especificando el script del pipeline o el Jenkinsfile.

### Configuración del Pipeline
1. **Script del Pipeline**: Puedes especificar el script del pipeline directamente o apuntar a un Jenkinsfile en tu repositorio de código fuente.
2. **Jenkinsfile**: Un Jenkinsfile es un script de Groovy que define el pipeline.

### Ejemplo de Jenkinsfile
```groovy
pipeline {
    agent any
    stages {
        stage('Build') { steps { /* ... */ } }
        stage('Test') { steps { /* ... */ } }
    }
}
```

---


## Creación de Jobs en Jenkins

Esta sección explica **paso a paso**, los conceptos precisos de cómo crear un job de Jenkins para ejecutar tu pipeline de automatización de pruebas.

El job es el algoritmo que será ejecutado por el servidor de Jenkins, este algoritmo está definido en el `Jenkinsfile`.

La estrategia recomendada es usar el tipo de job "Pipeline", esto es porque es el más flexible y es el recomendado por el equipo de Jenkins.

Esta es la estructura de los jobs usados en este framework:


```
ci-cd/
├── jenkins_smoke/          ← Smoke tests 
│   └── jenkinsfile
├── jenkins_api/            ← API tests only
│   └── jenkinsfile
├── jenkins_ui/             ← UI tests only
│   └── jenkinsfile
├── jenkins_stagin/         ← Combined staging tests
│   └── jenkinsfile
├── jenkins_regression/     ← Full regression
│   └── jenkinsfile

```  

### Tipos de Jobs en Jenkins 

Antes de crear un job, entender los tipos de jobs disponibles:

| Tipo de Job | Descripción | Caso de Uso |
|----------|-------------|----------|
| **Freestyle Project** | Simple, Basado en configuración de UI | Tareas Basicas, no complejas |
| **Pipeline** | Basado en código, utiliza un Jenkinsfile | **Recomendado para automatización** |
| **Multibranch Pipeline** | Crea pipelines para cada rama |**Multiples ramas (dev, staging, main)** | 
| **Folder** | Organiza jobs | Agrupa jobs relacionados |

**Recomendado para este framework, usar "Pipeline" o "Multibranch Pipeline".**

---

### Metodo 1: Pipeline Job (Single Branch)

#### Paso 1: Crear un nuevo job

1. **Acceso al Dashboard de Jenkins**
   - Abrir navegador: `http://localhost:8080`
   - Login with your admin credentials

2. **Click "New Item"**
   - On the left sidebar, click **"New Item"**

3. **Configure Job Name**
   - Enter a descriptive name: `QA-Automation-API-Tests`
   - Select **"Pipeline"**
   - Click **"OK"**

#### Paso 2: Configure General Settings

1. **Descripción** (Opcional pero recomendado)
   ```
   API Test Automation Pipeline
   Runs API tests using pytest against JSONPlaceholder API
   ```

2. **Discard Old Builds** (Recomendado)
   - Check "Discard old builds"
   - Days to keep builds: `30`
   - Max # of builds to keep: `20`

3. **GitHub Project** (Si se está usando GitHub)
   - Check "GitHub project"
   - Project url: `https://github.com/your-username/C-QA-Automation-Framework`

#### Paso 3: Disparadores (Opcional)

Decide como el pipeline debe iniciar:

**Opción A: Poll SCM** (Chequea por cambios periodicamente)
```
H/15 * * * *  # Cada 15 minutos
```

**Opción B: GitHub Webhook** (Dispara el pipeline al hacer push)
- Requiere configuración de webhook de GitHub
- Chequear "GitHub hook trigger for GITScm polling"

**Opción C: Build Periodicamente** (Programado)
```
H 2 * * *     # Diario a las 2 AM
H 2 * * 1-5   # Semanalmente a las 2 AM
```

**Opción D: Solo Manual**
- No chequear ningún disparador (ejecutar manualmente)

#### Paso 4: Configuración del Pipeline

**Existen dos formas de definir el pipeline:**

##### Opción A: Pipeline Script from SCM (Recomendado)

Este lee el Jenkinsfile directamente de tu repositorio Git.

1. **Definición**: Seleccionar **"Pipeline script de SCM"**

2. **SCM**: Seleccionar **"Git"**

3. **URL del repositorio**: Introduce la URL delrepositorio
   ```
   https://github.com/your-username/C-QA-Automation-Framework.git
   ```
   
4. **Credenciales**: 
   - Si es un repositorio publico: Seleccionar "none"
   - Si es un repositorio privado: Click "Add" → Add GitHub credentials

5. **Especificar la rama**: 
   ```
   */main
   ```
   O usar `*/develop` para la rama de desarrollo

6. **Script Path**: Path al Jenkinsfile en tu repositorio
   ```
   ci-cd/jenkins_stagin/jenkinsfile
   ```
   
7. **Click "Save"**

##### Opción B: Pipeline Script (Directo)

Escribe o pega el contenido del Jenkinsfile directamente en Jenkins.

1. **Definición**: Seleccionar **"Pipeline script"**

2. **Script**: Pega el contenido del Jenkinsfile
   ```groovy
   pipeline {
       agent any
       
       environment {
           PY_VER = "3.10"
       }
       
       stages {
           stage('Setup') {
               steps {
                   echo 'Setting up environment...'
                   sh "python${PY_VER} -m venv venv"
                   sh ". venv/bin/activate && pip install -r requiriments.txt"
               }
           }
           
           stage('Run API Tests') {
               steps {
                   echo 'Running API tests...'
                   sh ". venv/bin/activate && pytest tests/api_test/ -v"
               }
           }
       }
   }
   ```

3. **Click "Save"**

#### Paso 5: Ejecutar el Pipeline

1. **Click "Build Now"** on the job page
2. **Ver Progreso de la Construcción**: Click en el número de build (e.g., #1)
3. **Ver Salida de la Consola**: Click "Console Output" para ver los logs
4. **Ver Vista de Etapas**: Ver el estado de cada etapa visualmente

#### Paso 6: Ver Resultados

Después de que se complete la construcción:
- 🔵**Blue ball**: Éxito
- 🔴**Red ball**: Fallo
- ⚪**Gray ball**: Abortado
- 🟡**Yellow ball**: Instable (tests fallidos)

**Acceso a los Reportes:**
- Click en el número de build → **"Test Report"** or **"HTML Reports"**

---

### Método 2: Multibranch Pipeline (Multiple Branches)

Utiliza este método cuando tienes múltiples ramas (main, develop, feature branches).

#### Paso 1: Crear Multibranch Pipeline

1. **New Item** → Introduce el nombre: `QA-Automation-Framework`
2. Selecciona **"Multibranch Pipeline"**
3. Click **"OK"**

#### Paso 2: Configure Branch Sources

1. **Agregar fuente** → Selecciona **"Git"**

2. **Repositorio**: Introduce la URL de tu repositorio
   ```
   https://github.com/your-username/C-QA-Automation-Framework.git
   ```

3. **Credenciales**: Agrega si es necesario (para repositorios privados)

4. **Behaviors**: 
   - Descubrir ramas
   - Descubrir tags (opcional)

#### Paso 3: Configuración del Build

1. **Mode**: Selecciona **"by Jenkinsfile"**

2. **Script Path**: La ruta al Jenkinsfile
   ```
   ci-cd/jenkins_stagin/jenkinsfile
   ```

#### Paso 4: Scan Disparadores Multibranch Pipeline 

1. **Periodicamente si no se ejecuta de otra manera**
   ```
   1 hour
   ```
   Jenkins escanea por nuevas ramas cada hora

2. **Click "Save"**

Jenkins escanea automáticamente:
- Escanea el repositorio por nuevas ramas
- Crea un pipeline para cada rama con un Jenkinsfile
- Ejecuta pipelines cuando las ramas se actualizan

---

### Ejemplo de Configuración Rápida (API Tests)

Es un ejemplo completo para configurar pruebas de API:

**Job Name**: `API-Tests-Pipeline`

**Pipeline Script from SCM**:
- **SCM**: Git
- **Repository URL**: Introduce la URL de tu repositorio
- **Branch**: `*/main`
- **Script Path**: `ci-cd/jenkins_stagin/jenkinsfile`

**Build Triggers**:
- Poll SCM: `H/15 * * * *`

**Click "Save"** → **"Build Now"**

**Jenkins ejecutará:**
1. Clonar el repositorio
2. Leer el Jenkinsfile en `ci-cd/jenkins_stagin/jenkinsfile`
3. Ejecutar las etapas del pipeline
4. Publicar los reportes de los tests

---

### Solución de problemas (Troubleshooting)

#### Issue: "Negación de permisos" al ejecutar comandos shell
**Solución**: 
- Asegúrate de que el usuario de Jenkins tenga permisos adecuados
- Verifica que Python esté instalado: `which python3`

#### Issue: "`pip`: comando no encontrado"
**Solución**:
```bash
sudo apt install python3-pip
```

#### Issue: "Repositorio no encontrado"
**Solución**:
- Verifica que la URL del repositorio es correcta
- Agrega credenciales para repositorios privados

#### Issue: "Jenkinsfile no encontrado"
**Solución**:
- Verifica que la ruta al Jenkinsfile coincida con la ubicación real del archivo
- Usa el caso correcto: `jenkinsfile` vs `Jenkinsfile`
- Path es relativo a la raíz del repositorio: `ci-cd/jenkins_stagin/jenkinsfile`

#### Issue: "Los tests fallan pero el pipeline se ejecuta correctamente"
**Solución**:
- Remueve `|| true` de los comandos de pytest en el Jenkinsfile
- Esto permite que el pipeline falle cuando los tests fallan


---


---

## Ejemplos de Pipeline

### Ejemplo 1: Pipeline de Pruebas de API Completo
Ver ejemplo completo: `ci/cd/jenkins_api/jenkinsfile`

### Ejemplo 2: Pipeline de Pruebas UI Completo
Ver ejemplo completo: `ci/cd/jenkins_ui/jenkinsfile`

### Ejemplo 3: Pipeline de Pruebas de Staging Completo
Ver ejemplo completo: `ci/cd/jenkins_staging/jenkinsfile`

---

## 🔐 Gestión de Credenciales

### Agregar Credenciales:
1. `Manage Jenkins` → `Manage Credentials`
2. Selecciona domain → "Add Credentials"
3. Elige el tipo (Secret text, Username/Password, etc.)
4. Asigna ID

### Uso en Pipeline:
```groovy
environment {
    API_KEY = credentials('api-key-id')  // Secret text
    DB_CREDS = credentials('db-creds')   // Username:password
}

steps {
    // Automatically masked in logs
    sh 'curl -H "Authorization: Bearer ${API_KEY}" https://api.example.com'
    
    // Access separately
    sh 'echo "User: ${DB_CREDS_USR}"'
    sh 'echo "Pass: ${DB_CREDS_PSW}"'  // Hidden
}
```

**Mejores prácticas:**
- Nunca `hardcode` secrets  
- Use IDs descriptivos  
- Rotar credenciales regularmente  
- Limitar el alcance cuando sea posible  

---

## ⚠️ Consumo de Recursos & Implicaciones

### Memoria (RAM):
- **Jenkins Master**: 2-4 GB minimo
- **Por Build**: 500 MB - 2 GB
- **Agents**: 2-8 GB cada uno

**Aumento de heap:**
`heap size` significa tamaño de la pila de memoria, es decir, la cantidad de memoria que se le asigna a la JVM (Java Virtual Machine) para ejecutar el pipeline.

```bash
JAVA_OPTS="-Xmx4096m -Xms1024m"
```

### CPU:
- **Master**: 2+ cores
- **Selenium Tests**: CPU-intensive
- **Parallel Builds**: Multiplicar el uso de CPU

### Espacio en Disco:
- **Jenkins Home**: 10-50 GB
- **Workspaces**: 1-10 GB por job
- **Artifacts**: Reportes y logs acumulados

**Gestion de builds:**
```groovy
options {
    buildDiscarder(logRotator(
        numToKeepStr: '30',
        artifactNumToKeepStr: '10'
    ))
}
```

### Tiempo de ejecución:
- **API Tests**: 2-10 minutos
- **UI Tests**: 10-60 minutos
- **Regression**: 1-4 horas

**Optimización**: Ejecución paralela, caching, tests de humo primero

### Costos:
- **Self-hosted**: Hardware + mantenimiento
- **Cloud** (AWS/Azure): ~$30+/mes por instancia

---
---

## 📚 Recursos Oficiales

### Jenkins:
- **Website**: https://www.jenkins.io/
- **Documentation**: https://www.jenkins.io/doc/
- **Pipeline Syntax**: https://www.jenkins.io/doc/book/pipeline/syntax/
- **Plugins**: https://plugins.jenkins.io/
- **Tutorials**: https://www.jenkins.io/doc/tutorials/

### Groovy:
- **Website**: https://groovy-lang.org/
- **Documentation**: https://groovy-lang.org/documentation.html

### Community:
- **Stack Overflow**: https://stackoverflow.com/questions/tagged/jenkins
- **GitHub**: https://github.com/jenkinsci/jenkins

---

**Version**: 0.1.2  
**Author**: C-QA Automation Framework Team