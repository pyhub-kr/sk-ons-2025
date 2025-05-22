from django.db import models
from pgvector.django import VectorField
# from pyhub.rag.models.postgres import PGVectorDocument


class Document(models.Model):
    page_content = models.TextField()
    metadata = models.JSONField(default=dict)
    embeddings = VectorField(dimensions=3)
