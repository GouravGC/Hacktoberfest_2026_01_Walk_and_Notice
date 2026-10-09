# 📋 Walk & Notice — Evidence

This folder contains supporting evidence for **Walk & Notice**, submitted for **Hacktoberfest 2026 — Week 1: Touch Grass**.

The evidence demonstrates the project's working application, open-weight AI implementation, local inference, production deployment, CI/CD automation, containerization, GitHub Copilot usage, and real-world outdoor testing.

---

## 🎥 Demo Video

A complete demonstration of Walk & Notice has been recorded.

The video demonstrates the application flow, AI generation, deployment, development workflow, and the project's intended **Touch Grass** experience.

**Demo video:**
*Add the final video link here.*

---

# 📸 Evidence Index

| #  | Evidence                       | What It Demonstrates                                |
| -- | ------------------------------ | --------------------------------------------------- |
| 01 | `01-render-production.png`     | Live production application on Render               |
| 02 | `02-openrouter-generation.png` | Production AI generation through OpenRouter         |
| 03 | `03-gemma-ollama-local.png`    | Local Gemma 4 E4B inference through Ollama          |
| 04 | `04-github-actions.png`        | Successful automated CI/CD workflow                 |
| 05 | `05-ghcr.png`                  | Docker image published to GitHub Container Registry |
| 06 | `06-github-copilot.png`        | GitHub Copilot usage during development             |
| 07 | `07-repository.png`            | Open-source project structure and implementation    |
| 08 | `08-render-deployment.png`     | Production deployment configuration                 |
| 09 | `09-outdoor-test.png`          | Real-world outdoor testing                          |
| 10 | `10-mission-result.png`        | Generated outdoor observation mission               |

---

# 01 — Production Application

**File:** `screenshots/01-render-production.png`

This screenshot demonstrates that Walk & Notice is deployed as a working production application on Render.

### Production URL

https://walk-and-notice-latest.onrender.com/

The production application uses OpenRouter for AI generation.

---

# 02 — OpenRouter Generation

**File:** `screenshots/02-openrouter-generation.png`

This screenshot demonstrates a successful production AI generation request.

The deployed application uses:

```text
OpenRouter
    ↓
GPT-OSS-20B
    ↓
Outdoor Observation Mission
```

The API key is stored securely as an environment variable and is not exposed in the repository.

---

# 03 — Local Gemma + Ollama

**File:** `screenshots/03-gemma-ollama-local.png`

This screenshot demonstrates the local AI path.

```text
Gemma 4 E4B
     ↓
Ollama
     ↓
Python Application
     ↓
Walk & Notice
```

This demonstrates that the application can use an open-weight model locally rather than relying exclusively on a hosted API.

---

# 04 — GitHub Actions CI/CD

**File:** `screenshots/04-github-actions.png`

This screenshot demonstrates the successful GitHub Actions workflow.

The workflow:

1. Checks out the repository.
2. Sets up Python.
3. Installs dependencies.
4. Runs pytest.
5. Builds the Docker image.
6. Publishes the image to GHCR.

### Workflow

https://github.com/GouravGC/Hacktoberfest_2026_01_Walk_and_Notice/actions/runs/37967290589

The successful workflow is particularly relevant to the Hacktoberfest GitHub Copilot partner category because the challenge explicitly permits projects that **automate the project with GitHub Actions**.

---

# 05 — GitHub Container Registry

**File:** `screenshots/05-ghcr.png`

This screenshot demonstrates that the CI/CD workflow successfully publishes the application Docker image to GitHub Container Registry.

Production image:

```text
ghcr.io/gouravgc/walk-and-notice:latest
```

The container image is subsequently used for the production deployment.

---

# 06 — GitHub Copilot

**File:** `screenshots/06-github-copilot.png`

This screenshot provides evidence of GitHub Copilot being available and used during project development.

Copilot was used as an engineering assistance tool during development.

The project does **not** claim that Copilot is part of the runtime AI architecture.

The runtime AI system is based on Gemma/Ollama locally and GPT-OSS-20B through OpenRouter in production.

---

# 07 — Repository Structure

**File:** `screenshots/07-repository.png`

This screenshot demonstrates the project's open-source repository and implementation structure.

Repository:

https://github.com/GouravGC/Hacktoberfest_2026_01_Walk_and_Notice

Important project components include:

```text
app.py
src/
tests/
Dockerfile
.github/workflows/
requirements.txt
README.md
```

---

# 08 — Render Deployment

**File:** `screenshots/08-render-deployment.png`

This screenshot demonstrates the production deployment configuration on Render.

The production service runs the Docker image published to GHCR.

Production architecture:

```text
GitHub
   ↓
GitHub Actions
   ↓
Docker Build
   ↓
GHCR
   ↓
Render
   ↓
OpenRouter
   ↓
GPT-OSS-20B
```

Production application:

https://walk-and-notice-latest.onrender.com/

---

# 09 — Outdoor Test

**File:** `screenshots/09-outdoor-test.png`

This is the real-world evidence for the **Touch Grass** concept.

The generated mission is taken outside and performed in the real environment.

The purpose is to demonstrate that Walk & Notice is not designed to maximize screen time.

Its intended flow is:

```text
Generate
   ↓
Read
   ↓
Put phone away
   ↓
Go outside
   ↓
Observe
```

This evidence demonstrates the project's intended real-world use.

---

# 10 — Mission Result

**File:** `screenshots/10-mission-result.png`

This screenshot demonstrates the actual generated outdoor observation mission.

The mission follows the application's safety and formatting constraints and ends with:

> Now put your phone away.

The generated instruction is intended to be consumed quickly so that the user can return their attention to the physical environment.

---

# 🔗 Important Project Links

### GitHub Repository

https://github.com/GouravGC/Hacktoberfest_2026_01_Walk_and_Notice

### Streamlit Demo

https://walk-and-notice.streamlit.app

### Render Production

https://walk-and-notice-latest.onrender.com/

### GitHub Actions

https://github.com/GouravGC/Hacktoberfest_2026_01_Walk_and_Notice/actions/runs/37967290589

---

# 🏆 Evidence Summary

The evidence in this folder supports the following aspects of the project:

* ✅ Working public application
* ✅ Open-weight AI
* ✅ Local Gemma 4 E4B inference
* ✅ Ollama integration
* ✅ GPT-OSS-20B production inference
* ✅ OpenRouter integration
* ✅ Docker containerization
* ✅ GitHub Actions CI/CD
* ✅ Automated testing
* ✅ GHCR container publishing
* ✅ Render deployment
* ✅ GitHub Copilot development workflow
* ✅ Open-source GitHub repository
* ✅ Real-world outdoor testing
* ✅ Touch Grass challenge alignment

---

# 🌿 Final Principle

> **AI should help you leave the screen — not keep you on it.**

Walk & Notice generates the instruction.

The user takes it outside.

Then the phone goes away.
