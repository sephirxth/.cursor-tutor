本项目旨在搭建一个个人信息助手，充分利用LLM的能力，从各类信息源中获取信息，经过AI处理后，产生简报。



# Develop

1. 将自己的api_key写入config下的api_key.txt中
2. 在data目录下填写rss_feeds.txt, user_demand.txt
3. 运行代码




## TODO 
** 1. 多元化信息源 ** 

    - [ ] 传统媒体
    - [ ] 社交媒体
    - [ ] 学术论文
    - [ ] 专家观点
按照类别：

    - [ ] 邮件订阅
    - [ ] 微信公众号
    - [ ] 知乎
    - [X] RSS 
    - [ ] 等

 
** 2. 信息质量提高 ** 

    - [ ]  信息可信度评分系统
        - [ ] 煽动性、立场评估
    - [ ] 同一事件/主题的多方观点聚合、追踪  2024年9月22日 优先级：高
        - [ ] “主题”识别
        - [ ] “主题”存储
        - [ ] 对于一个新的信息，询问该信息是否与存储主题相关，并提取该信息对于某一主题的“观点”
            - [ ] 记录观点来源
            - [ ] 推测该观点来源代表了哪方利益
            - [ ] 观点的支撑论据与论点强度评分
            - [ ] 记录观点的时间
        - [ ] 事件时间线生成
 --------------------
实现 
主题识别 Agent
- [ ] 2024年9月22日 13点58分 需要将任务分解为6000字符的子任务



        输入：新的信息文本
        任务：识别文本中的主要主题和关键实体
        输出：主题列表和关键实体


        主题存储 Agent

        输入：主题识别Agent的输出
        任务：将新主题添加到存储中，更新现有主题的相关信息
        输出：更新后的主题存储状态


        主题相关性判断 Agent

        输入：新信息文本和现有主题列表
        任务：判断新信息是否与存储的主题相关
        输出：相关主题列表和相关度评分


        观点提取 Agent

        输入：信息文本和相关主题
        任务：提取文本中关于特定主题的观点
        输出：观点摘要和关键论点


        信息源分析 Agent

        输入：观点和信息来源
        任务：分析信息来源，推测其代表的利益方
        输出：信息来源类型和可能代表的利益方


        论点评估 Agent

        输入：观点和支撑论据
        任务：评估论点的强度和可信度
        输出：论点强度评分和可信度评分


        时间信息提取 Agent

        输入：信息文本
        任务：提取文本中的时间信息，确定观点或事件的时间点
        输出：标准化的时间信息


        事件时间线生成 Agent

        输入：一段时间内的所有相关观点和事件
        任务：根据时间顺序组织事件和观点，生成时间线
        输出：结构化的事件时间线


        观点聚合 Agent

        输入：同一主题的多个观点
        任务：对观点进行分类和聚合，识别主要立场
        输出：聚合后的观点概述和主要立场列表


        综合分析 Agent

        输入：所有前面Agent的输出结果
        任务：综合分析主题、观点、时间线等信息，生成总体报告
        输出：主题的综合分析报告，包括多方观点比较、事件发展脉络等

 --------------------


    - [X] AI摘要/标题
        - [X] 利用通义千问实现基本功能
        - [ ] 优化prompt
        - [ ] 尝试不同视角下的agent的总结
    - [ ] 信息去重
    - [ ] 根据大众点击趋势，调整信息源的权重等
 
** 3. 系统、可用性、易用性 **
    - [ ] 持久化数据储存模块
    - [ ] 网络访问性增强模块

    - [ ] 连接到obsidian等笔记工具
    - [ ] 根据用户习惯、推测用户需求，不断改进的功能  2024年9月22日 优先级：高
        - [ ] 周期总结和报告
        - [ ] 根据用户情况推荐：信息源的增删

# 参考、相关项目
1. [huginn/huginn: Create agents that monitor and act on your behalf. Your agents are standing by!](https://github.com/huginn/huginn)
2. [Significant-Gravitas/AutoGPT: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.](https://github.com/Significant-Gravitas/AutoGPT)
3. [DIYgod/RSSHub: 🧡 Everything is RSSible](https://github.com/DIYgod/RSSHub)
4. [IFTTT - Automate business & home](https://ifttt.com/)
