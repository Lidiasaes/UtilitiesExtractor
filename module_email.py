import re 

class ExtractEmail():  
    def extract_pattern(self,input_data):
        pattern = r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+'
        input_data = input_data.split()
        all_matches = []
        for token in input_data:
            match = re.search(pattern, token)
            if match:     
                all_matches.append(match.group(0))

        return all_matches
