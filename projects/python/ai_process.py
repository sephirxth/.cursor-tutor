import datetime
import sys
from http import HTTPStatus
import dashscope


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
    # 读取 rss_summary.txt 文件
    with open("rss_summary.txt", "r", encoding="utf-8") as f:
        content = f.read()

    # 调用 AI 进行总结
    summary = summarize_with_ai(content)

    if summary:
        # 将总结保存到新文件
        with open("ai_summary.txt", "w", encoding="utf-8") as f:
            f.write(f"AI 总结 - 生成时间: {datetime.datetime.now()}\n\n")
            f.write(summary)
        print("AI 总结已保存到ai_summary.txt文件中。")
    else:
        print("AI 总结生成失败。")
