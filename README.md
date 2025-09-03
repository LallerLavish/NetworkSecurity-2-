# AlgoForge  

<p align="center">

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker&logoColor=white)](https://www.docker.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![React](https://img.shields.io/badge/React-20232A?logo=react&logoColor=61DAFB)](https://react.dev/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-38B2AC?logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![C++](https://img.shields.io/badge/C++-00599C?logo=cplusplus&logoColor=white)](https://isocpp.org/)
[![Java](https://img.shields.io/badge/Java-007396?logo=java&logoColor=white)](https://www.java.com/)
[![OpenAI GPT-4](https://img.shields.io/badge/OpenAI-GPT--4-412991?logo=openai&logoColor=white)](https://openai.com/)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![AutoGen](https://img.shields.io/badge/AutoGen-Microsoft-0078D4?logo=microsoft&logoColor=white)](https://microsoft.github.io/autogen/)

</p>
  <!-- Tech Stack Icons -->
  <br/><br/>
  <img src="https://skillicons.dev/icons?i=react,typescript,tailwind,fastapi,python,cpp,java,firebase,docker,git" />

  <!-- AI Tools -->
  <br/><br/>
  <img src="https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/Gemini-4285F4?style=flat-square&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/AutoGen-0078D4?style=flat-square&logo=microsoft&logoColor=white" />
</p>  

---

AlgoForge is an end-to-end platform for **algorithm problem solving, AI-powered code generation, and solution analysis**.  
It combines a modern **React frontend** with a **FastAPI backend**, orchestrated by agentic AI for multi-language code generation, complexity analysis, and Firebase-based user management.  

 **[Watch Demo Video](https://your-demo-video-link.com)**  

---

##  Features  

-  **AI-powered code generation** (Python, Java, C++).  
-  **Multi-agent pipeline** for problem extraction, solution generation, and code fitting.  
-  **Automatic time/space complexity analysis** and solution explanation.  
-  **User authentication** via Firebase.  
-  **Problem history tracking** and solution review.  
-  **Modern, responsive UI** with dark mode support.  

---

##  Architecture  

- **Frontend:** React + TypeScript + Tailwind CSS (`frontend/`)  
- **Backend:** FastAPI + SQLAlchemy + Firebase Admin + Agentic AI (`backend/`)  
- **AI Pipeline:** Multi-agent orchestration for extraction, solution, and fitting (`backend/app/agentic_ai/`)  

---

##  Tech Stack  

<p align="center">
  <img src="https://skillicons.dev/icons?i=react,typescript,tailwind,fastapi,python,cpp,java,firebase,sqlite,docker,git" />
</p>  

---

##  Frontend  

- Built with [Create React App](https://github.com/facebook/create-react-app)  
- Styled using [Tailwind CSS](https://tailwindcss.com/) with custom scrollbars  
- Firebase authentication + storage  
- Key files:  
  - `src/App.tsx` → Main app and routing  
  - `src/pages/ProblemResult.tsx` → Solution display  
  - `src/services/api.ts` → API integration  

### Start Frontend  

```sh
cd frontend
npm install
npm start

