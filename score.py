import os


def add_score(difficulty, user_win, scores_file_name):
    # Determine the path according to the OS
    if os.name == "nt":
        file_path = (f"c:\\temp\\{scores_file_name}")
    else:
        file_path = (f"/tmp//{scores_file_name}")

    # calculate the last game score
    if user_win:
        score = int(difficulty) * 3 + 5
    else:
        score = 0

    # check if the score file exist
    if os.path.exists(file_path):
        score_file = open(file_path, 'r')
        # check that the file contain data, if not define content = 0.
        file_size = os.path.getsize(file_path)
        if file_size == 0:
            content = 0
        else:
            content = score_file.read()
        # verify that the chars in the score files are digit without any space
        digit_content = ''.join(char for char in content if char.isdigit())
        int_content = int(digit_content)
        new_score = int_content + score
        score_file=open(file_path, "w")
        score_file.write(str(new_score))
        score_file.close()
    else:
        score_file=open(file_path, "w")
        score_content=score_file.write("0")
        score_file.close()
