# pip install kagglehub

import kagglehub

# Download latest version
path = kagglehub.dataset_download("ahmeduzaki/nobel-prize-winners-dataset-1901-2025")

print("Path to dataset files:", path)