from django.db import models
from pgvector.django import VectorField
from pyhub.rag.models.postgres import PGVectorDocument


class Document(models.Model):
    page_content = models.TextField()
    metadata = models.JSONField(default=dict)
    embeddings = VectorField(dimensions=3)


# 1536차원 embedding 필드
class VectorDocument(PGVectorDocument):
    class Meta:
        ordering = ["pk"]
        indexes = [
            PGVectorDocument.make_hnsw_index(
                "chat_vectordoc_idx",  # 데이터베이스에서 유일한 이름
                # "vector",  # field type
                # "cosine",  # distance metric
            ),
        ]
