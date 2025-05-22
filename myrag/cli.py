import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from pyhub.llm import OpenAILLM
from chat.models import VectorDocument

# qs = Chat.objects.filter()

llm = OpenAILLM(
    initial_messages=[],
)

while True:
    humun_message = input("[Human] ").strip()
    if not humun_message:
        break

    # 분기: RAG 필요한지 여부?
    is_rag = humun_message.startswith("!")
    if is_rag:
        docs = VectorDocument.objects.similarity_search(humun_message)
        humun_message = f"<context>{str(docs)}</context>\n\nHuman: {humun_message}"
        print(humun_message)

    # ai_message = llm.ask(humun_message)
    # print("[AI]", ai_message)

    print("[AI] ", end="")
    ai_message = ''
    for chunk in llm.ask(humun_message, stream=True):
        print(chunk, end="", flush=True)
        ai_message += chunk
    print()

    # Chat.objects.bulk_create([
    #     Chat(role=Chat.Roles.user, content=humun_message),
    #     Chat(role=Chat.Roles.assistant, content=ai_message),
    # ])
