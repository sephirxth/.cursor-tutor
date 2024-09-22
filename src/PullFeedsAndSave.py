import os
import feedparser
from datetime import datetime
import html

class RSSProcessor:
    def __init__(self, rss_feed_file='data/rss_feeds.txt', output_dir='data'):
        self.rss_feed_file = rss_feed_file
        self.output_dir = output_dir
        self.rss_feeds = self.load_rss_feeds()

    def load_rss_feeds(self):
        try:
            with open(self.rss_feed_file, 'r', encoding='utf-8') as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"RSS源文件 {self.rss_feed_file} 未找到。")
            return []

    def fetch_and_parse_feeds(self):
        all_entries = []
        for feed_url in self.rss_feeds:
            try:
                feed = feedparser.parse(feed_url)
                all_entries.extend(feed.entries)
            except Exception as e:
                print(f"解析 {feed_url} 时出错: {e}")
        return all_entries

    def save_to_file(self, entries):
        today = datetime.now().strftime('%Y-%m-%d')
        filename = f"rss_summary_{today}.txt"
        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"RSS摘要 - 生成时间: {datetime.now()}\n\n")
            for entry in entries:
                f.write(f"标题: {entry.title}\n")
                f.write(f"链接: {entry.link}\n")
                f.write(f"发布时间: {entry.get('published', 'N/A')}\n")
                summary = html.unescape(entry.get('summary', 'N/A'))
                f.write(f"摘要: {summary}\n\n")

        print(f"RSS摘要已保存到 {filepath}")

    def process_and_save(self):
        if not self.rss_feeds:
            print("没有找到RSS源。请检查RSS源文件。")
            return

        entries = self.fetch_and_parse_feeds()
        if not entries:
            print("没有找到新的RSS条目。")
            return

        self.save_to_file(entries)

# 使用示例
if __name__ == "__main__":
    processor = RSSProcessor()
    processor.process_and_save()

 