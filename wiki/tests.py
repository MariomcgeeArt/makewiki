from django.contrib.auth.models import User
from django.test import TestCase
from wiki.models import Page



from django.test import TestCase
# canary test Passed!
class WikiTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)


class PageDetailViewTests(TestCase):
    def test_pageform(self):

        user = User.objects.create()
        user.save()
        article= Page.objects.create(title="My Test Article", content="test", author=user)
        article.save()


        response = self.client.get('/my-test-article/')


        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Test Article')
     

class CrerationTest(TestCase):

    def creationTest(self):




        post_request = self.client.post('/create/',
        {
            'title': 'Test Post',
            'content': 'test_test',
            'author': 'admin'
        })


        response = self.client.post('/create/')


        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')










class DetailPageTest(TestCase):
    
    
    
    
    def test_pagedetail(self):
        
        user = User.objects.create()
        user.save()
        article= Page.objects.create(title="My Test Article", content="test", author=user)
        article.save()


      

        post_request = self.client.post('/create/',
        {
            'title': 'Test Post',
            'content': 'test_test',
            'author': 'admin'
        })


        self.assertEqual(response.status_code, 302)


        new_page = Page.objects.filter(contentt='test_test')
        self.assertTrue(new_page.exists())

        # follow=True,   
        # )

        #Create a dictionary of key-value pairs containing the post data to be sent via the form. This should include a new page title and description.
        #Make a POST request to the details page with self.client.post().



        # self.assertEqual(post_request.status_code,302)







    def test_multiple_pages(self):
        # Make some test data to be displayed on the page.
        user = User.objects.create()
        user.save()

        Page.objects.create(title="My Test Page", content="test", author=user)
       

        # Issue a GET request to the MakeWiki homepage.
        # When we make a request, we get a response back.
        #load detail for pages slug 
        response = self.client.get('/my-test-page/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
       

        # Check that the number of pages passed to the template
        # matches the number of pages we have in the database.
        #checks if the response contect includes infor for Page objecrt requested.
      
        self.assertContains(response,'My Test Page')

        self.assertContains(response,'test')








# Check that we get a 302 status code. (Why 302 and not 200?)
 





# Check that the page object was modified in the test database.








