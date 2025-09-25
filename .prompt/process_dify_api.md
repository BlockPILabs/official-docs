你是一个程序员，你擅长使用GitHub action来监听仓库的修改，并实现一系列的工作流。

## 简单描述：
我需要监听该仓库的内容更改，当内容更改时，获取到更改文件的全部内容，然后调用Dify中我创建的Workflow的API进行文档的更新。

## 处理流程：
    1.监听仓库的变化获取变化的文件。
    2.获取到变化的文件并以File形式待传递。
    3.调用Dify的Workflow API (app 密钥： app-1Gg1wuRzZyRMxaNP7iaJz6Jx)
### API示例：
```python
import requests
import json

def upload_file(file_path, user):
    upload_url = "https://ai-agent.blockpi.org/v1/files/upload"
    headers = {
        "Authorization": "Bearer app-xxxxxxxx",
    }

    try:
        print("上传文件中...")
        with open(file_path, 'rb') as file:
            files = {
                'file': (file_path, file, 'text/plain')  # 确保文件以适当的MIME类型上传
            }
            data = {
                "user": user,
                "type": "TXT"  # 设置文件类型为TXT
            }

            response = requests.post(upload_url, headers=headers, files=files, data=data)
            if response.status_code == 201:  # 201 表示创建成功
                print("文件上传成功")
                return response.json().get("id")  # 获取上传的文件 ID
            else:
                print(f"文件上传失败，状态码: {response.status_code}")
                return None
    except Exception as e:
        print(f"发生错误: {str(e)}")
        return None

def run_workflow(file_id, user, response_mode="blocking"):
    workflow_url = "https://ai-agent.blockpi.org/v1/workflows/run"
    headers = {
        "Authorization": "Bearer app-xxxxxxxxx",
        "Content-Type": "application/json"
    }

    data = {
        "inputs": {
            "orig_mail": [{
                "transfer_method": "local_file",
                "upload_file_id": file_id,
                "type": "document"
            }]
        },
        "response_mode": response_mode,
        "user": user
    }

    try:
        print("运行工作流...")
        response = requests.post(workflow_url, headers=headers, json=data)
        if response.status_code == 200:
            print("工作流执行成功")
            return response.json()
        else:
            print(f"工作流执行失败，状态码: {response.status_code}")
            return {"status": "error", "message": f"Failed to execute workflow, status code: {response.status_code}"}
    except Exception as e:
        print(f"发生错误: {str(e)}")
        return {"status": "error", "message": str(e)}

# 使用示例
file_path = "{your_file_path}"
user = "difyuser"

# 上传文件
file_id = upload_file(file_path, user)
if file_id:
    # 文件上传成功，继续运行工作流
    result = run_workflow(file_id, user)
    print(result)
else:
    print("文件上传失败，无法执行工作流")
```
    
    4.完成并打印相关信息
## 要求：
    1.过滤build, .prompt, .gitbook, .github, README.md, SUMMARY.md目录文件夹下的文件更改