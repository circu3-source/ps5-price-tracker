import pytest
import asyncio
import re
from main import example

@pytest.mark.asyncio
async def test_ps5_agent_results():
    history = await example()
    final_result = history.final_result()
    
    print(f"\nAI 回傳結果：\n{final_result}")
    
    # 基本檢查
    assert final_result is not None
    
    # 呼叫驗證邏輯
    validate_price_logic(final_result)

def validate_price_logic(final_result):
    # 提取價格
    prices = re.findall(r'(\d{1,3}(?:,\d{3})*)', final_result)
    prices = [int(p.replace(',', '')) for p in prices if int(p.replace(',', '')) > 10000]
    
    print(f"解析到的價格：{prices}")
    assert len(prices) >= 3, f"數量不足，僅找到 {len(prices)} 個"
    assert prices == sorted(prices), "價格未正確排序"