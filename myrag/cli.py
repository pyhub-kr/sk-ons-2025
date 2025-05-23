import os

from pyhub.llm.types import Message

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from pyhub.llm import OpenAILLM, UpstageLLM, GoogleLLM, AnthropicLLM
from chat.models import VectorDocument

# def received_chat_message(request):
llm = OpenAILLM(
    model="gpt-4o",
    initial_messages=[
        Message(role="user", content="My name is chinseok."),
        # Message(role="", content=""),
    ],
)
# llm = UpstageLLM(model="solar-pro2-preview")  # UPSTAGE_API_KEY
# llm = GoogleLLM()
# llm = AnthropicLLM()

while True:
    humun_message = input("[Human] ").strip()
    if not humun_message:
        break

    # 분기: RAG 필요한지 여부?
    is_rag = humun_message.startswith("!")
    if is_rag:
        docs = VectorDocument.objects.similarity_search(humun_message)
        humun_message = f"<context>{str(docs)}</context>\n\nHuman: {humun_message}"

    # ai_message = llm.ask(humun_message)
    # print("[AI]", ai_message)

    print("[AI] ", end="")
    ai_message = ''
    for chunk in llm.ask(humun_message, stream=True):
        print(chunk, end="", flush=True)
        ai_message += chunk.text  # Reply 타입 (.text, .usage)
    print()

    # Chat.objects.bulk_create([
    #     Chat(role=Chat.Roles.user, content=humun_message),
    #     Chat(role=Chat.Roles.assistant, content=ai_message),
    # ])
