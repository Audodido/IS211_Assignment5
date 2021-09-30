import argparse
from urllib.request import proxy_bypass, urlopen
import csv
import re


class Queue():
    
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.self.items)


class Server():
    
    def __init__(self, spr):
        """intialize an instance"""

        self.processing_rate = spr
        self.current_request = None
        self.time_remaining = 0 #internal timer


    def tick(self):
        """Decrements the internal timer sets the printer to idle when task completed"""

        if self.current_request != None:
            self.time_remaining -= 1 #time remaining in the simulation
            if self.time_remaining <= 0:
                self.current_request = None


    def busy(self):
        if self.current_request != None:
            return True
        else:
            return False


    def start_next(self, new_request):
        self.current_request = new_request
        self.time_remaining = new_request[2] #new_request[2] is the time it will take to complete request (column 3 in the csv)


class Request():
    """represents a single server request"""

    def __init__(self, time, file_request):
        self.timestamp = time # used for computing wait time — time request was created/place in queue
        self.file_request = file_request # row[1] from csv_reader

    def get_stamp(self):
        return self.timestamp

    def get_file_request(self):
        return self.file_request

    def wait_time(self, current_time):
        return current_time - self.timestamp #amt of time spent in queue before request was processed


def simulation(num_seconds, requests_per_minute): ##defining terms of the sim
    
    web_server = Server(requests_per_minute):
    request_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()


def main(url):
    """open file from url and store contents"""
    with urlopen(url) as csv_file:
        csv_list = [i.decode("utf-8") for i in csv_file] #decode csv and store each row as a string in a big list
        csv_reader = csv.reader(csv_list, delimiter=',') #take each row (single string) and and break each string into separate elements of a smaller list
        
        # # temporary: just for checking to see whats working:
        # for line in csv_reader: 
        #     print(f'Second in simulation request occurred: {line[0]}')
        #     print(f'File request: {line[1]}')
        #     print(f'Time per task: {line[2]}')

        #instantiating a request object for each line in the list
        for line in csv_reader:
            r = Request(line[2], line[1])
            print(f'Second in simulation request occurred: {r.get_stamp()}')
            print(f'File request: {r.get_file_request()}')
            print(f'Time for task: {r.get_stamp()}')


main(args.file) 

