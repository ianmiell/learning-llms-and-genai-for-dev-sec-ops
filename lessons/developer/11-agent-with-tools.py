from dotenv import load_dotenv
load_dotenv()

from langchain.agents import Tool
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import OpenAI
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent

from _lessonshelper.pretty_print_callback_handler import PrettyPrintCallbackHandler
pretty_callback = PrettyPrintCallbackHandler()



# Give the agent memory
memory = ConversationBufferMemory(memory_key="chat_history")

# Prepare the LLM for the agent to use
llm = OpenAI(temperature=0, callbacks=[pretty_callback])

# Add search as a tool to the agent toolbox
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Current Search",
        func=search.run,
        description="useful for when you need to answer questions about current events or the current state of the world",
    ),
]

# Now initialize the agent
agent_chain = initialize_agent(
    llm=llm,
    tools=tools,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory
)
agent_chain.callbacks = [pretty_callback]

agent_chain.run(input="whats the current temperature in London?")

