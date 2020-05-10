#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests,json
from pprint import pprint

url='http://127.0.0.1:3335/get_simmilar/'
res = requests.post(url,data=json.dumps({'CV':'''business analyst singapore graduated with a degree in economics from the university of queensland. i have experience working in an office environment and team setting from my time in national service and during internships. i am a diligent and a fast learner, and i place utmost importance in ensuring quality and professionalism in my work.work experiencebusiness analystmaybank singapore-june 2018 to presentuat coordinator, to liaise between users and it to rectify defects and report progress of testing to project director• extraction and reporting of uat progression and results from hp alm ;• end to end testing for payment and settlement related projects, capturing and extracting relevant ;data and compilation of test scripts ;• liaise with it to ensure all backend screens (as400) correctly shows transactions from user testsinterncimb bank singapore, commercial banking, compliance and operational risk-january 2017 to february 2017• administrative paperwork ;• checking and organising of audit documents, making sure appropriate documents and forms have ;been filled in accordance with regulation ;• verifying and validating appropriate folders and documents are updated and archived preciselytemp administrative assistantcimb bank singapore, commercial banking, emerging businesses-march 2014 to may 2014drafted daily and weekly reports using word and excel for relationship managers based on sales ;figures and projected targets ;• helped compile and distribute employee notices and reports from oracle bi ;• researched information for higher-ups using as400, norkomintel assistantsingapore armed forces-april 2012 to february 2014• wrote detailed weekly reports pertaining to area of coverage ;• maintained appropriate filing of classified documents ;• daily researching of past and present history and current trends relating to area of coverage ;• composed daily summaries during overnight duties to be sent to saf command chaineducationbachelor of economics in business and industrythe university of queensland - st lucia qldjuly 2014 to december 2017a levelscatholic junior collegefebruary 2010 to december 2011as400, hp alm, ms officelinkshttps://www.linkedin.com/in/wen-xian-ng-a4285a160additional information  ;microsoft office  ;as400 ;hp alm  ;adaptable  ;works well under pressure ;activities & interests ;fencing - inter-school championships 2007 individual 3rd & team 2nd, asian schools championships 2007 team 3rd ;muai thai ;american football ;basketball'''}))

pprint( eval(res.text) )


# In[ ]:





# In[ ]:




