from .endpoints import Endpoint
from .flow import Flow



class MetricsBase:
    pass

class Metrics(MetricsBase):
    def __init__(self, loc, **kwargs):
        self.id = loc
        self.endpoints = []
        
    
    def add_to_analytics(self, func):
        functions = func() if type(func) == type(lambda x: x) else func
        # print(f"\n\n{functions}\n\n")
        existing_endpoint_names = [x['id'] for x in self.endpoints]
        # new_endpoint_names = [x.__name__ for x in functions]

        for i in range(len(functions)):
            if functions[i].__name__ in existing_endpoint_names:
                loc = existing_endpoint_names.index(functions[i].__name__)
                self.endpoints[loc]["endpoint"].hits += 1
            else:
                new_endpoint = Endpoint(name=functions[i].__name__, endpoint=functions[i], hits=1)
                self.endpoints.append({'id': functions[i].__name__, 'endpoint': new_endpoint})


    def display(self, **kwargs):

        # print(f"\n\n{self.id}\n\n")
        ep = None
        
        if 'id' in kwargs.keys():
            for i in self.endpoints:
                if i['id'] == kwargs['id']:
                    ep = [i]
                    break
        else:
            ep = self.endpoints  
        
        print("\n\nId:\tHits\n")
        
        for i in ep:
            data = i['endpoint'].stats()
            
            for j in data.keys():
                print(f"{j}: {data[j]}", end="\t")

            print()
            

