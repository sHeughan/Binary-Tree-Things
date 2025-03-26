from friendsbalt.acs import OrderedMap, StringDiff, AVLTree
#Objectives:
#store version of file
#store version history of multiple files
#restore prev. version
#see a log of changes
active_file = None
Files = []

class VersionControl:
    def __init__(self, text):
        self.versions = OrderedMap()
        self.v_num = -1

        self.save("", "File created")
        self.save(text, "Init")
    
    def save(self, new_text, comment):
        self.v_num += 1

        class Node:
            def __init__(self, n_comment = comment, timestamp = self.v_num, om = self.versions, diff = None):
                self.diff = diff
                self.restored = False
                self.comment = n_comment
                self.timestamp = timestamp
                self.om = om
    #            print("Timestamp is:", timestamp)
                if timestamp > 0:
                    last_diff = om[timestamp - 1]
                    diff = tuple((StringDiff(last_diff.diff, new_text)).additions[0])[1]
    #                print("Testing diffs:", StringDiff.raw_diff(last_diff.diff, new_text))
                    diff = str(diff)
    #                print("Last diff was:", om[timestamp - 1].diff)
                    self.diff = diff
                
                else:
                    self.diff = StringDiff.raw_diff("", new_text)
                
        node = Node()
    #    print("The diff is:", node.diff)
        self.versions[self.v_num] = node
    
    def log(self):
        print("Showing the edit history")
        for x in self.versions:
            if x[0] > 0 and x[1].restored == True: 
                print("Version " + str(x[0]) + ":", "'" + str(x[1].diff) + "',",  "(Restored)")
            else: print("Version " + str(x[0]) + ":", "'" + str(x[1].diff) + "',",  x[1].comment)

    def restore(self, version):
        self.v_num += 1
        self.versions[self.v_num] = self.versions[version]
        self.versions[self.v_num].restored = True
        print("Restoring the file...")


        
print("\nHello, and welcome to your text editor and saver! \n __________________")
while True == True:
    if len(Files) == 0:
        active_file = input("Please input the name of your file here: ")
        Files.append(active_file)
    
    elif len(Files) > 1:
        pass

    else:
        pass
    user_choice = input("\n" + str(active_file) + ".txt \n\nWhat would you like to do? \n Create text \n Delete file \n\nInsert choice here: ")
    if (user_choice == "Create text" or user_choice == "create text"): 
        input_text = input("You may enter your text here:\n\n")
        File = VersionControl(input_text)
    elif (user_choice == "Delete file" or user_choice == "delete file"):
        Files.remove(active_file)
    
    else:
        print("You must choose one of the options displayed above (Maybe check for typos?)")
        continue

    while True != False:
        user_choice = input("\n" + str(active_file) + ".txt \n\nWhat would you like to do? \n Edit \n View \n Edit log \n Restore \n\nInsert choice here: ")
        if (user_choice == "Edit" or user_choice == "edit"): 
            input_text = input("You may edit your text here:\n\n")
            input_comment = input("Please give a comment for your edit:\n\n")
            File.save(input_text, input_comment)
        
        if (user_choice == "Edit log" or user_choice == "edit log"): 
            print("_________")
            print("")
            File.log()
            input("\nType anything when you are ready to continue... ")
        
        if (user_choice == "View" or user_choice == "view"):
            print("_________")
            print("\nShowing the current text:")
            print(File.versions[File.v_num].diff)
            input("\nType anything when you are ready to continue... ")
        
        if (user_choice == "Restore" or user_choice == "restore"):
            print("_________")
            version_choice = input("\nWhich version number do you wish to restore to?\n")
            if File.versions[File.v_num] != None:
                File.restore(int(version_choice))
                print("\nRestored to version number: " + version_choice)
                input("\nType anything when you are ready to continue... ")
            
            else:
                print("Not a valid version number!")
                input("\nType anything when you are ready to continue... ")
                continue
            
# File.save("Hello! How are you man?", "Added a question")
# File.save("How are you man?", "Removed greeting")
# File.save("Hey, how are you doing today?", "Readded greeting")
# File.log()
# File.restore(3)
# File.log()