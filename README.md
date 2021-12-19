# final_devOps_course

run flask in docker:

1) Build image

`docker build -t my_flask_app:v0.1 my_flask_app/ `

2) run container

`docker run  -p 5000:5000 my_flask_app:v0.1`

3) navigate to http://127.0.0.1:5000/