from dotenv import load_dotenv
from browser_use import Agent, Browser
from browser_use.llm import ChatBrowserUse  # 確保與您截圖中的 import 一致
import asyncio

load_dotenv()

async def example():
    browser = Browser()
    llm = ChatBrowserUse()

    # 設定任務：前往 PChome 搜尋 PS5 並找出最便宜的三個價格
    task = (
        "前往 PChome (https://24h.pchome.com.tw/) 搜尋 'PS5 主機'。"
        "1. 提取所有商品名稱、價格與網址。"
        "2. 過濾掉價格低於 10,000 元的項目。"
        "3. 將符合條件的結果『按價格由低到高排序』。"
        "4. 僅列出最便宜的前三名，並以 Markdown 表格格式輸出。"
    )

    agent = Agent(
        task=task,
        llm=llm,
        browser=browser,
    )

    history = await agent.run()
    return history

if __name__ == "__main__":
    asyncio.run(example())