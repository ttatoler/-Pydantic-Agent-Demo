         
# Agent Demo

一个基于Gemini AI模型的简单智能代理项目，用于文件操作管理。

## 项目介绍

Agent Demo是一个轻量级的AI助手应用，它利用Google的Gemini 2.5 Flash模型，能够通过自然语言指令执行文件操作任务。该项目展示了如何使用pydantic_ai库构建一个具有特定功能的智能代理。

## 功能特点

- **自然语言交互**：通过简单的文字指令控制AI助手
- **文件操作**：支持读取、列出和重命名文件
- **上下文感知**：保持对话历史，实现连续对话体验
- **安全限制**：所有文件操作限制在`./test`目录内

## 系统要求

- Python 3.8+
- 有效的Gemini API密钥

## 安装步骤

1. 克隆或下载项目代码

2. 安装依赖包
   ```bash
   pip install pydantic_ai python-dotenv
   ```

3. 配置API密钥
   - 在项目根目录找到`.env`文件
   - 将`your_api_key_here`替换为你的实际Gemini API密钥
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

4. 创建测试目录
   ```bash
   mkdir test
   ```

## 使用方法

1. 运行主程序
   ```bash
   python main.py
   ```

2. 在命令行界面输入指令，例如：
   - "列出所有文件"
   - "读取文件example.txt"
   - "将file1.txt重命名为file2.txt"

## 项目结构

```
.
├── .env            # 环境变量配置文件，存储API密钥
├── main.py         # 主程序入口，包含Agent初始化和交互循环
├── tools.py        # 工具函数定义，包含文件操作相关功能
└── test/           # 文件操作的目标目录（需手动创建）
```

## 工具函数说明

项目包含三个主要工具函数：

1. **read_file(name)**
   - 功能：读取指定文件的内容
   - 参数：文件名（相对于test目录）
   - 返回：文件内容或错误信息

2. **list_files()**
   - 功能：列出test目录下的所有文件
   - 返回：文件路径列表

3. **rename_file(name, new_name)**
   - 功能：重命名文件
   - 参数：原文件名和新文件名（相对于test目录）
   - 返回：操作结果信息

## 注意事项

- 所有文件操作都限制在`./test`目录内，以确保安全性
- 首次使用前需要手动创建`test`目录

## 扩展开发

如需扩展项目功能，可以在`tools.py`中添加新的工具函数，并在`main.py`中的Agent初始化部分进行注册：

```python
agent = Agent(model,
              system_prompt="You are an experienced programmer",
              tools=[tools.read_file, tools.list_files, tools.rename_file, tools.your_new_tool])
```


        
