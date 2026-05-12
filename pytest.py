from app import RAG
import json

with open("document.txt", "r", encoding="utf-8") as file:
    text = file.read()

r = RAG(text)

l = ["what is RAG?", "what is MCP?", "what is Top-k and top-p?"]

for i in range(len(l)):

    if i != 0:
        a, b = r.splitter(l[i])

        output = {"query": l[i], "Result A": a, "Result B": b}

        json_output = json.dumps(output, indent=4)

        with open("output_test.md", "a", encoding="utf-8") as file:
            file.write("\n\n")
            file.write(json_output)
    else:
        a, b = r.splitter(l[i])

        output = {"query": l[i], "Result A": a, "Result B": b}

        json_output = json.dumps(output, indent=4)
        with open("output_test.md", "w", encoding="utf-8") as file:
            file.write(json_output)
