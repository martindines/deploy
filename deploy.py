from config import config


class deploy:
    remote = {}

    def deploy(self):
        config_object = config()
        remotes = config_object.get_remotes()
        if len(remotes) > 1:
            print('Please select remote')
        elif remotes:
            self.remote = remotes[0]
        return False