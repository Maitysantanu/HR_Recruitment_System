import re

SKILLS_DB = [
    "python", "java", "javascript", "typescript", "c", "c++", "c#", "r", "go", "rust",
    "kotlin", "swift", "scala", "perl", "ruby", "php", "bash", "shell scripting",
    "matlab", "julia",
    "machine learning", "deep learning", "nlp", "natural language processing",
    "computer vision", "data analysis", "data science", "statistical modeling",
    "feature engineering", "model deployment", "time series analysis",
    "reinforcement learning", "generative ai", "llm", "transfer learning",
    "anomaly detection", "recommendation systems", "a/b testing",
    "tensorflow", "pytorch", "keras", "scikit-learn", "xgboost", "lightgbm",
    "catboost", "hugging face", "spacy", "nltk", "opencv", "fastai",
    "mlflow", "optuna", "wandb",
    "pandas", "numpy", "scipy", "matplotlib", "seaborn", "plotly", "bokeh",
    "dask", "polars", "streamlit",
    "sql", "mysql", "postgresql", "sqlite", "mongodb", "redis", "cassandra",
    "dynamodb", "elasticsearch", "neo4j", "oracle", "ms sql server",
    "hbase", "influxdb", "snowflake", "bigquery",
    "spark", "hadoop", "kafka", "airflow", "dbt", "hive", "pig", "flink",
    "databricks", "nifi", "presto", "trino", "etl", "data pipelines",
    "data warehousing", "data modeling", "data governance",
    "aws", "azure", "gcp", "google cloud", "aws sagemaker", "azure ml",
    "aws lambda", "aws s3", "aws ec2", "aws redshift", "azure databricks",
    "google bigquery", "aws glue",
    "docker", "kubernetes", "jenkins", "git", "github", "gitlab", "ci/cd",
    "terraform", "ansible", "helm", "mlops", "model monitoring",
    "feature store", "kubeflow", "seldon",
    "flask", "django", "fastapi", "spring", "spring boot", "node.js",
    "express.js", "react", "angular", "vue.js", "next.js",
    "tableau", "power bi", "looker", "metabase", "grafana", "kibana",
    "excel", "google sheets", "qlik",
    "git", "github", "gitlab", "bitbucket", "jira", "confluence", "notion",
    "linux", "ubuntu", "centos", "windows server", "networking", "tcp/ip",
    "rest api", "graphql", "grpc", "microservices", "distributed systems",
    "data storytelling", "business intelligence", "communication",
    "problem solving", "agile", "scrum", "product analytics",
    "financial modeling", "risk analysis", "supply chain analytics",
    "healthcare analytics", "marketing analytics",
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text):
            found_skills.append(skill)

    return list(set(found_skills))
