class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_dict = {}  # Dictionary to store content and paths

        for path in paths:
            parts = path.split()
            directory = parts[0]
            files = parts[1:]

            for file in files:
                file_parts = file.split('(')
                file_name = file_parts[0]
                file_content = file_parts[1][:-1]

                full_path = directory + '/' + file_name

                if file_content in content_dict:
                    content_dict[file_content].append(full_path)
                else:
                    content_dict[file_content] = [full_path]

   
        duplicate_groups = []
        for group in content_dict.values(): 
            if len(group) > 1:
                duplicate_groups.append(group) 
    
        

        return duplicate_groups
        