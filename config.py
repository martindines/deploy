import os.path


class config:
    FILENAME = 'deploy.conf'

    def does_configuration_file_exist(self):
        return os.path.isfile(self.FILENAME)

    def get_content_from_configuration_file(self):
        if self.does_configuration_file_exist():
            file = open(self.FILENAME, 'r')
            return file.read()

    def get_remotes_from_content(self, content):
        remotes = []
        for line in content.split('\n'):
            line = line.split(',')
            remotes.append({
                'username': line[0],
                'host': line[1],
                'password': line[2]
            })

        return remotes

    def get_remotes(self):
        content = self.get_content_from_configuration_file()
        return self.get_remotes_from_content(content)