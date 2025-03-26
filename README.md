# MMT Copilot

## Setup Instructions

### 1. Clone the repo

git clone https://github.com/YOUR_USERNAME/mmt-copilot.git
cd mmt-copilot

2. Create a virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the API Gateway
bash
Copy
Edit
uvicorn api-gateway.main:main_app --reload
Visit: http://localhost:8000

Team Responsibilities
Module	Owner(s)	Description
codegen/	Team A	Code generation using LLM
sql-gen/	Team B	Natural language to SQL generation
query-recommender/	Team C	Smart API/query suggestions
rag/	Team D	Vector DB + RAG implementation
pricing/	Team E	ML-based pricing/demand prediction
shared/utils/	All Teams	Shared utilities (logging, wrappers)
api-gateway/	All Teams	Mount and serve all modules
How to Contribute
1. Create a new branch
bash
Copy
Edit
git checkout -b feature/your-feature-name
2. Make your changes
Ensure you're working in the appropriate module inside packages/.

3. Commit and push
bash
Copy
Edit
git add .
git commit -m "Add [feature name] in [module]"
git push origin feature/your-feature-name
4. Open a Pull Request
Open a PR on GitHub and request review from the team.

mmt-copilot/
├── packages/                  # All feature modules
│   ├── codegen/              # Code generation (FastAPI service ready)
│   ├── sql-gen/              # SQL query generator
│   ├── query-recommender/    # Smart query suggestions
│   ├── rag/                  # Retrieval-Augmented Generation
│   └── pricing/              # Dynamic pricing & demand forecasting
├── shared/
│   └── utils/                # Common utility functions (logging, API wrappers)
├── api-gateway/              # Main FastAPI app to mount all modules
├── frontend/                 # Optional UI (if needed later)
├── .env.example              # Template for secrets
├── .gitignore                # Files/folders to ignore in Git
├── requirements.txt          # Python dependencies
└── README.md                 # You're here!


## How to Run

```bash
uvicorn api-gateway.main:main_app --reload
```
