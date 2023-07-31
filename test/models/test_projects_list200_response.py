import unittest
from src.dopplersdk.models.ProjectsList200Response import ProjectsList200Response


class TestProjectsList200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_projects_list200_response(self):
        # Create ProjectsList200Response class instance
        test_model = ProjectsList200Response(page=9, projects=["occaecati", "tempore"])
        self.assertEqual(test_model.page, 9)
        self.assertEqual(test_model.projects, ["occaecati", "tempore"])


if __name__ == "__main__":
    unittest.main()
