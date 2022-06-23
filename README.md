# Aw_Tools_A-URL-extraction-tool

##  All the information on the target web page is recursively climbed to accurately extract the valid URL.Regular expression is used to filter valid urls and further verify the validity of URL through GET request. The breadth-first traversal is used to put the URL extracted from the web page into the queue of the production consumer model. After obtaining all the urls of the page, the first element of the queue is taken out for the same operation.  Store to a local SQLite database

Warning:Some websites will have anti-crawler mechanism, need to use effective and stable IP proxy to access.

![image](https://github.com/AllwenWeill/IMG/blob/main/%E7%88%AC%E8%99%AB.png) 
