
# Vedaz LLM‑Powered Astrologer Recommendation Engine

A take‑home submission demonstrating:

1. A **Research Task** write‑up (1–2 pages) covering LLM choice, hosting/scale, cost estimate, and privacy/safety.  
2. A **Technical Task**: a mini recommendation engine (`task2.py`) that mocks astrologer profiles and returns the top 3 matches for a dummy user query using Sentence Transformers.  
3. A **Bonus Task**: a small “VedazAI” agent (`task3.py`) that builds a chat prompt and—optionally—invokes Together.ai to generate a life insight and two actionable tips from a palm‑reading.

---

## Repository Contents

```text
├── LLM reccomendation for astrologers.pdf      # 1–2 page write‑up for the non‑coding research questions
├── task2.py               # Recommendation engine script (Sentence‑Transformers)
├── task3.py               # AI Astrologer demo (Together.ai chat integration)
├── .env.local.example     # Template for environment variables
└── README.md              # This file
````

---

## Environment Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/RohanDobriyal/Vedaz.git
   cd Vedaz
   ```

2. **Create & activate a virtual environment**

   ```bash
   python -m venv .venv
   # macOS / Linux
   source .venv/bin/activate
   # Windows PowerShell
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install sentence-transformers torch python-dotenv requests
   ```

4. **Configure your Together.ai API key**

   * Copy the example file:

     ```bash
     cp .env.local.example .env.local
     ```
   * Open `.env.local` and add your key (no quotes):

     ```text
     TOGETHER_API_KEY=your_together_api_key_here
     ```
   * Make sure `.env.local` is **in your working directory** when you run `task3.py`.

---

## Research Task

Open **`research_task.md`** in your editor or convert it to PDF (e.g., Word/Google Docs → Export → PDF). It includes:

1. **LLM Stack Recommendation**
2. **Hosting & Scaling Architecture**
3. **Monthly Cost Estimate** (for 50 000 MAU)
4. **Privacy & Safety Considerations**

---

## Technical Task: Recommendation Engine

Run the mini recommendation engine with:

```bash
python task2.py
```

* **Mocks 5 astrologer records** (tags: love, career, money, etc.)
* **Embeds** both the dummy user query and each astrologer’s tags via `all‑MiniLM‑L6‑v2`
* **Computes cosine similarity** and prints the **top 3** astrologers with scores.

---

## Bonus Task: VedazAI Chat Agent

Run the AI‑astrologer demo with:

```bash
python task3.py
```

* **Loads** your `TOGETHER_API_KEY` from `.env.local`
* **Builds** a system+user message payload for a palm‑reading
* **Sends** one chat/completions request to Together.ai
* **Prints** the generated life insight & two tips

> **Tip:** If you’re low on credits, you can comment out the API call and simply print the prompt logic. The code handles 402 (Payment Required) responses gracefully.

---

---



Good luck, and thank you for reviewing this submission!
