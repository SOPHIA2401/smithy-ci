import argparse
import os
from xmlrpc.client import boolean
from prettytable import PrettyTable

class Dredd:
    def __init__(self, endpoint, user, path, test_name, test_pass):
        if endpoint is not None:
            self.endpoint = endpoint
        else:     
            self.endpoint = "https://127.0.0.1:9200"
            # self.endpoint = "https://search-veggies-h3miursexyzr46hlbqin27fxei.us-east-1.es.amazonaws.com"

        if user is not None:
            self.user = user
        else:
            self.user = "admin:admin"
            # self.user = "sofigarg:T@rget2023"

        if path is not None:
            self.path = path
        else:
            self.path = ""    

        if test_name is not None:
            self.test_name  = test_name 
        else:
            self.test_name = ""  

        if test_pass is not None:
            self.test_pass  = test_pass 
        else:
            self.test_pass = False     

    def write_file(self): 
        file_obj = open("url.txt", mode='w', encoding='utf-8') 
        text = self.endpoint + " " + self.user 
        file_obj.write(text)
        file_obj.seek(0,0)
        file_obj.close()

    def dredd_work(self):
        # Walking in test directory tree and runing dredd framework.
        tp = 0
        tf = 0
        test_failed = []
        test_passed = []
        test_passes = PrettyTable()
        test_fails = PrettyTable()
        for dirpath, dirnames, files in os.walk("../models"+self.path):
            curr_path = dirpath.split('/')
            curr_dir = curr_path[len(curr_path)-1]         
            if files:
                print(dirpath)
                command = "dredd " + dirpath +"/"+ files[1]+ " " + self.endpoint+ " --user=" + self.user + " --hookfiles=" + dirpath + "/" + files[0] 
                if self.test_name != "":
                    if self.test_name == curr_dir:
                        result = os.system(command)
                        print("\n RESULT: ",result)
                        if(result != 0): 
                            test_failed.append([curr_dir,dirpath])
                            tf = tf+1
                        else:
                            tp = tp+1
                            test_passed.append([curr_dir,dirpath])                                  
                else:
                    result = os.system(command) 
                    print("\n RESULT: ",result) 
                    if(result != 0):
                        tf = tf+1
                        test_failed.append([curr_dir,dirpath])
                    else:
                        tp = tp+1
                        test_passed.append([curr_dir,dirpath]) 
        if self.test_pass == True:
            test_passes.field_names = ["Model Name", "Directory Path"]
            test_passes.add_rows(test_passed)
            test_passes.align='l'
            print("Results: Test cases passed.",test_passes,sep="\n")
        print("Total number of test cases: ", tp+tf)
        print("Test Passed: ",tp)
        print("Test failed: ",tf)
        test_fails.field_names = ["Model Name", "Directory Path"]
        test_fails.add_rows(test_failed)
        test_fails.align='l'
        print("Results: Test cases failed.",test_fails,sep="\n")
        return len(test_failed)       


# Parsing command line arguments:
parser = argparse.ArgumentParser()

parser.add_argument('--endpoint', type=str, required=False)
parser.add_argument('--user', type=str, required=False)
parser.add_argument('--path', type=str, required=False)
parser.add_argument('--testname', type=str, required=False)
parser.add_argument('--testpass', type=bool, required=False)
args = parser.parse_args()

# Check whether default arguments provided by user:
obj = Dredd(args.endpoint, args.user, args.path, args.testname, args.testpass )

# Creating a intermediate file for storing URL.
obj.write_file()

# Running dredd
exit(obj.dredd_work())

