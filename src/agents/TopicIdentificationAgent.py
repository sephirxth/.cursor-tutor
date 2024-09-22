import sys
from http import HTTPStatus
import dashscope
import json
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.IOByTime import read_rss_summary_by_time


class LLMTopicIdentificationAgent:
    def __init__(self, rss_file_path, user_demand_file_path, output_file_path, api_key_path):
        self.rss_file_path = rss_file_path
        self.user_demand_file_path = user_demand_file_path
        self.output_file_path = output_file_path
        self.api_key_path = api_key_path
        self.set_api_key()

    def set_api_key(self):
        with open(self.api_key_path, 'r') as file:
            api_key = file.read().strip()
        dashscope.api_key = api_key

    def read_rss_summary(self):
        return read_rss_summary_by_time()

    def read_user_demand(self):
        with open(self.user_demand_file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def identify_topics(self, text, user_demands):
        messages = [
            {
                "role": "system",
                "content": "你是一个专业的主题识别助手。你的任务是从给定的RSS摘要中识别与用户需求直接（或者长期来看间接）相关的主题。请仔细分析文本,提取重要的主题,并确保这些主题与用户的需求相关。"
            },
            {
                "role": "user",
                "content": f"以下是RSS摘要内容:\n\n{text}\n\n用户需求如下:\n\n{user_demands}\n\n请识别与用户需求相关的主题,并返回一个主题列表。每个主题应该是一个简短的短语或关键词。"
            }
        ]

        response = dashscope.Generation.call(
            model="qwen-max",
            messages=messages,
            result_format="message",
            max_tokens=2000,
            temperature=0.7,
            top_p=0.8,
        )

        if response.status_code == HTTPStatus.OK:
            content = response.output.choices[0]["message"]["content"]
            print(f"LLM响应内容: {content}")  # 打印LLM的响应内容以便调试
            topics = self.parse_topics(content)
            return topics
        else:
            print(
                "请求失败，状态码：%s，错误代码：%s，错误信息：%s"
                % (response.status_code, response.code, response.message)
            )
            return None

    def parse_topics(self, content):
        # 尝试解析JSON
        try:
            topics = json.loads(content)
            if isinstance(topics, list):
                return topics
        except json.JSONDecodeError:
            pass

        # 如果不是JSON，尝试按行分割
        topics = [line.strip() for line in content.split('\n') if line.strip()]
        
        # 如果行数过多，可能是整个文本内容，此时我们只取前10个单词作为主题
        if len(topics) > 10:
            topics = content.split()[:10]

        return topics

    def process(self):
        rss_content = self.read_rss_summary()
        user_demands = self.read_user_demand()
        
        identified_topics = self.identify_topics(rss_content, user_demands)
        
        if identified_topics:
            with open(self.output_file_path, 'w', encoding='utf-8') as file:
                json.dump(identified_topics, file, ensure_ascii=False, indent=2)
            print(f"已识别的主题已保存到 {self.output_file_path}")
            return identified_topics
        else:
            print("主题识别失败")
            return None

# 使用示例
if __name__ == "__main__":
    agent = LLMTopicIdentificationAgent(
        'data/rss_summary.html',
        'data/user_demand.txt',
        'data/llm_identified_topics.json',
        'config/api_key.txt'
    )
    identified_topics = agent.process()
    if identified_topics:
        print(f"已识别的主题: {identified_topics}")