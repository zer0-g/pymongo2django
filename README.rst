Installation
============

To install pymongo2django::

   copy pymongo2django directory to the django project directory storing the manage.py file

Software Requirement
====================

The follow software requirement to install pymongo2django app::
	
   * Python 2.7.x
   * Pymongo Driver (latest version preferred)
   * MongoDB Server (http://www.mongodb.org) only if database is installed
     locally on your machine otherwise you can access database from the 
     cloud through MongoDB servers online (http://www.mongolab.com/)

Setup
=====
To use pymongo2django with your Django project, just add these lines to your settings.py file::

Add to the 'INSTALLED_APPS' section the pymongo2django app and append it to the end of this section ::

   INSTALLED_APPS = (
      ...
      'pymongo2django',
   )

 ***IMPORTANT NOTES::
 Update the pymongo2django/settings.py file found inside the pymongo2django directory.
 Update these variables in the pymongo2django/settings.py file to use database.Ensure 
 also that the MongoDB server is running or   otherwise use a MongoDB server from an 
 online vender/host.

Example Accessing a collection via Document model
=================================================

For instance, to create a MongoDB instance to a collection via Document model class::

   >>> import pymongo2django
   >>> from book.models import Author
   >>> author  = Author()
   >>> author.setName(author.name)
   
To find an item in a collection::

   >>> import pymongo2django
   >>> from book.models import Author
   >>> author = Author()
   >>> author.setName(author.name)
   >>> for row in author.objects.find():
   >>> 		print row

Example Accessing a collection via DocumentSet model (ReplicaSet Configuration)
===============================================================================

For instance, to create MongoDB instance (using a Replica Set Configuration) to access a 
collection via DocumentSet model class::

   >>> import pymongo2django
   >>> from book.models import AuthorSet
   >>> authorset  = AuthorSet()
   >>> authorset.setName(authorset.name)
   
To find an item in a collection::

   >>> import pymongo2django
   >>> from book.models import AuthorSet
   >>> authorset = AuthorSet()
   >>> authorset.setName(authorset.name)
   >>> for row in authorset.objects.find():
   >>> 		print row


Sample views file using DocumentSet Model in the Books app
==========================================================
books/views.py::

 from django.http import HttpResponse
 from books.models import AuthorSet

 def myview(request):
     authorset = AuthorSet()
     authorset.setName(authorset.name)
     return HttpResponse('%s' % authorset.objects.find_one() )


Sample models file using DocumentSet Model in the Books app
===========================================================
books/models.py::

 from pymongo2django import DocumentSet

 class AuthorSet(DocumentSet):
      name='products'     


Sample views file using Document Model in the Books app
=======================================================
books/views.py::

 from django.http import HttpResponse
 from books.models import Author

 def myview(request):
     author = Author()
     author.setName(author.name)
     return HttpResponse('%s' % author.objects.find_one() )


Sample models file using Document Model in Books app
====================================================
books/models.py::

 from pymongo2django import Document

 class Author(Document):
      name='products'


 ***IMPORTANT NOTES:: 
 pymongo2django do not syncdb with Django DATABASE_SETTING found in the Django Project settings.py file. Adding to this 
 pymongo2django\settings.py cannot use multiple configuration settings. So once a Document model object or DocumentSet 
 object is created the settings for the database name is locked into either object type created. For instance a Document 
 Model object using a database name 'Work' and you want to change that database name to something else the current Document 
 model object is using. You would have to change the pymongo2django\settings.py file to reflect the changes for the new 
 database name and then re-instantiate the object when done. The same applies when using the DocumentSet only where the 
 current database setting being used is different from the new database settings.
