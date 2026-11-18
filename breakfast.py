from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

# Create the model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Prompt that pins the format
prompt = """Give me exactly 5 healthy breakfast ideas.
Format your answer as a numbered list.
One idea per line.
No introduction, no extra text, no explanations.
Just the 5 ideas."""

# Call the model
reply = llm.invoke(prompt)

# Print only the text content
print(reply.content)