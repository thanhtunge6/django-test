docker run -it -d --name test_container -p 8000:8080 -e DJANGO_SETTINGS_MODULE=django_test.settings -e IPYTHONDIR=/home/web/.ipython -v /Users/i346092/Desktop/test/django_test/:/app/src test-image /bin/bash