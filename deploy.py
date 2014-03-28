from config import config


class deploy:
    remote = {}

    def prompt_to_select_remote(self, remotes):
        print('Remotes in configuration:')
        for key, remote in enumerate(remotes):
            print('%s %s@%s' % (key, remote['username'], remote['host']))

    def deploy(self):
        config_object = config()
        remotes = config_object.get_remotes()
        if len(remotes) > 1:
            self.prompt_to_select_remote(remotes)
        elif remotes:
            self.remote = remotes[0]
        return False