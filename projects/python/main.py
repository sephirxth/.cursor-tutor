import datetime
import html
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# 设置环境变量，禁用代理
os.environ["NO_PROXY"] = "*"
import get_feeds
import ai_process
from http import HTTPStatus
import dashscope


def save_to_html(entries):
    with open("data/rss_summary.html", "w", encoding="utf-8") as f:
        f.write(f"""
        <html>
        <head>
            <title>RSS摘要</title>
            <meta charset="utf-8">
            <style>
                body {{ font-family: Arial, sans-serif; margin: 0 auto; max-width: 800px; padding: 20px; }}
                h1 {{ color: #333; }}
                .entry {{ border-bottom: 1px solid #eee; padding: 20px 0; }}
                .entry h2 {{ margin-top: 0; }}
                .entry .meta {{ color: #666; font-size: 0.9em; }}
            </style>
        </head>
        <body>
            <h1>RSS摘要 - 生成时间: {datetime.datetime.now()}</h1>
        """)

        for entry in entries:
            f.write(f"""
            <div class="entry">
                <h2><a href="{entry.link}">{html.escape(entry.title)}</a></h2>
                <p class="meta">发布时间: {entry.published}</p>
                <div class="summary">
                    {entry.summary}
                </div>
            </div>
            """)

        f.write("""
        </body>
        </html>
        """)


def save_to_plain_text(entries):
    with open("data/rss_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"RSS摘要 - 生成时间: {datetime.datetime.now()}\n\n")
        for entry in entries:
            f.write(f"标题: {entry.title}\n")
            f.write(f"链接: {entry.link}\n")
            f.write(f"发布时间: {entry.published}\n")
            f.write(f"摘要: {entry.summary}\n\n")


rss_feeds = [
    #'https://rsshub.app/gov/zhengce/zuixin',
    #'https://feeds.feedburner.com/solidot',
    "https://vercel-rssh-ub-neon.vercel.app/sciencenet/blog/recommend",
    "https://www.sciencenet.cn/xml/blog.aspx?di=20",
    # 添加更多RSS源...
]


if __name__ == "__main__":
    
    # 设置 API 密钥
    dashscope.api_key = ai_process.read_api_key()
    entries = get_feeds.parse_feeds(rss_feeds)
    save_to_plain_text(entries)
    # save_to_html(entries)
    ai_process.process_and_summarize()
    print("RSS摘要已保存到rss_summary.txt和rss_summary.html文件中。")
    print("AI 总结已保存到ai_summary.txt文件中。")
