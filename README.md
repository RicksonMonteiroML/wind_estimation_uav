# 🌬️ Wind Estimation for Multirotor UAVs using Physics-Aware Deep Learning

This repository contains a **research- and industry-grade framework** for **wind estimation in multirotor UAVs**, combining **physically consistent simulation**, **classical state estimation**, and **deep learning models** trained on **simulated ground-truth wind data**.

The project is designed as a **fully modular, reproducible pipeline**, covering the entire workflow:

> **Simulation → Dataset → Preprocessing → Training → Evaluation → Scientific Results**

---

## 🎯 Project Objectives

- Estimate **wind velocity acting on multirotor UAVs** using **onboard measurements only**
- Leverage **deep learning (LSTM)** for temporal modeling of wind dynamics
- Ensure **physical coherence** by explicitly modeling:
  - 6-DOF UAV dynamics (Newton–Euler)
  - Wind as **relative air velocity**
- Compare learning-based approaches against **physics-based estimators (EKF)**
- Provide a **reproducible and extensible research platform** suitable for scientific publications

---

## 🧱 Key Features

- ✅ **Physics-consistent UAV model** (6-DOF Newton–Euler)
- 🌪️ **Parametric wind models** (constant, stochastic, turbulent)
- 🛰️ **Realistic onboard sensor simulation** (IMU, state, control inputs)
- 📦 **Versioned dataset generation** with ground-truth wind
- 🧠 **Deep learning estimators** for temporal wind estimation (LSTM)
- 📐 **Extended Kalman Filter (EKF)** as a strong physics-based baseline
- 🔁 **Strict separation between simulation, physics, and learning**
- ♻️ **Fully reproducible experiments** (configs, seeds, logging)

---

## 🧠 Design Philosophy

This repository follows **clean architecture principles** and best practices from:

- **Robotics & aerial systems**
- **Machine Learning & MLOps**
- **Scientific computing**

Key design rules:
- Physics is **never hard-coded** inside neural networks
- Learning models are **agnostic to the simulator**
- Simulation, estimation, and evaluation are **loosely coupled**
- Every experiment is **config-driven and reproducible**

---

## 📁 Repository Structure (High-Level)

```text
wind_estimation_uav/
├── physics/        # UAV dynamics and aerodynamics
├── simulation/     # AirSim and custom simulators
├── sensors/        # Onboard sensor models
├── data/           # Dataset generation and preprocessing
├── estimation/     # EKF and learning-based estimators
├── training/       # Training pipelines and experiment control
├── evaluation/     # Metrics, plots, and statistical analysis
├── config/         # Versioned experiment configurations
└── experiments/    # Reproducible experiment entry points
```

---

## 📊 Scientific Scope

This framework is suitable for research in:
- Wind estimation and disturbance rejection
- Learning-based state estimation
- Hybrid physics–ML systems
- Simulation-to-real transfer
- UAV autonomy and robustness

The architecture is intentionally designed to support:
- Ablation studies
- Fair baseline comparisons
- Extension to different UAV platforms and estimators

---

## 🚀 Intended Audience

- Researchers in **aerial robotics and autonomy**
- Engineers working with **UAV state estimation**
- ML practitioners interested in **physics-aware learning**
- Graduate students developing **publishable research**

---

## 📌 Status

🚧 Active development  
📚 Research-oriented  
🧪 Simulation-first, real-world ready

---

## 🧠 Core Principle

> **Wind is treated as a latent physical state, not a learned shortcut.**

---

## 🔑 Ponto-chave

**The strict separation between physics, simulation, and learning is the foundation that makes this project scientifically defensible, reproducible, and extensible.**
