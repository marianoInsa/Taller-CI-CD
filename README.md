# TALLER CI/CD

Este proyecto forma parte del Taller de Integración y Entrega Continua de la materia Ingeniería y Calidad de Software de la carrera Ingeniería en Sistemas de Información (UTN FRRe, 2025).

---

## 📌 Descripción

El objetivo principal de este taller es aplicar los conceptos de integración y entrega continua a través del desarrollo de una aplicación simple que funcione como:

- ✅ **Contador de Caracteres**: Cuenta letras y números en un texto, ignorando caracteres especiales.
- ✅ **Contador de Palabras**: Cuenta la cantidad de palabras con una longitud específica.

El proyecto abarca todos los aspectos de un pipeline moderno de CI/CD: control de versiones, testing, inspección de código, mecanismo de feedback y despliegue automatizado. Además, se incluyen pruebas de estrés como agregado.

---

## 🛠️ Tecnologías Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=for-the-badge&logo=fastapi)
![Pytest](https://img.shields.io/badge/-Pytest-0A9EDC?style=for-the-badge&logo=pytest)
![Docker](https://img.shields.io/badge/-Docker-2496ED?style=for-the-badge&logo=docker)
![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/Github%20Actions-282a2e?style=for-the-badge&logo=githubactions&logoColor=367cfe)
![Sonar](https://img.shields.io/badge/Sonarqube-5190cf?style=for-the-badge&logo=sonarqube&logoColor=white)
![Azure](https://img.shields.io/badge/microsoft%20azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white)
![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)

---

## 🧪 Testing e Inspección

- 🔹 Pruebas unitarias con `Pytest` y cobertura con `Coverage`.
- 🔹 Integración de análisis de código estático con `SonarQube`.
- 🔹 `GitHub Actions` para automatizar test.

```bash
# Ejecutar pruebas y generar reporte de cobertura
coverage run -m pytest
coverage xml
```

- SonarQube proporciona un conjunto de métricas que pueden ser muy útiles:

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=marianoInsa_Taller-CI-CD&metric=bugs)](https://sonarcloud.io/dashboard?id=marianoInsa_Taller-CI-CD)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=marianoInsa_Taller-CI-CD&metric=code_smells)](https://sonarcloud.io/dashboard?id=marianoInsa_Taller-CI-CD)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=marianoInsa_Taller-CI-CD&metric=coverage)](https://sonarcloud.io/dashboard?id=marianoInsa_Taller-CI-CD)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=marianoInsa_Taller-CI-CD&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=marianoInsa_Taller-CI-CD)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=marianoInsa_Taller-CI-CD&metric=ncloc)](https://sonarcloud.io/dashboard?id=marianoInsa_Taller-CI-CD)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=marianoInsa_Taller-CI-CD&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=marianoInsa_Taller-CI-CD)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=marianoInsa_Taller-CI-CD&metric=alert_status)](https://sonarcloud.io/dashboard?id=marianoInsa_Taller-CI-CD)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=marianoInsa_Taller-CI-CD&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=marianoInsa_Taller-CI-CD)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=marianoInsa_Taller-CI-CD&metric=security_rating)](https://sonarcloud.io/dashboard?id=marianoInsa_Taller-CI-CD)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=marianoInsa_Taller-CI-CD&metric=sqale_index)](https://sonarcloud.io/dashboard?id=marianoInsa_Taller-CI-CD)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=marianoInsa_Taller-CI-CD&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=marianoInsa_Taller-CI-CD)

---

## 🚀 Despliegue

- 🔸 El entorno de entrega utiliza **Azure App Services** con estrategia de despliegue **One Deploy**.
- 🔸 El código se despliega automáticamente desde GitHub tras pasar las pruebas.
- 🔸 [URL del despliegue](https://iyc-taller-ayajggbwd5f0d8gx.brazilsouth-01.azurewebsites.net/static/index.html)

```bash
# Construcción y ejecución local con Docker
docker compose build
docker compose up -d
```

---

## 🔧 Pruebas de Estrés

Se utilizó **Taurus** (via Docker) junto con **JMeter** para evaluar el rendimiento de la aplicación.

```bash
cd stress-tests
docker run -it --rm -v "${PWD}:/bzt-configs" blazemeter/taurus jmeter-test/jmeter.yml
```

---

## 🧩 Estructura del Repositorio

```
📦 raiz/
 ┣ 📁 .github/workflows/        # Pipelines de CI/CD
 ┣ 📁 app/                      # Código fuente FastAPI
 ┣ 📁 docs/                     # Documentación extendida
 ┣ 📁 static/                   # FrontEnd
 ┣ 📁 stress-tests/             # Pruebas de estrés (Taurus + JMeter)
 ┣ 📁 tests/                    # Pruebas unitarias
 ┣ 📄 .coverage                 # Configuración para los tests
 ┣ 📄 .dockerignore
 ┣ 📄 .gitignore
 ┣ 📄 Dockerfile
 ┣ 📄 README.md
 ┣ 📄 coverage.xml              # Resultados de los tests para SonarQube
 ┣ 📄 docker-compose.yml
 ┣ 📄 requirements.txt          # Dependencias utilizadas
 ┗ 📄 sonar-project.properties  # Configuración de SonarQube
```

---

## ✍️ Autor

- **Mariano Gastón Insaurralde**
- Estudiante de Ingeniería en Sistemas de Información
- Universidad Tecnológica Nacional - Facultad Regional Resistencia

---
