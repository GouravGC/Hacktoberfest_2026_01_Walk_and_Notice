# 🌿 Walk & Notice

> **AI should help you leave the screen — not keep you on it.**

Walk & Notice is an AI-powered outdoor observation mission generator built for **Hacktoberfest 2026 — Week 1: Touch Grass**.

Instead of using AI to create another experience that keeps people glued to their screens, Walk & Notice uses AI for a few seconds to create a personalized outdoor mission — and then explicitly tells you to **put your phone away**.

The goal is simple:

**Generate → Read → Go Outside → Notice the World.**

---

## 🌱 Live Demo

🚀 **Try Walk & Notice:**
https://walk-and-notice.streamlit.app

💻 **Source Code:**
https://github.com/GouravGC/Hacktoberfest_2026_01_Walk_and_Notice

---

## 🎯 Hacktoberfest 2026 — Touch Grass

This project was created for **Hacktoberfest 2026 Week 1**, based on the **Touch Grass** challenge.

The challenge asks developers to explore how open-source AI can encourage people to spend more time in the real world rather than increasing their screen time.

Walk & Notice takes that idea literally.

The AI is not the destination.

**The outside world is.**

---

## 💡 The Problem

AI applications are increasingly designed to maximize screen interaction.

We use AI to:

* Generate content
* Answer questions
* Summarize information
* Create images
* Write code
* Automate tasks
* Keep us engaged online

But what if AI did the opposite?

What if an AI application intentionally encouraged you to **stop using the application**?

That is the idea behind Walk & Notice.

---

## 🌿 The Solution

Walk & Notice generates a short, personalized outdoor observation mission based on four simple preferences:

### ⏱️ Duration

Choose how much time you have:

* 15 minutes
* 30 minutes

### 🌳 Environment

Choose where you are going:

* Urban park
* Garden
* Street
* Neighborhood
* Open outdoor area

### 🔎 Interest

Choose what you want to notice:

* Birds
* Trees
* Sounds
* Nature
* People and surroundings
* Anything interesting

### ⚡ Energy Level

Choose how you are feeling:

* Low
* Medium
* High

The AI then creates one concise outdoor mission.

And finally:

> **Now put your phone away.**

---

## 🧠 How It Works

```text
┌───────────────────────┐
│     User Preferences  │
│                       │
│ Duration              │
│ Environment           │
│ Interest              │
│ Energy                │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│   Streamlit Interface │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│   Prompt Construction │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Open-Weight AI Model  │
│   GPT-OSS-20B         │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Outdoor Mission       │
│                       │
│ 1. Observe...         │
│ 2. Walk...            │
│ 3. Notice...          │
│ 4. Reflect...         │
└───────────┬───────────┘
            │
            ▼
      📱 PUT PHONE AWAY
            │
            ▼
       🌳 REAL WORLD
```

The screen is intentionally the **shortest part of the experience**.

---

## 🤖 AI Technology

Walk & Notice uses the open-weight **GPT-OSS-20B** model through **OpenRouter**.

The model is instructed to generate:

* Exactly four steps
* Short, actionable instructions
* Missions matching the selected preferences
* Safe outdoor activities
* No requirement for a camera, phone, or recording

The application only displays the generated mission.

It does **not** expose model reasoning or internal reasoning traces to the user.

---

## 🛡️ Safety by Design

Outdoor activities should remain simple and safe.

The AI is explicitly instructed to:

* Stay on public paths
* Avoid approaching wildlife
* Avoid traffic and unsafe areas
* Avoid climbing
* Avoid touching dangerous objects
* Require no special equipment
* Require no phone, camera, or recording

The application is designed around **observation**, not risky exploration.

---

## ✨ Example

A user might select:

```text
Duration: 15 minutes
Environment: Urban park
Interest: Birds
Energy: Low
```

The generated mission could look like:

```text
1. Walk to the park's shaded pond.
2. Sit on the bench beside the pond.
3. Observe sparrows and finches for 10 minutes.
4. Note any bird songs in your mind.

Now put your phone away.
```

The application has done its job.

Now the user leaves the screen.

---

## 🏗️ Project Structure

```text
Hacktoberfest_2026_01_Walk_and_Notice/
│
├── app.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
├── README.md
│
├── src/
│   ├── __init__.py
│   ├── generator.py
│   └── prompts.py
│
└── notebooks/
    └── Hacktoberfest_2026_01_Walk_and_Notice.ipynb
```

### Main Components

**`app.py`**

The Streamlit application and user interface.

**`src/generator.py`**

Handles communication with the OpenRouter API and generates outdoor missions.

**`src/prompts.py`**

Contains the system prompt and safety constraints used to guide mission generation.

**`notebooks/`**

Contains the original development and experimentation notebook.
