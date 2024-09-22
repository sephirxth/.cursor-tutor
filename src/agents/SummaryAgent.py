import datetime
import sys
from http import HTTPStatus
import dashscope
import os
from datetime import datetime, timedelta
import glob


from utils.IOByTime import read_rss_summary_by_time

def read_api_key():
    with open("config/api_key.txt", "r") as file:
        return file.read().strip()


def validate_request_result(response):
    if response.status_code != HTTPStatus.OK:
        print(
            "请求失败，状态码：%s，错误代码：%s，错误信息：%s"
            % (response.status_code, response.code, response.message)
        )
        sys.exit(response.status_code)
    else:
        print(response)


def summarize_with_ai(text):
    messages = [
        {
            "role": "system",
            "content": "你是一个专业的智能摘要助手，擅长提炼RSS文章的核心内容。请按以下要求总结给定的RSS摘要：\n1. 提取文章的主要观点和关键信息\n2. 保持客观中立的语气\n3. 区分事实陈述和观点评论\n4. 保留原文的时效性信息（如日期、时间等）\n5. 总结长度不超过200字",
        },
        {"role": "user", "content": f"请总结以下RSS摘要内容：\n\n{text}"},
    ]

    response = dashscope.Generation.call(
        model="qwen-max",
        messages=messages,
        result_format="message",
        max_tokens=2000,  # 约200个汉字
        temperature=0.7,
        top_p=0.8,
    )

    if response.status_code == HTTPStatus.OK:
        summary = response.output.choices[0]["message"]["content"]
        return summary
    else:
        print(
            "请求失败，状态码：%s，错误代码：%s，错误信息：%s"
            % (response.status_code, response.code, response.message)
        )
        return None


def process_and_summarize():
   
    # 例如，调用AI进行摘要等操作
    summary = summarize_with_ai(read_rss_summary_by_time())
    return summary
