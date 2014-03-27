import unittest, sys, os
sys.path.append('./')
from config import config


class TestConfig(unittest.TestCase):

    def setUp(self):
        self.object = config()

    def createConfigurationFile(self):
        open(self.object.FILENAME, 'a')

    def deleteConfigurationFile(self):
        os.remove(self.object.FILENAME)

    def createConfigurationFileWithContent(self, content):
        file = open(self.object.FILENAME, 'w')
        file.write(content)
        file.close()

    def test_ItDoesntHaveConfigurationFile(self):
        self.assertFalse(self.object.does_configuration_file_exist(), 'Configuration file exists - Expected no configuration file')

    def test_ItHasConfigurationFile(self):
        self.createConfigurationFile()
        self.assertTrue(self.object.does_configuration_file_exist(), 'Configuration file doesnt exist - Expected configuration file')
        self.deleteConfigurationFile()

    def test_ItRaisesExceptionWhenGettingContentsFromEmptyConfigurationFile(self):
        self.assertRaises(Exception, self.object.get_content_from_configuration_file)

    def test_ItGetContentsFromConfigurationFile(self):
        fileContent = 'Hello, world!'
        self.createConfigurationFileWithContent(fileContent)
        self.assertEqual(self.object.get_content_from_configuration_file(), fileContent, 'Contents could not be retrieved from file')
        self.deleteConfigurationFile()

    def test_ItGetsListWhenGettingRemotesFromEmptyContent(self):
        fileContent = ''
        self.assertEqual(self.object.get_remotes_from_content(fileContent), [], 'Expected to get empty List when configuration is does not contain remotes')

    def test_ItGetsRemoteFromContent(self):
        testFileContent = 'username,0.0.0.0,password'
        self.createConfigurationFileWithContent(testFileContent)

        fileContent = self.object.get_content_from_configuration_file()
        expected = [
            {
                'username': 'username',
                'host': '0.0.0.0',
                'password': 'password'
            }
        ]

        self.assertEqual(self.object.get_remotes_from_content(fileContent), expected, 'Remotes not extracted from contents')
        self.deleteConfigurationFile()

    def test_ItGetsRemotesFromContent(self):
        testFileContent = 'username,0.0.0.0,password\nusername1,0.0.0.1,password1'
        self.createConfigurationFileWithContent(testFileContent)

        fileContent = self.object.get_content_from_configuration_file()
        expected = [
            {
                'username': 'username',
                'host': '0.0.0.0',
                'password': 'password'
            },
            {
                'username': 'username1',
                'host': '0.0.0.1',
                'password': 'password1'
            }
        ]

        self.assertEqual(self.object.get_remotes_from_content(fileContent), expected, 'Remotes not extracted from contents')
        self.deleteConfigurationFile()

    def test_ItGetsListWhenGettingRemotesFromEmptyConfig(self):
        self.assertEqual(self.object.get_remotes(), [], 'Remotes not returned')

    def test_ItGetsRemotes(self):
        testFileContent = 'username,0.0.0.0,password\nusername1,0.0.0.1,password1'
        self.createConfigurationFileWithContent(testFileContent)
        expected = [
            {
                'username': 'username',
                'host': '0.0.0.0',
                'password': 'password'
            },
            {
                'username': 'username1',
                'host': '0.0.0.1',
                'password': 'password1'
            }
        ]

        self.assertEqual(self.object.get_remotes(), expected, 'Remotes not returned')
        self.deleteConfigurationFile()

    def tearDown(self):
        return

if __name__ == '__main__':
    unittest.main()