📘 LangChain Experiments

A collection of hands-on experiments exploring LangChain, Hugging Face models, LLMs, and embeddings.
This repository documents my journey while learning how to work with modern AI pipelines such as chat models, text-generation models, and embedding models.

🚀 Overview

This project includes:
LangChain integrations with Hugging Face API
Chat model examples
Embedding generation experiments
Classic LLM usage tests
Environment variable setup
Python 3.13 compatible examples

All scripts are small, focused experiments — helpful for learning, debugging, and building more advanced pipelines later.

📁 Project Structure
LangChain/
│
├── ChatModels/          # Chat-based LLM examples
├── EmbeddingModels/     # Embeddings using HF models
├── LLMs/                # Simple LLM tests (non-chat)
│
├── requirements.txt     # Dependencies
├── .env.example         # Example environment variables
└── README.md            # This file

⚙️ Setup Instructions
1️⃣ Clone the repo
git clone https://github.com/PinkPanther21/LangChain.git
cd LangChain

2️⃣ Create virtual environment
python -m venv venv

Activate:
Windows → venv\Scripts\activate
Linux/macOS → source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure environment variables
Create a .env file based on .env.example:
HF_API_KEY=hf_xxxxxxxxxxxxxxxxxxxxx
Each script is self-contained and demonstrates a specific concept.

📌 Notes & Known Issues
Some older LangChain classes are deprecated — new versions under langchain-huggingface are used.
Hugging Face models require correct model naming (sentence-transformers/all-MiniLM-L6-v2 etc).
You must use HF Inference API or self-hosted TGI for certain model types.
Python 3.13 support confirmed.


📚 References
LangChain Docs — https://python.langchain.com
HuggingFace Inference API — https://huggingface.co/inference-api


