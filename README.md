# 📝 Ollama-Gemma-Summarizer

- This Python project leverages the capabilities of Ollama and Gemma to generate summaries of meetings or conversations between the members or people.

## 🚀 Pre-Requisites

Before you begin, ensure you have met the following requirements installed in your system:

- [Ollama](https://ollama.com/)
- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

## 🛠️ Installation and Setup

###  🔧 Setting up Ollama and Gemma on your system

- After installing Ollama make sure that Ollama is running in the background.
- Open up your terminal and run the following command to install the gemma:2b model on your local system : `ollama run gemma:2b`

### 🔄 Cloning and running the project

- Run the following command serially for cloning the project : 

```
$ git clone <forked_repo_url>
$ cd Ollama-Gemma-Generator
```

- To set up the Virtual environment and run the project : 

```
$ pip install virtualenv
$ py -m venv summarizer
$ pip install -r requirements.txt
$ source summarizzer/Scripts/activate
```

- After completeing all the above steps, run main.py to laund the project window.

## 📂 File Structure

```
Ollama-Gemma-Summarize/
|
├── assets/
│   ├── admin.js
│   └── users.js
│
├── src/
│   ├── Admin_routes.js
│   └── Users_routes.js     
│
├── README.md
├── requirements.txt
└── .gitignore
```