from config import config


class deploy:
    remote = {}

    def deploy(self):
        config_object = config()
        remotes = config_object.get_remotes()
        if len(remotes) > 1:
            print('Remotes in configuration:')
            for key, remote in enumerate(remotes):
                print('%s %s@%s' % (key, remote['username'], remote['host']))
        elif remotes:
            self.remote = remotes[0]
        return False