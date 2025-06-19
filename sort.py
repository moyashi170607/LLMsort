from google import genai
from google.genai import types
import os
import dotenv


dotenv.load_dotenv()

array = []

array = input("ソートする要素を,で区切って入力してください。\n").split(',')

print("Original array:", array)

print("Sorting the array...")



client = genai.Client(api_key=os.getenv("Gemini_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="""次の配列をソートし、結果だけを[]で囲み、返してください。また、ソートは数字なら数字の大きさで昇順に、"""
    """文字列ならあなたが思うそれらの単語が表すもののランキングで1位から順に並べ替えてください。"""
    """与えられたものが文字列ならソート結果を[]で囲み出力したのち、ランキングの評価基準を端的に出力して。"""+ str(array)
    # config=types.GenerateContentConfig(
    #     thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    # ),
)
print(response.text)