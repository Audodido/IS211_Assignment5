import argparse
from urllib.request import proxy_bypass, urlopen
import csv
import re
import time


class Queue():
    
    def __init__(self):
        self.items = []

    def items(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Server():
    
    def __init__(self):
        """intialize an instance"""

        # self.processing_rate = spr
        self.current_request = None
        self.time_remaining = 0 #internal timer

    def tick(self):
        """Decrements the internal timer sets the server to idle when task completed"""

        if self.current_request != None:
            self.time_remaining = self.time_remaining - 1 
            if self.time_remaining <= 0:
                self.current_request = None

    def busy(self):
        if self.current_request != None:
            return True
        else:
            #print("BUSY!!!") ### IF BUSY GO TO DIFF, NON-BUSY SERVER???
            return False

    def start_next(self, new_request):
        self.current_request = new_request
        self.time_remaining = new_request.get_processing_time() 


class Request():
    """represents a single server request"""

    def __init__(self, time, processing_time):
        self.timestamp = time # used for computing wait time —- time request was created/place in queue
        self.processing_time = processing_time # row[2] from csv_reader

    def get_stamp(self):
        return self.timestamp

    def get_processing_time(self):
        return self.processing_time

    def wait_time(self, current_time):
        if current_time - self.timestamp <= 0:
            #print(self.processing_time)
            return self.processing_time
        else:
            return current_time - self.timestamp #amt of time spent in queue before request was processed
            #print(current_time - self.timestamp)


def simulateOneServer(file): 

    web_server = Server()
    request_queue = Queue()
    waiting_times = [] 

 
    csv_file = urlopen(file)
    csv_list = [i.decode("utf-8") for i in csv_file] #decode csv and store each row as a string in a big list
    csv_reader = csv.reader(csv_list, delimiter=',') #take each row (single string) and and break each string into separate elements of a smaller list
    requests = [[int(row[0]), row[1], int(row[2])] for row in csv_reader] #converts row[0] and row[2] from csv to ints
    
    # print(requests[2][1])
    #loads up the queue
    # for r in requests:
    #     print(r)           
        # request = Request(r[0], r[2])
        # request_queue.enqueue(request)
    
    #current_request = request_queue.dequeue() #assigns first request from queue to current_request var


    for current_second in range(len(requests)):
        
        request = Request(requests[current_second][0], requests[current_second][2])
        request_queue.enqueue(request)
        #print(current_second, requests[current_second][0], requests[current_second][2])        
        #print(requests[current_second][0] - current_second)
        # current_request = request_queue.dequeue() #assigns first request from queue to current_request var
        
        if (not web_server.busy()) and (not request_queue.is_empty()):
            next_request = request_queue.dequeue()
            waiting_times.append(next_request.wait_time(current_second)) 
            web_server.start_next(next_request)
            current_request = next_request
        
        web_server.tick()
    
    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average wait %1.1f secs" % average_wait)
    # for w in waiting_times:
    #     print(w)

    


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()

    # def main(file):
    #     simulateOneServer(file) 

    # simulateOneServer(args.file) 
    # main(args.file)
    file = args.file
    simulateOneServer(file)


