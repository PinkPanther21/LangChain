# 🚀 LangChain Experiments

A curated collection of hands-on experiments exploring **LangChain**, Hugging Face models, LLMs, and embeddings.  
This repository documents my journey to mastering modern AI pipelines: chat models, text generation, embeddings, and more.

---

## 🗺️ Overview

This project demonstrates:

- **LangChain** integrations with Hugging Face API
- **Chat model** examples
- **Embedding generation** experiments
- **Classic LLM** usage tests
- **Environment variable** setup
- **Python 3.13** compatibility

All scripts are small and focused — perfect for learning, debugging, or serving as templates for advanced pipelines.

---

## 📁 Project Structure

```
LangChain/
│
├── ChatModels/          # Chat-based LLM examples
├── EmbeddingModels/     # Embeddings via Hugging Face
├── LLMs/                # Simple LLM tests (non-chat)
│
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment variables
└── README.md            # This file
```

---

## ⚙️ Setup Instructions

**1️⃣ Clone the repository**
```bash
git clone https://github.com/PinkPanther21/LangChain.git
cd LangChain
```

**2️⃣ Create and activate a virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

**3️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```

**4️⃣ Set up environment variables**

- Copy `.env.example` to `.env`
- Add your Hugging Face API Key:
    ```
    HF_API_KEY=hf_xxxxxxxxxxxxxxxxxxxxx
    ```

**Each script is self-contained and demonstrates a specific AI concept.**

---

## 📝 Notes & Known Issues

- Some older LangChain classes are deprecated — newer versions under `langchain-huggingface` are used.
- Hugging Face models require accurate names (e.g. `sentence-transformers/all-MiniLM-L6-v2`).
- For some model types, use the HF Inference API or self-hosted TGI.
- Python 3.13 support confirmed.

---

## 📚 References

- [LangChain Documentation](https://python.langchain.com)
- [Hugging Face Inference API](https://huggingface.co/inference-api)

---
