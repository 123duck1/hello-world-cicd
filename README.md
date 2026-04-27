一、作业目标
本作业的目标是为一个简单的 Hello World Python 项目，基于 GitHub Actions 搭建一条自动化 CI/CD（持续集成 / 持续部署）流水线，实现代码提交后的自动拉取、环境配置、单元测试和程序运行，验证自动化流程的可行性。
二、项目结构
项目目录结构如下：
hello-world-cicd/
├── .github/
│   └── workflows/
│       └── ci.yml       # GitHub Actions 流水线配置文件
├── main.py               # 主程序（Hello World 示例）
└── test_main.py          # 单元测试文件

三、核心代码说明
1. 主程序 main.py
实现了一个简单的 hello() 函数，返回指定字符串，并在主程序中打印输出。
def hello():
    return "Hello World"

if __name__ == "__main__":
    print(hello())

2. 单元测试文件 test_main.py
验证 hello() 函数的返回值是否符合预期。
from main import hello

def test_hello():
    assert hello() == "Hello World"
    print("测试通过！")

if __name__ == "__main__":
    test_hello()

  CI/CD 流水线配置 .github/workflows/ci.yml
GitHub Actions 自动化流水线配置文件，定义触发条件、运行环境与执行步骤。
name: Hello World CI/CD Pipeline

# 触发条件：代码推送到 main 分支时自动运行
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest  # 运行环境：GitHub 提供的 Ubuntu 虚拟机
    steps:
      # 步骤1：拉取仓库代码
      - name: Checkout code
        uses: actions/checkout@v4

      # 步骤2：配置 Python 环境
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      # 步骤3：执行单元测试
      - name: Run tests
        run: |
          python test_main.py
四、流水线运行流程
触发条件：本地代码推送到 GitHub 仓库的 main 分支时，自动触发流水线。
执行步骤：
拉取代码：从仓库拉取最新代码到运行环境。
配置环境：安装 Python 3.11 环境。
单元测试：运行 test_main.py 中的测试用例，验证函数逻辑。
运行结果：所有步骤执行成功，流水线显示绿色 对勾，说明 CI/CD 流程配置完成。
五、仓库与流水线验证
项目 GitHub 仓库地址：https://github.com/123duck1/hello-world-cicd
流水线查看：进入仓库「Actions」标签页，可查看所有步骤的执行日志与运行状态。
成功标志：流水线全部通过，显示绿色对勾，表示自动构建、测试流程正常工作。
