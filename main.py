from typing import NoReturn
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai import Agent

from dotenv import load_dotenv 
import tools

load_dotenv() # 加载环境变量
model = GeminiModel("gemini-2.5-flash-preview-04-17") # 创建模型实例

agent = Agent(model,
              system_prompt="You are an experienced programmer",
              tools=[tools.read_file, tools.list_files, tools.rename_file])

def main() -> NoReturn:
    history = [] # 用于存储对话历史

    while True: # 循环对话
        user_input = input("Input: ")
        resp = agent.run_sync(user_input,
                              message_history=history)
        history = list(resp.all_messages())
        print(resp.output)


if __name__ == "__main__":
    main()