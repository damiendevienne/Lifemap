#SOLR CONFIGURATION

Lifemap uses two Solr documents, named `taxo` and `ascen`. Once created, the configuration for `addi` stays the default one, while the `taxo` one needs a bit more work: 
in `[PATH-TO-SOLR]/server/solr/taxo/conf/`, replace `schema.xml` by the content of `schema.taxo.xml`, and `solrconfig.xml` by the content of `solrconfig.taxo.xml`. The names of the files should not be changed. Solr needs restart after each update. 
