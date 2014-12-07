import mock

import unittest

from gocdapi.go import Go
from gocdapi.pipeline_group import PipelineGroup
from gocdapi.pipeline_groups import PipelineGroups

from gocdapi.custom_exceptions import GoCdApiException

class TestPipelineGroups(unittest.TestCase):

    DATA0 = """
        [
            {
               "pipelines":[

               ],
               "name":"Super_group"
            }
        ]
    """

    @mock.patch.object(PipelineGroups, 'get_data')
    def setUp(self, get_data_pipeline_groups):
        get_data_pipeline_groups.return_value = self.DATA0
        self.baseurl = 'http://dummyurl'

        go = Go(self.baseurl)

        self.pipeline_groups = go.pipeline_groups
        print self.pipeline_groups.get_data

    def test_pipeline_group_exists(self):
        group_name = 'Super_group'
        self.assertIn(group_name, self.pipeline_groups)

        group_name = 'false-group_name'
        self.assertNotIn(group_name, self.pipeline_groups)

    def test_check_URL(self):
        self.assertEquals(self.pipeline_groups.url, '%s/go/api/config/pipeline_groups/' % self.baseurl)

    @mock.patch.object(PipelineGroups, 'get_data')
    def test_get_pipeline_group(self, get_data_pipeline_groups):
        get_data_pipeline_groups.return_value = self.DATA0
        group_name = 'Super_group'
        print self.pipeline_groups.get_data
        pipeline_group = self.pipeline_groups[group_name]
        self.assertIsInstance(pipeline_group, PipelineGroup)

        group_name = 'false-group_name'
        with self.assertRaises(GoCdApiException):
            self.pipeline_groups[group_name]

    def test_pipeline_groups_iterable(self):
        for pipeline_group in self.pipeline_groups.values():
            self.assertIsInstance(pipeline_group, PipelineGroup)

    def test_repr(self):
        repr(self.pipeline_groups)


if __name__ == '__main__':
    unittest.main()