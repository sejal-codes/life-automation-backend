# Life Automation Project

A simple full-stack task automation project built with **FastAPI** (backend) and **plain HTML/JS** (frontend), deployed on **Google Cloud Run** and **Firebase Hosting**.

---

## **Project Overview**

- Add tasks to a list
- Generate AI-style task plans for a given task
- Frontend interacts with backend via REST API

---

## **Backend**

- Built with **FastAPI**
- Endpoints:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/tasks` | GET | Get all tasks |
| `/tasks` | POST | Add a new task (`{"name": "task name"}`) |
| `/generate_task` | POST | Generate step-by-step plan (`{"name": "task name"}`) |
| `/status` | GET | Check backend status |

- Live URL: [Backend on Cloud Run](https://life-automation-api-116300109834.asia-south1.run.app)

---

## **Frontend**

- Plain **HTML, CSS, JS**
- Connects to backend API
- Live URL: [Frontend on Firebase](https://life-automation-frontend-f272b.web.app)

---

## **Local Setup**

1. **Backend**:

```bash
cd life-automation-backend
pip install -r requirements.txt
uvicorn main:app --reload
