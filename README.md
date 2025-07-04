# 🤖 AI Calendar Scheduler Agent ⏰📅

Bring productivity to the next level — just tell your AI assistant what’s on your plate, and it schedules everything into your Google Calendar with surgical precision. No more juggling time slots — your **LLM-powered Calendar Agent** does it for you.

---

## 🚀 What It Does

This project uses **CrewAI**, **LangChain**, **Google Calendar API**, and **Composio SDK** to:
- Accept your **natural language** to-do list (e.g., \`1PM-3PM -> Code\`)
- Understand and process your schedule with **Gemini/OpenAI**
- Create calendar events directly into **your Google Calendar**
- ⚙️ Fully agentic — works via LLM + tool-based actions

---

## 🎯 Example Use Case

\`\`\`bash
📝 To-Do:
1PM - 3PM -> Code,
5PM - 7PM -> Meeting,
9AM - 12AM -> Learn something,
8PM - 10PM -> Game

🤖 Output:
✅ Events added to Google Calendar titled "Code", "Meeting", etc. on today’s date.
\`\`\`

---

## 🧠 Tech Stack

| Tool        | Purpose                         |
|-------------|----------------------------------|
| 🧠 Gemini / OpenAI | Natural language understanding |
| 🛠️ LangChain       | Tool integration layer         |
| 🧰 CrewAI          | Agent + Task coordination     |
| 🔌 Composio        | Connects to Google Calendar   |
| 🕒 Google Calendar API | Calendar event creation   |
| 💻 Python         | Core logic and orchestration |

---

## 🔧 How to Run

1. **Clone the Repo**

```bash
git clone https://github.com/<your-username>/ai-calendar-agent.git
cd ai-calendar-agent
```

2. **Create \`.env\` file**

```
GOOGLE_API_KEY=your-google-api-key
COMPOSIO_API_KEY=your-composio-key
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Agent**

```bash
python calendar_agent.py
```

---

## 🧪 What's Next?

- [ ] Web UI with Streamlit
- [ ] Voice-based scheduling input
- [ ] Deploy with daily auto-run
- [ ] Add support for recurring events

---

## 📘 Learn More

- [CrewAI](https://github.com/joaomdmoura/crewai)
- [Composio](https://docs.composio.dev/)
- [LangChain](https://docs.langchain.com/)

---

## 💡 Inspiration

> “Don’t manage your time. Train an AI to do it.”

---

## 📬 Contact

Created by [Adarsh Kumar Singh](https://www.linkedin.com/in/adarsh-kumar-singh-data/) — feel free to reach out for questions or collaborations.