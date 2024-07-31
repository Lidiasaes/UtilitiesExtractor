import re 

class DOI():
    doi_patterns = [r'10\.\d{4,9}/[\w\-._;()/:]+']
                    # add more patterns 
                    
    @staticmethod # static method
    def extract_doi(input_data):
        all_matches = []
        for pattern in DOI.doi_patterns:
            matches = re.findall(pattern,input_data,)
            all_matches.extend(matches) 
        
        cleaned_matches =  [match.rstrip(".,!?;") for match in all_matches] # if doi ends with a punctuation mark, then it is removed
        return cleaned_matches


    @staticmethod
    def is_valid_regex(pattern):
        try:
            re.compile(pattern)
            return True
        except re.error:
                return False