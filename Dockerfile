FROM quay.io/centos/arm64v8
WORKDIR /home
RUN cd /etc/yum.repos.d/
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
RUN yum update -y
RUN yum -y install java-11-openjdk java-11-openjdk-devel curl -y
RUN cd /home/
RUN mkdir -p downloads
RUN cd downloads
RUN mkdir -p jirahome
RUN curl https://product-downloads.atlassian.com/software/jira/downloads/atlassian-jira-software-9.2.0.tar.gz --output atlassian-jira-software-9.2.0.tar.gz
RUN tar -xvf atlassian-jira-software-9.2.0.tar.gz
ENV JIRA_HOME=/home/downloads/jirahome
COPY ./dbconfig.xml /home/downloads/jirahome/
CMD ["atlassian-jira-software-9.2.0-standalone/bin/start-jira.sh", "-fg"]
