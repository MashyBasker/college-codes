class Diff:

    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

    def file_to_list(self, filename):
        lst = open(filename).read().split('\n')
        return lst

    def get_indexes(self) -> list:
        same = []
        different = []
        # getting the filepaths
        file1path = self.file1
        file2path = self.file2
        
        # read file and split by newlines
        file1list = self.file_to_list(file1path)
        file2list = self.file_to_list(file2path)

        # get line index of unequal lines
        for i in range(min(len(file1list), len(file2list))):
            # convert line to same format string
            file1line = file1list[i].replace(" ", "").lower()
            file2line = file2list[i].replace(" ", "").lower()
            
            if file1line != file2line:
                different.append(i)
            elif file1line == file2line:
                same.append(i)

        return same, different
    
    def find_similar_lines(self):
        file1path = self.file1
        file2path = self.file2

        file1list = self.file_to_list(file1path)
        file2list = self.file_to_list(file2path)

        flist1 = [x.replace(" ", "").lower() for x in file1list]
        flist2 = [x.replace(" ", "").lower() for x in file2list]

        c = 0
        for l in flist1:
            if l in flist2:
                c += 1
        return c



    def display_pretty_output(self):
        same_lines, diff_lines = self.get_indexes()
        print(f"Total number of different lines(at same index):\t{len(diff_lines)}")
        print(f"Total number of similar lines(at same index):\t{len(same_lines)}")
        print(f"Total number of similar lines(at different indexes):\t{self.find_similar_lines()}")
        


def main():
    cmd = Diff("file1.txt", "file2.txt")
    print(cmd.display_pretty_output())


if __name__ == "__main__":
    main()

