
# MMT Copilot

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/mmt-copilot.git
cd mmt-copilot
```

2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the API Gateway
```bash
uvicorn api-gateway.main:main_app --reload
Visit: http://localhost:8000
```


How to Contribute
1. Create a new branch
```bash
git checkout -b feature/your-feature-name
2. Make your changes
Ensure you're working in the appropriate module inside packages/.
```

3. Commit and push
```bash
git add .
git commit -m "Add [feature name] in [module]"
git push origin feature/your-feature-name
```
4. Open a Pull Request
Open a PR on GitHub and request review from the team.




## How to Run

```bash
uvicorn api-gateway.main:main_app --reload
```
