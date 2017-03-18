# Python Pictometry SDK
# TODO: Make this a proper python package (i.e. installable), rather than just a file.
# Originally posted at: https://gist.github.com/fvox13/cd66c7bdac277246ee475781d8fa3dd6
# Author: Steven L Smith, Perdix Software, Inc.
#
#
#
# 	MIT License
# 	
# 	Copyright (c) 2017 Perdix Software
# 	
# 	Permission is hereby granted, free of charge, to any person obtaining a copy
# 	of this software and associated documentation files (the "Software"), to deal
# 	in the Software without restriction, including without limitation the rights
# 	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# 	copies of the Software, and to permit persons to whom the Software is
# 	furnished to do so, subject to the following conditions:
# 	
# 	The above copyright notice and this permission notice shall be included in all
# 	copies or substantial portions of the Software.
# 	
# 	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# 	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# 	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# 	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# 	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# 	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# 	SOFTWARE.


from calendar import timegm
from time import gmtime
import hmac

PICTOMETRY_API_KEY = "123abc"
PICTOMETRY_SECRET = "really-long-string"
PICTOMETRY_IPA_LOAD_URL = "http://pol.pictometry.com/ipa/v1/load.php"


def generate_pictometry_url():
	url = PICTOMETRY_IPA_LOAD_URL + "?apikey=" + PICTOMETRY_API_KEY + "&ts=" + str(int(timegm(gmtime())))
	signature = hmac.new(PICTOMETRY_SECRET, msg=url).hexdigest()
	return url + "&ds=" + signature
