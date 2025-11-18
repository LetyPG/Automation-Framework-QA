# CI/CD Integration Guide - Jenkins & Test Automation

## 📚 Table of Contents
1. [What is CI/CD](#what-is-cicd)
2. [What is Jenkins](#what-is-jenkins)
3. [Jenkins Core Concepts](#jenkins-core-concepts)
4. [Groovy Language Basics](#groovy-language-basics)
5. [Requirements & Installation](#requirements--installation)
6. [Pipeline Examples](#pipeline-examples)
7. [Credentials Management](#credentials-management)
8. [Resource Consumption](#resource-consumption--implications)
9. [Alternative CI/CD Tools](#alternative-cicd-tools)
10. [Official Resources](#official-resources)

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

## Creating Jenkins Jobs

This section explains **step-by-step** how to create a Jenkins job to execute your test automation pipeline.

The jobs is the algorithm that will be executed by the Jenkins server, this algorithm is defined in the Jenkinsfile.


The recomended strategy is to use the "Pipeline" job type, this is because it is the most flexible and it is the one that is recommended by the Jenkins team.

This is the structure of the jobs used in this framework:

```
ci-cd/
├── jenkins_smoke/          ← Smoke tests (NEW!)
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

### Best Practices

1. **Use Pipeline from SCM**: Keep Jenkinsfile in repository
2. **Descriptive Names**: Use clear job names like `API-Tests-Staging`
3. **Organize with Folders**: Group related jobs
4. **Set Build Retention**: Don't keep builds forever
5. **Use Credentials Manager**: Never hardcode secrets
6. **Tag Builds**: Use build descriptions for important builds
7. **Monitor Disk Space**: Old builds consume space

---

### Next Steps

After creating your first job:

1. **Add Credentials**: For API keys, passwords
2. **Configure Notifications**: Email or Slack on failures
3. **Set up Webhooks**: Automatic triggers from Git
4. **Create More Pipelines**: UI tests, staging, production
5. **Explore Blue Ocean**: Modern UI for pipelines (`http://localhost:8080/blue`)

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