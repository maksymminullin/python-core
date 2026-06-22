from pathlib import Path

p = Path(".") / "test-text.txt"

file_full_name = p.name  # get file full name : test-text.txt

file_extension = p.suffix  # get file extension : .txt

file_name = p.stem  # get file name without extension test-text


text = p.read_text()  # get old text

p.write_text("new content")  # replaced the old content with "new content"

new_text = p.read_text()  # get text new content

p.touch()  # create new file

new_file = p.rename(
    "new-test-text.txt"
)  # rename file or move to another place and return new Path

with new_file.open(mode="r") as f:
    print(f.name)  # new-test-text.txt
    print(f.readline())  # new contents
