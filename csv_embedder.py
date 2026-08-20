import pandas as pd
import numpy as np
from fastembed import TextEmbedding

df = pd.read_csv("internships.csv")

columns_to_extract = ["internship_title","sector_name","field_name","skills_set","detailed_description"]

df['combined_text'] = df[columns_to_extract].fillna('').astype(str).agg(''.join,axis=1)
documents = df["combined_text"].to_list()

model = TextEmbedding()

print("Generating embeddings...")
embeddings_list = list(model.embed(documents))


embeddings_matrix = np.array(embeddings_list)
np.save('documents_embedding.npy',embeddings_matrix)
print("DONE")