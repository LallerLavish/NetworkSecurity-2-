# ⚡ AlgoForge  

<p align="center">
  <!-- Build & Repo Stats -->
  <img src="https://badgen.net/github/status/LallerLavish/AlgoForge" />
  <img src="https://badgen.net/github/checks/LallerLavish/AlgoForge" />
  <img src="https://badgen.net/github/last-commit/LallerLavish/AlgoForge" />
  <img src="https://badgen.net/github/branches/LallerLavish/AlgoForge" />
  <img src="https://badgen.net/github/stars/LallerLavish/AlgoForge" />
  <img src="https://badgen.net/github/forks/LallerLavish/AlgoForge" />
  <img src="https://badgen.net/github/contributors/LallerLavish/AlgoForge" />
  <img src="https://badgen.net/github/issues/LallerLavish/AlgoForge" />

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
