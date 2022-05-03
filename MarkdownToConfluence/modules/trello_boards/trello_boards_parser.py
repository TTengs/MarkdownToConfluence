import re, requests

def parse_boards(filename: str):
    with open(filename, 'r') as f:
        lines = f.readlines()   
    with open(filename, 'w') as f:
        for line in lines:
            res = parse_board(line)
            new_line = res if res.endswith('\n') else res + '\n'
            f.write(new_line)

def parse_board(line: str) -> str:
    boards = re.findall(r'((https://)(trello.com/b/)[a-zA-Z\d]+([/][\w-]+)*)', line) #official atlassian regex magic
    new_line = line
    for board in boards:
        board_url = board[0]
        board_tag = f'<ac:structured-macro ac:name=\"trello-board\" ac:schema-version=\"1\" data-layout=\"default\" ac:macro-id=\"39a55cc39b49f1a520d43a1c87bf1f07\"><ac:parameter ac:name=\"url\">{board_url}</ac:parameter><ac:parameter ac:name=\"height\">760px</ac:parameter></ac:structured-macro>'
        new_line = new_line.replace(board_url, board_tag)
    return new_line

def run(filename):
    parse_boards(filename)