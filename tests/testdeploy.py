import unittest, sys
sys.path.append('./')
from config import config
from deploy import deploy


class TestDeploy(unittest.TestCase):

    def setUp(self):
        self.object = deploy()
        self.config = config()

    def createConfigurationFileWithContent(self, content):
        file = open(self.config.FILENAME, 'w')
        file.write(content)
        file.close()

    def test_ItDoesntDeployWithoutARemoteInConfiguration(self):
        self.assertFalse(self.object.deploy(), 'Expected deploy to halt because remotes are empty')

    def test_ItSetsARemoteWithASingleRemoteInConfiguration(self):
        testFileContent = 'username,0.0.0.0,password'
        self.createConfigurationFileWithContent(testFileContent)

        expected = {
            'username': 'username',
            'host': '0.0.0.0',
            'password': 'password'
        }

        self.object.deploy()
        self.assertEqual(self.object.remote, expected, 'Expected deploy to set remote to X, but remote value is not X')

    def test_ItListsPossibleRemotesWithMultipleRemotesInConfiguration(self):
        testFileContent = 'username,0.0.0.0,password\nusername1,0.0.0.1,password1'
        self.createConfigurationFileWithContent(testFileContent)

        self.assertTrue(self.object.deploy() == 'Please select remote', 'Expected deploy to prompt user to select remote')


if __name__ == '__main__':
    unittest.main()