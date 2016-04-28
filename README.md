# Lifemap

Lifemap is a tool that allows exploring on-line, in a manner similar to geographic maps, a complete representation of the Tree of Life. It relies on some tools created in the context of the OpenStreetMap project: mapnik and mod_tile. 

The tree is the taxonomy of the NCBI. The code available here is divided into different folders corresponding to different aspects of the project
* PIPELINE: the main functions of Lifemap, allowing to go from the retrieval of the NCBI taxonomy to the creation of a PostgreSQL/PostGIS database. 
* WEBSITE: All HTML5/CSS/JAVASCRIPT codes for the Lifemap web sites (the general public one, the pro one and the mobile one). For convenience, and to ensure compatibility, all javascript library that Lifemap uses are also included.
* PHONE-APP: Everything necessary for PhoneGap to create a mobile app for Lifemap
* OTHER: Configuration and style files, as well as modified source code of mod_tile that allows more zoom level to be rendered.


