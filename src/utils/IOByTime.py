import os
from datetime import datetime, timedelta
import glob

def read_rss_summary_by_time(days_range=7):
    # 获取当前日期
    today = datetime.now()
    
    # 计算一周前的日期
    week_ago = today - timedelta(days=days_range)
    
    # 构建文件匹配模式
    file_pattern = "data/rss_summary_*.txt"
    
    # 获取所有匹配的文件
    matching_files = glob.glob(file_pattern)
    
    # 筛选出一周内的文件
    recent_files = []
    for file in matching_files:
        # 从文件名中提取日期
        try:
            file_date_str = file.split('_')[-1].split('.')[0]
            file_date = datetime.strptime(file_date_str, "%Y-%m-%d")
            if week_ago <= file_date <= today:
                recent_files.append(file)
        except ValueError:
            # 如果日期解析失败，跳过该文件
            continue
    
    # 按日期排序文件，最新的在前
    recent_files.sort(reverse=True)
    
    # 读取并合并文件内容
    content = ""
    for file in recent_files:
        with open(file, "r", encoding="utf-8") as f:
            content += f.read() + "\n\n"  # 在每个文件内容之间添加空行
    
    if not content:
        print("没有找到最近一周内的RSS摘要文件。")
        return 
    
    # 打印或保存结果
    print(f"已读取并合并 {len(recent_files)} 个文件。")
    return content
    # 如果需要，可以在这里添加保存摘要的代码