import requests
import json

class GetPrograms:

    def get_programs(self):
        URL = "https://web.archive.org/web/20180303155827/https://data.cityofnewyork.us/resource/uvks-tn5n.json"
        response = requests.get(URL)
        if response.status_code == 200:
            return response.content
        else:
            print("Failed to retrieve data. Status code:", response.status_code)
            return None

    def program_school(self):
        programs_list = []
        programs_json = self.get_programs()
        if programs_json:
            programs = json.loads(programs_json)
            for program in programs:
                # print(program)  # Add this line to check the structure of 'program'
                if "agency" in program:  # Check if "agency" key exists in the program
                    programs_list.append(program["agency"])
                else:
                    print("Program does not have 'agency' key:", program)
        else:
            print("Failed to get programs data.")
        return programs_list  

programs = GetPrograms()
programs_schools = programs.program_school()

for school in set(programs_schools):
    print(school)
