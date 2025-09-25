import os
import sys

def main():
    changed = os.getenv("CHANGED_FILES", "")
    if not changed.strip():
        print("No changed files provided. Exiting.")
        sys.exit(0)

    files = [f for f in changed.splitlines() if f]
    print(f"::group::Modified files ({len(files)})")
    for fp in files:
        print(f" - {fp}")
        # ===== 在此处加入你的业务逻辑 =====
        # 例如：
        if fp.endswith(".py"):
        #     # 对每个 Python 文件跑单元测试或 lint
          os.system(f"pytest {fp}")
        elif fp.endswith(".md"):
        #     # 校验文档格式
          os.system(f"markdownlint {fp}")
        # ==================================

    print("::endgroup::")

if __name__ == "__main__":
    main()
