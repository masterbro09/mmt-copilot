# MMT Copilot

An AI developer copilot for MakeMyTrip APIs.

This repo contains the AI Developer Copilot for MakeMyTrip APIs. It provides modules for:

Code generation & debugging

SQL generation for travel data

Smart query recommendations

RAG-based dynamic suggestions

AI-powered pricing/demand forecasting

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
