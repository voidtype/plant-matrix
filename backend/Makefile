build:
	docker build -t neworder .
run:	build
	-docker stop neworder
	-docker rm neworder
	docker run -p 80:8000 --name neworder -d neworder
deploy:
	ssh root@144.202.8.17 "git -C /root/blog/blog/ pull origin master"
	ssh root@144.202.8.17 "(cd /root/blog/blog/backend/ && make run)"
