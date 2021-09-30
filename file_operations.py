import os
import glob
import socket


if __name__ == '__main__':

    each_file_words, total_words, top_three_words = [], 0, []

    # Lists all the test files in the home directory (Eg: /home/data)
    file_names = glob.glob('*.txt')

    # Reading each file and couting the total number of words
    for i in file_names:
        temp_count = 0
        if i in ['Limerick.txt', 'IF.txt']:
            file_data = open(os.path.join(os.getcwd(), i), "rt").read()
            words = file_data.split()
            if i == 'IF.txt':  # Check for IF.txt file
                # Gets the each word count in reverse order
                sorted_words_count = sorted({w: words.count(w) for w in words}.items(),
                                            key=lambda x: x[1], reverse=True)
                for item in sorted_words_count:  # Gets the top three words and their count
                    if temp_count != 3:
                        top_three_words.append(item)
                        temp_count += 1

            each_file_words.append("Words in `{0}` file is - {1}\n".format(i, len(words)))
            total_words += len(words)


    # Load all the data into the result.txt file
    with open(os.path.join(os.getcwd(), 'result.txt'), 'w') as f:
        f.write("Lists all the files in the `/home/data` directory\n")
        f.write("{} \n".format(str(file_names)))
        for each in each_file_words:
            f.write(each)

        # Prints the total number of words from both the files
        f.write("Total Number of words in both files - `{}`\n".format(total_words))

        # Prints the top three words and their counts
        f.write("Top three words and their counts - `{}`\n".format(top_three_words))

        # Prints the IP Address of the current machine
        f.write("IP Address of this machine - `{}`\n".format(socket.gethostbyname(socket.gethostname())))
