import re 

class ExtractURL():  
    def extract_url_pattern(self,input_data):
        pattern = [r'\b(?:https?://|www\.)\S+\b',  
                   r'\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}\b', 
                   r'\b[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+\b', 
                   r'\b[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}(?=\b)', 
 ]
        input_data = input_data.split()
        all_matches = []
        for token in input_data:
            for p in pattern:    
                match = re.search(p, token)
                if match:     
                    all_matches.append(match.group(0))

        return list(set(all_matches))
