# python-nmap Makefile

VERSION=`python setup.py --version`
ARCHIVE=`python setup.py --fullname`


manifest:
	@python setup.py sdist --manifest-only

test:
	@nosetests nmap -v

testcase:
	@./nmap-6.40/nmap -sV scanme.nmap.org -oX scanme_output.xml

install:
	@python3 setup.py install

archive: doc
	@python3 setup.py sdist
	@echo Archive is create and named dist/$(ARCHIVE).tar.gz
	@echo -n md5sum is :
	@md5sum dist/$(ARCHIVE).tar.gz

license:
	@python3 setup.py --license

register:
	@python3 setup.py register
	@python3 setup.py sdist upload

doc:
	@pydoc3 -w nmap/nmap.py
	@cd docs && make html

web:
	@echo $(VERSION) > web/python-nmap_CURRENT_VERSION.txt
	@cp dist/$(ARCHIVE).tar.gz web/
	@m4 -DVERSION=$(VERSION) -DMD5SUM=$(shell md5sum dist/$(ARCHIVE).tar.gz |cut -d' ' -f1) -DDATE=$(shell date +%Y-%m-%d) web/index.gtm.m4 > web/index.gtm
	@(cd /home/xael/ESPACE_KM/xael.org/web/xael.org/www.xael.org/html/norman/python ; make)
	@(cd /home/xael/ESPACE_KM/xael.org/web/xael.org/www.xael.org/html/norman/ ; make ftp-all)

web2:
	@echo $(VERSION) > web2/python-nmap_CURRENT_VERSION.txt
	@cp dist/$(ARCHIVE).tar.gz web2/
	@m4 -DVERSION=$(VERSION) -DMD5SUM=$(shell md5sum dist/$(ARCHIVE).tar.gz |cut -d' ' -f1) -DDATE=$(shell date +%Y-%m-%d) web2/index.md.m4 > web2/index.md
	@m4 -DVERSION=$(VERSION) -DMD5SUM=$(shell md5sum dist/$(ARCHIVE).tar.gz |cut -d' ' -f1) -DDATE=$(shell date +%Y-%m-%d) web2/index-en.md.m4 > web2/index-en.md
	@bash -c 'source /usr/local/bin/virtualenvwrapper.sh; workon xael.org; make ftp_upload'

changelog:
	vi CHANGELOG

hgcommit:
	@hg tag $(VERSION)
	@hg commit
	@hg push

release: test manifest doc changelog hgcommit register web2


.PHONY: web web2
