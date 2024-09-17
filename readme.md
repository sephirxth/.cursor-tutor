本项目旨在从各类信息源中获取信息，经过AI处理后，产生简报。
个人项目，供个人使用

This project aims to gather information from various sources, process it with AI, and generate briefings.
Personal project for individual use.

信息源头包括：
- RSS 
- 邮件订阅
从RSS feed中获取文章，并使用AI进行摘要的简单项目。

Information sources include:
- RSS
- Email subscriptions
A simple project to fetch articles from RSS feeds and summarize them using AI.

## TODO 
** 1. 信息源的多样性 **
    - [ ] 邮件订阅
    - [ ] 微信公众号
    - [ ] 知乎
    - [ ] 等    
    - [X] RSS

** 1. Diversity of Information Sources **
    - [ ] Email subscriptions
    - [ ] WeChat Official Accounts
    - [ ] Zhihu
    - [ ] Others
    - [X] RSS

** 2. 面向个人的信息总结 **
    - [X] AI摘要
        - [X] 利用通义千问实现基本功能
        - [ ] 优化prompt
        - [ ] 尝试不同视角下的agent的总结
    - [ ] 记录个人阅读历史信息记录，或记录信息结果的反馈
    - [ ] 根据大众点击趋势，调整信息源的权重等

** 2. Personalized Information Summary **
    - [X] AI summary
        - [X] Implement basic functionality using Tongyi Qianwen
        - [ ] Optimize prompts
        - [ ] Try summaries from different agent perspectives
    - [ ] Record personal reading history or feedback on information results
    - [ ] Adjust information source weights based on popular click trends

** 3. 可用性、易用性 **
    - [ ] 持久化数据储存模块
    - [ ] 网络访问性增强模块

** 3. Usability and User-Friendliness **
    - [ ] Persistent data storage module
    - [ ] Enhanced network accessibility module