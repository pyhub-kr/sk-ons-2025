from uuid import uuid4

from django.conf import settings
from django.db import models
from pgvector.django import VectorField
from pyhub.rag.models.postgres import PGVectorDocument


# class Room(models.Model):
#     owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     uuid = models.UUIDField(default=uuid4)
#
#
# class Chat(models.Model):
#     class Roles(models.TextChoices):
#         user = "user"
#         assistant = "assistant"
#
#     # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     # room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     role = models.CharField(max_length=20, choices=Roles.choices)
#     content = models.TextField()


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
