from llm_client import get_client, Message

def main():
    print(get_client("ollama").chat("qwen3:8b",[Message(role="user", content="hi!")]))


if __name__ == "__main__":
    main()
