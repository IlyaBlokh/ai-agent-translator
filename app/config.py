from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
model = init_chat_model("gpt-4o-mini", model_provider="openai")
system_template = "Translate the following text from English into {language}. This is a translation for a mobile game. Keep all line breaks as in the english text. Don't translate digits, words TON, KAIA, USDT and all words inside the arrow brackets, like <color> - you should keep them as is. Provide only translation in your response."
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)