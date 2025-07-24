
from sentence_transformers import SentenceTransformer, util
import torch
astrologers = [
    {"name": "Astro A", "tags": "love marriage career"},
    {"name": "Astro B", "tags": "wealth money career"},
    {"name": "Astro C", "tags": "relationship love companionship"},
    {"name": "Astro D", "tags": "family health well-being"},
    {"name": "Astro E", "tags": "education learning growth"},
]

model = SentenceTransformer('all-MiniLM-L6-v2')
astro_embeddings = model.encode(
    [a['tags'] for a in astrologers],
    convert_to_tensor=True,
    show_progress_bar=False
)
def recommend(user_input: str, top_k: int = 3):
    """
    Given a user_input string, return top_k astrologers with their similarity scores.
    """
    query_emb = model.encode(user_input, convert_to_tensor=True)
    cos_scores = util.cos_sim(query_emb, astro_embeddings)[0]
    top_results = torch.topk(cos_scores, k=top_k)
    results = []
    for score, idx in zip(top_results.values, top_results.indices):
        results.append({
            "name": astrologers[idx]['name'],
            "score": float(score.cpu().item())
        })
    return results

if __name__ == "__main__":
    user_query = "I'm looking for guidance on my job."
    recs = recommend(user_query, top_k=3)

    print(f"User Query:\n  {user_query}\n")
    print("Top 3 Recommendations:")
    for rank, rec in enumerate(recs, start=1):
        print(f"  {rank}. {rec['name']} (score: {rec['score']:.4f})")
