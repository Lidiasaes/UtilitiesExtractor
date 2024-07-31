from module_email import ExtractEmail
from module_doi import DOI
from module_url import ExtractURL
import re 

class UtilitiesExtractor():
    def __init__(self, input_data, module_activation):
        self.input_data = input_data
        self.module_activation = module_activation
        
        self.modules = ["email", "doi", "add_doi", "extract_website"]
    
    @staticmethod 
    def info():
        return "UtilitiesExtractor: class.\nModules: email, doi, add_doi, extract_website."

    def email(self):
        if self.module_activation == "email":
            email_extractor = ExtractEmail()
            return email_extractor.extract_pattern(self.input_data)
        else:
            raise ValueError(f"module_activation '{self.module_activation}' is not available. Check UtilitiesExtractor.info for available modules")
        

    def doi(self):
        if self.module_activation == "doi":
            doi_extractor = DOI()
            return doi_extractor.extract_doi(self.input_data,)
        
        else: 
            raise ValueError(f"module_activation '{self.module_activation}' is not available. Check UtilitiesExtractor.info for available modules")
    

    def add_doi(self):
        if self.module_activation == "add_doi":
            #assert isinstance(self.input_data, str)
            if DOI.is_valid_regex(self.input_data):   # check if regex is valid              
                print(f"Adding new regular expression to doi_patterns: {self.input_data}")
                DOI.doi_patterns.append(self.input_data)

            else:
                print("Invalid regular expression")
        else:
            raise ValueError(f"module_activation '{self.module_activation}' is not available. Check UtilitiesExtractor.info for available modules")


    def url(self):
        if self.module_activation == "extract_website":
            url_extractor = ExtractURL()
            return url_extractor.extract_url_pattern(self.input_data)
        
        else:
            raise ValueError(f"module_activation '{self.module_activation}' is not available. Check UtilitiesExtractor.info for available modules")



print("---------")
test_sample = ["myhouseishere.right@gmail.com aidfñafiña fñidi hihi@hptmdi.eus","125_myhouseishere.right@gmail.es.com", "hihi@hptmdi.eus",
               "blabnlab blab doi: 10.1016/j.avb.2012.09.003", "DOI:10.1016/j.avb.2012.09.003", "Check out this paper with DOI 10.1000/xyz123.",
               "exploringfrance.com", "www.google.com",
]



if __name__ == "__main__":


    info = UtilitiesExtractor.info()
    print(info)

    dictionary_extractions = {"email": [], "doi":[], "extract_website": []}
    # add doi rule
    utility_extractor = UtilitiesExtractor(r'(?i)^MiKasa$', "add_doi")
    utility_extractor.add_doi()

    # test .doi()
    for i in test_sample:
        try:
            utility_extractor = UtilitiesExtractor(i, "doi")
            print(utility_extractor.doi())

        except ValueError as e:
            print(e)
    print("----------------------------\n")

    for i in test_sample:   
        try:
            utility_extractor = UtilitiesExtractor(i, "email")
            email_values = utility_extractor.email()
            print("Emails:", email_values)
            dictionary_extractions['email'].extend(email_values)
        

        except ValueError as e:
            print("Email Error", e)
    
    print(dictionary_extractions)
    
    print("----------------------------\n")

    for i in test_sample:
        try:
            utility_extractor = UtilitiesExtractor(i, "doi")
            doi_values= utility_extractor.doi()
            print("DOI:", doi_values)
            dictionary_extractions["doi"].extend(doi_values)

        except ValueError as e:
            print("DOI Error", e)


    print("----------------------------\n")

    for i in test_sample:
        try:
            utility_extractor = UtilitiesExtractor(i, "extract_website")
            url_values = utility_extractor.url()
            print("Website:", url_values)
            dictionary_extractions["extract_website"].extend(url_values)
        except ValueError as e:
            print("Website Error", e)

    print("RAW Dictionary with extracted information", dictionary_extractions)

    def clean_dictionary(dictionary_extractions):
        # create copies to avoid modifying dic
        email_list = dictionary_extractions.get("email", [])
        doi_list = dictionary_extractions.get("doi", [])
        website_list = dictionary_extractions.get("extract_website", [])

        #in case there are nested lists, then flatten
        if isinstance(email_list[0], list):
            email_list = [item for sublist in email_list for item in sublist]
        if isinstance(doi_list[0], list):
            doi_list =  [item for sublist in doi_list for item in sublist]
        
        def substring_of_any_list(value, other_list):
            return any(value in other for other in other_list)
        
        cleaned_website_list = [value for value in website_list if not substring_of_any_list(value,email_list) and not substring_of_any_list(value, doi_list)]


        cleaned_dictionary = {
            "email": set(email_list),
            "doi": set(doi_list),
            "extract_website": set(cleaned_website_list)
        }
        return cleaned_dictionary              


    cleaned_dic = clean_dictionary(dictionary_extractions=dictionary_extractions)
    print("\nCleaned dictionary", cleaned_dic)
