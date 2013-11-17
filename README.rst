Installation
============

To install pymongo2django::

   copy pymongo2django to the django project directory storing the manage.py file

Software Requirement
====================

The follow software requirement to install pymongo2django app::
	
   * Python 2.7.x
   * Pymongo Driver (latest version preferred)
   * MongoDB Server (http://www.mongodb.org) only if database is installed
     locally on your machine otherwise you can access database from the 
     cloud through MongoDB servers online (http://www.mongolab.com/)

Usage
=====
To use pymongo2django with your Django project, just add these lines to your settings.py file::

Add to the 'INSTALLED_APPS' section the pymongo2django app and append it to the end of this section ::

   INSTALLED_APPS = (
      ...
      'pymongo2django',
   )

Update the pymongo2django/settings.py file found inside the pymongo2django directory.
Update the variables in this file to use database.

Example Accessing DB instance
=============================

For instance, to create a DB instance::

   >>> from pymongo2django import get_DBInstance
   >>> db = get_DBInstance()
   
To find an item in a collection::

   >>> from pymongo2django import get_DBInstance
   >>> db = get_DBInstance()
   >>> col = db.tester
   >>> for row in col.find():
   >>> 		print row


Example Accessing a collection via Document model
================================================

For instance, to create a collection instance via Document model class::

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


Sample Views.py in Django app Books
===================================

from django.http import HttpResponse
from books.models import Author
# Create your views here.
def myview(request):
    author = Author()
    author.setName(author.name)
    return HttpResponse('%s' % author.objects.find_one() )


Sample Models.py in Django app Books
===================================

from pymongo2django import Document

class Author(Document):
    name='products'