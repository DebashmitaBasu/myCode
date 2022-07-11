#! python3
# -*- coding: utf-8 -*-
#title					:timeTaken.py
#author					:Debashmita
#date of creation		:11/07/2022 15:50
#==============================================================================
#later incorporate into code as function - user defined, built-in

from datetime import datetime
startTime = datetime.now()

#do something

print('Time taken: {}'.format(datetime.now() - startTime))