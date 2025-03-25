import os

folders = [
    "packages/codegen",
    "packages/sql-gen",
    "packages/query-recommender",
    "packages/rag",
    "packages/pricing",
    "shared/utils",
    "api-gateway",
    "frontend"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    gitkeep_path = os.path.join(folder, ".gitkeep")
    with open(gitkeep_path, "w") as f:
        f.write("")
    print(f"✅ Created {gitkeep_path}")
