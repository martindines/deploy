import unittest, sys, os, StringIO
sys.path.append('./')
from config import config
from deploy import deploy

'''
Notes
Take a look at: with mock.patch('__builtin__.raw_input', return_value='x'):
For mocking user input. Arguably how the app receives input shouldn't be coupled
'''

class TestDeploy(unittest.TestCase):

    def setUp(self):
        self.object = deploy()
        self.config = config()

        self.output = StringIO.StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output

    def createConfigurationFileWithContent(self, content):
        file = open(self.config.FILENAME, 'w')
        file.write(content)
        file.close()

    def deleteConfigurationFile(self):
        os.remove(self.config.FILENAME)

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
        self.deleteConfigurationFile()

    def test_ItPromptsToSelectARemoteWhenMultipleRemotesInConfiguration(self):
        testFileContent = 'username,0.0.0.0,password\nusername1,0.0.0.1,password1'
        self.createConfigurationFileWithContent(testFileContent)
        self.object.deploy()
        self.assertEqual(self.output.getvalue().strip(), 'Remotes in configuration:\n0 username@0.0.0.0\n1 username1@0.0.0.1', 'Expected deploy to prompt user to select remote')
        self.deleteConfigurationFile()

    def tearDown(self):
        self.output.close()
        sys.stdout = self.saved_stdout

if __name__ == '__main__':
    unittest.main()