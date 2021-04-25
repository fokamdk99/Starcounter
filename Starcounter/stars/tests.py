from django.test import TestCase, RequestFactory, Client
from . import views
import json

# Create your tests here.

class ExampleViewTestCase(TestCase):
    def test_get_known_user(self):
        status_code = 200
        view_class = views.Git_handler
        kwargs = {'user_name':'fokamdk99'}

        client = Client()

        url = f"/stars/{kwargs['user_name']}"
        req = RequestFactory().get(url)
        resp = view_class.as_view()(req, *[], **kwargs)
        json_resp = json.loads(resp.content.decode('utf-8'))
        #import pdb; pdb.set_trace()
        self.assertEqual(json_resp['user_name'], kwargs['user_name'])
        self.assertEqual(resp.status_code, status_code)

    def test_post(self):
        status_code = 405
        view_class = views.Git_handler
        kwargs = {'user_name':'fokamdk99'}

        client = Client()

        url = f"/stars/{kwargs['user_name']}"
        req = RequestFactory().post(url)
        resp = view_class.as_view()(req, *[], **kwargs)
        #import pdb; pdb.set_trace()
        self.assertEqual(resp.status_code, status_code)

    def test_get_unknown_user(self):
        status_code = 200
        view_class = views.Git_handler
        kwargs = {'user_name':'mnbmnbmnbmnb'}
        message = 'user not found'

        client = Client()

        url = f"/stars/{kwargs['user_name']}"
        req = RequestFactory().get(url)
        resp = view_class.as_view()(req, *[], **kwargs)
        json_resp = json.loads(resp.content.decode('utf-8'))
        #import pdb; pdb.set_trace()
        self.assertEqual(json_resp['message'], message)
        self.assertEqual(resp.status_code, status_code)