#Importing necessary packages
from dotenv import load_dotenv
import os

import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI

from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
# from pdf_engine import nsu_engine

#loads the environment variable located in .env file
load_dotenv()

#Specifying path to our custom dataset
chatBot_path = os.path.join("data", "students.csv")
chatBot_df = pd.read_csv(chatBot_path)

#Setting up our chatbot
chatBot_query_engine = PandasQueryEngine(
  df = chatBot_df, verbose=True, instruction_str=instruction_str
)
chatBot_query_engine.update_prompts({"pandas_prompt": new_prompt})

#The set of tools the chatbot will be using to respond to the user prompts
tools = [
  note_engine,
  QueryEngineTool(
    query_engine = chatBot_query_engine,
    metadata = ToolMetadata(
      name = "chatBot_data",
      description = "Here is a dataset of random students and their performances in their respective field of study",
    ),
  ),
]

#Setting up our GPT model
llm = OpenAI(model = "gpt-3.5-turbo-0125")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

#While loop to constantly generate prompts until the user quits
while (prompt := input("Ask something (q to quit): ")) != "q":
  result = agent.query(prompt)
  print(result)