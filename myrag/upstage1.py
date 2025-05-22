import os
import sys
import json
import requests  # or 비동기하실 때에는 httpx

# os.environ.get("UPSTAGE_API_KEY")
UPSTAGE_API_KEY = "up_1hdeok3F3LeOT9QelpXG0IFNH9nic"


def main(filename: str) -> None:
    if not os.path.exists(filename):
        print(f"file not found: {filename}", file=sys.stderr)
        return

    output_filename = os.path.splitext(filename)[0] + ".json"

    url = "https://api.upstage.ai/v1/document-digitization"
    headers = {"Authorization": f"Bearer {UPSTAGE_API_KEY}"}
    files = {"document": open(filename, "rb")}
    data = {
        "ocr": "force",
        "base64_encoding": "['chart', 'figure', 'table']",
        "model": "document-parse",
    }

    response = requests.post(url, headers=headers, files=files, data=data)
    print(response)

    with open(output_filename, "wt", encoding="utf-8") as f:
        json_string = json.dumps(response.json(), ensure_ascii=False, indent=4)
        f.write(json_string)

    print(f"saved to {output_filename}")

if __name__ == "__main__":
    main(sys.argv[1])
