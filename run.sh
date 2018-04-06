#!/bin/bash
if [ -z "$VCAP_APP_PORT" ];
   then SERVER_PORT=80;
   else SERVER_PORT="$VCAP_APP_PORT";
fi
echo port is $SERVER_PORT
docker build ./build -t test-image
docker run -it --name test_container -p 8000:8080 -e DJANGO_SETTINGS_MODULE=django_test.settings -e IPYTHONDIR=/home/web/.ipython -v /Users/i346092/Desktop/test/django_test/:/app/src test-image /bin/bash
docker exec test_container python manage.py runserver 0.0.0.0:8080